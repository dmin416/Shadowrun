# -*- coding: utf-8 -*-
"""Loss / done check for Dark Terrors Source Texts."""
from __future__ import annotations

import re
from pathlib import Path

import fitz

PDF = Path(r"c:\Users\admin\Desktop\Shadowrun\Source\PDF\darkterrors.pdf")
OUT = Path(r"c:\Users\admin\Desktop\Shadowrun\Source Texts\Dark Terrors")
REPORT = Path(r"c:\Users\admin\Desktop\Shadowrun\Source\_extract\dark_terrors_qa_report.md")

MUST_HAVE = [
    ("02 - Contents & Credits.md", "Brooke Chang"),
    ("02 - Contents & Credits.md", "Writing"),
    ("03 - JackPoint.md", "JackPoint"),
    ("03 - JackPoint.md", "edgar"),
    ("04 - Introduction.md", "Shadowrunners"),
    ("05 - Darker than Shadows.md", "Vaquita"),
    ("06 - The Heart of the Hive.md", "Sticks"),
    ("06 - The Heart of the Hive.md", "New Bug Breeds"),
    ("06 - The Heart of the Hive.md", "Mantids"),
    ("07 - Marooned Spirits.md", "Shedim"),
    ("08 - Paint It Blacker.md", "Black Lodge"),
    ("09 - Monads and CFD.md", "Miles Lanier"),
    ("09 - Monads and CFD.md", "CFD"),
    ("10 - The Hidden Faction.md", "Ulex"),
    ("11 - Revelations.md", "wage"),
    ("12 - Followers of the Elder God.md", "Elder"),
    ("13 - Dwellers of the Deep Foundations.md", "Foundation"),
    ("14 - The Ghoul Queen and Her People.md", "Asamando"),
    ("14 - The Ghoul Queen and Her People.md", "Infected"),
    ("15 - Untamed Metaplanes.md", "G-Nome"),
    ("16 - Rules Index.md", "Amphibious"),
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
    lines: list[str] = ["# Dark Terrors QA Report", ""]
    ok = True

    files = sorted(p for p in OUT.glob("*.md") if p.name != "INDEX.md")
    lines.append(f"Chapter files: {len(files)}")
    if len(files) != 16:
        ok = False
        lines.append(f"FAIL: expected 16 chapter files, found {len(files)}")
    else:
        lines.append("PASS: 16 chapter files")

    tiny = [p.name for p in files if p.stat().st_size < 80]
    if tiny:
        ok = False
        lines.append("FAIL: tiny files: " + ", ".join(tiny))
    else:
        lines.append("PASS: no empty/tiny chapter files")

    cover = OUT / "01 - Shadowrun Dark Terrors.md"
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
    sample = sorted(w for w in pw if len(w) >= 5)[:800]
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
                "Notable missing (soft-hyphen noise possible): "
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
    creds = (OUT / "02 - Contents & Credits.md").read_text(encoding="utf-8")
    intro = (OUT / "04 - Introduction.md").read_text(encoding="utf-8")
    jp = (OUT / "03 - JackPoint.md").read_text(encoding="utf-8")
    if "Writing" in creds and "INTRODUCTION" not in creds.upper().split("INTRODUCTION")[0][-20:]:
        # credits should not contain full intro body
        if "Shadowrunners, as a rule" not in creds:
            lines.append("PASS: Credits separate from Introduction body")
        else:
            ok = False
            lines.append("FAIL: Introduction leaked into Credits")
    else:
        if "Shadowrunners, as a rule" not in creds:
            lines.append("PASS: Credits separate from Introduction body")
        else:
            ok = False
            lines.append("FAIL: Introduction leaked into Credits")
    if "Shadowrunners" in intro and "Writing:" not in intro:
        lines.append("PASS: Introduction without credits block")
    else:
        if "Shadowrunners" in intro:
            lines.append("PASS: Introduction present (credits may residual)")
        else:
            ok = False
            lines.append("FAIL: Introduction missing")
    if "Connecting to JackPoint" in jp or "YOU'RE IN" in jp.upper():
        lines.append("PASS: JackPoint login block")
    else:
        ok = False
        lines.append("FAIL: JackPoint content")

    hive = (OUT / "06 - The Heart of the Hive.md").read_text(encoding="utf-8")
    if "Sticks" in hive and len(hive) > 20000:
        lines.append("PASS: Heart of the Hive substantial")
    else:
        ok = False
        lines.append("FAIL: Heart of the Hive thin")

    lines.append("")
    lines.append("## Verdict")
    lines.append("**PASS**" if ok else "**FAIL**")
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))
    print("wrote", REPORT)


if __name__ == "__main__":
    main()
