# -*- coding: utf-8 -*-
"""Rebuild Council Island markdown from PDF with correct JackPoint + headers."""
from __future__ import annotations

import re
from pathlib import Path

import fitz

PDF = fitz.open(r"c:\Users\admin\Desktop\Shadowrun\Source\PDF\seattlesprawl.pdf")
OUT = Path(r"c:\Users\admin\Desktop\Shadowrun\Source Texts\Seattle Sprawl\14 - Council Island.md")

SPEAKERS = {
    "SeaTac Sweetie",
    "Elijah",
    "Bull",
    "Man-of-Many-Names",
    "Kane",
    "Hard Exit",
    "Mika",
    "Baka Dabora",
    "Sunshine",
    "Snopes",
    "Plan 9",
    "Pistons",
    "Turbo Bunny",
    "Traveler Jones",
    "Ma'Fan",
    "Nephrine",
    "Glitch",
    "Butch",
    "Winterhawk",
    "Stone",
    "2XL",
    "Netcat",
    "Kay St. Irregular",
    "Dr. Spin",
}


def clean_pdf_text() -> str:
    parts = []
    for i in range(67, 72):
        t = PDF[i].get_text("text") or ""
        # drop running headers/footers
        lines = []
        for line in t.splitlines():
            s = line.strip()
            if not s:
                lines.append("")
                continue
            if re.match(r"^>>?\s*SEATTLE SPRAWL", s, re.I):
                continue
            if re.match(r"^<<?\s*COUNCIL ISLAND", s, re.I):
                continue
            if re.match(r"^\d+\s+COUNCIL ISLAND", s, re.I):
                continue
            if re.match(r"^COUNCIL ISLAND\s+\d+", s, re.I):
                continue
            if s in {">>", "<<"}:
                continue
            lines.append(line)
        parts.append("\n".join(lines))
    text = "\n".join(parts)
    # normalize quotes / dashes
    text = text.replace("\u2019", "'").replace("\u2018", "'")
    text = text.replace("\u201c", '"').replace("\u201d", '"')
    text = text.replace("\u2014", "-").replace("\u2013", "-")
    text = text.replace("\ufb01", "fi").replace("\ufb02", "fl")
    # join hyphenated line breaks
    text = re.sub(r"([A-Za-z])-\n\s*([a-z])", r"\1\2", text)
    # join soft line breaks within paragraphs (keep blank / > markers)
    return text


def reflow_paragraph(s: str) -> str:
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n+", " ", s)
    return s.strip()


def emit_comment(body: str, speaker: str) -> str:
    body = reflow_paragraph(body)
    return f"> {body}\n>\n> {speaker}\n"


def main() -> None:
    raw = clean_pdf_text()

    # Keep At a Glance table from existing file header
    existing = OUT.read_text(encoding="utf-8")
    m = re.search(r"(?s)^(# Council Island.*?\n\n## Council Island at a Glance\n\n\|.*?\n\n)", existing)
    if not m:
        raise SystemExit("could not find At a Glance header")
    header = m.group(1)

    # Strip At a Glance block from PDF raw if present
    body_start = raw
    # Find narrative start
    idx = body_start.find("In the nineteenth and twentieth centuries")
    if idx < 0:
        raise SystemExit("narrative start not found")
    body_start = body_start[idx:]

    # Remove COUNCIL ISLAND AT A GLANCE table leftovers before narrative if any remain
    # Parse into blocks: body paragraphs, comments, section headers
    lines = body_start.splitlines()
    blocks: list[tuple[str, str]] = []  # type, text
    i = 0
    headers = {
        "SPECIAL OCCASIONS": "## Special Occasions",
        "CRIME SCENE": "## Crime Scene",
        "WHERE TO SHOP": "## Where to Shop",
        "WHERE TO SQUAT": "## Where to Squat",
        "YOU WON'T FIND THIS ELSEWHERE": "## You Won't Find This Elsewhere",
        "YOU WON'T FIND": "## You Won't Find This Elsewhere",  # split header
        "OPPOSITION REPORT": "## Opposition Report",
    }

    buf: list[str] = []
    mode = "body"  # body | comment

    def flush_body():
        nonlocal buf
        if not buf:
            return
        text = reflow_paragraph("\n".join(buf))
        if text:
            blocks.append(("body", text))
        buf = []

    def flush_comment(speaker: str):
        nonlocal buf
        text = reflow_paragraph("\n".join(buf))
        if text or speaker:
            blocks.append(("comment", (text, speaker)))
        buf = []

    while i < len(lines):
        line = lines[i]
        s = line.strip()

        # split YOU WON'T FIND / THIS ELSEWHERE
        if s.upper() == "THIS ELSEWHERE":
            i += 1
            continue

        up = s.upper()
        if up in headers or (up.startswith("YOU WON") and "FIND" in up):
            flush_body()
            if mode == "comment":
                # shouldn't happen without speaker
                mode = "body"
            title = headers.get(up)
            if not title and up.startswith("YOU WON"):
                title = "## You Won't Find This Elsewhere"
            if title:
                blocks.append(("header", title))
            i += 1
            continue

        if s == ">":
            # start or continue comment marker from PDF
            # peek: if next non-empty is speaker-only after collecting, handled below
            i += 1
            # collect until next > or header
            cbuf: list[str] = []
            while i < len(lines):
                ns = lines[i].strip()
                if ns == ">":
                    # might be speaker line next
                    i += 1
                    if i < len(lines):
                        sp = lines[i].strip()
                        # speaker alone?
                        if sp in SPEAKERS or sp.replace("'", "'") in SPEAKERS:
                            blocks.append(("comment", (reflow_paragraph("\n".join(cbuf)), sp)))
                            i += 1
                            break
                        if sp == ">":
                            continue
                        # another comment body without closing? treat as new comment start
                        # actually PDF pattern is: > body... > Speaker
                        # if we hit > and next isn't speaker, append?
                        cbuf.append(lines[i])
                        i += 1
                        continue
                    break
                up2 = ns.upper()
                if up2 in headers or (up2.startswith("YOU WON") and "FIND" in up2) or up2 == "THIS ELSEWHERE":
                    # comment without speaker? rare
                    if cbuf:
                        blocks.append(("body", reflow_paragraph("\n".join(cbuf))))
                    break
                # speaker alone on line without second > ?
                if ns in SPEAKERS and not cbuf:
                    blocks.append(("comment", ("", ns)))
                    i += 1
                    break
                cbuf.append(lines[i])
                i += 1
            continue

        # plain body line
        if not s:
            i += 1
            continue
        # accumulate body until blank or >
        bbuf = [line]
        i += 1
        while i < len(lines):
            ns = lines[i].strip()
            if not ns:
                i += 1
                # allow single blank inside para? treat as para break
                break
            if ns == ">":
                break
            up2 = ns.upper()
            if up2 in headers or (up2.startswith("YOU WON") and "FIND" in up2) or up2 == "THIS ELSEWHERE":
                break
            bbuf.append(lines[i])
            i += 1
        blocks.append(("body", reflow_paragraph("\n".join(bbuf))))

    # Post-process: fix known body-vs-comment misclassifications from PDF
    # (narrative lines sometimes lack > in extract between comments)
    out_parts = [header.rstrip(), ""]
    for kind, val in blocks:
        if kind == "header":
            out_parts.append("")
            out_parts.append(val)
            out_parts.append("")
        elif kind == "body":
            text = val
            # skip tiny junk
            if len(text) < 2:
                continue
            out_parts.append(text)
            out_parts.append("")
        elif kind == "comment":
            body, speaker = val
            if not body and not speaker:
                continue
            if body and speaker:
                out_parts.append(f"> {body}")
                out_parts.append(">")
                out_parts.append(f"> {speaker}")
                out_parts.append("")
            elif speaker and not body:
                # orphan speaker - attach to previous body as comment? skip
                out_parts.append(f"> {speaker}")
                out_parts.append("")
            else:
                out_parts.append(f"> {body}")
                out_parts.append("")

    text = "\n".join(out_parts)
    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"

    # Location H3s for major sites (match other chapters lightly)
    for name in [
        "Grand Council Lodge",
        "Totem Tower",
        "Aquaculture Lodge",
        "Camp Seagull",
        "Council Island Hospital",
        "Eagle Lodge",
        "Museum Lodge",
        "Passport Lodge",
        "Council Island Inn",
        "Friendship Restaurant",
        "Marge's Flowers and Nursery",
    ]:
        # only promote if paragraph starts with location cue
        pass

    OUT.write_text(text, encoding="utf-8")
    print("Wrote", OUT)
    print("chars", len(text))
    # quick sanity
    for h in [
        "## Special Occasions",
        "## Crime Scene",
        "## Where to Shop",
        "## Where to Squat",
        "## You Won't Find This Elsewhere",
        "## Opposition Report",
    ]:
        print(h, "OK" if h in text else "MISSING")
    smash = len(re.findall(r"> .*" "##", text))
    print("inline ## smash count", smash)


if __name__ == "__main__":
    main()
