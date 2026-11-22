#!/usr/bin/env python3
"""Refresh the language bars on development.html from the GitHub API.

Each .repo-card links to owner/name; its .lang-bar and .lang-list are rebuilt
from /repos/owner/name/languages. Nothing else in the page is touched.
Uses GITHUB_TOKEN if set (higher rate limit), otherwise anonymous.
"""
import json, os, re, sys, urllib.request

PAGE = os.path.join(os.path.dirname(__file__), "..", "development.html")
COLORS = {"Python": "#3572A5", "TypeScript": "#3178c6", "JavaScript": "#f1e05a", "CSS": "#a370d6",
          "HTML": "#e34c26", "Dockerfile": "#4f7a8c", "Shell": "#89e051", "C#": "#3fae2a"}


def languages(repo):
    req = urllib.request.Request(f"https://api.github.com/repos/{repo}/languages",
                                 headers={"Accept": "application/vnd.github+json", "User-Agent": "portfolio-language-refresh"})
    if os.environ.get("GITHUB_TOKEN"):
        req.add_header("Authorization", "Bearer " + os.environ["GITHUB_TOKEN"])
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def render(langs):
    total = sum(langs.values())
    items = sorted(langs.items(), key=lambda kv: -kv[1])
    bar = "".join(f'<span style="width:{v / total * 100:.2f}%;background:{COLORS.get(k, "#888")}" title="{k}"></span>'
                  for k, v in items)
    lst = "".join(f'<li><i style="background:{COLORS.get(k, "#888")}"></i>{k} <b>{v / total * 100:.1f}%</b></li>'
                  for k, v in items if v / total >= 0.005)
    return (f'<div class="lang-bar" role="img" aria-label="Language breakdown">{bar}</div>\n'
            f'        <ul class="lang-list">{lst}</ul>')


def main():
    page = open(PAGE, encoding="utf-8").read()

    def fix(m):
        block = m.group(0)
        repo = re.search(r'href="https://github\.com/([^"/]+/[^"/]+)"', block).group(1)
        try:
            langs = languages(repo)
        except Exception as e:  # keep the old bar if the API fails
            print(f"skip {repo}: {e}", file=sys.stderr)
            return block
        if not langs:
            return block
        return re.sub(r'<div class="lang-bar".*?</ul>', lambda _: render(langs), block, flags=re.S)

    new = re.sub(r'<div class="repo-card.*?\n      </div>', fix, page, flags=re.S)
    if new != page:
        open(PAGE, "w", encoding="utf-8").write(new)
        print("updated")
    else:
        print("no changes")


if __name__ == "__main__":
    main()
