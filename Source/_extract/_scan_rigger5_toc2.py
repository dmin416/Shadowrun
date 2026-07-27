# -*- coding: utf-8 -*-
import re
import pypdf

pdf = pypdf.PdfReader(r"c:\Users\admin\Desktop\Shadowrun\Source\PDF\rigger5.pdf")
# Full TOC from pages 2-4
toc = "\n".join((pdf.pages[i].extract_text() or "") for i in range(2, 5))
print(toc)
print("---")
# verify specific indices
for i in [5, 6, 10, 24, 32, 36, 40, 70, 78, 94, 110, 116, 150, 172, 185, 193]:
    t = pdf.pages[i].extract_text() or ""
    lines = [ln.strip() for ln in t.splitlines() if ln.strip()][:6]
    print(f"idx {i}: {lines}")
