import webbrowser

def name_targeting(company, name):
    dork = f'site:linkedin.com/in/ AND "{company}" AND "{name}"'
    url = f"https://www.google.com/search?q={dork}"
    webbrowser.open(url)
    with open("reports/results.txt", "a") as r:
        r.write(f"[Name Targeting] {url}\n")
