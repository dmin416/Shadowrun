# -*- coding: utf-8 -*-
"""Extract Run & Gun PDF into Source Texts/Run and Gun/*.md"""
from __future__ import annotations

import re
from pathlib import Path

import fitz

PDF = Path(r"c:\Users\admin\Desktop\Shadowrun\Source\PDF\runandgun.pdf")
OUT = Path(r"c:\Users\admin\Desktop\Shadowrun\Source Texts\Run and Gun")

# (filename, title, start_pdf_idx inclusive, end_pdf_idx exclusive)
# Print page N ~= PDF page N ~= PDF index N-1 for body text.
SECTIONS = [
    ("01 - Contents and Credits.md", "Contents and Credits", 1, 5),
    ("02 - Catspaw.md", "Catspaw", 5, 9),
    ("03 - Fight for Your Life.md", "Fight for Your Life", 9, 10),
    ("04 - What You Don't Know Kills You.md", "What You Don't Know Kills You", 10, 17),
    ("05 - Arsenal.md", "Arsenal", 17, 55),
    ("06 - Armor and Protection.md", "Armor and Protection", 55, 87),
    ("07 - Tactics and Tools.md", "Tactics and Tools", 87, 105),
    ("08 - Killshots and More.md", "Killshots and More", 105, 127),
    ("09 - Martial Arts.md", "Martial Arts", 127, 142),
    ("10 - Fixin All the Broken Drek.md", "Fixin' All the Broken Drek", 142, 143),
    ("11 - Staying Alive.md", "Staying Alive", 143, 169),
    ("12 - Blow Up Good.md", "Blow Up Good", 169, 197),
    ("13 - Hostile Extraction.md", "Hostile Extraction", 197, 201),
    ("14 - Run and Gun Tables.md", "Run and Gun Tables", 201, 213),
]

SOFT_PAIRS = {
    "weap ons": "weapons",
    "peo ple": "people",
    "char acter": "character",
    "char acters": "characters",
    "equip ment": "equipment",
    "ammu nition": "ammunition",
    "avail ability": "availability",
    "fire arms": "firearms",
    "gren ades": "grenades",
    "explo sives": "explosives",
    "protec tion": "protection",
    "acces sories": "accessories",
    "modi fier": "modifier",
    "modi fiers": "modifiers",
    "oppo nent": "opponent",
    "oppo nents": "opponents",
    "resis tance": "resistance",
    "penetra tion": "penetration",
    "conceala bility": "concealability",
    "func tion": "function",
    "func tionality": "functionality",
    "wire less": "wireless",
    "com mlink": "commlink",
    "com mlinks": "commlinks",
    "cyber ware": "cyberware",
    "bio ware": "bioware",
    "shadow runners": "shadowrunners",
    "metro plex": "metroplex",
    "neces sary": "necessary",
    "espe cially": "especially",
    "partic ular": "particular",
    "partic ularly": "particularly",
    "gener ally": "generally",
    "typi cally": "typically",
    "actu ally": "actually",
    "imme diately": "immediately",
    "auto matically": "automatically",
    "addi tional": "additional",
    "addi tionally": "additionally",
    "circum stances": "circumstances",
    "appro priate": "appropriate",
    "demoli tions": "demolitions",
    "detona tors": "detonators",
    "environ ment": "environment",
    "environ mental": "environmental",
    "radia tion": "radiation",
    "pollu tion": "pollution",
    "under water": "underwater",
    "mar tial": "martial",
    "tech nique": "technique",
    "tech niques": "techniques",
}


def clean(text: str) -> str:
    repl = {
        "\u2014": "-",
        "\u2013": "-",
        "\u2018": "'",
        "\u2019": "'",
        "\u201c": '"',
        "\u201d": '"',
        "\ufb01": "fi",
        "\ufb02": "fl",
        "\xa0": " ",
        "\u2022": "*",
        "\u2026": "...",
        "\u00b7": "*",
    }
    for a, b in repl.items():
        text = text.replace(a, b)

    # join hyphenated line breaks
    text = re.sub(r"(\w)-\n(\w)", r"\1\2", text)
    text = text.replace("\f", "\n")

    lines: list[str] = []
    for line in text.splitlines():
        s = line.rstrip()
        # running headers / footers
        if re.match(r"^RUN\s*&\s*GUN\s*$", s, re.I):
            continue
        if re.match(r"^\d+\s+.+\s*>>\s*$", s):
            continue
        if re.match(r"^<<\s+.+\s+\d+\s*$", s):
            continue
        if re.match(r"^>>\s+.+\s*<<\s*$", s):
            continue
        if re.match(r"^CONTENTS?/CREDITS\s*$", s, re.I):
            continue
        if re.match(r"^\d+\s+CONTENTS?/CREDITS\s*$", s, re.I):
            continue
        if re.match(r"^CONTENTS?/CREDITS\s+\d+\s*$", s, re.I):
            continue
        # lone page numbers
        if re.match(r"^\d{1,3}$", s):
            continue
        # page + chapter running titles (e.g. "6 Catspaw", "Catspaw 7")
        if re.match(
            r"^(?:\d{1,3}\s+)?"
            r"(?:Catspaw|Fight for Your Life|What You Don't Know Kills You|"
            r"Arsenal|Armor|Tactics|Killshots|Martial Arts|Staying Alive|"
            r"Blow Up Good|Hostile Extraction|Run\s*&\s*Gun Tables|"
            r"Contents)"
            r"(?:\s*&\s*Protection|\s*&\s*Tools|\s+and More)?"
            r"(?:\s+\d{1,3})?$",
            s,
            re.I,
        ):
            continue
        lines.append(s)

    text = "\n".join(lines)
    for a, b in SOFT_PAIRS.items():
        text = re.sub(re.escape(a), b, text, flags=re.I)

    # collapse excess blank lines
    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"
    return text


def main() -> None:
    import sys

    only = set(sys.argv[1:]) if len(sys.argv) > 1 else None
    doc = fitz.open(str(PDF))
    OUT.mkdir(parents=True, exist_ok=True)

    if not only:
        keep = {s[0] for s in SECTIONS} | {"INDEX.md"}
        for p in OUT.glob("*.md"):
            if p.name not in keep:
                print("note: leftover file", p.name)

    for fname, title, start, end in SECTIONS:
        if only and fname not in only and Path(fname).name not in only:
            continue
        if fname == "01 - Contents and Credits.md":
            import importlib.util

            spec = importlib.util.spec_from_file_location(
                "rebuild_rng_01", Path(__file__).with_name("rebuild_rng_01.py")
            )
            mod = importlib.util.module_from_spec(spec)
            assert spec.loader is not None
            spec.loader.exec_module(mod)
            mod.main()
            continue
        parts: list[str] = []
        for i in range(start, min(end, len(doc))):
            parts.append(doc[i].get_text("text") or "")
        body = clean("\n\n".join(parts))
        if not body.strip():
            body = (
                "(No extractable text on these PDF pages. "
                "Likely image-only or blank. See PDF pages "
                f"~{start}-{end - 1}.)\n"
            )
        md = (
            f"# {title}\n\n"
            f"**Source:** Run & Gun | `Source/PDF/runandgun.pdf` | "
            f"PDF page index {start}-{end - 1}\n\n"
            f"{body}"
        )
        for a, b in (("\u2014", "-"), ("\u2013", "-")):
            md = md.replace(a, b)
        path = OUT / fname
        path.write_text(md, encoding="utf-8")
        print("wrote", fname, "bytes", path.stat().st_size)

    if only:
        return

    index_rows = "\n".join(
        f"| {n:02d} | [{title}]({fname.replace(' ', '%20')}) | {start}-{end - 1} |"
        for n, (fname, title, start, end) in enumerate(SECTIONS, 1)
    )
    index = f"""# Run & Gun

Combat core book: weapons, armor, tactics, martial arts, demolitions.

**PDF:** `Source/PDF/runandgun.pdf` ({len(doc)} pages; print page ≈ PDF page for body text)

Source Texts extracted via `Source/_extract/extract_run_and_gun.py` (pymupdf).

**Pipeline (every chapter):** extract → format → loss-check → done-check

## Chapters

| # | File | PDF idx |
| --- | --- | --- |
{index_rows}

Page index 0 is cover art. Pages 213-215 (idx) are copyright / blank; credits live in chapter 01.

## Related

- Encyclopedia gear from RnG is already filled (Firearms, Melee, Armor, Ammo, Accessories, Grenades, etc.)
- Mechanics combat options / martial arts still need these Source Texts

## Pipeline status

- [x] Extract (raw chapter markdown from PDF)
- [ ] Format (headings, JackPoint comments, tables; strip leftover headers)
- [ ] Loss-check vs PDF
- [ ] Done-check
"""
    (OUT / "INDEX.md").write_text(
        index.replace("\u2014", "-").replace("\u2013", "-"), encoding="utf-8"
    )
    print("updated INDEX.md")


if __name__ == "__main__":
    main()
