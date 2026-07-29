# -*- coding: utf-8 -*-
"""Loss / done check for Aetherology Source Texts."""
from __future__ import annotations

import re
from pathlib import Path

import fitz

PDF = Path(r"c:\Users\admin\Desktop\Shadowrun\Source\PDF\Shadowrun_5E_Aetherology.pdf")
OUT = Path(r"c:\Users\admin\Desktop\Shadowrun\Source Texts\Aetherology")
REPORT = Path(r"c:\Users\admin\Desktop\Shadowrun\Source\_extract\aetherology_qa_report.md")

MUST_HAVE = [
    ("01 - Shadowrun Aetherology.md", "Adam Large"),
    ("01 - Shadowrun Aetherology.md", "Topps"),
    ("02 - JackPoint.md", "JackPoint"),
    ("02 - JackPoint.md", "Magister"),
    ("03 - Astral Sea.md", "Aetherology"),
    ("03 - Astral Sea.md", "Dweller"),
    ("03 - Astral Sea.md", "Al Azif"),
    ("04 - Metaplanes.md", "Plane of Faerie"),
    ("04 - Metaplanes.md", "Seelie"),
    ("04 - Metaplanes.md", "Metaplane of Man"),
    ("04 - Metaplanes.md", "Muspellheim"),
    ("04 - Metaplanes.md", "Desh'veroi"),
    ("04 - Metaplanes.md", "Vhortas"),
    ("04 - Metaplanes.md", "Remembering Carlos"),
    ("05 - Greater Beings in Astral Space.md", "Dweller on the Threshold"),
    ("05 - Greater Beings in Astral Space.md", "Hungry Void"),
    ("05 - Greater Beings in Astral Space.md", "Violet Gas"),
    ("05 - Greater Beings in Astral Space.md", "Deep Metaplanes"),
    ("06 - Rules.md", "Astral Rift"),
    ("06 - Rules.md", "Background Count"),
    ("06 - Rules.md", "Maya Cloud"),
    ("06 - Rules.md", "Gum Toad"),
    ("06 - Rules.md", "Tsuchigumo"),
    ("06 - Rules.md", "Korrigan Pact"),
    ("06 - Rules.md", "Transfer Energy"),
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
    lines: list[str] = ["# Aetherology QA Report", ""]
    ok = True

    files = sorted(p for p in OUT.glob("*.md") if p.name != "INDEX.md")
    lines.append(f"Chapter files: {len(files)}")
    if len(files) != 6:
        ok = False
        lines.append(f"FAIL: expected 6 chapter files, found {len(files)}")
    else:
        lines.append("PASS: 6 chapter files")

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
    sample = sorted(w for w in pw if len(w) >= 5)[:500]
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
            lines.append("Notable missing (soft-hyphen noise possible): " + ", ".join(missing[:15]))

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

    # Mid-page split sanity
    lines.append("")
    lines.append("## Split sanity")
    meta = (OUT / "04 - Metaplanes.md").read_text(encoding="utf-8")
    greater = (OUT / "05 - Greater Beings in Astral Space.md").read_text(encoding="utf-8")
    rules = (OUT / "06 - Rules.md").read_text(encoding="utf-8")
    if "Twisted Web" in meta and "GREATER BEINGS" not in meta.upper().replace(
        "GREATER BEINGS IN ASTRAL SPACE", ""
    ):
        # chapter 04 should end with Twisted Web, not contain Rules
        pass
    if "Twisted Web" in meta and "Below are rules" not in meta:
        lines.append("PASS: Metaplanes ends before Rules body")
    else:
        ok = False
        lines.append("FAIL: Metaplanes/Rules boundary")
    if "Dweller on the Threshold" in greater and "Deep Metaplanes" in greater:
        lines.append("PASS: Greater Beings has Dweller + Deep Metaplanes")
    else:
        ok = False
        lines.append("FAIL: Greater Beings missing key sections")
    if "Below are rules" in rules and "Gum Toad" in rules:
        lines.append("PASS: Rules has intro + spirits")
    else:
        ok = False
        lines.append("FAIL: Rules missing intro/spirits")
    if "Twisted Web" in meta and "We thought we were all powerful" not in meta:
        lines.append("PASS: Metaplanes does not include Greater Beings intro")
    else:
        ok = False
        lines.append("FAIL: Greater Beings intro leaked into Metaplanes")

    lines.append("")
    lines.append("## Verdict")
    lines.append("**PASS**" if ok else "**FAIL**")
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))
    print("wrote", REPORT)


if __name__ == "__main__":
    main()
