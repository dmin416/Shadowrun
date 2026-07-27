# -*- coding: utf-8 -*-
"""Safer Forbidden Arcana structure repair (Karma qualities + junk strip only)."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(r"c:\Users\admin\Desktop\Shadowrun\Source Texts\Forbidden Arcana")

KARMA_HEADER = re.compile(
    r"(?<![A-Za-z/#])"
    r"([A-Z][A-Z0-9](?:[A-Z0-9 \-'/\[\]]{0,50}[A-Z0-9\]\.])?)"
    r"\s+"
    r"(\d+\s+KARMA(?:\s+PER LEVEL)?(?:\s*\([^)]{0,40}\))?)"
    r"(?=\s+Minimum Requirements?:)",
)

RUNNING = re.compile(
    r"(?:^|\s)FORBIDDEN ARCANA(?:\s+[A-Z][A-Z&\- ]{1,30})?\s*\d{1,3}(?:\s+[A-Z][A-Z&\- ]{1,30}\s*>>)?(?=\s|$)",
)
RUNNING_PAGE = re.compile(
    r"(?:^|\s)\d{1,3}\s+[A-Z][A-Z&\- ]{2,30}\s*>>(?=\s|$)",
)


def title_case(s: str) -> str:
    small = {"a", "an", "the", "and", "or", "of", "in", "on", "for", "to", "vs", "at"}
    parts = []
    for i, w in enumerate(s.split()):
        if w.startswith("[") and w.endswith("]"):
            inner = w[1:-1]
            parts.append("[" + " ".join(
                (x.lower() if j and x.lower() in small else x[:1].upper() + x[1:].lower())
                for j, x in enumerate(inner.split())
            ) + "]")
            continue
        lw = w.lower()
        if i > 0 and lw in small:
            parts.append(lw)
        else:
            parts.append(w[:1].upper() + w[1:].lower() if w.isalpha() or w.isalnum() else w)
    return " ".join(parts)


def fix_ocr(text: str) -> str:
    text = re.sub(r"\bp\.\s*(\d)\s+(\d{2})\b", r"p. \1\2", text)
    text = re.sub(r"\b(20\d)\s+(\d)\b", r"\1\2", text)
    text = text.replace("Jack - Pointers", "JackPointers")
    text = text.replace("Jack - Point", "JackPoint")
    text = text.replace("second-incommand", "second-in-command")
    text = text.replace("findyourself", "find-yourself")
    return text


def promote(text: str) -> str:
    m = re.match(r"(?s)^(#[^\n]+\n\n\*\*Source:\*\*[^\n]+\n\n)(.*)$", text)
    if not m:
        return fix_ocr(text.replace("\u2014", "-").replace("\u2013", "-"))
    head, body = m.group(1), m.group(2)
    body = RUNNING.sub(" ", body)
    body = RUNNING_PAGE.sub(" ", body)

    def karma_sub(mm: re.Match) -> str:
        name = mm.group(1).strip()
        karma = mm.group(2).strip()
        if len(name) < 3 or name.count(" ") > 7:
            return mm.group(0)
        # reject sentence-like
        bad = ("THE OPTIONS", "THIS INCLUDES", "WHEN USING", "MOST OF")
        if any(name.startswith(b) for b in bad):
            return mm.group(0)
        return f"\n\n### {title_case(name)}\n\n**{karma}**\n\n"

    body = KARMA_HEADER.sub(karma_sub, body)

    # Tradition blocks: NAME (UPDATE|NEW) DESCRIPTION -> ## + ### Description
    # Only when NAME is reasonable length and all caps words
    body = re.sub(
        r"(?<![A-Za-z])([A-Z][A-Z0-9][A-Z0-9 \-'/]{1,35}?)\s+\((UPDATE|NEW)\)\s+DESCRIPTION\b",
        lambda mm: f"\n\n## {title_case(mm.group(1))} ({title_case(mm.group(2))})\n\n### Description\n\n",
        body,
    )

    # Subsection labels only after a newline/start (not mid-sentence ALL CAPS)
    for lab, level in (
        ("RELATED MENTOR SPIRITS", "###"),
        ("IDEALS", "###"),
        ("SORCERY", "###"),
        ("CONJURING", "###"),
        ("ENCHANTING", "###"),
        ("RULES", "###"),
        ("TRADITION UPDATES", "##"),
        ("NEW TRADITIONS", "##"),
        ("MENTOR SPIRITS", "##"),
        ("MAGICAL ODDITIES", "##"),
        ("MAGICAL DEMOGRAPHICS", "##"),
    ):
        body = re.sub(
            rf"(?:(?<=\n)|^)\s*{re.escape(lab)}\b",
            f"\n\n{level} {title_case(lab)}\n\n",
            body,
        )

    body = fix_ocr(body)
    body = body.replace("\u2014", "-").replace("\u2013", "-")
    body = re.sub(r"[ \t]{2,}", " ", body)
    body = re.sub(r"\n{3,}", "\n\n", body)
    return head + body.strip() + "\n"


def main() -> None:
    # Only reformat chapter bodies that benefit; leave Contents/TOC alone
    targets = [
        "05 - Magic Mastery.md",
        "07 - Traditions.md",
        "08 - Blood Magic.md",
        "10 - Where the Wild Things Are.md",
        "11 - Advanced Alchemy.md",
        "04 - Seeing the Invisible World.md",
    ]
    for name in targets:
        p = ROOT / name
        if not p.exists():
            print("missing", name)
            continue
        t = p.read_text(encoding="utf-8")
        newt = promote(t)
        p.write_text(newt, encoding="utf-8")
        print(
            f"{name}: H2={len(re.findall(r'^## ', newt, re.M))} "
            f"H3={len(re.findall(r'^### ', newt, re.M))}"
        )


if __name__ == "__main__":
    main()
