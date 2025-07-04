import webbrowser

def social_media(username):
    queries = [
        f"site:linkedin.com/in {username}",
        f"site:twitter.com {username}",
        f"site:instagram.com {username}",
        f"site:facebook.com {username}"
    ]
    for q in queries:
        url = f"https://www.google.com/search?q={q}"
        webbrowser.open(url)
        with open("reports/results.txt", "a") as r:
            r.write(f"[Social OSINT] {url}\n")
