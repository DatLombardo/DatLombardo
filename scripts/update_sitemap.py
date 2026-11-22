#!/usr/bin/env python3
"""Rewrite sitemap.xml with each page's lastmod taken from its last git commit."""
import os, subprocess

ROOT = os.path.join(os.path.dirname(__file__), "..")
BASE = "https://datlombardo.ca/"
PAGES = [("", "index.html", "1.0"), ("lifeStory.html", "lifeStory.html", "0.7"), ("vitae.html", "vitae.html", "0.7"),
         ("development.html", "development.html", "0.7"), ("publications.html", "publications.html", "0.7"),
         ("MScThesis.html", "MScThesis.html", "0.7")]


def lastmod(path):
    out = subprocess.run(["git", "log", "-1", "--format=%cs", "--", path], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    return out or None


rows = []
for url, path, pri in PAGES:
    d = lastmod(path)
    tag = f"<lastmod>{d}</lastmod>" if d else ""
    rows.append(f"  <url><loc>{BASE}{url}</loc>{tag}<priority>{pri}</priority></url>\n")
xml = ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
       + "".join(rows) + "</urlset>\n")
p = os.path.join(ROOT, "sitemap.xml")
if not os.path.exists(p) or open(p).read() != xml:
    open(p, "w").write(xml)
    print("updated")
else:
    print("no changes")
