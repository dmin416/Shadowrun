# -*- coding: utf-8 -*-
"""
Polish Source Texts for the six books:
- soft hyphens / spaced syllable breaks
- common mid-word PDF splits (Run & Gun style pairs)
- demote bad ## headings (TOC leftovers, page-number headers)
- split flattened gear/critter/vehicle tables into rows
- break giant fiction/prose paragraphs into readable chunks
- keep code fences / lists intact
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(r"c:\Users\admin\Desktop\Shadowrun\Source Texts")
BOOKS = [
    "Rigger 5",
    "Street Grimoire",
    "Forbidden Arcana",
    "Run Faster",
    "Street Lethal",
    "Howling Shadows",
    "Chrome Flesh",
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
    "nano ware": "nanoware",
    "nano tech": "nanotech",
    "gene tech": "genetech",
    "gene ware": "geneware",
    "cyber tech": "cybertech",
    "cyber psychosis": "cyberpsychosis",
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
    "informa tion": "information",
    "organiza tion": "organization",
    "organiza tions": "organizations",
    "corpo ration": "corporation",
    "corpo rations": "corporations",
    "tradi tion": "tradition",
    "tradi tions": "traditions",
    "initia tion": "initiation",
    "meta magic": "metamagic",
    "spell caster": "spellcaster",
    "spell casting": "spellcasting",
    "sum moning": "summoning",
    "banish ing": "banishing",
    "augmen tation": "augmentation",
    "augmen tations": "augmentations",
    "vehi cle": "vehicle",
    "vehi cles": "vehicles",
    "motor cycle": "motorcycle",
    "motor cycles": "motorcycles",
    "water craft": "watercraft",
    "air craft": "aircraft",
    "drone s": "drones",
    "crit ter": "critter",
    "crit ters": "critters",
    "para normal": "paranormal",
    "extra planar": "extraplanar",
    "techno critter": "technocritter",
    "techno critters": "technocritters",
    "proto sapient": "protosapient",
    "proto sapients": "protosapients",
    "back ground": "background",
    "mana sphere": "manasphere",
    "astral space": "astral space",  # keep
    "twenty five": "twenty-five",
    "twentyfive": "twenty-five",
    "hiself": "himself",
    "ahippocrates": "a Hippocrates",
    "counterpelling": "Counterspelling",
    "Counterpelling": "Counterspelling",
    "particular - ly": "particularly",
    "Facilityformation": "Facility formation",
    "Facility - formation": "Facility formation",
    "MetaEr - gonomics": "MetaErgonomics",
    "Clairvoy - ance": "Clairvoyance",
}

# Keep these as real section headers even if short
KEEP_H2 = {
    "introduction",
    "game information",
    "credits",
    "contents",
    "positive qualities",
    "negative qualities",
    "life modules",
    "combat spells",
    "detection spells",
    "health spells",
    "illusion spells",
    "manipulation spells",
    "shadow rituals",
    "motorcycles",
    "cars",
    "trucks",
    "vans",
    "drones",
    "microdrones",
    "minidrones",
    "small drones",
    "medium drones",
    "large drones",
    "huge drones",
    "adventure hooks",
    "compiled tables",
    "critter tables",
    "tea & sympathy",
    "tea and sympathy",
    "traditions",
    "blood magic",
    "blades",
    "clubs",
    "weapons",
    "armor",
    "advantages",
    "disadvantages",
    "fiction opener",
    "headware",
    "eyeware",
    "earware",
    "bodyware",
    "cyberlimbs",
    "bioware",
    "cultured bioware",
    "nanoware",
    "genetech",
    "drugs",
}


def fix_soft_hyphens(text: str) -> str:
    def join_hyphen(m: re.Match) -> str:
        a, b = m.group(1), m.group(2)
        # Keep brand suffixes: Falcon-EX, Ares-AT, etc.
        if b.isupper() and 1 <= len(b) <= 4:
            return f"{a}-{b}"
        return a + b

    text = re.sub(r"([A-Za-z]{2,})-\s+([A-Za-z]{2,})", join_hyphen, text)

    def spaced_hyphen(m: re.Match) -> str:
        a, b = m.group(1), m.group(2)
        if a.isdigit() or b.isdigit():
            return m.group(0)
        if not a.isalpha() or not b.isalpha():
            return m.group(0)
        if b.isupper() and 1 <= len(b) <= 4 and a[0].isupper():
            return f"{a}-{b}"
        # Pure syllable wraps: "per - fection", "sur - veillance"
        if a.islower() and b.islower() and len(a) <= 12 and len(b) <= 12:
            return a + b
        # Short/medium Titlecase wraps: "Per - ception", "Clairvoy - ance"
        if a[0].isupper() and a[1:].islower() and b.islower() and len(a) <= 10 and len(b) <= 12:
            return a + b
        return m.group(0)

    text = re.sub(r"([A-Za-z0-9]+)\s+-\s+([A-Za-z0-9]+)", spaced_hyphen, text)
    return text


def fix_soft_pairs(text: str) -> str:
    for a, b in SOFT_PAIRS.items():
        text = re.sub(re.escape(a), b, text, flags=re.I)
    # generic mid-word split: lowercase letter space lowercase letter inside words of pattern "xxx yyy" where both short
    # already covered by pairs; also fix "long ago" style left alone
    return text


def is_table_header_line(s: str) -> bool:
    u = s.upper()
    return (
        "NAME HANDL" in u
        or "NAME HANDLING" in u
        or (u.startswith("NAME ") and "SPEED" in u and "ACCEL" in u)
        or (u.startswith("NAME ") and "B A R S" in u)
        or re.search(r"\bB\s+A\s+R\s+S\s+W\s+L\s+I\s+C\b", u)
    )


def split_flat_table(para: str) -> str | None:
    """If paragraph looks like a flattened vehicle/critter table, split to code block rows."""
    if "NAME HANDL" not in para.upper() and not (
        para.upper().startswith("NAME ") and "SPEED" in para.upper() and "¥" in para
    ):
        # also: long line with many ¥ and digit clusters
        if para.count("¥") < 3 and " p. " not in para:
            return None
        if "NAME " not in para.upper()[:40] and para.count("¥") < 5:
            return None

    # Split before capitalized product-ish tokens that precede a handling-like number pattern
    # Pattern: Word/Word-Word then digit or digit/digit
    header_m = re.match(
        r"^(NAME\s+HANDL(?:ING)?(?:\s+\w+){3,20})\s+(.*)$",
        para,
        re.I,
    )
    if not header_m:
        # try looser
        if not para.upper().startswith("NAME "):
            return None
        parts = para.split(" ", 12)
        # fall through with whole para as body
        header = "NAME HANDL SPEED ACCEL BODY ARMOR PILOT SENS SEATS AVAIL COST REF"
        body = para
        # strip leading NAME ... REF if present
        m2 = re.match(r"^(NAME\b.*?REF)\s+(.*)$", para, re.I)
        if m2:
            header, body = m2.group(1), m2.group(2)
        else:
            return None
    else:
        header, body = header_m.group(1), header_m.group(2)

    # Split rows: look for "Name ... p. N" or cost¥ then next Capitalized name
    # Prefer split before sequences: Capital letter... then number/number or number
    rows = re.split(
        r"(?=\b[A-Z][A-Za-z0-9'\"/\-]*(?:[ \-][A-Z][A-Za-z0-9'\"/\-]*){0,6}\s+\d)",
        body,
    )
    rows = [r.strip() for r in rows if r.strip()]
    if len(rows) < 2:
        # alternate: split on " p. NNN" boundaries keeping delimiter with prior
        chunks = re.split(r"(?<=\bp\.\s?\d{1,3}(?:,\s*[A-Za-z &]+)?)\s+(?=[A-Z])", body)
        rows = [c.strip() for c in chunks if c.strip()]
    if len(rows) < 2:
        return None

    lines = [header] + rows
    return "```\n" + "\n".join(lines) + "\n```"


def demote_bad_heading(h: str) -> str | None:
    """Return None to drop, plain text to demote, or original to keep as ##."""
    raw = h[3:].strip() if h.startswith("## ") else h.strip()
    low = raw.lower()

    if low in KEEP_H2:
        return h if h.startswith("## ") else f"## {raw}"

    # Exact short known titles that got prose smashed onto the same line
    for keep in sorted(KEEP_H2, key=len, reverse=True):
        if low.startswith(keep + " ") and len(raw) > len(keep) + 20:
            # "## Introduction Once upon..." -> keep heading, rest as prose
            rest = raw[len(keep) :].strip()
            return f"## {raw[: len(keep)]}\n\n{rest}"

    # TOC leftovers with many page numbers: "Introduction 5 Home Security 6 ..."
    page_nums = re.findall(r"\b\d{1,3}\b", raw)
    if len(page_nums) >= 3 and len(raw) > 40 and raw.count(" ") >= 6:
        return None  # drop TOC dump
    if len(page_nums) >= 2 and re.match(r"^[\w\s,&'\-]{3,60}\d{1,3}\s+[\w\s,&'\-]+\d{1,3}", raw):
        return None

    # "Posted By:" smashed into heading
    if "posted by" in low:
        return f"**{raw}**"

    # Cost lines as headers
    if re.search(r"\bcost:\s*\d+\s*karma\b", low):
        return f"**{raw}**"

    # Very long "headers" that are really prose (possibly with numbers)
    if len(raw) > 80 and raw.count(" ") > 10:
        return raw  # demote to paragraph

    # Headers that are mostly a page map: "Introduction 5"
    if re.match(r"^[\w\s,&'\-]{3,40}\s+\d{1,3}\s*$", raw) and low not in KEEP_H2:
        return None

    return h if h.startswith("## ") else f"## {raw}"


def split_forum_posts(para: str) -> list[str]:
    """Split smashed JackPoint-style posts: '> Name > text > Other > more'."""
    if para.count(">") < 2:
        return [para]
    # Split before ' > Handle' tokens (handle = capitalized word(s))
    parts = re.split(r"\s+(?=>\s+[A-Z][A-Za-z0-9/]{1,30}\b)", para)
    parts = [p.strip() for p in parts if p.strip()]
    return parts if len(parts) > 1 else [para]


def break_giant_paragraph(para: str, max_chars: int = 900) -> list[str]:
    if len(para) <= max_chars:
        return [para]
    # Don't break tables/code-ish
    if para.startswith("```") or para.startswith("|") or para.upper().startswith("NAME HANDL"):
        return [para]
    if para.startswith("#"):
        return [para]

    # Forum dump first
    posts = split_forum_posts(para)
    if len(posts) > 1:
        out: list[str] = []
        for post in posts:
            out.extend(break_giant_paragraph(post, max_chars))
        return out

    # Flattened bullet lists (not gear tables with AVAIL "-" columns)
    if (
        " - " in para
        and para.count(" - ") >= 4
        and "¥" not in para
        and "NAME HANDL" not in para.upper()
        and not re.search(r"\b\d+/\d+\b", para)
    ):
        bullets = re.split(r"\s+(?=-\s)", para)
        bullets = [b.strip() for b in bullets if b.strip()]
        if len(bullets) >= 3 and all(len(b) < 500 for b in bullets[:5]):
            return bullets

    # Split on sentence boundaries, regroup
    parts = re.split(r"(?<=[.!?])\s+(?=[\"'A-Z>])", para)
    if len(parts) == 1:
        # Hard wrap as last resort for giant blobs
        if len(para) > max_chars * 2:
            hard: list[str] = []
            buf = ""
            for word in para.split():
                if not buf:
                    buf = word
                elif len(buf) + 1 + len(word) <= max_chars:
                    buf = buf + " " + word
                else:
                    hard.append(buf)
                    buf = word
            if buf:
                hard.append(buf)
            return hard
        return [para]

    out: list[str] = []
    buf = ""
    for sent in parts:
        if not buf:
            buf = sent
        elif len(buf) + 1 + len(sent) <= max_chars:
            buf = buf + " " + sent
        else:
            out.append(buf.strip())
            buf = sent
    if buf.strip():
        out.append(buf.strip())
    return out or [para]


def unwrap_false_code_blocks(text: str) -> str:
    """Turn prose mistakenly fenced as code back into paragraphs."""

    def repl(m: re.Match) -> str:
        body = m.group(1).strip("\n")
        u = body.upper()
        if (
            "NAME HANDL" in u
            or re.search(r"\bB\s+A\s+R\s+S\b", u)
            or "DV " in u
            or "ACC " in u
            or body.count("¥") >= 2
            or "CONDITION MONITOR" in u
        ):
            return m.group(0)
        # Prose: join soft wraps into a paragraph
        lines = [ln.strip() for ln in body.splitlines() if ln.strip()]
        para = " ".join(lines)
        para = fix_soft_hyphens(para)
        return para

    text = re.sub(r"```\n(.*?)```", repl, text, flags=re.S)
    # Join orphan wraps: "... From air\n\nvehicles that ..."
    text = re.sub(
        r"([a-z,;:])\n\n([a-z])",
        r"\1 \2",
        text,
    )
    return text


def polish_body(body: str) -> str:
    body = fix_soft_hyphens(body)
    body = fix_soft_pairs(body)
    body = unwrap_false_code_blocks(body)
    for a, b in (("\u2014", "-"), ("\u2013", "-"), ("—", "-"), ("–", "-")):
        body = body.replace(a, b)

    lines = body.splitlines()
    out: list[str] = []
    in_code = False
    i = 0
    while i < len(lines):
        ln = lines[i]
        if ln.strip().startswith("```"):
            in_code = not in_code
            out.append(ln)
            i += 1
            continue
        if in_code:
            # Join book-name wraps: "Hard\nTargets", "Stolen\nSouls", "p. 139,\nHard"
            cur = ln.strip()
            prev = out[-1].strip() if out else ""
            if (
                cur
                and prev
                and not prev.startswith("```")
                and re.match(r"^[A-Z][A-Za-z0-9'&\-]{1,24}$", cur)
                and not re.search(r"\d", cur)
                and (
                    prev.endswith(",")
                    or re.match(r"^[A-Z][A-Za-z0-9'&\-]{1,24}$", prev)
                )
                and not re.search(r"\d", prev)
            ):
                out[-1] = out[-1].rstrip() + " " + cur
                i += 1
                continue
            out.append(ln)
            i += 1
            continue

        if ln.startswith("## "):
            fixed = demote_bad_heading(ln)
            if fixed is None:
                i += 1
                continue
            out.append(fixed)
            i += 1
            continue

        # Flattened table paragraph
        if ln and not ln.startswith("#") and not ln.startswith("-"):
            tab = split_flat_table(ln.strip())
            if tab:
                out.append("")
                out.append(tab)
                out.append("")
                i += 1
                continue

        # Giant paragraph break (including forum lines starting with >)
        if ln.strip() and not ln.startswith(("#", "|", "`")):
            chunks = break_giant_paragraph(ln.strip())
            for j, ch in enumerate(chunks):
                if j:
                    out.append("")
                out.append(ch)
            i += 1
            continue

        out.append(ln)
        i += 1

    text = "\n".join(out)
    text = re.sub(r"\n{3,}", "\n\n", text)
    # Clean "danger - ous" style leftover after paragraph join misses
    text = fix_soft_hyphens(text)
    text = fix_soft_pairs(text)
    return text.strip() + "\n"


def polish_file(path: Path) -> bool:
    raw = path.read_text(encoding="utf-8")
    lines = raw.splitlines()
    if not lines or not lines[0].startswith("# "):
        return False
    title = lines[0]
    src = ""
    body_start = 1
    for i, ln in enumerate(lines[1:], start=1):
        if ln.startswith("**Source:**"):
            src = ln
            body_start = i + 1
            break
    while body_start < len(lines) and lines[body_start].strip() == "":
        body_start += 1
    body = "\n".join(lines[body_start:])
    new_body = polish_body(body)
    new = f"{title}\n\n{src}\n\n{new_body}" if src else f"{title}\n\n{new_body}"
    for a, b in (("\u2014", "-"), ("\u2013", "-"), ("—", "-"), ("–", "-")):
        new = new.replace(a, b)
    if new != raw:
        path.write_text(new, encoding="utf-8")
        return True
    return False


def main():
    changed = 0
    total = 0
    for book in BOOKS:
        folder = ROOT / book
        for p in sorted(folder.glob("[0-9]*.md")):
            total += 1
            if polish_file(p):
                changed += 1
                print("polished", book, p.name, p.stat().st_size)
            else:
                print("unchanged", book, p.name)
    print(f"done: {changed}/{total} files changed")


if __name__ == "__main__":
    main()
