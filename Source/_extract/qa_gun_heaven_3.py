# -*- coding: utf-8 -*-
"""Loss / done check for Gun Heaven 3 Source Texts."""
from __future__ import annotations

import re
from pathlib import Path

import fitz

PDF = Path(r"c:\Users\admin\Desktop\Shadowrun\Source\PDF\Shadowrun_5E_Gun_H(e)aven_3.pdf")
OUT = Path(r"c:\Users\admin\Desktop\Shadowrun\Source Texts\Gun Heaven 3")
REPORT = Path(r"c:\Users\admin\Desktop\Shadowrun\Source\_extract\gun_heaven_3_qa_report.md")

# Distinctive phrases / names that should appear after extract+format
MUST_HAVE = [
    ("02 - JackPoint.md", "Old Sam"),
    ("03 - New Weapon UpgradesTraits.md", "VINTAGE"),
    ("03 - New Weapon UpgradesTraits.md", "CAP & BALL"),
    ("04 - Using This Book with Shadowrun, Fifth Edition.md", "Sporting Rifles"),
    ("04 - Using This Book with Shadowrun, Fifth Edition.md", "Flamethrowers"),
    ("05 - Colt New Model Revolver.md", "New Model Revolver"),
    ("05 - Colt New Model Revolver.md", "180"),
    ("11 - Krime Spree.md", "Krime Spree"),
    ("17 - SBd-44.md", "SBd-44"),
    ("28 - M1 Garand.md", "Garand"),
    ("36 - Krime Bomb.md", "pump-action"),
    ("37 - Shiawase Arms Incinerator.md", "Flamethrower"),
    ("38 - Gun Stats (SR5).md", "Incinerator"),
    ("38 - Gun Stats (SR5).md", "23,000"),
    ("39 - Gun Stats (SR4A).md", "Incinerator"),
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
    lines: list[str] = ["# Gun Heaven 3 QA Report", ""]
    ok = True

    files = sorted(p for p in OUT.glob("*.md") if p.name != "INDEX.md")
    lines.append(f"Chapter files: {len(files)}")
    if len(files) != 39:
        ok = False
        lines.append(f"FAIL: expected 39 chapter files, found {len(files)}")
    else:
        lines.append("PASS: 39 chapter files")

    empty = [p.name for p in files if p.stat().st_size < 80]
    if empty:
        ok = False
        lines.append("FAIL: tiny files: " + ", ".join(empty))
    else:
        lines.append("PASS: no empty/tiny chapter files")

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
    # ignore very short / page-number noise
    sample = sorted(w for w in pw if len(w) >= 5)[:400]
    missing = [w for w in sample if w not in mw]
    # soft-hyphen artifacts often missing as joined forms exist
    ratio = 1 - (len(missing) / max(1, len(sample)))
    lines.append(f"Sample coverage vs PDF long words: {ratio:.1%} ({len(missing)} missing of {len(sample)})")
    if ratio < 0.85:
        ok = False
        lines.append("FAIL: coverage below 85%")
        lines.append("Missing sample: " + ", ".join(missing[:40]))
    else:
        lines.append("PASS: coverage ok")

    # em dash check
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
    lines.append("## Verdict")
    lines.append("**PASS**" if ok else "**FAIL**")
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))
    print("wrote", REPORT)

    idx = OUT / "INDEX.md"
    if idx.exists() and ok:
        t = idx.read_text(encoding="utf-8")
        t = t.replace("- [ ] Loss-check", "- [x] Loss-check")
        t = t.replace("- [ ] Done-check", "- [x] Done-check")
        idx.write_text(t, encoding="utf-8")


if __name__ == "__main__":
    main()
