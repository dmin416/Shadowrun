# -*- coding: utf-8 -*-
"""Loss-check / done-check Hard Targets Source Texts vs PDF."""
from __future__ import annotations

import re
from pathlib import Path

import fitz

ROOT = Path(r"c:\Users\admin\Desktop\Shadowrun")
PDF_PATH = ROOT / "Source" / "PDF" / "Shadowrun_5E_Hard_Targets.pdf"
FOLDER = ROOT / "Source Texts" / "Hard Targets"
REPORT = ROOT / "Source" / "_extract" / "hard_targets_qa_report.md"

SECTIONS: list[tuple[str, int, int]] = [
    ("01 - Shadowrun Hard Targets.md", 0, 2),
    ("02 - Table of Contents.md", 2, 4),
    ("03 - Credits.md", 3, 4),
    ("04 - JackPoint.md", 4, 5),
    ("05 - Introduction.md", 5, 6),
    ("06 - Justice for Hire.md", 6, 10),
    ("07 - Desperate Times.md", 10, 42),
    ("08 - ...And Desperate Measures.md", 42, 62),
    ("09 - Killers, Saviors, and Hunters.md", 62, 76),
    ("10 - Slow and Steady Death.md", 76, 80),
    ("11 - Havana Dale A Todo Meter!.md", 80, 144),
    ("12 - Chameleon.md", 144, 148),
    ("13 - Becoming Death.md", 148, 178),
    ("14 - The Wetwork Toolkit.md", 178, 198),
    ("15 - Game Information.md", 198, 208),
]

MUST_HAVE = [
    "Neutral Ground",
    "Havana",
    "CFD",
    "Blackwing",
    "Wetwork",
    "assassin",
    "Ordo Maximus",
    "Aztechnology",
]


def normalize(s: str) -> str:
    s = s.replace("\u2014", "-").replace("\u2013", "-")
    s = s.replace("—", "-").replace("–", "-")
    s = re.sub(r"\s+", " ", s)
    return s.upper()


def sample_tokens(text: str, n: int = 14) -> list[str]:
    words = re.findall(r"[A-Za-z][A-Za-z']{3,}", text)
    skip = {
        "that", "this", "with", "from", "have", "were", "they", "them",
        "their", "when", "what", "your", "into", "than", "then", "some",
        "will", "would", "could", "about", "there", "these", "those",
        "shadowrun", "page", "hard", "targets", "source", "index",
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

        # Cover may be empty
        if fname.startswith("01 -") and path.stat().st_size < 400:
            rows.append(f"| {fname} | PASS | cover stub; {path.stat().st_size} bytes |")
            continue

        tokens = sample_tokens(pdf_text, 16)
        missing = [t for t in tokens if normalize(t) not in normalize(md)]
        miss_ratio = len(missing) / max(len(tokens), 1)
        status = "PASS"
        detail = f"tokens {len(tokens) - len(missing)}/{len(tokens)}; {path.stat().st_size} bytes"
        min_size = 200 if fname.startswith("03 -") else 400
        if path.stat().st_size < min_size and not fname.startswith("01 -"):
            status = "FAIL"
            issues.append(f"{fname} too small ({path.stat().st_size})")
        elif miss_ratio > 0.55 and path.stat().st_size > 500:
            status = "WARN"
            notes.append(f"{fname}: missing sample tokens {missing[:8]}")
        rows.append(f"| {fname} | {status} | {detail} |")

    for needle in MUST_HAVE:
        if normalize(needle) not in normalize(full_md):
            issues.append(f"book missing must-have: {needle}")

    for p in FOLDER.glob("*.md"):
        if p.name == "INDEX.md" or p.name.startswith("01 -"):
            continue
        if p.stat().st_size < 150:
            issues.append(f"thin file {p.name}")

    warns = [r for r in rows if "| WARN |" in r]
    verdict = "PASS" if not issues else "FAIL"
    report = [
        "# Hard Targets QA",
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
    for x in notes[:12]:
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
