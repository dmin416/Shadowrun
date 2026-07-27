# -*- coding: utf-8 -*-
import re
from pathlib import Path
import os

html_path = Path(os.environ["TEMP"]) / "thyamath_index2.html"
html = html_path.read_text(encoding="latin-1", errors="replace")
links = re.findall(r'href=(["\'])(.*?)\1', html, re.I)
hrefs = [h[1] for h in links]
print(f"Total hrefs: {len(hrefs)}\n")
print("=== All Shadowrun / PDF / SR links ===")
for h in hrefs:
    if re.search(r"Shadowrun|SR5|SR4|\.pdf", h, re.I):
        print(h)

print("\n=== Shadowrun 5e section (raw) ===")
m = re.search(r"(?is)Shadowrun\s*5e(.*?)(?:Shadowrun\s*4e|Toon|Warhammer|Yggdrasill|</body>)", html)
if not m:
    m = re.search(r"(?is)##\s*Shadowrun\s*5e(.*?)(?:##\s*|<h2)", html)
idx = html.lower().find("shadowrun 5")
print(html[idx : idx + 12000] if idx >= 0 else "section not found")
