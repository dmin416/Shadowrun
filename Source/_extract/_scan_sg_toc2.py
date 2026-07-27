# -*- coding: utf-8 -*-
import pypdf

pdf = pypdf.PdfReader(r"c:\Users\admin\Desktop\Shadowrun\Source\PDF\streetgrimoire.pdf")
# TOC continues on pages 3-6ish; also find chapter starts
toc = "\n".join((pdf.pages[i].extract_text() or "") for i in range(3, 8))
print(toc[-4000:])
print("---VERIFY---")
for i in [5, 6, 10, 24, 38, 54, 78, 102, 120, 138, 156, 160, 170, 180, 200, 210, 220, 230]:
    if i >= len(pdf.pages):
        continue
    t = pdf.pages[i].extract_text() or ""
    lines = [ln.strip() for ln in t.splitlines() if ln.strip()][:5]
    print(f"idx {i}: {lines}")
