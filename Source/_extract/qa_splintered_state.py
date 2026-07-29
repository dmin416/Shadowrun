# -*- coding: utf-8 -*-
"""Loss / done check for Splintered State Source Texts."""
from __future__ import annotations

import re
from pathlib import Path

import fitz

PDF = Path(
    r"c:\Users\admin\Desktop\Shadowrun\Source\PDF\pdfcoffee.com_shadowrun-5e-splintered-state-pdf-free.pdf"
)
OUT = Path(r"c:\Users\admin\Desktop\Shadowrun\Source Texts\Splintered State")
REPORT = Path(r"c:\Users\admin\Desktop\Shadowrun\Source\_extract\splintered_state_qa_report.md")

MUST_HAVE = [
    ("02 - Contents & Credits.md", "Devon Oratz"),
    ("03 - Everyone Wants to Change the World.md", "Seth Dietrich"),
    ("04 - Politics and Paydata.md", "Plot Synopsis"),
    ("04 - Politics and Paydata.md", "Operation Daybreak"),
    ("05 - Scene 0 Rounded Up.md", "Scan This"),
    ("05 - Scene 0 Rounded Up.md", "Annie Goldsmith"),
    ("06 - Scene 1 You Know the Drill.md", "Banshee"),
    ("07 - Scene 2 Without a Hitch.md", "Novelty Hills"),
    ("07 - Scene 2 Without a Hitch.md", "Oxycode"),
    ("08 - Scene 3 Lying Down on the Job.md", "Operation Daybreak"),
    ("09 - Scene 4 A Knock at the Door.md", "Caesar"),
    ("10 - Scene 5 Caveat Venditor.md", "basilisk"),
    ("11 - Scene 6 Friends with High Prices.md", "Brackhaven"),
    ("12 - Scene 7 Threading the Needle (Optional).md", "Brackhaven Investments"),
    ("13 - Picking Up the Pieces.md", "Karma"),
    ("14 - Legwork.md", "Seth Dietrich"),
    ("15 - Matrix Legwork.md", "Matrix Search"),
    ("16 - Cast of Shadows.md", "Dana Oaks"),
    ("16 - Cast of Shadows.md", "Tauren"),
    ("17 - But No One Wants to Die.md", "Project Daybreak"),
    ("18 - Player Handouts.md", "Handout"),
]


def pdf_words() -> set[str]:
    doc = fitz.open(str(PDF))
    text = "\n".join((doc[i].get_text("text") or "") for i in range(len(doc)))
    doc.close()
    text = text.replace("\u2014", "-").replace("\u2013", "-")
    words = re.findall(r"[A-Za-z0-9][A-Za-z0-9'/-]{2,}", text)
    return {w.lower() for w in words}


def md_words() -> set[str]:
    blob = []
    for p in OUT.glob("*.md"):
        if p.name == "INDEX.md":
            continue
        blob.append(p.read_text(encoding="utf-8"))
    text = "\n".join(blob)
    words = re.findall(r"[A-Za-z0-9][A-Za-z0-9'/-]{2,}", text)
    return {w.lower() for w in words}


def main() -> None:
    lines: list[str] = ["# Splintered State QA Report", ""]
    ok = True

    files = sorted(p for p in OUT.glob("*.md") if p.name != "INDEX.md")
    lines.append(f"Chapter files: {len(files)}")
    if len(files) != 18:
        ok = False
        lines.append(f"FAIL: expected 18 chapter files, found {len(files)}")
    else:
        lines.append("PASS: 18 chapter files")

    # Cover may be image-only stub; others should be substantial
    tiny = [p.name for p in files if p.stat().st_size < 80]
    if tiny:
        ok = False
        lines.append("FAIL: tiny files: " + ", ".join(tiny))
    else:
        lines.append("PASS: no empty/tiny chapter files")

    cover = OUT / "01 - Shadowrun Splintered State.md"
    if cover.exists() and "No extractable text" in cover.read_text(encoding="utf-8"):
        lines.append("NOTE: ch.01 cover is image-only (expected)")

    lines.append("")
    lines.append("## Phrase checks")
    for fname, phrase in MUST_HAVE:
        path = OUT / fname
        if not path.exists():
            ok = False
            lines.append(f"FAIL missing file: {fname}")
            continue
        body = path.read_text(encoding="utf-8")
        if phrase.lower() not in body.lower():
            ok = False
            lines.append(f"FAIL {fname}: missing `{phrase}`")
        else:
            lines.append(f"PASS {fname}: `{phrase}`")

    lines.append("")
    lines.append("## Word coverage (sample)")
    pw, mw = pdf_words(), md_words()
    sample = sorted(w for w in pw if len(w) >= 5)[:600]
    missing = [w for w in sample if w not in mw]
    ratio = 1 - (len(missing) / max(1, len(sample)))
    lines.append(
        f"Sample coverage vs PDF long words: {ratio:.1%} "
        f"({len(missing)} missing of {len(sample)})"
    )
    if ratio < 0.85:
        ok = False
        lines.append("FAIL: coverage below 85%")
        lines.append("Missing sample: " + ", ".join(missing[:40]))
    else:
        lines.append("PASS: coverage ok")
        if missing[:15]:
            lines.append(
                "Notable missing (soft-hyphen/ad noise possible): "
                + ", ".join(missing[:15])
            )

    lines.append("")
    bad_em = []
    for p in files:
        t = p.read_text(encoding="utf-8")
        if "\u2014" in t or "—" in t:
            bad_em.append(p.name)
    if bad_em:
        ok = False
        lines.append("FAIL em dashes in: " + ", ".join(bad_em))
    else:
        lines.append("PASS: no em dashes")

    lines.append("")
    lines.append("## Split sanity")
    s0 = (OUT / "05 - Scene 0 Rounded Up.md").read_text(encoding="utf-8")
    s4 = (OUT / "09 - Scene 4 A Knock at the Door.md").read_text(encoding="utf-8")
    s5 = (OUT / "10 - Scene 5 Caveat Venditor.md").read_text(encoding="utf-8")
    pick = (OUT / "13 - Picking Up the Pieces.md").read_text(encoding="utf-8")
    matrix = (OUT / "15 - Matrix Legwork.md").read_text(encoding="utf-8")
    cast = (OUT / "16 - Cast of Shadows.md").read_text(encoding="utf-8")

    if "Scan This" in s0 and "Annie Goldsmith" in s0:
        lines.append("PASS: Scene 0 starts at Scan This")
    else:
        ok = False
        lines.append("FAIL: Scene 0 split")
    if "Scan This" in s4 and "Caesar" in s4:
        lines.append("PASS: Scene 4 has Scan This + Caesar")
    else:
        ok = False
        lines.append("FAIL: Scene 4 content")
    if "Caveat Venditor" in s5 or "basilisk" in s5.lower() or "Scan This" in s5:
        lines.append("PASS: Scene 5 body present")
    else:
        ok = False
        lines.append("FAIL: Scene 5 body")
    if "Karma" in pick and "1,000" in pick:
        lines.append("PASS: Picking Up has Money/Karma")
    else:
        ok = False
        lines.append("FAIL: Picking Up content")
    if "Matrix Search" in matrix and "Agent Seth" not in matrix:
        lines.append("PASS: Matrix Legwork before Cast")
    else:
        # Agent Seth might appear in matrix search results as name
        if "Matrix Search" in matrix and "CAST OF SHADOWS" not in matrix.upper():
            lines.append("PASS: Matrix Legwork section present")
        else:
            ok = False
            lines.append("FAIL: Matrix/Cast boundary")
    if "Dana Oaks" in cast and "Tauren" in cast:
        lines.append("PASS: Cast of Shadows has key NPCs")
    else:
        ok = False
        lines.append("FAIL: Cast of Shadows NPCs")

    lines.append("")
    lines.append("## Verdict")
    lines.append("**PASS**" if ok else "**FAIL**")
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))
    print("wrote", REPORT)


if __name__ == "__main__":
    main()
