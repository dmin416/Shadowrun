# -*- coding: utf-8 -*-
"""Loss-check Seattle Sprawl Source Texts vs PDF page ranges."""
from __future__ import annotations

import re
import unicodedata
from collections import Counter
from pathlib import Path

import fitz

PDF = Path(r"c:\Users\admin\Desktop\Shadowrun\Source\PDF\seattlesprawl.pdf")
ROOT = Path(r"c:\Users\admin\Desktop\Shadowrun\Source Texts\Seattle Sprawl")

# (filename, start_idx inclusive, end_idx exclusive)
SECTIONS = [
    ("01 - Contents and Credits.md", 2, 6),
    ("02 - Whirlwind Tour.md", 6, 10),
    ("03 - Emerald Shadows.md", 10, 13),
    ("04 - Downtown.md", 13, 18),
    ("05 - Bellevue.md", 18, 24),
    ("06 - Tacoma.md", 24, 30),
    ("07 - Everett.md", 30, 34),
    ("08 - Renton.md", 34, 39),
    ("09 - Auburn.md", 39, 45),
    ("10 - Snohomish.md", 45, 52),
    ("11 - Fort Lewis.md", 52, 57),
    ("12 - Redmond.md", 57, 62),
    ("13 - Puyallup.md", 62, 67),
    ("14 - Council Island.md", 67, 72),
    ("15 - Outremer.md", 72, 83),
    ("16 - The Seattle Underground.md", 83, 88),
]

JUNK = re.compile(
    r"^(?:"
    r"\d+$"
    r"|EMERALD SHADOWS"
    r"|SEATTLE SPRAWL"
    r"|SHADOWRUN:?\s*SEATTLE SPRAWL"
    r"|CONTENTS?\s*&?\s*CREDITS?"
    r"|>>.*<<"
    r"|<<.*>>"
    r")$",
    re.I,
)


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKC", s)
    for a, b in (
        ("\u2014", "-"),
        ("\u2013", "-"),
        ("\u2018", "'"),
        ("\u2019", "'"),
        ("\u201c", '"'),
        ("\u201d", '"'),
        ("\ufb01", "fi"),
        ("\ufb02", "fl"),
        ("¥", "YEN"),
        ("™", ""),
    ):
        s = s.replace(a, b)
    s = s.lower()
    s = re.sub(r"[^a-z0-9%]+", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def tokens(text: str) -> list[str]:
    return [t for t in norm(text).split() if len(t) >= 3]


def significant_phrases(text: str) -> set[str]:
    """Pull likely headings / named things from raw PDF text."""
    phrases: set[str] = set()
    for line in text.splitlines():
        s = line.strip()
        if not s or JUNK.match(s):
            continue
        # ALL CAPS short titles
        if re.match(r"^[A-Z0-9][A-Z0-9 /,'\".:&()-]{2,60}$", s) and sum(c.isalpha() for c in s) >= 3:
            phrases.add(norm(s))
        # POSTED BY / TURF / COLORS
        if re.match(r"^(POSTED BY|TURF|COLORS)\b", s, re.I):
            phrases.add(norm(s))
        # Title-ish lines with colon stats
        if re.match(r"^[A-Za-z].{0,40}:\s*\S", s) and len(s) < 80:
            key = s.split(":", 1)[0]
            phrases.add(norm(key))
    return {p for p in phrases if len(p) >= 4}


def main() -> None:
    doc = fitz.open(str(PDF))
    report: list[str] = []
    total_miss_phrases = 0
    total_miss_rare = 0

    for fname, start, end in SECTIONS:
        md_path = ROOT / fname
        md = md_path.read_text(encoding="utf-8") if md_path.exists() else ""
        pdf_parts = []
        for i in range(start, min(end, len(doc))):
            pdf_parts.append(doc[i].get_text("text") or "")
        pdf = "\n".join(pdf_parts)

        pdf_tok = tokens(pdf)
        md_tok = set(tokens(md))
        pdf_count = Counter(pdf_tok)
        md_count = Counter(tokens(md))

        # rare/content words in PDF missing from MD (freq 1-8, length>=5)
        missing_rare = []
        for w, c in pdf_count.items():
            if c > 8 or len(w) < 5:
                continue
            if w in {
                "emerald",
                "shadows",
                "seattle",
                "sprawl",
                "shadowrun",
                "contents",
                "credits",
                "page",
            }:
                continue
            if md_count.get(w, 0) == 0:
                missing_rare.append((c, w))
        missing_rare.sort(reverse=True)

        # significant phrases
        pdf_phrases = significant_phrases(pdf)
        md_norm = norm(md)
        miss_phrases = sorted(p for p in pdf_phrases if p not in md_norm and len(p) >= 5)
        # filter soft misses: phrase words mostly present
        hard_miss = []
        for p in miss_phrases:
            words = p.split()
            if not words:
                continue
            hit = sum(1 for w in words if w in md_tok)
            if hit / len(words) < 0.6:
                hard_miss.append(p)

        pdf_chars = len(re.sub(r"\s+", "", pdf))
        md_chars = len(re.sub(r"\s+", "", md))
        # ignore markdown table pipes etc roughly
        ratio = (md_chars / pdf_chars) if pdf_chars else 0

        total_miss_phrases += len(hard_miss)
        total_miss_rare += len(missing_rare)

        report.append(f"## {fname} (PDF idx {start}-{end - 1})")
        report.append(f"- PDF chars (no ws): {pdf_chars}")
        report.append(f"- MD chars (no ws): {md_chars}")
        report.append(f"- MD/PDF char ratio: {ratio:.2f}")
        report.append(f"- PDF tokens: {len(pdf_tok)} unique={len(pdf_count)}")
        report.append(f"- Hard-miss phrases ({len(hard_miss)}):")
        for p in hard_miss[:25]:
            report.append(f"  - {p}")
        if len(hard_miss) > 25:
            report.append(f"  - ... +{len(hard_miss) - 25} more")
        report.append(f"- Rare PDF tokens missing from MD ({len(missing_rare)}):")
        for c, w in missing_rare[:30]:
            report.append(f"  - {w} (pdf x{c})")
        if len(missing_rare) > 30:
            report.append(f"  - ... +{len(missing_rare) - 30} more")
        report.append("")

        # flag low ratio
        if ratio < 0.75:
            report.append(f"**FLAG: low MD/PDF ratio {ratio:.2f}**")
            report.append("")

    out = Path(r"c:\Users\admin\Desktop\Shadowrun\Source\_extract\seattle_loss_check.md")
    header = [
        "# Seattle Sprawl loss-check",
        "",
        f"Total hard-miss phrases: {total_miss_phrases}",
        f"Total rare missing tokens: {total_miss_rare}",
        "",
        "Hard-miss = ALL-CAPS/title phrases from PDF where <60% of words appear in MD.",
        "Rare missing = PDF tokens len>=5 with freq<=8 absent from MD (noise expected from headers/OCR).",
        "",
    ]
    out.write_text("\n".join(header + report), encoding="utf-8")
    print("wrote", out)
    print("hard-miss phrases", total_miss_phrases)
    print("rare missing tokens", total_miss_rare)


if __name__ == "__main__":
    main()
