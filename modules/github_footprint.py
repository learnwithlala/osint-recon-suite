import webbrowser

def github_footprint(company):
    dork = f'site:github.com "{company}"'
    url = f"https://www.google.com/search?q={dork}"
    webbrowser.open(url)
    with open("reports/results.txt", "a") as r:
        r.write(f"[GitHub Footprint] {url}\n")
