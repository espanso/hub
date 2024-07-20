import sys
import urllib.request
import urllib.parse
import re


def get_bib_info(bib):
    """Extracts author, title, and year from a given bib entry."""
    author = re.search(r"author\s*=\s*{(.*?)}", bib, re.DOTALL)
    if author is None:
        author = re.search(r"editor\s*=\s*{(.*?)}", bib, re.DOTALL)
    author = author.group(1) if author is not None else "Unknown"
    title = re.search(r"title\s*=\s*{(.*?)}", bib, re.DOTALL).group(1)
    year = re.search(r"year\s*=\s*{(.*?)}", bib).group(1)
    return author, title, year


def format_bib_key(author, title, year):
    """Formats the bib key using author's last name, first three words of the title, and the year."""
    author_lastname = author.split(" and")[0].split()[-1].lower()
    first_three_words = "".join(
        re.sub(r"[^a-zA-Z]", "", word) for word in title.split()[:3]
    )
    key = f"{author_lastname}{first_three_words}{year}"
    return key


def extract_url(selected_entry):
    """Extracts the URL part from the selected entry in the espanso form"""
    pattern = r"\(([^()]*\/.*\/[^()]*)\)$"
    match = re.search(pattern, selected_entry)
    if match:
        return match.group(1)
    else:
        return None


def get_bib(selected_entry):
    """Gets the bib from the selected entry in the espanso form"""
    full_url = f"https://dblp.org/rec/{extract_url(selected_entry)}.bib"
    with urllib.request.urlopen(full_url) as bib_response:
        bib = bib_response.read().decode()
        if "not found" not in bib:
            author, title, year = get_bib_info(bib)
            key = format_bib_key(author, title, year)
            output = re.sub(r"\{DBLP:.*?\,", "{" + key + ",", bib)
        else:
            output = "Not found in DBLP"
    print(output)


try:
    get_bib(sys.argv[1])
except Exception as e:
    output = str(e)
