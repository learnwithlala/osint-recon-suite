import webbrowser

def breach_check(email):
    urls = [
        f"https://haveibeenpwned.com/account/{email}",
        f"https://intelx.io/?s={email}",
        f"https://pastebin.com/search?q={email}"
    ]
    for url in urls:
        webbrowser.open(url)
        with open("reports/results.txt", "a") as r:
            r.write(f"[Breach Check] {url}\n")
