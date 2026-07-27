# -*- coding: utf-8 -*-
"""Rebuild Run & Gun 01 Contents and Credits in Chrome Flesh style."""
from __future__ import annotations

import re
from pathlib import Path

import fitz

PDF = Path(r"c:\Users\admin\Desktop\Shadowrun\Source\PDF\runandgun.pdf")
OUT = Path(r"c:\Users\admin\Desktop\Shadowrun\Source Texts\Run and Gun\01 - Contents and Credits.md")

MAJOR = {
    "CATSPAW",
    "FIGHT FOR YOUR LIFE",
    "WHAT YOU DON'T KNOW KILLS YOU",
    "ARSENAL",
    "ARMOR & PROTECTION",
    "ARMOR AND PROTECTION",
    "TACTICS & TOOLS",
    "TACTICS AND TOOLS",
    "KILLSHOTS AND MORE",
    "MARTIAL ARTS",
    "FIXIN' ALL THE BROKEN DREK",
    "STAYING ALIVE",
    "BLOW UP GOOD",
    "HOSTILE EXTRACTION",
    "RUN & GUN TABLES",
    "RUN AND GUN TABLES",
}


def clean_char(s: str) -> str:
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
        "\u00b7": "*",
    }
    for a, b in repl.items():
        s = s.replace(a, b)
    return s


def parse_toc(text: str) -> list[tuple[str, str, bool]]:
    """Return list of (title, page, is_major)."""
    lines = [clean_char(ln).strip() for ln in text.splitlines()]
    # drop headers/footers
    filtered: list[str] = []
    for s in lines:
        if not s:
            continue
        if re.match(r"^>>|^<<|CONTENTS/CREDITS|TABLE OF CONTENTS", s, re.I):
            continue
        if re.match(r"^RUN\s*&\s*GUN\s*$", s, re.I):
            continue
        if re.match(r"^\d+\s+CONTENTS", s, re.I):
            continue
        filtered.append(s)

    entries: list[tuple[str, str, bool]] = []
    i = 0
    while i < len(filtered):
        title = filtered[i]
        # merge wrapped titles that continue with indent / lowercase / paren
        while i + 1 < len(filtered) and not re.match(r"^\d{1,3}$", filtered[i + 1]):
            nxt = filtered[i + 1]
            if nxt.startswith("(") or nxt[:1].islower() or title.endswith(("-", ",")):
                title = (title + " " + nxt).strip()
                i += 1
                continue
            # Environmental Effects wrap after Injury Modifiers,...
            if title.rstrip().endswith(",") or "Modifiers," in title:
                title = (title + " " + nxt).strip()
                i += 1
                continue
            break
        page = ""
        if i + 1 < len(filtered) and re.match(r"^\d{1,3}$", filtered[i + 1]):
            page = filtered[i + 1]
            i += 2
        else:
            i += 1
        if not title:
            continue
        is_major = title.upper().replace(" AND ", " & ") in {
            m.replace(" AND ", " & ") for m in MAJOR
        } or title.upper() in MAJOR
        if is_major:
            # Title Case major chapter names for readability
            raw = title
            title = title.replace("&", "and").title().replace("And", "and")
            # fix known casing from .title() apostrophe quirks
            fixes = {
                "What You Don'T Know Kills You": "What You Don't Know Kills You",
                "Fight For Your Life": "Fight for Your Life",
                "Fixin' All the Broken Drek": "Fixin' All the Broken Drek",
                "Run and Gun Tables": "Run & Gun Tables",
                "Armor and Protection": "Armor & Protection",
                "Tactics and Tools": "Tactics & Tools",
            }
            title = fixes.get(title, title)
            if "Don't" in raw or "DON'T" in raw.upper():
                title = title.replace("Don'T", "Don't").replace("Dont", "Don't")
            title = fixes.get(title, title)
        entries.append((title, page, is_major))
    return entries


def format_credits(text: str) -> str:
    t = clean_char(text)
    lines = []
    for ln in t.splitlines():
        s = ln.strip()
        if not s:
            continue
        if re.match(r"^>>|^<<|RUN\s*&\s*GUN$|CONTENTS/CREDITS", s, re.I):
            continue
        if re.match(r"^<<\s*CONTENTS", s, re.I):
            continue
        lines.append(s)
    body = " ".join(lines)
    # light cleanup of weird spaces around commas from PDF
    body = re.sub(r"\s+,", ",", body)
    body = re.sub(r"\s{2,}", " ", body)

    # Split into structured credits where possible
    out: list[str] = []
    # copyright block ends at Find us online / credits
    m = re.search(r"Find us online:(.*?)RUN & GUN CREDITS(.*)$", body, re.I | re.S)
    if not m:
        return body + "\n"

    pre = body[: m.start()].strip()
    online = m.group(1).strip()
    cred = m.group(2).strip()

    out.append(pre)
    out.append("")
    out.append("Find us online:")
    # Prefer explicit URL/email extraction
    emails = re.findall(r"[\w.+-]+@[\w.-]+", online)
    urls = re.findall(r"https?://\S+", online)
    labels = re.findall(r"\(([^)]+)\)", online)
    # pair in order: email first, then urls with labels
    if emails:
        lab = labels[0] if labels else "Shadowrun questions"
        out.append(f"- {emails[0]} ({lab})")
    for i, url in enumerate(urls):
        lab = labels[i + 1] if i + 1 < len(labels) else url
        out.append(f"- {url} ({lab})" if not url.startswith(lab) else f"- {url}")
    if not emails and not urls:
        out.append(f"- {online}")

    out.append("")
    out.append("## Run & Gun Credits")
    out.append("")

    # normalize credit fields
    cred = re.sub(r"\s+", " ", cred)
    fields = [
        "Writing",
        "Additional Contributions",
        "Editing",
        "Art Direction",
        "Cover Art",
        "Cover Layout",
        "Iconography",
        "Interior Art",
        "Interior Layout",
        "Shadowrun Line Developer",
        "Playtesting",
        "Proofreading",
        "SPECIAL DEDICATION",
    ]
    # insert breaks before field labels
    for f in fields:
        cred = re.sub(rf"(?<!^)({re.escape(f)}:)", r"\n\1", cred)
    cred = re.sub(r"(SPECIAL DEDICATION)", r"\n## Special Dedication\n", cred)

    for ln in cred.splitlines():
        ln = ln.strip()
        if not ln:
            continue
        if ln.startswith("## "):
            out.append("")
            out.append(ln)
            out.append("")
            continue
        if ":" in ln and not ln.startswith("http"):
            key, val = ln.split(":", 1)
            out.append(f"- **{key.strip()}:** {val.strip()}")
        else:
            out.append(ln)
    return "\n".join(out).strip() + "\n"


def main() -> None:
    doc = fitz.open(str(PDF))
    toc_text = "\n".join(doc[i].get_text("text") for i in range(1, 4))
    credits_text = doc[4].get_text("text")

    entries = parse_toc(toc_text)
    rows: list[str] = []
    for title, page, is_major in entries:
        if not page:
            continue
        display = title
        if is_major:
            display = f"**{title}**"
        rows.append(f"| {display} | {page} |")

    credits = format_credits(credits_text)

    md = (
        "# Contents and Credits\n\n"
        "**Source:** Run & Gun | `Source/PDF/runandgun.pdf` | PDF page index 1-4\n\n"
        "## Table of Contents\n\n"
        "| Section | Page |\n"
        "| --- | --- |\n"
        + "\n".join(rows)
        + "\n\n"
        + credits
    )
    for a, b in (("\u2014", "-"), ("\u2013", "-"), ("—", "-"), ("–", "-")):
        md = md.replace(a, b)
    OUT.write_text(md, encoding="utf-8")
    print("wrote", OUT, "entries", len(rows), "bytes", OUT.stat().st_size)


if __name__ == "__main__":
    main()
