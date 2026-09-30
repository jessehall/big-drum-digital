#!/usr/bin/env python3
"""Version shared assets so a deployment cannot reuse stale browser CSS."""
from pathlib import Path
import hashlib
import re
import sys

root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
versions = {name: hashlib.sha256((root / name).read_bytes()).hexdigest()[:12]
            for name in ("styles.css", "app.js", "assets/favicon.svg")}
pattern = re.compile(r"\b(href|src)=([\"'])([^\"']+)\2")

def stamp(match):
    attribute, quote, value = match.groups()
    path = value.split("?", 1)[0]
    for name, version in versions.items():
        if path == name or path.endswith("/" + name):
            return f"{attribute}={quote}{path}?v={version}{quote}"
    return match.group(0)

for page in root.rglob("*.html"):
    if ".git" in page.parts:
        continue
    before = page.read_text()
    after = pattern.sub(stamp, before)
    if after != before:
        page.write_text(after)
