# -*- coding: utf-8 -*-
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(r"c:\Users\admin\Desktop\Shadowrun")

print("=== CHARGEN INVENTORY ===")
for p in sorted((ROOT / "Mechanics/Character Creation").glob("*.md")):
    t = p.read_text(encoding="utf-8")
    m = re.search(r"(?s)## Inventory.*?(?:\n---|\n## [^I])", t)
    block = m.group(0) if m else ""
    open_n = block.count("- [ ]")
    done_n = block.count("- [x]")
    print(f"{p.name:35} [x]={done_n} [ ]={open_n}")

print("\n=== COMBAT + CORE RES INVENTORY ===")
for rel in [
    "Dice and Tests.md",
    "Edge.md",
    "Combat/Overview.md",
    "Combat/Initiative.md",
    "Combat/Action Economy.md",
]:
    t = (ROOT / "Mechanics" / rel).read_text(encoding="utf-8")
    m = re.search(r"(?s)## Inventory.*?\n---", t)
    block = m.group(0) if m else ""
    print(f"{rel:40} [x]={block.count('- [x]')} [ ]={block.count('- [ ]')}")

print("\n=== ENCYCLOPEDIA UNVERIFIED ROW COUNTS ===")
for p in sorted((ROOT / "Encyclopedia").glob("*.md")):
    if p.name == "INDEX.md":
        continue
    t = p.read_text(encoding="utf-8")
    # count lines that look like unverified catalog notes
    n = len(re.findall(r"UNVERIFIED|unverified \(no|no local PDF", t, re.I))
    if n:
        print(f"{p.name:42} callouts~{n}")

print("\n=== SERRATED EDGE CHAPTER CHAR COUNTS ===")
for p in sorted((ROOT / "Source Texts/Serrated Edge").glob("*.md")):
    t = p.read_text(encoding="utf-8")
    body = re.sub(r"\s+", "", t)
    print(f"{p.name:40} chars={len(body):6}")

print("\n=== ACTION ECONOMY ACTION COUNT ===")
t = (ROOT / "Mechanics/Combat/Action Economy.md").read_text(encoding="utf-8")
for section in ["Free Actions", "Simple Actions", "Complex Actions", "Interrupt Actions"]:
    m = re.search(rf"(?s)## {section}.*?(?=\n## |\Z)", t)
    if not m:
        print(section, "MISSING SECTION")
        continue
    rows = [
        L
        for L in m.group(0).splitlines()
        if L.startswith("|") and "---" not in L and not L.startswith("| Action")
    ]
    print(f"{section}: {len(rows)} rows")
