# -*- coding: utf-8 -*-
"""Re-extract RnG pages with reading order by (y, x) block position."""
from __future__ import annotations

import re
from pathlib import Path

import fitz

PDF = Path(r"c:\Users\admin\Desktop\Shadowrun\Source\PDF\runandgun.pdf")


def page_text_sorted(page: fitz.Page) -> str:
    blocks = page.get_text("dict").get("blocks", [])
    text_blocks = []
    for b in blocks:
        if b.get("type") != 0:
            continue
        lines = []
        for line in b.get("lines", []):
            spans = sorted(line.get("spans", []), key=lambda s: s.get("bbox", [0])[0])
            t = "".join(s.get("text", "") for s in spans).rstrip()
            if t:
                lines.append(t)
        if not lines:
            continue
        x0, y0, x1, y1 = b["bbox"]
        text_blocks.append((y0, x0, "\n".join(lines)))
    text_blocks.sort(key=lambda t: (round(t[0] / 5) * 5, t[1]))
    return "\n\n".join(t[2] for t in text_blocks)


def main() -> None:
    doc = fitz.open(str(PDF))
    # sample pages 18-19 (idx 17-18)
    for i in (17, 18, 105, 106):
        t = page_text_sorted(doc[i])
        print("====", i + 1, "====")
        print(t[:1200])
        print()


if __name__ == "__main__":
    main()
