# -*- coding: utf-8 -*-
"""Done-check polish for short RnG chapters."""
from __future__ import annotations

import re
from pathlib import Path

OUT = Path(r"c:\Users\admin\Desktop\Shadowrun\Source Texts\Run and Gun")


def polish_fight() -> None:
    p = OUT / "03 - Fight for Your Life.md"
    t = p.read_text(encoding="utf-8")
    # PDF has " crumbed", "over table", "thee percent" as printed; keep them.
    # Strip odd leading space/control before Jimbo quote.
    t = t.replace('" Jimbo.', '"Jimbo.')
    t = t.replace("\uFFFD Jimbo.", '"Jimbo.')
    p.write_text(t, encoding="utf-8")
    print("polished", p.name)


def polish_fixin() -> None:
    p = OUT / "10 - Fixin All the Broken Drek.md"
    t = p.read_text(encoding="utf-8")
    # PDF prints "thee percent"; keep as source-faithful.
    t = t.replace(
        "MAKING THE BLIND SEE\nAND THE DEAF HEAR",
        "## Making the Blind See and the Deaf Hear",
    )
    t = t.replace("FIXIN' THAT OLD BEATER", "## Fixin' That Old Beater")
                if "| Part |" not in t:
        t = re.sub(
            r"## Fixin' That Old Beater\n.*?(?=\Z)",
            """## Fixin' That Old Beater

| Part | Threshold | Price |
| --- | --- | --- |
| Antenna | 4 | 20¥ |
| Axle | 18 | 2,000¥ |
| Door lock | 12 | 800¥ |
| Engine block | 24 | 25 percent of vehicle cost |
| Fuel tank/battery | 18 | 1,200¥ |
| Window motor | 12 | 800¥ |
| Window | 12 | 300¥ |
""",
            t,
            count=1,
            flags=re.S,
        )
    p.write_text(t, encoding="utf-8")
    print("polished", p.name)


def polish_hostile() -> None:
    p = OUT / "13 - Hostile Extraction.md"
    t = p.read_text(encoding="utf-8")
    # move byline
    t = t.replace("\nBY JOHN HELFERS\n", "\n")
    if "*By John Helfers*" not in t:
        t = t.replace(
            "PDF page index 197-200\n\n",
            "PDF page index 197-200\n\n*By John Helfers*\n\n",
        )
    t = t.replace("offthe-main-drag", "off-the-main-drag")
    # "behind behind" and "M.O.D." appear in the PDF as printed; leave them.
    p.write_text(t, encoding="utf-8")
    print("polished", p.name)


def polish_catspaw() -> None:
    p = OUT / "02 - Catspaw.md"
    t = p.read_text(encoding="utf-8")
    t = re.sub(r"\s*BY ROBYN ['\"]RAT['\"] KING\s*", "\n\n", t)
    t = re.sub(r" *✖ *", "\n\n✖\n\n", t)
    t = re.sub(r"\n{3,}", "\n\n", t)
    p.write_text(t, encoding="utf-8")
    print("polished", p.name)


def main() -> None:
    polish_catspaw()
    polish_fight()
    polish_fixin()
    polish_hostile()


if __name__ == "__main__":
    main()
