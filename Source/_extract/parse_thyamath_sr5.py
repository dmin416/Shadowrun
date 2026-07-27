# -*- coding: utf-8 -*-
import os
import re
from pathlib import Path

html = (Path(os.environ["TEMP"]) / "thyamath_index2.html").read_text(
    encoding="latin-1", errors="replace"
)

# Pull SR5 block between Shadowrun 5e heading and next major game or end
m = re.search(
    r'(?is)<h2[^>]*>\s*Shadowrun\s*5e\s*</h2>(.*?)(?:<h2[^>]*>|</body>)',
    html,
)
if not m:
    # try looser
    i = html.lower().find("shadowrun 5e")
    print("fallback idx", i)
    chunk = html[i : i + 5000]
else:
    chunk = m.group(1)

print("=== Shadowrun 5e HTML chunk ===")
print(chunk)

print("\n=== Absolute SR5 links ===")
base = "http://thyamath.fr/"
for href, text in re.findall(r'<a\s+href="([^"]+)"[^>]*>(.*?)</a>', chunk, re.I | re.S):
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    if href.startswith("http"):
        url = href
    else:
        url = base + href.lstrip("/")
    print(f"{text}\n  {url}\n")
