# -*- coding: utf-8 -*-
"""Loss-check / done-check Chrome Flesh Source Texts vs chromeflesh.pdf."""
from __future__ import annotations

import re
from pathlib import Path

import pypdf

ROOT = Path(r"c:\Users\admin\Desktop\Shadowrun")
PDF_PATH = ROOT / "Source" / "PDF" / "chromeflesh.pdf"
FOLDER = ROOT / "Source Texts" / "Chrome Flesh"
REPORT = ROOT / "Source" / "_extract" / "chrome_flesh_qa_report.md"

# (filename, title needle for PDF header, printed start page, printed end exclusive)
# Printed page N is at PDF index N for this book (cover/blank = 0-1).
SECTIONS: list[tuple[str, str, int, int]] = [
    ("01 - Contents and Credits.md", "CONTENTS", 2, 3),
    ("02 - Introduction.md", "INTRODUCTION", 3, 4),
    ("03 - My Brother's Keeper.md", "BROTHER", 4, 8),
    ("04 - Clusterfcked - Augments post-CFD.md", "CLUSTER", 8, 26),
    ("05 - Fixing What's Broke.md", "FIXING", 26, 54),
    ("06 - Enhanced Life.md", "ENHANCED LIFE", 54, 62),
    ("07 - Shiny - The Latest Chrome.md", "SHINY", 62, 94),
    ("08 - The Body Redefined.md", "BODY REDEFINED", 94, 126),
    ("09 - Steeling the Future.md", "STEELING", 126, 130),
    ("10 - Hacking the Metahuman Code.md", "HACKING THE METAHUMAN", 130, 168),
    ("11 - Quick & Dirty Augmentations.md", "QUICK", 168, 194),
    ("12 - The Murky Future.md", "MURKY", 194, 222),
    ("13 - Compiled Augmentation Tables.md", "COMPILED AUGMENTATION", 222, 240),
]

MUST_HAVE = [
    "Attention coprocessor",
    "Cognitive fragmentation",
    "CFD",
    "Increased Costs",
    "Control rig",
    "Muscle augmentation",
    "Nanite hunters",
    "Genetic optimization",
    "Phalanx",
    "Reverser",
]


def normalize(s: str) -> str:
    s = s.replace("\u2014", "-").replace("\u2013", "-")
    s = s.replace("—", "-").replace("–", "-")
    s = re.sub(r"\s+", " ", s)
    return s.upper()


def sample_tokens(text: str, n: int = 10) -> list[str]:
    words = re.findall(r"[A-Za-z][A-Za-z']{3,}", text)
    skip = {
        "that", "this", "with", "from", "have", "were", "they", "them",
        "their", "when", "what", "your", "into", "than", "then", "some",
        "will", "would", "could", "about", "there", "these", "those",
        "shadowrun", "page", "contents", "credits", "chrome", "flesh",
    }
    out: list[str] = []
    seen: set[str] = set()
    for w in words:
        lw = w.lower()
        if lw in skip or lw in seen:
            continue
        seen.add(lw)
        out.append(w)
        if len(out) >= n:
            break
    return out


def main() -> None:
    pdf = pypdf.PdfReader(str(PDF_PATH))
    n_pages = len(pdf.pages)
    issues: list[str] = []
    notes: list[str] = []
    chapter_rows: list[str] = []

    idx = FOLDER / "INDEX.md"
    if not idx.exists():
        issues.append("Missing INDEX.md")
    else:
        idx_text = idx.read_text(encoding="utf-8")
        for fname, _, _, _ in SECTIONS:
            if fname.replace(" ", "%20") not in idx_text and fname not in idx_text:
                # loose: stem title
                title = fname.split(" - ", 1)[-1].replace(".md", "")
                if title not in idx_text:
                    issues.append(f"INDEX may not link {fname}")

    all_text_parts: list[str] = []
    for fname, needle, start, end in SECTIONS:
        path = FOLDER / fname
        if not path.exists():
            issues.append(f"Missing {fname}")
            chapter_rows.append(f"| {fname} | FAIL | missing file |")
            continue
        body = path.read_text(encoding="utf-8")
        all_text_parts.append(body)
        size = path.stat().st_size
        chap_issues: list[str] = []
        if size < 200:
            chap_issues.append(f"thin ({size}B)")
        if not body.startswith("# "):
            chap_issues.append("no H1")
        soft = body.count("\u00ad")
        em = body.count("\u2014")
        if soft:
            chap_issues.append(f"{soft} soft hyphens")
        if em:
            chap_issues.append(f"{em} em dashes")
        giant = sum(1 for ln in body.splitlines() if len(ln) >= 1200)
        if giant:
            chap_issues.append(f"{giant} paras >=1200 chars")

        # PDF header needle on start page
        if start < n_pages:
            head = (pdf.pages[start].extract_text() or "")[:500].upper()
            if needle not in head and needle not in (pdf.pages[start].extract_text() or "").upper():
                # ch03 fiction may not have chapter title on page
                if fname.startswith("03"):
                    notes.append(f"{fname}: fiction start; needle soft-check skipped")
                else:
                    chap_issues.append(f"PDF p{start} missing needle {needle}")

        # Loss sample mid-chapter
        sample_idxs = [start]
        if end - start > 3:
            sample_idxs.append(start + (end - start) // 2)
        body_n = normalize(body)
        for si in sample_idxs:
            if si >= n_pages:
                continue
            page_txt = pdf.pages[si].extract_text() or ""
            if len(page_txt.strip()) < 40:
                continue
            # Prefer text after chapter needle so shared pages (credits+intro) don't false-fail
            upper = page_txt.upper()
            cut = upper.find(needle)
            sample_src = page_txt[cut:] if cut >= 0 else page_txt
            tokens = sample_tokens(sample_src, 8)
            hits = sum(1 for tok in tokens if normalize(tok) in body_n)
            if tokens and hits < max(2, len(tokens) // 3):
                chap_issues.append(
                    f"loss vs PDF idx {si}: {hits}/{len(tokens)} tokens "
                    f"({', '.join(tokens[:5])})"
                )

        status = "PASS" if not chap_issues else "FAIL"
        detail = "; ".join(chap_issues) if chap_issues else "ok"
        chapter_rows.append(f"| {fname} | {status} | {detail} |")
        for c in chap_issues:
            issues.append(f"{fname}: {c}")

    all_n = normalize("\n".join(all_text_parts))
    missing_must = [m for m in MUST_HAVE if normalize(m) not in all_n]
    if missing_must:
        issues.append(f"Missing must-have markers: {', '.join(missing_must)}")

    # Coverage orphans
    covered: set[int] = set()
    for _, _, start, end in SECTIONS:
        for i in range(start, end):
            covered.add(i)
    orphans = [i for i in range(2, min(240, n_pages)) if i not in covered]
    if orphans:
        notes.append(f"Unmapped PDF indices (sample): {orphans[:15]}")

    ok = not issues
    lines = [
        "# Chrome Flesh QA report",
        "",
        f"PDF: `{PDF_PATH.name}` ({n_pages} pages)",
        f"Folder: `Source Texts/Chrome Flesh/`",
        f"Overall: **{'PASS' if ok else 'FAIL'}**",
        "",
        "## Chapters",
        "",
        "| File | Status | Notes |",
        "| --- | --- | --- |",
        *chapter_rows,
        "",
        "## Issues",
        "",
    ]
    if issues:
        lines.extend(f"- {x}" for x in issues)
    else:
        lines.append("- None")
    lines.extend(["", "## Notes", ""])
    if notes:
        lines.extend(f"- {x}" for x in notes)
    else:
        lines.append("- None")
    lines.append("")
    REPORT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Overall: {'PASS' if ok else 'FAIL'} ({len(issues)} issues)")
    for x in issues[:30]:
        print(" -", x)
    print("wrote", REPORT)


if __name__ == "__main__":
    main()
