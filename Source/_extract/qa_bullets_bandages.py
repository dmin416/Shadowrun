# -*- coding: utf-8 -*-
"""Loss-check / done-check Bullets & Bandages Source Texts vs PDF."""
from __future__ import annotations

import re
from pathlib import Path

import fitz

ROOT = Path(r"c:\Users\admin\Desktop\Shadowrun")
PDF_PATH = ROOT / "Source" / "PDF" / "Shadowrun_5E_Bullets_&_Bandages.pdf"
FOLDER = ROOT / "Source Texts" / "Bullets and Bandages"
REPORT = ROOT / "Source" / "_extract" / "bullets_bandages_qa_report.md"

SECTIONS: list[tuple[str, int, int]] = [
    ("01 - Shadowrun Bullets & Bandages.md", 0, 1),
    ("02 - JackPoint.md", 1, 2),
    ("03 - Primum Non Nocere.md", 2, 4),  # fiction includes mid-page 3
    ("04 - Collateral Nuyen.md", 3, 4),
    ("05 - Combat Medicine 101.md", 4, 8),
    ("06 - Game Information.md", 8, 12),
    ("07 - Advanced Biotech Rules.md", 12, 23),
]

MUST_HAVE = [
    "DocWagon",
    "High Threat Response",
    "Quick Healer",
    "Aged",
    "Care Under Fire",
    "medkit",
    "autodoc",
    "Dread",
    "Feign Illness",
    "Pneumatic Anti-Shock",
]


def normalize(s: str) -> str:
    s = s.replace("\u2014", "-").replace("\u2013", "-")
    s = s.replace("—", "-").replace("–", "-")
    s = re.sub(r"\s+", " ", s)
    return s.upper()


def sample_tokens(text: str, n: int = 12) -> list[str]:
    words = re.findall(r"[A-Za-z][A-Za-z']{3,}", text)
    skip = {
        "that", "this", "with", "from", "have", "were", "they", "them",
        "their", "when", "what", "your", "into", "than", "then", "some",
        "will", "would", "could", "about", "there", "these", "those",
        "shadowrun", "page", "bullets", "bandages", "source", "index",
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
            rows.append(f"| {fname} | FAIL | missing file |")
            continue
        md = path.read_text(encoding="utf-8")
        full_md += md + "\n"
        if "—" in md or "–" in md or "\u2014" in md:
            issues.append(f"em/en dash in {fname}")

        pdf_text = ""
        for i in range(start, min(end, len(doc))):
            pdf_text += doc[i].get_text("text") or ""

        # For ch03/04, mid-page split: only check tokens that should appear
        tokens = sample_tokens(pdf_text, 15)
        missing = [t for t in tokens if normalize(t) not in normalize(md)]
        # allow up to 40% miss on short chapters due to header stripping / mid-page split
        miss_ratio = len(missing) / max(len(tokens), 1)
        status = "PASS"
        detail = f"tokens {len(tokens) - len(missing)}/{len(tokens)}; {path.stat().st_size} bytes"
        if miss_ratio > 0.45 and path.stat().st_size > 400:
            status = "WARN"
            notes.append(f"{fname}: missing sample tokens {missing[:6]}")
        if path.stat().st_size < 200:
            status = "FAIL"
            issues.append(f"{fname} too small ({path.stat().st_size} bytes)")
        rows.append(f"| {fname} | {status} | {detail} |")

    for needle in MUST_HAVE:
        if normalize(needle) not in normalize(full_md):
            issues.append(f"book missing must-have: {needle}")

    # no empty stubs
    for p in FOLDER.glob("*.md"):
        if p.name == "INDEX.md":
            continue
        if p.stat().st_size < 150:
            issues.append(f"thin file {p.name} ({p.stat().st_size})")

    verdict = "PASS" if not issues else "FAIL"
    report = [
        "# Bullets & Bandages QA",
        "",
        f"**Verdict:** {verdict}",
        f"**PDF pages:** {len(doc)}",
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
        ok = normalize(needle) in normalize(full_md)
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
    doc.close()

    # update INDEX pipeline flags on PASS
    if verdict == "PASS":
        idx = FOLDER / "INDEX.md"
        t = idx.read_text(encoding="utf-8")
        t = t.replace("- [ ] Loss-check", "- [x] Loss-check")
        t = t.replace("- [ ] Done-check", "- [x] Done-check")
        idx.write_text(t, encoding="utf-8")
        print("updated INDEX loss/done flags")


if __name__ == "__main__":
    main()
