# -*- coding: utf-8 -*-
"""Per-chapter loss + quality check for one RnG Source Text file."""
from __future__ import annotations

import argparse
import re
import unicodedata
from pathlib import Path

import fitz

PDF = Path(r"c:\Users\admin\Desktop\Shadowrun\Source\PDF\runandgun.pdf")
OUT = Path(r"c:\Users\admin\Desktop\Shadowrun\Source Texts\Run and Gun")

SECTIONS = {
    "01": ("01 - Contents and Credits.md", 1, 5),
    "02": ("02 - Catspaw.md", 5, 9),
    "03": ("03 - Fight for Your Life.md", 9, 10),
    "04": ("04 - What You Don't Know Kills You.md", 10, 17),
    "05": ("05 - Arsenal.md", 17, 55),
    "06": ("06 - Armor and Protection.md", 55, 87),
    "07": ("07 - Tactics and Tools.md", 87, 105),
    "08": ("08 - Killshots and More.md", 105, 127),
    "09": ("09 - Martial Arts.md", 127, 142),
    "10": ("10 - Fixin All the Broken Drek.md", 142, 143),
    "11": ("11 - Staying Alive.md", 143, 169),
    "12": ("12 - Blow Up Good.md", 169, 197),
    "13": ("13 - Hostile Extraction.md", 197, 201),
    "14": ("14 - Run and Gun Tables.md", 201, 213),
}


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKC", s)
    for a, b in (
        ("\u2014", "-"),
        ("\u2013", "-"),
        ("—", "-"),
        ("–", "-"),
        ("\u2018", "'"),
        ("\u2019", "'"),
        ("\u201c", '"'),
        ("\u201d", '"'),
        ("\ufb01", "fi"),
        ("\ufb02", "fl"),
    ):
        s = s.replace(a, b)
    s = re.sub(r"\s+", " ", s)
    return s.lower()


def compact(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", norm(s))


def phrases(page_text: str, min_len: int = 24) -> list[str]:
    out: list[str] = []
    for raw in page_text.splitlines():
        line = raw.strip()
        if len(line) < min_len:
            continue
        if re.match(r"^>>|^<<|RUN\s*&\s*GUN|CONTENTS/CREDITS", line, re.I):
            continue
        if re.match(r"^\d+\s+.+\s*>>\s*$", line):
            continue
        if line.upper() in {
            "ACC",
            "REACH",
            "DV",
            "AP",
            "AVAIL",
            "COST",
            "ITEM",
            "MODE",
            "AMMO",
            "RC",
            "NAME",
            "PAGE",
            "PART",
            "THRESHOLD",
            "PRICE",
        }:
            continue
        out.append(line)
    return out


def check(chap: str) -> None:
    fname, start, end = SECTIONS[chap]
    path = OUT / fname
    md = path.read_text(encoding="utf-8")
    md_n = norm(md)
    md_c = compact(md)
    doc = fitz.open(str(PDF))
    pdf = "".join((doc[i].get_text("text") or "") for i in range(start, end))
    pdf_n = norm(pdf)

    print(f"=== {fname} (PDF idx {start}-{end - 1}) ===")
    print(f"exists: {path.exists()} size={path.stat().st_size}")
    print(f"has H1: {md.startswith('# ')}")
    print(f"has Source line: {'**Source:**' in md}")
    print(f"emdash: {('—' in md) or ('\u2014' in md)}")
    body = md.split("**Source:**", 1)[-1]
    if "\n" in body:
        body = body.split("\n", 1)[1]
    ratio = len(body) / max(1, len(pdf))
    print(f"size ratio md/pdf: {ratio:.2f}")

    # word overlap (alpha words len>=4)
    def words(t: str) -> set[str]:
        return set(re.findall(r"[a-z][a-z']{3,}", norm(t)))

    pw, mw = words(pdf), words(md)
    # ignore common running-header leftovers
    noise = {
        "arsenal",
        "contents",
        "credits",
        "killshots",
        "martial",
        "staying",
        "alive",
        "tactics",
        "tools",
        "armor",
        "protection",
        "hostile",
        "extraction",
        "tables",
        "blow",
        "good",
        "catspaw",
        "fixin",
        "broken",
        "drek",
    }
    miss = sorted(w for w in (pw - mw) if w not in noise)
    print(f"missing words (>=4): {len(miss)}")
    if miss:
        print("  sample:", ", ".join(miss[:40]))

    # per-page phrase hits
    weak = []
    for i in range(start, end):
        sample = sorted(phrases(doc[i].get_text("text") or ""), key=len, reverse=True)[:10]
        if not sample:
            continue
        hits = 0
        misses = []
        for p in sample:
            chunk = compact(p)[:36]
            if chunk and chunk in md_c:
                hits += 1
            else:
                # try first 30 of norm
                if norm(p)[:30] in md_n:
                    hits += 1
                else:
                    misses.append(p[:70])
        rate = hits / len(sample)
        if rate < 0.8:
            weak.append((i + 1, rate, misses[:3]))
    print(f"weak pages (<80% phrase hit): {len(weak)}")
    for page, rate, misses in weak:
        print(f"  PDF p{page} hit={rate:.0%}")
        for m in misses:
            print(f"    miss: {m}")

    # glued-word heuristic
    glued = re.findall(r"[a-z]{4,}[A-Z][a-z]{2,}", md)
    print(f"camelGlue candidates: {len(glued)}")
    if glued:
        print("  ", glued[:15])

    # heading count
    h2 = len(re.findall(r"^## ", md, re.M))
    print(f"## headings: {h2}")
    print("PASS" if ratio >= 0.85 and len(weak) == 0 and not (("—" in md) or ("\u2014" in md)) else "NEEDS_WORK")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("chap", choices=sorted(SECTIONS))
    args = ap.parse_args()
    check(args.chap)


if __name__ == "__main__":
    main()
