# -*- coding: utf-8 -*-
"""Scan Forbidden Arcana TOC for chapter page map."""
import pypdf

pdf = pypdf.PdfReader(r"c:\Users\admin\Desktop\Shadowrun\Source\PDF\forbiddenarcana.pdf")
print("pages", len(pdf.pages))
for i in range(min(8, len(pdf.pages))):
    t = pdf.pages[i].extract_text() or ""
    print(f"==== idx {i} ====")
    print(t[:1800])
    print()
