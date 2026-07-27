# -*- coding: utf-8 -*-
"""Dump TOC print-page numbers for Run Faster, Street Lethal, Howling Shadows."""
import re
import pypdf

BOOKS = [
    ("runfaster.pdf", [
        "INTRODUCTION", "DECADE", "WHO YOU ARE", "ETHICS", "SPICE OF RUNNERS",
        "MORE THAN SKIN", "RUN ON THE WILD", "CONSTRUCTION KITS", "MESS OF METAHUMANITY",
        "INTO THE NIGHT", "AS YOU AS YOU", "DOMESTICALLY", "WHO YOU KNOW",
        "BOSSES", "DUMP OF ONE", "PACK YOUR KIT",
    ]),
    ("streetlethal.pdf", [
        "INTRODUCTION", "PROVING GROUNDS", "EXPANDED ARSENAL", "MILITARY AND FUTURE",
        "OPPOSITION REPORT", "AT SEA", "UNCONVENTIONAL", "LETHAL ARTS", "ADVENTURE HOOKS",
    ]),
    ("howlingshadows.pdf", [
        "INTRODUCTION", "NO JUSTICE", "NATURE IS A BITCH", "UNTAMED SECURITY",
        "MUNDANE CRITTERS", "DINGOBAT", "PARANORMAL ANIMALS", "MUTANTS",
        "EXTRAPLANAR", "RUN IN THE WOODS", "TECHNOCRITTERS", "PROTOSAPIENTS",
        "DRAKES", "BUILDING MAN", "GAME INFORMATION", "CRITTER TABLES",
    ]),
]

base = r"c:\Users\admin\Desktop\Shadowrun\Source\PDF"
for fname, keys in BOOKS:
    pdf = pypdf.PdfReader(f"{base}\\{fname}")
    print(f"\n===== {fname} pages={len(pdf.pages)} =====")
    # print early TOC pages
    for i in range(2, min(6, len(pdf.pages))):
        t = pdf.pages[i].extract_text() or ""
        # pull lines that look like CHAPTER  N
        for ln in t.splitlines():
            if re.search(r"\b\d{1,3}\s*$", ln.strip()) and len(ln.strip()) < 60:
                if any(c.isalpha() for c in ln):
                    print(f"  toc[{i}] {ln.strip()}")
