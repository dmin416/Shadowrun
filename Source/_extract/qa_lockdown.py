# -*- coding: utf-8 -*-
"""Loss-check / done-check Lockdown Source Texts vs PDF."""
from __future__ import annotations

import re
from pathlib import Path

import pypdf

ROOT = Path(r"c:\Users\admin\Desktop\Shadowrun")
PDF_PATH = ROOT / "Source" / "PDF" / "shadowrun-lockdown-pdf.pdf"
FOLDER = ROOT / "Source Texts" / "Lockdown"
REPORT = ROOT / "Source" / "_extract" / "lockdown_qa_report.md"

SECTIONS: list[tuple[str, str, int, int]] = [
    ("01 - Shadowrun Lockdown.md", "COVER", 0, 2),
    ("02 - Contents & Credits.md", "CONTENTS", 2, 6),
    ("03 - JackPoint.md", "JACKPOINT", 6, 7),
    ("04 - Introduction.md", "INTRODUCTION", 7, 8),
    ("05 - Harbor Heist.md", "HARBOR", 8, 12),
    ("06 - A Runner's Guide to Boston.md", "BOSTON", 12, 78),
    ("07 - Locking the Hub.md", "HUB", 78, 106),
    ("08 - Inside the QZ A Wanderer's Guide.md", "QZ", 106, 150),
    ("09 - Beantown Bound.md", "BEANTOWN", 150, 162),
    ("10 - Trainyard Troubles.md", "TRAINYARD", 162, 172),
    ("11 - Digging Deeper.md", "DIGGING", 172, 184),
    ("12 - Bringing Down the House.md", "HOUSE", 184, 198),
    ("13 - Game Information.md", "GAME", 198, 228),
    ("14 - Familiar Faces.md", "FACES", 228, 236),
    ("15 - Special Thanks.md", "THANKS", 236, 242),
]

MUST_HAVE = [
    "Boston",
    "quarantine",
    "CFD",
    "Cognitive Fragmentation",
    "Harbor Heist",
    "Beantown Bound",
    "Trainyard Troubles",
    "Character Trove",
    "Lockdown CFD",
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
        "shadowrun", "page", "contents", "credits", "lockdown", "boston",
        "posted", "jackpoint",
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
            candidates = [
                fname,
                fname.replace(" ", "%20"),
                fname.replace(" ", "%20").replace("&", "%26").replace("'", "%27"),
            ]
            if not any(c in idx_text for c in candidates):
                issues.append(f"INDEX may not link {fname}")

    all_text_parts: list[str] = []
    for fname, _needle, start, end in SECTIONS:
        path = FOLDER / fname
        if not path.exists():
            issues.append(f"Missing {fname}")
            chapter_rows.append(f"| {fname} | FAIL | missing file |")
            continue

        md = path.read_text(encoding="utf-8")
        all_text_parts.append(md)
        if not md.startswith("# "):
            issues.append(f"{fname}: missing H1")

        if "No extractable text" in md:
            pdf_chars = sum(
                len(pdf.pages[i].extract_text() or "")
                for i in range(start, min(end, n_pages))
            )
            if pdf_chars > 200:
                issues.append(f"{fname}: stub but PDF has {pdf_chars} chars")
                chapter_rows.append(f"| {fname} | FAIL | stub vs PDF text |")
            else:
                notes.append(f"{fname}: image-only OK ({pdf_chars} PDF chars)")
                chapter_rows.append(f"| {fname} | PASS | image-only |")
            continue

        pdf_text = "\n".join(
            pdf.pages[i].extract_text() or "" for i in range(start, min(end, n_pages))
        )
        md_body = re.sub(r"^#.*$", "", md, count=1, flags=re.M)
        md_body = re.sub(r"^\*\*Source:\*\*.*$", "", md_body, count=1, flags=re.M)
        md_norm = normalize(md_body)
        pdf_norm = normalize(pdf_text)

        md_alnum = re.sub(r"[^A-Z0-9]", "", md_norm)
        pdf_alnum = re.sub(r"[^A-Z0-9]", "", pdf_norm)
        if len(pdf_alnum) < 50:
            notes.append(f"{fname}: thin PDF text ({len(pdf_alnum)} alnum)")
            chapter_rows.append(f"| {fname} | PASS | thin PDF |")
            continue

        ratio = len(md_alnum) / max(len(pdf_alnum), 1)
        tokens = sample_tokens(pdf_text, 12)
        missing = [t for t in tokens if t.upper() not in md_norm]
        status = "PASS"
        detail = f"ratio={ratio:.2f} md={len(md_alnum)} pdf={len(pdf_alnum)}"
        if ratio < 0.55:
            status = "FAIL"
            issues.append(f"{fname}: low retention {detail}")
        elif ratio < 0.75:
            status = "WARN"
            notes.append(f"{fname}: moderate retention {detail}")
        if len(missing) > 4:
            if status == "PASS":
                status = "WARN"
            notes.append(f"{fname}: missing sample tokens {missing[:6]}")
            detail += f"; missing={missing[:4]}"
        chapter_rows.append(f"| {fname} | {status} | {detail} |")

    combined = "\n".join(all_text_parts)
    for needle in MUST_HAVE:
        if needle.lower() not in combined.lower():
            issues.append(f"Book-wide missing landmark: {needle}")

    em = combined.count("\u2014") + combined.count("—")
    if em:
        issues.append(f"Em dashes present: {em}")

    fail_rows = [r for r in chapter_rows if "| FAIL |" in r]
    hard_fail = [i for i in issues if "Em dashes" not in i]
    overall = "PASS" if not fail_rows and not hard_fail else "FAIL"

    lines = [
        "# Lockdown QA report",
        "",
        f"**Overall:** {overall}",
        f"PDF pages: {n_pages}",
        f"Folder: `Source Texts/Lockdown/`",
        "",
        "## Chapters",
        "",
        "| File | Status | Detail |",
        "| --- | --- | --- |",
        *chapter_rows,
        "",
        "## Issues",
        "",
    ]
    if issues:
        lines.extend(f"- {i}" for i in issues)
    else:
        lines.append("- (none)")
    lines += ["", "## Notes", ""]
    if notes:
        lines.extend(f"- {n}" for n in notes)
    else:
        lines.append("- (none)")
    lines.append("")
    REPORT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Overall {overall}; wrote {REPORT}")
    for i in issues[:20]:
        print("ISSUE:", i)


if __name__ == "__main__":
    main()
