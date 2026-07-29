# -*- coding: utf-8 -*-
"""Loss-check / done-check Complete Trog Source Texts vs PDF."""
from __future__ import annotations

import re
from pathlib import Path

import fitz

ROOT = Path(r"c:\Users\admin\Desktop\Shadowrun")
PDF_PATH = ROOT / "Source" / "PDF" / "completetrog.pdf"
FOLDER = ROOT / "Source Texts" / "Complete Trog"
REPORT = ROOT / "Source" / "_extract" / "complete_trog_qa_report.md"

SECTIONS: list[tuple[str, int, int]] = [
    ("01 - Contents and Credits.md", 2, 5),
    ("02 - Introduction.md", 5, 6),
    ("03 - JackPoint.md", 6, 8),
    ("04 - Belinda.md", 8, 12),
    ("05 - What Are You.md", 12, 20),
    ("06 - Living as a Trog In.md", 20, 60),
    ("07 - True Blue Trog.md", 60, 65),
    ("08 - Working As a Trog In.md", 65, 98),
    ("09 - Trog Heroes.md", 98, 122),
    ("10 - Trog Enemies.md", 122, 132),
    ("11 - Trog Runners.md", 132, 164),
    ("12 - United We Stomp.md", 164, 184),
    ("13 - Everything Trog.md", 184, 194),
]

MUST_HAVE = [
    "Black Forest",
    "Suzie Blue",
    "Humanis",
    "Ork Rights Committee",
    "Antenna Grill",
    "Or'zet",
    "2XL",
    "Bull",
    "Life Modules",
]


def normalize(s: str) -> str:
    s = s.replace("\u2014", "-").replace("\u2013", "-")
    s = s.replace("—", "-").replace("–", "-")
    s = s.replace("'", "'").replace("'", "'")
    s = re.sub(r"\s+", " ", s)
    return s.upper()


def sample_tokens(text: str, n: int = 14) -> list[str]:
    words = re.findall(r"[A-Za-z][A-Za-z']{3,}", text)
    skip = {
        "that", "this", "with", "from", "have", "were", "they", "them",
        "their", "when", "what", "your", "into", "than", "then", "some",
        "will", "would", "could", "about", "there", "these", "those",
        "shadowrun", "page", "complete", "trog", "source", "index",
        "posted", "contents", "credits",
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
    doc = fitz.open(str(PDF_PATH))
    issues: list[str] = []
    notes: list[str] = []
    rows: list[str] = []
    full_md = ""

    for fname, start, end in SECTIONS:
        path = FOLDER / fname
        if not path.exists():
            issues.append(f"MISSING {fname}")
            rows.append(f"| {fname} | FAIL | missing |")
            continue
        md = path.read_text(encoding="utf-8")
        full_md += md + "\n"
        if "—" in md or "–" in md or "\u2014" in md:
            issues.append(f"em/en dash in {fname}")

        pdf_text = ""
        for i in range(start, min(end, len(doc))):
            pdf_text += doc[i].get_text("text") or ""

        tokens = sample_tokens(pdf_text, 16)
        missing = [t for t in tokens if normalize(t) not in normalize(md)]
        miss_ratio = len(missing) / max(len(tokens), 1)
        status = "PASS"
        detail = f"tokens {len(tokens) - len(missing)}/{len(tokens)}; {path.stat().st_size} bytes"
        if path.stat().st_size < 300:
            status = "FAIL"
            issues.append(f"{fname} too small ({path.stat().st_size})")
        elif miss_ratio > 0.5:
            status = "WARN"
            notes.append(f"{fname}: missing sample tokens {missing[:8]}")
        rows.append(f"| {fname} | {status} | {detail} |")

    for needle in MUST_HAVE:
        if normalize(needle) not in normalize(full_md):
            # Or'zet may appear as Orzet without apostrophe
            alt = needle.replace("'", "")
            if normalize(alt) not in normalize(full_md):
                issues.append(f"book missing must-have: {needle}")

    # empty stubs
    for p in FOLDER.glob("*.md"):
        if p.name == "INDEX.md":
            continue
        if p.stat().st_size < 200:
            issues.append(f"thin file {p.name}")

    warns = [r for r in rows if "| WARN |" in r]
    verdict = "PASS" if not issues else "FAIL"
    report = [
        "# Complete Trog QA",
        "",
        f"**Verdict:** {verdict}",
        f"**PDF pages:** {len(doc)}",
        f"**WARN chapters:** {len(warns)}",
        "",
        "## Chapters",
        "",
        "| File | Status | Detail |",
        "| --- | --- | --- |",
        *rows,
        "",
        "## Must-have landmarks",
        "",
    ]
    for needle in MUST_HAVE:
        ok = normalize(needle) in normalize(full_md) or normalize(
            needle.replace("'", "")
        ) in normalize(full_md)
        report.append(f"- [{'x' if ok else ' '}] {needle}")
    report += ["", "## Issues", ""]
    if issues:
        report.extend(f"- {x}" for x in issues)
    else:
        report.append("- (none)")
    if notes:
        report += ["", "## Notes", ""]
        report.extend(f"- {x}" for x in notes)

    REPORT.write_text("\n".join(report) + "\n", encoding="utf-8")
    print(verdict)
    print("wrote", REPORT)
    for x in issues:
        print("ISSUE:", x)
    for x in notes[:10]:
        print("NOTE:", x)
    doc.close()

    if verdict == "PASS":
        idx = FOLDER / "INDEX.md"
        t = idx.read_text(encoding="utf-8")
        t = t.replace("- [ ] Loss-check", "- [x] Loss-check")
        t = t.replace("- [ ] Done-check", "- [x] Done-check")
        idx.write_text(t, encoding="utf-8")
        print("updated INDEX loss/done flags")


if __name__ == "__main__":
    main()
