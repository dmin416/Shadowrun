# -*- coding: utf-8 -*-
"""Extract Serrated Edge PDF into Source Texts/Serrated Edge/*.md"""
from pathlib import Path
import re
import pypdf

PDF = Path(r"c:\Users\admin\Desktop\Shadowrun\Source\PDF\serratededge.pdf")
OUT = Path(r"c:\Users\admin\Desktop\Shadowrun\Source Texts\Serrated Edge")

# Align with existing stub naming where possible.
# (filename, title, start_pdf_idx inclusive, end_pdf_idx exclusive)
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


def clean(text: str) -> str:
    repl = {
        "\u2014": "-", "\u2013": "-", "—": "-", "–": "-",
        "\u2018": "'", "\u2019": "'", "\u201c": '"', "\u201d": '"',
        "\ufb01": "fi", "\ufb02": "fl",
        "\xa0": " ",
    }
    for a, b in repl.items():
        text = text.replace(a, b)
    text = re.sub(r"(\w)-\n(\w)", r"\1\2", text)
    text = text.replace("\f", "\n")
    lines = []
    for line in text.splitlines():
        s = line.rstrip()
        if re.match(r"^>>?\s*SERRATED EDGE", s, re.I):
            continue
        if re.match(r"^CONTENTS?\s*&\s*CREDITS\s+\d+$", s, re.I):
            continue
        if re.match(r"^\d+\s+CONTENTS?\s*&\s*CREDITS\s*$", s, re.I):
            continue
        if re.match(r"^AFTERMATH\s+\d+$", s, re.I):
            continue
        if re.match(r"^\d+\s+AFTERMATH\s*$", s, re.I):
            continue
        if re.match(r"^SCENE \d+:.+\s{2,}\d+\s*$", s, re.I):
            continue
        lines.append(s)
    text = "\n".join(lines)
    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"
    return text


def main():
    pdf = pypdf.PdfReader(str(PDF))
    OUT.mkdir(parents=True, exist_ok=True)

    # Remove obsolete empty stubs that no longer match section list
    keep = {s[0] for s in SECTIONS} | {"INDEX.md"}
    for p in OUT.glob("*.md"):
        if p.name not in keep and p.stat().st_size == 0:
            p.unlink()
            print("removed empty stub", p.name)

    for fname, title, start, end in SECTIONS:
        parts = []
        for i in range(start, min(end, len(pdf.pages))):
            t = pdf.pages[i].extract_text() or ""
            parts.append(t)
        body = clean("\n\n".join(parts))
        if not body.strip():
            body = (
                "(No extractable text on these PDF pages. "
                "Likely image-only map or blank. See PDF pages "
                f"~{start}-{end - 1}.)\n"
            )
        md = (
            f"# {title}\n\n"
            f"**Source:** Serrated Edge (Denver Adventure 1) | "
            f"`Source/PDF/serratededge.pdf` | PDF page index {start}-{end - 1}\n\n"
            f"{body}"
        )
        for a, b in (("\u2014", "-"), ("\u2013", "-"), ("—", "-"), ("–", "-")):
            md = md.replace(a, b)
        path = OUT / fname
        path.write_text(md, encoding="utf-8")
        print("wrote", fname, "bytes", path.stat().st_size)

    index = """# Serrated Edge

Denver Adventure 1 (start of the Denver trilogy). PDF: `Source/PDF/serratededge.pdf` (66 pages).

Source Texts extracted via `Source/_extract/extract_serrated_edge.py` (pypdf). Formatting pass: `Source/_extract/format_serrated_edge.py`. Image-only pages may have little or no text.

## Sections

| # | File | PDF idx |
| --- | --- | --- |
| 0 | [GM Adventure Brief](00%20-%20GM%20Adventure%20Brief.md) | (LLM / GM spine) |
| 1 | [Contents and Credits](01%20-%20Contents%20and%20Credits.md) | 2-3 |
| 2 | [Denver: Serrated Edge Introduction](02%20-%20Denver%20-%20Serrated%20Edge%20Introduction.md) | 4-9 (fiction + intro) |
| 3 | [Scene 1: The Meet](03%20-%20Scene%201%20-%20The%20Meet.md) | 10-13 |
| 4 | [Scene 2: The Clinic](04%20-%20Scene%202%20-%20The%20Clinic.md) | 14-23 |
| 5 | [Scene 3: Delivery & Attack](05%20-%20Scene%203%20-%20Delivery%20and%20Attack.md) | 24-25 |
| 6 | [Scene 4: The Doctor is In (Trouble)](06%20-%20Scene%204%20-%20The%20Doctor%20is%20In%20(Trouble).md) | 26-29 |
| 7 | [Scene 5: Digging a Little Deeper](07%20-%20Scene%205%20-%20Digging%20a%20Little%20Deeper.md) | 30-35 |
| 8 | [Scene 6: Working for the Men](08%20-%20Scene%206%20-%20Working%20for%20the%20Men.md) | 36-39 |
| 9 | [Scene 7: Thwarting the Bombers](09%20-%20Scene%207%20-%20Thwarting%20the%20Bombers.md) | 40-47 |
| 10 | [Scene 8: Cutting Out the Cancer](10%20-%20Scene%208%20-%20Cutting%20Out%20the%20Cancer.md) | 48-49 |
| 11 | [Aftermath](11%20-%20Aftermath.md) | 50-56 (Karma, rep, NPC stats) |
| 12 | [At the Top](12%20-%20At%20the%20Top.md) | 57 |
| 13 | [Player Handouts](13%20-%20Player%20Handouts.md) | 58-59 |
| 14 | [Denver Map](14%20-%20Denver%20Map.md) | 60 (caption; map is image) |
| 15 | [Where to go in Denver](15%20-%20Where%20to%20go%20in%20Denver.md) | 61 |
| 16 | [Medical Center Map](16%20-%20Medical%20Center%20Map.md) | 62 (likely image-only) |

## Related

- Trilogy: Serrated Edge → False Flag (not in local PDF set per `books to get.md`)
- Encyclopedia INDEX: adventure/locale kit, not a gear catalog
- Prior clinic extract: `Source/_extract/med_se_clinic.txt`

## Status

- [x] Extract PDF → chapter Source Texts + INDEX
- [x] GM adventure brief (`00 - GM Adventure Brief.md`)
- [x] Formatting pass (reflow, section H2s, soft-hyphen fix)
- [x] Gear/stat audit: no new shop Avail/Cost SKUs; NPC loadouts + Scene 7 detonator frag profile only
"""
    (OUT / "INDEX.md").write_text(
        index.replace("\u2014", "-").replace("—", "-"), encoding="utf-8"
    )
    print("updated INDEX.md")


if __name__ == "__main__":
    main()
