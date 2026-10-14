# Copyright (c) Asyntai. Licensed under the MIT license.
"""Asyntai AI Assistant for Espanso, macOS and Linux side.

Espanso runs this script through the shell extension (see package.yml) and
types whatever it prints. Windows runs asyntai.ps1, which does the same work.

    python3 asyntai.py ask    question from the :ask form (ESPANSO_FORM1_QUESTION)
    python3 asyntai.py clip   question from the clipboard (ESPANSO_CLIP)
    python3 asyntai.py key    save the API key from the :asyntaikey form (ESPANSO_FORM1_KEY)

The script only talks to asyntai.com, only sends the API key in the
Authorization header, and only writes one file: the saved API key. It uses the
Python standard library alone, so there is nothing to pip install.
"""

import json
import os
import re
import secrets
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

LIVE_BASE = "https://asyntai.com"
USER_AGENT = "AsyntaiEspanso/0.1"
TIMEOUT = 90
# The other Asyntai launchers mark their own questions the same way, so the
# owner's test questions are easy to tell apart from visitor chats.
ASK_MARKER = "espanso_ask_"

NO_KEY = "Asyntai: add your API key first. Type :asyntaikey in an empty text field."
BAD_KEY = "Asyntai: this API key no longer works. Type :asyntaikey and paste a new key."


class AsyntaiError(Exception):
    def __init__(self, message, status=0):
        super().__init__(message)
        self.status = status


def key_path():
    if sys.platform == "win32":
        root = os.environ.get("APPDATA") or os.path.expanduser("~")
    else:
        root = os.environ.get("XDG_CONFIG_HOME") or os.path.join(os.path.expanduser("~"), ".config")
    return os.path.join(root, "asyntai", "espanso-api-key")


def read_key():
    key = os.environ.get("ASYNTAI_API_KEY", "").strip()
    if key:
        return key
    try:
        with open(key_path(), encoding="utf-8") as f:
            return f.read().strip()
    except OSError:
        return ""


def save_key(key):
    path = key_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    # The key is a secret: create the file readable by its owner only.
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        f.write(key)


def base_url():
    # A local Asyntai server can be used for development, nothing else, so
    # the key can never be sent to a third-party host.
    base = os.environ.get("ASYNTAI_BASE_URL", "").strip().rstrip("/")
    if base:
        host = urllib.parse.urlsplit(base).hostname or ""
        if host in ("127.0.0.1", "localhost"):
            return base
    return LIVE_BASE


def call(method, path, key, body=None):
    headers = {
        "Authorization": "Bearer " + key,
        "Accept": "application/json",
        "User-Agent": USER_AGENT,
    }
    data = None
    if body is not None:
        data = json.dumps(body).encode("utf-8")
        headers["Content-Type"] = "application/json"
    request = urllib.request.Request(base_url() + path, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
            status, raw = response.status, response.read()
    except urllib.error.HTTPError as e:
        status, raw = e.code, (e.read() if e.fp else b"")
    except Exception:
        raise AsyntaiError("Asyntai: no answer from asyntai.com. Check your internet connection and try again.")

    try:
        root = json.loads(raw.decode("utf-8", "replace")) if raw.strip() else {}
    except ValueError:
        root = None
    error = root.get("error") if isinstance(root, dict) and isinstance(root.get("error"), str) else ""

    if status == 401:
        raise AsyntaiError(BAD_KEY, status)
    if status == 403:
        raise AsyntaiError("Asyntai: " + (error or "the Asyntai API needs the Starter plan or higher."))
    if status == 429:
        raise AsyntaiError("Asyntai: " + (error or "your chatbot reached its message limit."))
    if status >= 400 or not isinstance(root, dict) or root.get("success") is False:
        raise AsyntaiError("Asyntai: " + (error or "the server answered with status %d." % status))
    return root


def plain(text):
    """Make a chat answer fit a plain text field: links as "text (url)", no bold."""
    def link(m):
        label, url = m.group(1).strip(), m.group(2).strip()
        if not label or label == url or url.startswith("mailto:") or url.startswith("tel:"):
            return label or url
        return "%s (%s)" % (label, url)

    text = re.sub(r"\[([^\]]*)\]\((\S+?)\)", link, text)
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text, flags=re.S)
    text = re.sub(r"__(.+?)__", r"\1", text, flags=re.S)
    text = re.sub(r"^#{1,6}\s+", "", text, flags=re.M)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def ask(question):
    question = (question or "").strip()
    if not question:
        return "Asyntai: the question is empty. Type :ask and write a question."
    key = read_key()
    if not key:
        return NO_KEY
    session = "%s%d_%s" % (ASK_MARKER, int(time.time() * 1000), secrets.token_hex(3))
    root = call("POST", "/api/v1/chat/", key, {"message": question, "session_id": session})
    answer = root.get("response") if isinstance(root.get("response"), str) else ""
    return plain(answer) or "Asyntai: your chatbot gave an empty answer."


def set_key(key):
    key = (key or "").strip()
    if not key:
        return "Asyntai: the API key is empty. Type :asyntaikey and paste your key."
    try:
        root = call("GET", "/api/v1/websites/", key)
    except AsyntaiError as e:
        if e.status == 401:
            return "Asyntai: this is not a valid API key. In Asyntai, open Settings, then API, and copy the key again."
        raise
    # Save only a key that Asyntai accepts.
    save_key(key)
    sites = [w for w in root.get("websites") or [] if isinstance(w, dict)]
    primary = next((w for w in sites if w.get("is_primary")), sites[0] if sites else None)
    domain = primary.get("domain") if primary and isinstance(primary.get("domain"), str) else ""
    if domain:
        return "Asyntai API key saved. Your chatbot for %s is ready: type :ask to ask it." % domain
    return "Asyntai API key saved. Type :ask to ask your chatbot."


def main(argv):
    mode = argv[1] if len(argv) > 1 else ""
    try:
        if mode == "ask":
            out = ask(os.environ.get("ESPANSO_FORM1_QUESTION"))
        elif mode == "clip":
            out = ask(os.environ.get("ESPANSO_CLIP"))
        elif mode == "key":
            out = set_key(os.environ.get("ESPANSO_FORM1_KEY"))
        else:
            out = "Asyntai: unknown command."
    except AsyntaiError as e:
        out = str(e)
    except Exception:
        out = "Asyntai: something went wrong. Please try again."
    # Espanso reads stdout as UTF-8 on every system.
    sys.stdout.buffer.write(out.encode("utf-8"))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
