# -*- coding: utf-8 -*-
import re
from pathlib import Path
import fitz

doc = fitz.open(r"c:\Users\admin\Desktop\Shadowrun\Source\PDF\runandgun.pdf")
OUT = Path(r"c:\Users\admin\Desktop\Shadowrun\Source Texts\Run and Gun")


def words(t: str) -> set[str]:
    return set(re.findall(r"[A-Za-z][A-Za-z']{3,}", t.lower()))


for label, fname, a, b in [
    ("01", "01 - Contents and Credits.md", 1, 5),
    ("14", "14 - Run and Gun Tables.md", 201, 213),
]:
    md = (OUT / fname).read_text(encoding="utf-8")
    pdf = "".join(doc[i].get_text("text") for i in range(a, b))
    miss = sorted(words(pdf) - words(md))
    # filter common footer noise
    noise = {"arsenal", "contents", "credits", "gun", "run", "page"}
    miss = [m for m in miss if m not in noise]
    print(f"=== {label} missing {len(miss)} ===")
    print(miss[:100])
