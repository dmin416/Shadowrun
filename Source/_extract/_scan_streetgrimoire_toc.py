# -*- coding: utf-8 -*-
"""Dump Street Grimoire TOC and verify chapter starts."""
import pypdf

pdf = pypdf.PdfReader(r"c:\Users\admin\Desktop\Shadowrun\Source\PDF\streetgrimoire.pdf")
print("pages", len(pdf.pages))
for i in range(min(6, len(pdf.pages))):
    t = pdf.pages[i].extract_text() or ""
    print(f"==== idx {i} ====")
    print(t[:2000])
    print()
