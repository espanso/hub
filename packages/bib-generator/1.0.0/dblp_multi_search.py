import urllib.request
import urllib.parse
import json
import sys


def search(query):
    """Searches for a publication and retrieves the top 5 matches."""
    options = {"q": query, "format": "json", "h": 5}
    output = ""
    url = f"https://dblp.org/search/publ/api?{urllib.parse.urlencode(options)}"
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode())
        hit = data.get("result", {}).get("hits", {}).get("hit", [])

        if hit:
            for item in hit:
                info = item.get("info", {})
                title = info.get("title", "No title found")
                output += f"{title} ({info.get('url').replace("https://dblp.org/rec/", "")})\n"
        else:
            print("No results found in DBLP")
    print(output.strip())


try:
    search(sys.argv[1])
except Exception as e:
    output = str(e)
