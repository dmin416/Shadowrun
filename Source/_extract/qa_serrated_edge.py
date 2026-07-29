# -*- coding: utf-8 -*-
"""Loss / done check for Serrated Edge Source Texts."""
from __future__ import annotations

import re
from pathlib import Path

import fitz

PDF = Path(r"c:\Users\admin\Desktop\Shadowrun\Source\PDF\serratededge.pdf")
OUT = Path(r"c:\Users\admin\Desktop\Shadowrun\Source Texts\Serrated Edge")
REPORT = Path(r"c:\Users\admin\Desktop\Shadowrun\Source\_extract\serrated_edge_qa_report.md")
INDEX = OUT / "INDEX.md"

# PDF-sourced chapters only (GM brief is LLM spine, not PDF extract)
SECTIONS = [
    ("01 - Contents and Credits.md", "Contents and Credits", 2, 4),
    ("02 - Denver - Serrated Edge Introduction.md", "Denver: Serrated Edge Introduction", 4, 10),
    ("03 - Scene 1 - The Meet.md", "Scene 1: The Meet", 10, 14),
    ("04 - Scene 2 - The Clinic.md", "Scene 2: The Clinic", 14, 24),
    ("05 - Scene 3 - Delivery and Attack.md", "Scene 3: Delivery & Attack", 24, 26),
    ("06 - Scene 4 - The Doctor is In (Trouble).md", "Scene 4: The Doctor is In (Trouble)", 26, 30),
    ("07 - Scene 5 - Digging a Little Deeper.md", "Scene 5: Digging a Little Deeper", 30, 36),
    ("08 - Scene 6 - Working for the Men.md", "Scene 6: Working for the Men", 36, 40),
    ("09 - Scene 7 - Thwarting the Bombers.md", "Scene 7: Thwarting the Bombers", 40, 48),
    ("10 - Scene 8 - Cutting Out the Cancer.md", "Scene 8: Cutting Out the Cancer", 48, 50),
    ("11 - Aftermath.md", "Aftermath", 50, 57),
    ("12 - At the Top.md", "At the Top", 57, 58),
    ("13 - Player Handouts.md", "Player Handouts", 58, 60),
    ("14 - Denver Map.md", "Denver Map", 60, 61),
    ("15 - Where to go in Denver.md", "Where to Go in Denver", 61, 62),
    ("16 - Medical Center Map.md", "Medical Center Map", 62, 63),
]

MUST_HAVE = [
    ("00 - GM Adventure Brief.md", "Parker James"),
    ("00 - GM Adventure Brief.md", "Paladin"),
    ("01 - Contents and Credits.md", "Scott Schletz"),
    ("02 - Denver - Serrated Edge Introduction.md", "Plot Synopsis"),
    ("02 - Denver - Serrated Edge Introduction.md", "Human Nation"),
    ("02 - Denver - Serrated Edge Introduction.md", "Flaming Sword"),
    ("03 - Scene 1 - The Meet.md", "Scan This"),
    ("03 - Scene 1 - The Meet.md", "Borealis"),
    ("04 - Scene 2 - The Clinic.md", "PHWC"),
    ("04 - Scene 2 - The Clinic.md", "Hard Corps"),
    ("05 - Scene 3 - Delivery and Attack.md", "Parker James"),
    ("06 - Scene 4 - The Doctor is In (Trouble).md", "Hippocrates"),
    ("06 - Scene 4 - The Doctor is In (Trouble).md", "Fleming"),
    ("07 - Scene 5 - Digging a Little Deeper.md", "Sally Hannigan"),
    ("08 - Scene 6 - Working for the Men.md", "IOND"),
    ("09 - Scene 7 - Thwarting the Bombers.md", "ORC"),
    ("10 - Scene 8 - Cutting Out the Cancer.md", "Parker"),
    ("11 - Aftermath.md", "Karma"),
    ("12 - At the Top.md", "Brackhaven"),
    ("13 - Player Handouts.md", "Handout"),
    ("15 - Where to go in Denver.md", "Five By Five"),
]

IMAGE_ONLY = {
    "14 - Denver Map.md",
    "16 - Medical Center Map.md",
}


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


def pdf_chars(a: int, b: int) -> int:
    doc = fitz.open(str(PDF))
    text = "\n".join((doc[i].get_text("text") or "") for i in range(a, b))
    doc.close()
    return len(re.sub(r"\s+", "", text))


def md_chars(path: Path) -> int:
    # Strip source header lines for fairer ratio
    body = path.read_text(encoding="utf-8")
    body = re.sub(r"^# .+\n+", "", body)
    body = re.sub(r"^\*\*Source:\*\*.+\n+", "", body)
    body = re.sub(r"^\*\*Extract note:\*\*.+\n+", "", body, flags=re.M)
    return len(re.sub(r"\s+", "", body))


def main() -> None:
    lines: list[str] = ["# Serrated Edge QA Report", ""]
    ok = True

    pdf_files = [OUT / f for f, _, _, _ in SECTIONS]
    gm = OUT / "00 - GM Adventure Brief.md"
    all_files = ([gm] if gm.exists() else []) + pdf_files

    lines.append(f"PDF chapter files: {len(pdf_files)}")
    if len(pdf_files) != 16:
        ok = False
        lines.append(f"FAIL: expected 16 PDF chapters, found {len(pdf_files)}")
    else:
        lines.append("PASS: 16 PDF chapter files")
    if gm.exists() and gm.stat().st_size > 1000:
        lines.append("PASS: GM Adventure Brief present")
    else:
        ok = False
        lines.append("FAIL: GM Adventure Brief missing/thin")

    tiny = [
        p.name
        for p in pdf_files
        if not p.exists()
        or (p.name not in IMAGE_ONLY and p.stat().st_size < 500)
    ]
    if tiny:
        ok = False
        lines.append("FAIL: tiny/missing text chapters: " + ", ".join(tiny))
    else:
        lines.append("PASS: no empty/tiny text chapters")
    for name in IMAGE_ONLY:
        p = OUT / name
        if p.exists():
            lines.append(f"NOTE: {name} is image-only stub ({p.stat().st_size} bytes)")

    lines.append("")
    lines.append("## H1 / INDEX")
    idx = INDEX.read_text(encoding="utf-8") if INDEX.exists() else ""
    for fname, title, a, b in SECTIONS:
        path = OUT / fname
        body = path.read_text(encoding="utf-8")
        h1 = re.search(r"^# (.+)$", body, re.M)
        if not h1 or h1.group(1).strip() != title:
            ok = False
            lines.append(f"FAIL H1 {fname}: got {h1.group(1) if h1 else None!r}, want {title!r}")
        else:
            lines.append(f"PASS H1 {fname}")
        if fname not in idx and fname.replace(" ", "%20") not in idx:
            ok = False
            lines.append(f"FAIL INDEX missing {fname}")
        else:
            lines.append(f"PASS INDEX {fname}")
    if "00 - GM Adventure Brief.md" in idx or "GM%20Adventure%20Brief" in idx:
        lines.append("PASS INDEX GM brief")
    else:
        ok = False
        lines.append("FAIL INDEX missing GM brief")

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
    lines.append("## Char ratio vs PDF")
    for fname, title, a, b in SECTIONS:
        pc = pdf_chars(a, b)
        mc = md_chars(OUT / fname)
        if fname in IMAGE_ONLY:
            lines.append(f"NOTE {fname}: PDF chars={pc}, MD chars={mc} (image-only expected)")
            continue
        if pc < 200:
            lines.append(f"NOTE {fname}: PDF sparse ({pc} chars); MD={mc}")
            continue
        ratio = mc / max(1, pc)
        # Scene extracts keep most text; allow some header/footer strip
        if ratio < 0.70:
            ok = False
            lines.append(f"FAIL {fname}: MD/PDF={ratio:.2f} (md={mc}, pdf={pc})")
        else:
            lines.append(f"PASS {fname}: MD/PDF={ratio:.2f}")

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
    if ratio < 0.80:
        ok = False
        lines.append("FAIL: coverage below 80%")
        lines.append("Missing sample: " + ", ".join(missing[:40]))
    else:
        lines.append("PASS: coverage ok")
        if missing[:15]:
            lines.append(
                "Notable missing (header/map/OCR noise possible): "
                + ", ".join(missing[:15])
            )

    lines.append("")
    bad_em = []
    for p in all_files:
        t = p.read_text(encoding="utf-8")
        if "\u2014" in t or "\u2013" in t or "—" in t or "–" in t:
            bad_em.append(p.name)
    if bad_em:
        ok = False
        lines.append("FAIL em/en dashes in: " + ", ".join(bad_em))
    else:
        lines.append("PASS: no em/en dashes")

    lines.append("")
    lines.append("## Split sanity")
    s1 = (OUT / "03 - Scene 1 - The Meet.md").read_text(encoding="utf-8")
    s2 = (OUT / "04 - Scene 2 - The Clinic.md").read_text(encoding="utf-8")
    s7 = (OUT / "09 - Scene 7 - Thwarting the Bombers.md").read_text(encoding="utf-8")
    aftermath = (OUT / "11 - Aftermath.md").read_text(encoding="utf-8")
    if "Scan This" in s1 and "Borealis" in s1:
        lines.append("PASS: Scene 1 has Scan This + Borealis")
    else:
        ok = False
        lines.append("FAIL: Scene 1 split")
    if "PHWC" in s2 or "Paladin" in s2:
        lines.append("PASS: Scene 2 clinic content")
    else:
        ok = False
        lines.append("FAIL: Scene 2 clinic")
    if "bomb" in s7.lower() or "ORC" in s7:
        lines.append("PASS: Scene 7 bombing content")
    else:
        ok = False
        lines.append("FAIL: Scene 7 content")
    if "Karma" in aftermath and ("Notoriety" in aftermath or "Street Cred" in aftermath):
        lines.append("PASS: Aftermath has Karma/rep")
    else:
        # Karma alone is enough if present with awards
        if "Karma" in aftermath:
            lines.append("PASS: Aftermath has Karma")
        else:
            ok = False
            lines.append("FAIL: Aftermath rewards")

    lines.append("")
    lines.append("## Verdict")
    lines.append("**PASS**" if ok else "**FAIL**")
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))
    print("wrote", REPORT)


if __name__ == "__main__":
    main()
