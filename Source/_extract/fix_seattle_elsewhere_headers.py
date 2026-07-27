# -*- coding: utf-8 -*-
"""Fix split 'You Won't Find This Elsewhere' headers and McNeil casing."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(r"c:\Users\admin\Desktop\Shadowrun\Source Texts\Seattle Sprawl")
SKIP = {"01 - Contents and Credits.md", "INDEX.md"}


def main() -> None:
    for path in sorted(ROOT.glob("*.md")):
        if path.name in SKIP:
            continue
        text = path.read_text(encoding="utf-8")
        orig = text
        # join split section title
        text = re.sub(
            r"(?im)^YOU WON'?T FIND\s*\nTHIS ELSEWHERE\s*$",
            "## You Won't Find This Elsewhere\n",
            text,
        )
        text = re.sub(
            r"(?im)^You Won'?t Find\s*\nThis Elsewhere\s*$",
            "## You Won't Find This Elsewhere\n",
            text,
        )
        text = text.replace("## Mcneil Island", "## McNeil Island")
        text = re.sub(r"\n{3,}", "\n\n", text)
        if text != orig:
            path.write_text(text, encoding="utf-8")
            print("fixed", path.name)
        else:
            print("ok", path.name)


if __name__ == "__main__":
    main()
