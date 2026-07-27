# -*- coding: utf-8 -*-
import re
import pypdf

pdf = pypdf.PdfReader(r"c:\Users\admin\Desktop\Shadowrun\Source\PDF\rigger5.pdf")
print("pages", len(pdf.pages))
targets = [
    "INTRODUCTION",
    "HOME SECURITY",
    "HOT RUBBER",
    "ALL THE ANGLES",
    "ON THE BLEEDING EDGE",
    "THE ORDER OF CHAOS",
    "DEMOLITION DERBY",
    "RULING THE WAVES",
    "AIR SUPERIORITY",
    "ONE RIG TO RULE",
    "THE AUTOMATED ARMY",
    "BUILDING THE PERFECT",
    "MAXIMUM PURSUIT",
    "VEHICLE AND DRONE",
    "TABLES",
]
seen = set()
for i, page in enumerate(pdf.pages):
    t = page.extract_text() or ""
    head = "\n".join(t.splitlines()[:12]).upper()
    for tgt in targets:
        if tgt in head and tgt not in seen:
            # printed page near end
            nums = re.findall(r"\b(\d{1,3})\b", "\n".join(t.splitlines()[-5:]))
            print(f"idx {i:3d}  {tgt:25s}  tailnums={nums[-3:]}  head={t.splitlines()[:3]}")
            seen.add(tgt)
