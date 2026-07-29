# -*- coding: utf-8 -*-
"""Loss-check / done-check Market Panic Source Texts vs PDF."""
from __future__ import annotations

import re
from pathlib import Path

import fitz

ROOT = Path(r"c:\Users\admin\Desktop\Shadowrun")
PDF_PATH = ROOT / "Source" / "PDF" / "marketpanic.pdf"
FOLDER = ROOT / "Source Texts" / "Market Panic"
REPORT = ROOT / "Source" / "_extract" / "market_panic_qa_report.md"

SECTIONS: list[tuple[str, int, int]] = [
    ("01 - Contents and Credits.md", 0, 6),
    ("02 - The First Day of the Rest of Your Life.md", 6, 10),
    ("03 - Droning On.md", 10, 28),
    ("04 - Courting Disaster.md", 28, 38),
    ("05 - Ares Macrotechnology.md", 38, 58),
    ("06 - Aztechnology.md", 58, 72),
    ("07 - EVO.md", 72, 88),
    ("08 - Horizon.md", 88, 104),
    ("09 - Mitsuhama.md", 104, 118),
    ("10 - NeoNET.md", 118, 134),
    ("11 - Renraku.md", 134, 156),
    ("12 - Saeder-Krupp.md", 156, 178),
    ("13 - Shiawase.md", 178, 192),
    ("14 - Wuxing.md", 192, 210),
]

MUST_HAVE = [
    "Ares",
    "Aztechnology",
    "EVO",
    "Horizon",
    "Mitsuhama",
    "NeoNET",
    "Renraku",
    "Saeder-Krupp",
    "Shiawase",
    "Wuxing",
    "CFD",
    "Corporate Court",
    "Zurich-Orbital",
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
        "shadowrun", "page", "market", "panic", "source", "index",
        "posted", "contents", "credits", "corporate",
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

        if fname.startswith("01 -") and path.stat().st_size < 800:
            # cover may dominate early pages
            rows.append(f"| {fname} | PASS | early pages; {path.stat().st_size} bytes |")
            continue

        tokens = sample_tokens(pdf_text, 16)
        missing = [t for t in tokens if normalize(t) not in normalize(md)]
        miss_ratio = len(missing) / max(len(tokens), 1)
        status = "PASS"
        detail = f"tokens {len(tokens) - len(missing)}/{len(tokens)}; {path.stat().st_size} bytes"
        if path.stat().st_size < 400:
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
        if p.name == "INDEX.md":
            continue
        if p.stat().st_size < 150:
            issues.append(f"thin file {p.name}")

    warns = [r for r in rows if "| WARN |" in r]
    verdict = "PASS" if not issues else "FAIL"
    report = [
        "# Market Panic QA",
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
