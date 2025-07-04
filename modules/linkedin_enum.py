import webbrowser

def linkedin_enum(company):
    dork = f'site:linkedin.com/in/ AND "{company}"'
    url = f"https://www.google.com/search?q={dork}"
    webbrowser.open(url)
    with open("reports/results.txt", "a") as r:
        r.write(f"[LinkedIn Enum] {url}\n")

