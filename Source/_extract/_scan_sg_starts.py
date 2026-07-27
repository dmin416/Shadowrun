# -*- coding: utf-8 -*-
import re
import pypdf

pdf = pypdf.PdfReader(r"c:\Users\admin\Desktop\Shadowrun\Source\PDF\streetgrimoire.pdf")
print("pages", len(pdf.pages))
# Search for chapter title as first meaningful line / header
chapters = [
    "INTRODUCTION",
    "WHERE FEW DARE TO TREAD",
    "SURVIVING MAGIC",
    "MAGIC IN THE WORLD",
    "MAGICAL TRADITIONS",
    "MAGICAL SOCIETIES",
    "DARK MAGIC",
    "EXPANDED GRIMOIRE",
    "SHADOW RITUALS",
    "SECRETS OF THE INITIATES",
    "BUTCHER",
    "PHYSICAL MAGIC",
    "THE IMMATERIAL TOUCH",
    "TURNING LEAD",
]
for i, page in enumerate(pdf.pages):
    t = page.extract_text() or ""
    # look at early lines and header patterns
    head = "\n".join(t.splitlines()[:15])
    for ch in chapters:
        if ch in head.upper():
            # avoid TOC pages (lots of page numbers)
            if head.count("\n") > 3 and i > 5:
                # check if it's a chapter start banner
                if re.search(rf"^{ch}", head.upper(), re.M) or f"<< {ch}" in head.upper() or f"{ch}" in head.upper()[:80]:
                    nums = re.findall(r"\b(\d{1,3})\b", "\n".join(t.splitlines()[-4:]))
                    print(f"idx {i:3d}  {ch:30s}  sample={t.splitlines()[:2]!r}")
                    break
