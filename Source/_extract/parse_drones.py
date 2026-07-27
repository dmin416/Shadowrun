# -*- coding: utf-8 -*-
"""Extract drone catalog writeups + stats from Rigger 5 PDF."""
import fitz
import re
import json

doc = fitz.open(r"c:\Users\admin\Desktop\Shadowrun\Source\PDF\rigger5.pdf")

# Full catalog text with page markers
parts = []
for i in range(127, 149):
    parts.append(f"\n@@@@@PAGE {i+1}@@@@\n")
    parts.append(doc[i].get_text())
catalog = "".join(parts)
open("r5_catalog_raw.txt", "w", encoding="utf-8").write(catalog)

# Compiled tables
table_text = "\n".join(doc[i].get_text() for i in range(188, 191))
open("r5_drone_tables_raw.txt", "w", encoding="utf-8").write(table_text)

# Pull Core drone section pages from core PDF for page numbers
core = fitz.open(r"c:\Users\admin\Desktop\Shadowrun\Source\PDF\shadowrunfiftheditioncorerulebook_V2.pdf")
for i in range(core.page_count):
    t = core[i].get_text()
    if "Shiawase Kanmushi" in t and "Sikorsky-Bell Microskimmer" in t:
        print("Core drones start page", i + 1)
        open("core_drones.txt", "w", encoding="utf-8").write(t)
        if i + 1 < core.page_count:
            open("core_drones2.txt", "w", encoding="utf-8").write(core[i + 1].get_text())
        break

print("catalog", len(catalog), "table", len(table_text))
