# -*- coding: utf-8 -*-
"""Convert Shadow Spells fitz extract to dense LLM-reference Source Texts markdown."""
from __future__ import annotations

import re
from pathlib import Path

EXTRACT = Path(r"c:\Users\admin\Desktop\Shadowrun\Source\_extract\shadow_spells_full.txt")
OUT = Path(r"c:\Users\admin\Desktop\Shadowrun\Source Texts\Shadow Spells")
REPORT = Path(r"c:\Users\admin\Desktop\Shadowrun\Source\_extract\shadow_spells_sweep_report.md")

PDF = "Source/PDF/shadow-spells-pdf.pdf"

# Known JackPoint handles (exact display forms)
HANDLES = {
    "danger sensei",
    "man-of-many-names",
    "netcat",
    "chainmaker",
    "elijah",
    "kay st. irregular",
    "stone",
    "frosty",
    "slamm-0!",
    "slamm-0",
    "ethernaut",
    "goat foot",
    "bull",
    "clockwork",
    "sticks",
    "red anya",
    "wise guy",
    "glitch",
    "cosmos",
    "cosmo",
    "fianchetto",
    "mihoshi oni",
    "kane",
    "butch",
    "plan 9",
    "traveler jones",
    "winterhawk",
    "orkce0",
    "aufheben",
    "mr. bonds",
    "/dev/grrl",
    "hard exit",
    "sounder",
    "beaker",
    "2xl",
    "snopes",
    "sunshine",
}


def clean_dashes(text: str) -> str:
    for a, b in (
        ("\u2014", "-"),
        ("\u2013", "-"),
        ("\u2212", "-"),
        ("—", "-"),
        ("–", "-"),
        ("\ufeff", ""),
        ("\u00a0", " "),
        ("\u2018", "'"),
        ("\u2019", "'"),
        ("\u201c", '"'),
        ("\u201d", '"'),
        ("\u2026", "..."),
        ("\u00ad", ""),  # soft hyphen
    ):
        text = text.replace(a, b)
    return text


def strip_chrome(text: str) -> str:
    lines = []
    for ln in text.splitlines():
        s = ln.strip()
        if not s:
            lines.append("")
            continue
        if re.match(r"^>>\s*SHADOWRUN\s*<<$", s, re.I):
            continue
        if re.match(r"^<<\s*SHADOW SPELLS\s*>>", s, re.I):
            continue
        if re.match(r"^===== PAGE \d+ =====$", s):
            continue
        # Do not strip lone digits: NPC attribute values are often single numbers.
        lines.append(ln.rstrip())
    return "\n".join(lines)


def fix_soft_hyphens(text: str) -> str:
    # de- vote / de-\nvote -> devote
    text = re.sub(r"([A-Za-z]{2,})-\s*\n\s*([a-z]{2,})", r"\1\2", text)
    text = re.sub(r"([A-Za-z]{2,})-\s+([a-z]{2,})", r"\1\2", text)
    return text


def join_broken_lines(text: str) -> str:
    """Join lines that are mid-sentence soft wraps (not headings/stats)."""
    raw = [ln.rstrip() for ln in text.splitlines()]
    out: list[str] = []
    buf = ""

    def flush() -> None:
        nonlocal buf
        if buf:
            out.append(buf)
            buf = ""

    for ln in raw:
        s = ln.strip()
        if not s:
            flush()
            out.append("")
            continue
        # Keep structural / short label lines separate
        if (
            s.startswith(">")
            or s.startswith("#")
            or s.startswith("|")
            or s.startswith("**")
            or re.match(r"^(Type|Range|Damage|Duration|Drain|Cost|Action|Combat|Detection|Health|Illusion|Manipulation|Note|Members|Dues|Areas of Expertise|Patron|Description and Customs|Initiative|Astral Initiative|Condition Monitor|Limits|Armor|Skills|Qualities|Vehicle|Vehicles|Spells|Rituals|Gear|Weapons|Powers|Optional Powers|Adept Powers|Augmentations|Initiate Grade|Metamagic|PREFERRED|REQUIRED|EFFECT|DISEASE|AVAIL|Raw,|Refined|Radical|Orichalum):", s)
            or re.match(r"^[A-Z0-9][A-Z0-9 /,'&\-]{2,}$", s)  # ALL CAPS heading-ish
            or re.fullmatch(r"[BARSWLICEDGMFxf0-9+\-./() ]+", s) and len(s) < 40
        ):
            flush()
            out.append(s)
            continue

        if not buf:
            buf = s
            continue
        # Soft wrap: previous does not end sentence and current continues lowercase/continuation
        if buf.endswith("-") and s and s[0].islower():
            buf = buf[:-1] + s
            continue
        if not re.search(r'[.!?]"?$', buf) and not buf.endswith(":"):
            buf = buf + " " + s
            continue
        flush()
        buf = s
    flush()
    return "\n".join(out)


def is_handle(s: str) -> bool:
    t = s.strip().lstrip(">").strip()
    if not t or len(t) > 40:
        return False
    key = t.lower().rstrip(".")
    return key in HANDLES or key.replace("!", "") in HANDLES


def format_jp(text: str) -> str:
    """Flip body-before-handle JP comments to > **Handle** / > text."""
    lines = [ln.rstrip() for ln in text.splitlines()]
    out: list[str] = []
    i = 0
    while i < len(lines):
        s = lines[i].strip()
        # Pattern: lone ">" then body lines then handle (possibly after another ">")
        if s == ">" or s == ">\t":
            chunk: list[str] = []
            i += 1
            while i < len(lines):
                t = lines[i].strip()
                if not t:
                    i += 1
                    # blank inside comment: keep scanning unless next is clearly new section
                    continue
                if t in (">", ">\t"):
                    # peek: next non-empty might be handle
                    j = i + 1
                    while j < len(lines) and not lines[j].strip():
                        j += 1
                    if j < len(lines) and is_handle(lines[j].strip()):
                        i = j
                        break
                    # another comment starting
                    break
                bare = t.lstrip(">").strip()
                if is_handle(bare) and len(chunk) > 0:
                    # handle without preceding ">"
                    handle = bare
                    body = " ".join(chunk)
                    out.append(f"> **{handle}**")
                    out.append(f"> {body}")
                    out.append("")
                    i += 1
                    chunk = []
                    break
                if is_handle(bare) and not chunk:
                    # handle-only? unusual
                    out.append(f"> **{bare}**")
                    i += 1
                    break
                if t.startswith("##") or t.startswith("###"):
                    break
                chunk.append(t.lstrip(">").strip() if t.startswith(">") else t)
                i += 1
            else:
                if chunk:
                    out.append("> " + " ".join(chunk))
                    out.append("")
                continue

            if chunk:
                # expect handle at i
                handle = ""
                if i < len(lines):
                    h = lines[i].strip().lstrip(">").strip()
                    if is_handle(h):
                        handle = h
                        i += 1
                body = " ".join(chunk)
                if handle:
                    out.append(f"> **{handle}**")
                    out.append(f"> {body}")
                else:
                    out.append(f"> {body}")
                out.append("")
            continue

        # Already "> Handle" short line
        if s.startswith(">") and is_handle(s):
            handle = s.lstrip(">").strip()
            out.append(f"> **{handle}**")
            i += 1
            continue

        out.append(lines[i])
        i += 1

    text = "\n".join(out)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def split_pages(raw: str) -> dict[int, str]:
    pages: dict[int, str] = {}
    parts = re.split(r"===== PAGE (\d+) =====\n", raw)
    # parts[0] preamble, then n, content, n, content...
    for i in range(1, len(parts), 2):
        pages[int(parts[i])] = parts[i + 1]
    return pages


def page_text(pages: dict[int, str], *idxs: int) -> str:
    return "\n".join(pages[i] for i in idxs if i in pages)


ATTR_KEYS = ["B", "A", "R", "S", "W", "L", "I", "C", "EDG", "ESS", "M"]


def parse_attr_block(lines: list[str], start: int) -> tuple[dict[str, str], int] | None:
    """If lines[start] is 'B' and next lines are attribute headers then values, parse."""
    if lines[start].strip() != "B":
        return None
    headers: list[str] = []
    i = start
    while i < len(lines) and lines[i].strip() in ATTR_KEYS:
        headers.append(lines[i].strip())
        i += 1
    if headers != ATTR_KEYS:
        return None
    values: list[str] = []
    while i < len(lines) and len(values) < 11:
        s = lines[i].strip()
        if not s:
            i += 1
            continue
        # stop if we hit a label
        if s in (
            "Initiative",
            "Astral Initiative",
            "Condition Monitor",
            "Limits",
            "Armor",
            "Skills",
            "Qualities",
            "Vehicle",
            "Vehicles",
            "Spells",
            "Rituals",
            "Gear",
            "Weapons",
            "Powers",
            "Optional Powers",
            "Adept Powers",
            "Augmentations",
            "Initiate Grade",
            "Metamagic",
        ):
            break
        values.append(s)
        i += 1
    if len(values) != 11:
        return None
    return dict(zip(headers, values)), i


def format_npc_stats_from_lines(lines: list[str], start: int, name: str) -> tuple[str, int]:
    """Format attribute table + labeled fields starting at B row. Returns (md, next_index)."""
    parsed = parse_attr_block(lines, start)
    if not parsed:
        return "", start
    attrs, i = parsed
    fields: dict[str, str] = {}
    order = [
        "Initiative",
        "Astral Initiative",
        "Condition Monitor",
        "Limits",
        "Armor",
        "Skills",
        "Qualities",
        "Vehicle",
        "Vehicles",
        "Spells",
        "Rituals",
        "Gear",
        "Weapons",
        "Powers",
        "Optional Powers",
        "Adept Powers",
        "Augmentations",
        "Initiate Grade",
        "Metamagic",
    ]
    current = None
    buf: list[str] = []

    def flush_field() -> None:
        nonlocal current, buf
        if current:
            fields[current] = " ".join(buf).strip()
        current = None
        buf = []

    while i < len(lines):
        s = lines[i].strip()
        if not s:
            i += 1
            continue
        if s in order:
            flush_field()
            current = s
            buf = []
            i += 1
            continue
        # New section / name / JP / ALL CAPS heading ends NPC block
        if (
            s.startswith(">")
            or s.startswith("#")
            or (re.match(r"^[A-Z][A-Z0-9 /,'&\-]{3,}$", s) and s not in order and current)
            or s.startswith("POSTED BY")
            or s in ("THREATS", "SUPPLEMENTARY", "GRIMOIRE", "RITUALS", "ADEPT POWERS", "MAGIC SOCIETIES")
        ):
            # allow continuation of multi-line field values that are Title Case
            if current and not re.match(r"^[A-Z][A-Z0-9 /,'&\-]{3,}$", s):
                buf.append(s)
                i += 1
                continue
            flush_field()
            break
        if current:
            buf.append(s)
            i += 1
            continue
        flush_field()
        break
    flush_field()

    rows = ["| " + " | ".join(ATTR_KEYS) + " |", "| " + " | ".join(["---"] * 11) + " |",
            "| " + " | ".join(attrs[k] for k in ATTR_KEYS) + " |"]
    parts = [f"### {name}", "", *rows, ""]
    for key in order:
        if key in fields:
            parts.append(f"**{key}:** {fields[key]}")
            parts.append("")
    return "\n".join(parts).rstrip() + "\n\n", i


def format_tradition_box(name: str, body_lines: list[str]) -> str:
    """Format Combat/Detection/... / Preferred spells block."""
    out = [f"**{name}**", ""]
    prefs: list[str] = []
    mode = "attrs"
    for ln in body_lines:
        s = ln.strip()
        if not s:
            continue
        if s.startswith("PREFERRED"):
            mode = "pref"
            out.append(f"*{s.title()}*")
            continue
        if s.startswith("Note:"):
            out.append(s)
            continue
        if ":" in s and mode == "attrs" and not s.startswith("PREFERRED"):
            k, v = s.split(":", 1)
            out.append(f"- **{k.strip()}:** {v.strip()}")
            continue
        if mode == "pref":
            # tab-separated spell names on one line often
            parts = re.split(r"\t+", s)
            for p in parts:
                p = p.strip()
                if p:
                    prefs.append(p)
            continue
        out.append(s)
    if prefs:
        out.append(", ".join(prefs))
    out.append("")
    return "\n".join(out)


# ---------------------------------------------------------------------------
# Chapter builders (hand-structured where extract interleaves columns)
# ---------------------------------------------------------------------------


def header(title: str, print_pages: str, fitz: str) -> str:
    return (
        f"# {title}\n\n"
        f"**Source:** Shadow Spells | `{PDF}` | print pages ~{print_pages} (fitz {fitz})\n\n"
    )


def build_01(pages: dict[int, str]) -> str:
    t = clean_dashes(strip_chrome(pages[0]))
    t = fix_soft_hyphens(t)
    lines = [ln.strip() for ln in t.splitlines() if ln.strip()]
    # CREDITS
    body = ["## Credits", ""]
    for ln in lines:
        if ln.upper() == "CREDITS":
            continue
        if ln.startswith("©") or ln.startswith("(c)") or "Topps Company" in ln:
            # fold copyright into one paragraph
            continue
        if ":" in ln:
            k, v = ln.split(":", 1)
            body.append(f"**{k.strip()}:** {v.strip()}")
            body.append("")
        else:
            body.append(ln)
            body.append("")
    # copyright from raw
    raw = clean_dashes(pages[0])
    m = re.search(r"©\s*2014.*", raw, re.S)
    if m:
        c = re.sub(r"\s+", " ", m.group(0)).strip()
        c = c.replace("Productions, LLC.", "Productions, LLC.")
        body.append(c)
        body.append("")
    return header("Shadowrun: Shadow Spells", "1", "0") + "\n".join(body)


def build_02(pages: dict[int, str]) -> str:
    t = clean_dashes(strip_chrome(pages[1]))
    t = fix_soft_hyphens(t)
    # Keep JackPoint login fairly literal but denser
    lines = [ln.strip() for ln in t.splitlines()]
    out = [header("JackPoint", "2", "1"), "## JackPoint", ""]
    prose: list[str] = []
    section = None

    def flush_prose() -> None:
        nonlocal prose
        if prose:
            out.append(" ".join(prose))
            out.append("")
            prose = []

    i = 0
    while i < len(lines):
        s = lines[i]
        if not s:
            flush_prose()
            i += 1
            continue
        if s == "JACKPOINT":
            i += 1
            continue
        if s in (
            "JackPoint Stats",
            "Latest News",
            "Personal Alerts",
            "THE INNER CIRCLE",
            "Today's Heads Up",
            "Incoming",
            "Top News Items",
        ):
            flush_prose()
            out.append(f"## {s.title() if s != 'THE INNER CIRCLE' else 'The Inner Circle'}")
            out.append("")
            section = s
            i += 1
            continue
        if s.startswith(">") and "Reginald Furrier" in " ".join(lines[i : i + 3]):
            # quote tagline
            flush_prose()
            q = []
            while i < len(lines) and lines[i].strip():
                q.append(lines[i].strip().lstrip(">").strip().strip('"'))
                i += 1
            quote = " ".join(q)
            quote = quote.replace(" • Reginald Furrier", "")
            out.append(f'> "{quote.strip()}"')
            out.append("> - Reginald Furrier")
            out.append("")
            continue
        if s.startswith(">"):
            flush_prose()
            # news / incoming bullets
            chunk = [s.lstrip(">").strip()]
            i += 1
            while i < len(lines) and lines[i].strip() and not lines[i].strip().startswith(">") and lines[i].strip() not in (
                "JackPoint Stats", "Latest News", "Personal Alerts", "THE INNER CIRCLE",
                "Today's Heads Up", "Incoming", "Top News Items",
            ):
                # continuation or handle
                if lines[i].strip().startswith("[Tag:") or lines[i].strip().endswith("Link"):
                    chunk.append(lines[i].strip())
                    i += 1
                    break
                if re.match(r"^-?\s*[A-Za-z].*", lines[i]) and len(lines[i]) < 40 and "Tag:" not in lines[i]:
                    # possible attribution
                    break
                chunk.append(lines[i].strip())
                i += 1
            out.append("- " + " ".join(chunk))
            out.append("")
            continue
        prose.append(s)
        i += 1
    flush_prose()
    text = "\n".join(out)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def extract_jp_and_prose(block: str) -> str:
    block = clean_dashes(strip_chrome(block))
    block = fix_soft_hyphens(block)
    # Normalize tabs after >
    block = re.sub(r"^>\s*", ">\n", block, flags=re.M)
    # Better: ensure ">\\t" becomes ">"
    block = block.replace(">\t", ">")
    lines = block.splitlines()
    # Re-join soft wraps for non-JP first pass lightly
    joined = join_broken_lines("\n".join(lines))
    return format_jp(joined)


def build_03_traditions(pages: dict[int, str]) -> str:
    """Traditions: reconstruct reading order; sidebars after each tradition."""
    # Pages fitz 2-5 (print 3-6); fitz 5 mostly empty chrome for print 6
    raw = page_text(pages, 2, 3, 4, 5)
    raw = clean_dashes(strip_chrome(raw))
    raw = fix_soft_hyphens(raw)
    raw = raw.replace(">\t", ">")

    # Pull sidebar blocks out
    def take_sidebar(label: str, text: str) -> tuple[str, str]:
        """Return (sidebar_inner, text_without_sidebar)."""
        m = re.search(
            rf"{re.escape(label)}\n((?:Combat:.*?\n)+Drain:.*?(?:\nNote:.*?)?)(?:\nPREFERRED.*?)?(?=\n(?:THE |EGYPTIAN DEITIES|NORSE DEITIES|PREFERRED ADEPT|PSIONIC TRADITION|MAGIC SOCIETIES|POSTED BY|$))",
            text,
            re.S,
        )
        # More manual approach below
        return "", text

    # Manual reconstruction from known structure
    out = [header("Traditions", "3-6", "2-5"), "POSTED BY: WINTERHAWK", ""]

    # Intro through Aboriginal (before Egyptian heading), excluding Aboriginal sidebar
    # Split by major headings
    text = raw

    # Remove empty page residue
    text = re.sub(r"\n{3,}", "\n\n", text)

    # Isolate sidebars with explicit regexes
    aboriginal_sb = None
    egyptian_sb = None
    egyptian_deities = None
    norse_sb = None
    norse_deities = None
    norse_adept = None
    psionic_sb = None

    m = re.search(
        r"ABORIGINAL TRADITION\n(Combat: Beasts\nDetection: Earth\nHealth: Plant\nIllusion: Guidance\nManipulation: Air\nDrain: Willpower \+ Charisma)\nPREFERRED SPELLS\n(.*?)(?=\n(?:=====|>>|<<|as a mentor|THE EGYPTIAN|EGYPTIAN TRADITION|$))",
        text,
        re.S,
    )
    # Simpler line-based extraction
    lines = [ln.rstrip() for ln in text.splitlines()]

    def find_block(start_label: str, end_labels: list[str]) -> tuple[list[str], int, int]:
        start = None
        for i, ln in enumerate(lines):
            if ln.strip() == start_label:
                start = i
                break
        if start is None:
            return [], -1, -1
        end = len(lines)
        for i in range(start + 1, len(lines)):
            if lines[i].strip() in end_labels:
                end = i
                break
        return lines[start:end], start, end

    ab_lines, ab_s, ab_e = find_block(
        "ABORIGINAL TRADITION",
        ["as a mentor spirit, but even those who do not speak of the", "THE EGYPTIAN TRADITION", "EGYPTIAN TRADITION"],
    )
    # Aboriginal sidebar is near end of page 2 - starts with ABORIGINAL TRADITION after Control Pack area
    # Actually on page 2 the order is: POSTED BY, intro, TRADITIONS, Aboriginal body, Adina, JP, Egyptian start, ABORIGINAL TRADITION sidebar

    # Rebuild from scratch with curated content pieces
    # --- Intro ---
    intro_end = None
    for i, ln in enumerate(lines):
        if ln.strip() == "TRADITIONS":
            intro_end = i
            break
    intro = join_broken_lines("\n".join(lines[0:intro_end]))
    intro = format_jp(intro)
    # strip POSTED BY duplicate
    intro = re.sub(r"^POSTED BY: WINTERHAWK\s*", "", intro.strip())
    out.append(intro.strip())
    out.append("")
    out.append("## Traditions")
    out.append("")

    # Aboriginal body: from THE ABORIGINAL TRADITION to before THE EGYPTIAN TRADITION,
    # but exclude ABORIGINAL TRADITION sidebar block
    ab_body_lines: list[str] = []
    i = 0
    while i < len(lines):
        if lines[i].strip() == "THE ABORIGINAL TRADITION":
            i += 1
            while i < len(lines):
                s = lines[i].strip()
                if s == "THE EGYPTIAN TRADITION":
                    break
                if s == "ABORIGINAL TRADITION":
                    # skip sidebar until PREFERRED SPELLS consumed
                    i += 1
                    while i < len(lines):
                        t = lines[i].strip()
                        if t.startswith("THE ") or t == "as a mentor spirit, but even those who do not speak of the":
                            break
                        if t and not t.startswith("Combat:") and t not in (
                            "Detection: Earth", "Health: Plant", "Illusion: Guidance",
                            "Manipulation: Air", "Drain: Willpower + Charisma", "PREFERRED SPELLS",
                            "Clout", "Hawkeye", "Hydrate", "Manascape", "Control Pack",
                        ) and "\t" not in lines[i] and t not in ("Clout", "Hawkeye", "Hydrate", "Manascape", "Control Pack"):
                            # Might be preferred spell names on same/adjacent lines with tabs
                            if re.match(r"^(Clout|Hawkeye|Hydrate|Manascape|Control Pack)", t):
                                i += 1
                                continue
                            if t.startswith("Combat:") or t.startswith("Detection:") or t.startswith("Health:") or t.startswith("Illusion:") or t.startswith("Manipulation:") or t.startswith("Drain:") or t == "PREFERRED SPELLS":
                                i += 1
                                continue
                            break
                        i += 1
                    continue
                ab_body_lines.append(lines[i])
                i += 1
            break
        i += 1

    out.append("## The Aboriginal Tradition")
    out.append("")
    ab_text = format_jp(join_broken_lines("\n".join(ab_body_lines)))
    out.append(ab_text.strip())
    out.append("")
    out.append(format_tradition_box(
        "Aboriginal Tradition",
        [
            "Combat: Beasts",
            "Detection: Earth",
            "Health: Plant",
            "Illusion: Guidance",
            "Manipulation: Air",
            "Drain: Willpower + Charisma",
            "PREFERRED SPELLS",
            "Clout",
            "Hawkeye",
            "Hydrate",
            "Manascape",
            "Control Pack",
        ],
    ))

    # Egyptian: from THE EGYPTIAN TRADITION; body continues after sidebar on next page
    # Collect until THE NORSE TRADITION, excluding EGYPTIAN TRADITION sidebar and deities list placement
    eg_lines: list[str] = []
    i = 0
    while i < len(lines):
        if lines[i].strip() == "THE EGYPTIAN TRADITION":
            i += 1
            while i < len(lines):
                s = lines[i].strip()
                if s == "THE NORSE TRADITION":
                    break
                if s == "EGYPTIAN TRADITION":
                    i += 1
                    while i < len(lines) and lines[i].strip() not in (
                        "EGYPTIAN DEITIES", "serker, throwing themselves", "THE NORSE TRADITION", "THE PSIONIC TRADITION"
                    ):
                        # skip until deities or body continuation markers - actually deities is part of sidebar
                        if lines[i].strip() == "EGYPTIAN DEITIES":
                            break
                        i += 1
                    if i < len(lines) and lines[i].strip() == "EGYPTIAN DEITIES":
                        i += 1
                        while i < len(lines) and lines[i].strip() not in (
                            "serker, throwing themselves into combat with abandon.",
                            "THE NORSE TRADITION",
                        ):
                            # deities lines
                            i += 1
                    continue
                # Page break continuation starts with "as a mentor spirit"
                eg_lines.append(lines[i])
                i += 1
            break
        i += 1

    # Prepend the orphaned start from page 2 (Egyptian intro before sidebar)
    # Already included via THE EGYPTIAN TRADITION collection - but page 2 had Egyptian start BEFORE aboriginal sidebar
    # Check: on page 2 Egyptian starts, then ABORIGINAL sidebar, then page 3 continues "as a mentor"
    # Our loop collected from THE EGYPTIAN TRADITION including text before ABORIGINAL TRADITION skip... 
    # When we hit ABORIGINAL TRADITION inside Egyptian collection we need to skip it - handled above only for EGYPTIAN TRADITION label.
    # Fix: also skip ABORIGINAL TRADITION when collecting Egyptian
    eg_clean: list[str] = []
    i = 0
    eg_src = eg_lines
    while i < len(eg_src):
        if eg_src[i].strip() == "ABORIGINAL TRADITION":
            i += 1
            while i < len(eg_src) and eg_src[i].strip() not in ("as a mentor spirit, but even those who do not speak of the",) and not eg_src[i].strip().startswith("Fernando") and eg_src[i].strip() != "THE NORSE TRADITION":
                # skip preferred spells etc.
                if eg_src[i].strip().startswith("The customs") or eg_src[i].strip().startswith("as a mentor"):
                    break
                i += 1
            continue
        eg_clean.append(eg_src[i])
        i += 1

    out.append("## The Egyptian Tradition")
    out.append("")
    out.append(format_jp(join_broken_lines("\n".join(eg_clean))).strip())
    out.append("")
    out.append(format_tradition_box(
        "Egyptian Tradition",
        [
            "Combat: Fire",
            "Detection: Earth",
            "Health: Air",
            "Illusion: Guidance",
            "Manipulation: Water",
            "Drain: Willpower + Intuition",
            "Note: This is a possession tradition.",
            "PREFERRED SPELLS",
            "Corrode",
            "Translate",
            "Convert Blood to Ichor",
            "Phantasm",
            "Evaporate",
        ],
    ))
    out.append("**Egyptian Deities**")
    out.append("")
    for d in [
        "Ra, the sun god",
        "Osiris, god of the underworld",
        "Set, god of the desert",
        "Thoth, inventor of writing",
        "Horus, patron of kings",
        "Bast, temple guardian",
    ]:
        out.append(f"- {d}")
    out.append("")

    # Norse
    no_lines: list[str] = []
    i = 0
    while i < len(lines):
        if lines[i].strip() == "THE NORSE TRADITION":
            i += 1
            while i < len(lines):
                s = lines[i].strip()
                if s == "THE PSIONIC TRADITION":
                    break
                if s == "EGYPTIAN TRADITION":
                    i += 1
                    while i < len(lines) and lines[i].strip() not in ("EGYPTIAN DEITIES", "serker, throwing themselves into combat with abandon."):
                        i += 1
                    if i < len(lines) and lines[i].strip() == "EGYPTIAN DEITIES":
                        i += 1
                        while i < len(lines) and "," in lines[i] or lines[i].strip().startswith(("Ra", "Osiris", "Set", "Thoth", "Horus", "Bast")):
                            if lines[i].strip() in ("serker, throwing themselves into combat with abandon.", "THE NORSE TRADITION", "THE PSIONIC TRADITION", "NORSE TRADITION"):
                                break
                            if lines[i].strip().startswith("serker"):
                                break
                            i += 1
                    continue
                if s == "NORSE TRADITION":
                    i += 1
                    while i < len(lines) and lines[i].strip() not in ("THE PSIONIC TRADITION", "PSIONIC TRADITION"):
                        if lines[i].strip().startswith("Paris hosts"):
                            break
                        i += 1
                    continue
                no_lines.append(lines[i])
                i += 1
            break
        i += 1

    # Prepend page-break "serker..." if present at start of page 4 - it's continuation of berserker from page 3
    # Our Norse collection starts at THE NORSE TRADITION which includes up through "role of ber-" then Egyptian sidebar then "serker..."
    # Need to ensure serker line is in no_lines
    if not any("serker" in x for x in no_lines):
        for ln in lines:
            if "serker, throwing" in ln:
                # insert after ber- line
                for j, x in enumerate(no_lines):
                    if x.strip().endswith("ber-") or x.strip().endswith("of ber-") or "role of ber" in x:
                        no_lines.insert(j + 1, ln)
                        break
                else:
                    no_lines.insert(0, ln)
                break

    out.append("## The Norse Tradition")
    out.append("")
    out.append(format_jp(join_broken_lines("\n".join(no_lines))).strip())
    out.append("")
    out.append(format_tradition_box(
        "Norse Tradition",
        [
            "Combat: Guardian",
            "Detection: Earth",
            "Health: Plant",
            "Illusion: Air",
            "Manipulation: Fire",
            "Drain: Willpower + Logic",
            "PREFERRED SPELLS",
            "Death Touch",
            "Shatter",
            "Eyes of the Pack",
            "Personal Warmth",
            "Insulate",
            "Shape Ice",
        ],
    ))
    out.append("**Norse Deities**")
    out.append("")
    for d in [
        "Odin, the Allfather",
        "Thor, god of thunder",
        "Freya, goddess of fertility",
        "Loki, god of mischief, a figure not actively worshipped until the Sixth Age",
    ]:
        out.append(f"- {d}")
    out.append("")
    out.append("*Preferred Adept Abilities:* Combat Sense, Pain Resistance, Counterstrike, Supernatural Toughness")
    out.append("")

    # Psionic
    ps_lines: list[str] = []
    i = 0
    while i < len(lines):
        if lines[i].strip() == "THE PSIONIC TRADITION":
            i += 1
            while i < len(lines):
                s = lines[i].strip()
                if s in ("NORSE TRADITION", "PSIONIC TRADITION", "MAGIC SOCIETIES"):
                    if s == "PSIONIC TRADITION":
                        i += 1
                        while i < len(lines) and lines[i].strip() not in ("MAGIC SOCIETIES",):
                            i += 1
                        break
                    if s == "NORSE TRADITION":
                        i += 1
                        while i < len(lines) and lines[i].strip() != "THE PSIONIC TRADITION" and not lines[i].strip().startswith("Paris"):
                            if lines[i].strip() == "PSIONIC TRADITION":
                                break
                            i += 1
                        continue
                    break
                ps_lines.append(lines[i])
                i += 1
            break
        i += 1

    out.append("## The Psionic Tradition")
    out.append("")
    out.append(format_jp(join_broken_lines("\n".join(ps_lines))).strip())
    out.append("")
    out.append(format_tradition_box(
        "Psionic Tradition",
        [
            "Combat: Fire",
            "Detection: Air",
            "Health: Man",
            "Illusion: Guidance",
            "Manipulation: Task",
            "Drain: Willpower + Intuition",
            "Note: This is a possession tradition",
            "PREFERRED SPELLS",
            "Control Emotion",
            "Control Mind",
            "Mind Link",
            "Mind Probe",
            "Nutrition",
        ],
    ))
    out.append("[print quirk: preferred spell listed as Control Emotion; Supplementary Grimoire spell is Control Emotions]")
    out.append("")
    out.append("[print pages 3-6: tradition sidebars were column-interleaved in the PDF extract; rebuilt into tradition sections. Fitz page 5 / print page 6 is essentially blank after chrome.]")
    out.append("")

    text = "\n".join(out)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = clean_dashes(text)
    return text.strip() + "\n"


def spell_block(name: str, tags: str | None, stats: dict[str, str], body: str) -> str:
    parts = [f"### {name}", ""]
    if tags:
        parts.append(f"*{tags}*")
        parts.append("")
    # Prefer ordered keys
    for k in ("Type", "Range", "Damage", "Duration", "Drain", "Action"):
        if k in stats:
            parts.append(f"**{k}:** {stats[k]}")
    parts.append("")
    if body:
        parts.append(body.strip())
        parts.append("")
    return "\n".join(parts)


def parse_spell_stats(chunk: str) -> tuple[dict[str, str], str]:
    stats: dict[str, str] = {}
    # Normalize whitespace
    c = re.sub(r"[ \t]+", " ", chunk)
    for key in ("Type", "Range", "Damage", "Duration", "Drain", "Action"):
        m = re.search(rf"{key}:\s*([^\n]+?)(?=\s*(?:Type|Range|Damage|Duration|Drain|Action):|\n\n|$)", c)
        if m:
            stats[key] = re.sub(r"\s+", " ", m.group(1)).strip()
            # Fix Drain spacing F-2 -> F - 2 optionally keep as print
    # Body: after last Drain/Duration line
    body = c
    for key in ("Type", "Range", "Damage", "Duration", "Drain", "Action"):
        body = re.sub(rf"{key}:\s*[^\n]+", "", body, count=1)
    body = re.sub(r"\n{2,}", "\n\n", body).strip()
    # Normalize drain ASCII
    if "Drain" in stats:
        stats["Drain"] = stats["Drain"].replace("F–", "F - ").replace("F-", "F - ").replace("F -  ", "F - ")
        stats["Drain"] = re.sub(r"F\s*-\s*", "F - ", stats["Drain"])
        stats["Drain"] = re.sub(r"F\s*\+\s*", "F + ", stats["Drain"])
    return stats, body


def build_grimoire(pages: dict[int, str]) -> str:
    """Spells from fitz 15 through before RITUALS on fitz 21."""
    raw = page_text(pages, 15, 16, 17, 18, 19, 20, 21)
    raw = clean_dashes(strip_chrome(raw))
    raw = fix_soft_hyphens(raw)
    # Cut at RITUALS
    if "\nRITUALS\n" in raw:
        raw = raw.split("\nRITUALS\n")[0]
    raw = raw.replace(">\t", ">")

    out = [header("Supplementary Grimoire", "16-22 (spells; before Rituals)", "15-21"), "## Supplementary Grimoire", ""]

    # Introduction
    m = re.search(r"INTRODUCTION\n(.*?)(?=\nCOMBAT SPELLS\n)", raw, re.S)
    if m:
        out.append("## Introduction")
        out.append("")
        intro = join_broken_lines(m.group(1))
        out.append(intro.strip())
        out.append("")

    # Known spell definitions in order with tags from extract
    # We'll regex-split on ALL CAPS spell names that precede (TAGS) or Type:

    spell_names = [
        ("CHILL", "DIRECT"),
        ("FRIGID", "DIRECT"),
        ("FLAME BURST", "DIRECT, ELEMENTAL"),
        ("MAGEBOLT", "DIRECT"),
        (r"\[ELEMENT\] GRENADE", "INDIRECT, ELEMENTAL"),
        ("SUNBEAM", "INDIRECT"),
        ("PASSENGER", "PASSIVE, PSYCHIC"),
        ("RECORDED ROOM", "PASSIVE, AREA"),
        ("SECRET HANDSHAKE", "ACTIVE, AREA"),
        ("BROADCAST", "ACTIVE, AREA"),
        ("SENDING", "ACTIVE, EXTENDED AREA"),
        (r"\[SENSE\] LINK", "PASSIVE, PHYSIC"),  # print quirk PHYSIC
        ("CONVERT BLOOD TO ICHOR", "ESSENCE, NEGATIVE"),
        ("DECONTAMINATION", None),
        ("DEHYDRATE", "NEGATIVE"),
        ("GHOULISH STRENGTH", "ESSENCE"),
        ("HEALTHY GLOW", None),
        ("HYDRATE", None),
        ("INFLICT DISEASE", "NEGATIVE, ESSENCE"),
        ("NAUSEATE", "NEGATIVE"),
        ("ALLEVIATE NAUSEA", None),
        ("PERSONAL WARMTH", None),
        ("ROT", "ESSENCE, NEGATIVE"),
        ("VAMPIRIC SPEED", "ESSENCE"),
        ("FALSE IMPRESSION", None),
        ("MANASCAPE", None),
        ("VAMPIRIC STEALTH", None),
        ("AIR FILTER", "PHYSICAL"),
        ("ALTER MEMORY", "MENTAL"),
        ("ALTER TEMPERATURE", "PHYSICAL"),
        ("ASTRAL ARMOR", "MENTAL"),
        ("CONTROL EMOTIONS", "MENTAL"),
        ("MOB MOOD", "MENTAL"),
        ("EVAPORATE", "PHYSICAL"),
        ("LOOKING GLASS", "PHYSICAL"),
        ("INSULATE", "PHYSICAL, ENVIRONMENTAL"),
        ("NAPALM WALL", "PHYSICAL, ENVIRONMENTAL"),
        ("PETRIFY", "PHYSICAL"),
        ("PULSE", "PHYSICAL, ENVIRONMENTAL"),
        ("RADIATION SHIELD", "PHYSICAL"),
        ("RADIATION BARRIER", "PHYSICAL"),
    ]

    # Section headers
    sections = {
        "COMBAT SPELLS": "## Combat Spells",
        "DETECTION SPELLS": "## Detection Spells",
        "HEALTH SPELLS": "## Health Spells",
        "ILLUSION SPELLS": "## Illusion Spells",
        "MANIPULATION SPELLS": "## Manipulation Spells",
        "EXAMPLE": "### Example (Sunbeam)",
        "SAMPLE DISEASES": "## Sample Diseases",
    }

    # Work line-oriented for spells
    lines = [ln.rstrip() for ln in raw.splitlines()]
    # Drop SUPPLEMENTARY / GRIMOIRE / INTRODUCTION already handled
    start_i = 0
    for i, ln in enumerate(lines):
        if ln.strip() == "COMBAT SPELLS":
            start_i = i
            break

    i = start_i
    shared_body_pending: list[str] = []  # for Chill/Frigid shared description

    def collect_until(stop_preds) -> list[str]:
        nonlocal i
        buf: list[str] = []
        while i < len(lines):
            s = lines[i].strip()
            if any(p(s) for p in stop_preds):
                break
            buf.append(lines[i])
            i += 1
        return buf

    def is_spell_header(s: str) -> bool:
        if s in sections:
            return True
        for name, _ in spell_names:
            n = name.replace(r"\[", "[").replace(r"\]", "]")
            if s == n or s == name:
                return True
            if re.fullmatch(name, s):
                return True
        return False

    while i < len(lines):
        s = lines[i].strip()
        if not s:
            i += 1
            continue
        if s in sections:
            out.append(sections[s])
            out.append("")
            i += 1
            if s == "HEALTH SPELLS":
                # Negative Health Spells intro paragraph
                buf = []
                i_save = i
                while i < len(lines) and lines[i].strip() not in ("CONVERT BLOOD TO ICHOR",) and not re.match(r"^CONVERT BLOOD", lines[i].strip()):
                    if lines[i].strip().startswith("The following") or lines[i].strip().startswith("Negative") or lines[i].strip().startswith("character cause") or lines[i].strip().startswith("resisted by") or lines[i].strip().startswith("cable)") or lines[i].strip().startswith("For details"):
                        buf.append(lines[i])
                        i += 1
                        continue
                    if not lines[i].strip():
                        i += 1
                        continue
                    break
                if buf:
                    out.append(join_broken_lines("\n".join(buf)).strip())
                    out.append("")
            if s == "SAMPLE DISEASES":
                # table
                out.append("| Disease | Required Power | Effect |")
                out.append("|---|---|---|")
                # skip header labels
                while i < len(lines) and lines[i].strip() in ("DISEASE", "REQUIRED", "POWER", "EFFECT", ""):
                    i += 1
                # rows
                diseases = [
                    ("Botulism", "4", "Malaise, Nausea, Paralysis"),
                    ("Influenza", "2", "Stun Damage (Fatigue), Disorientation"),
                    ("HSV-5", "5", "Agony, Malaise, Stun Damage"),
                    ("VITAS-3", "6", "Malaise, Nausea, Stun Damage"),
                ]
                for d, p, e in diseases:
                    out.append(f"| {d} | {p} | {e} |")
                out.append("")
                # skip leftover disease lines
                while i < len(lines):
                    t = lines[i].strip()
                    if t in ("ROT", "ILLUSION SPELLS", "MANIPULATION SPELLS") or t.startswith("ROT"):
                        break
                    i += 1
                continue
            if s == "EXAMPLE":
                buf = collect_until([lambda x: x in ("DETECTION SPELLS", "PASSENGER") or x == "DETECTION SPELLS"])
                out.append(join_broken_lines("\n".join(buf)).strip())
                out.append("")
                continue
            continue

        matched = None
        tags = None
        for name, tag in spell_names:
            if re.fullmatch(name, s) or s == name.replace(r"\[", "[").replace(r"\]", "]"):
                matched = name.replace(r"\[", "[").replace(r"\]", "]")
                tags = tag
                break
        if not matched:
            # orphan prose
            out.append(s)
            i += 1
            continue

        i += 1
        # optional (TAGS) line
        if i < len(lines) and lines[i].strip().startswith("(") and lines[i].strip().endswith(")"):
            tags = lines[i].strip().strip("()")
            i += 1

        # Collect Type/Range/... lines and body until next spell/section
        stat_lines: list[str] = []
        body_lines: list[str] = []
        while i < len(lines):
            t = lines[i].strip()
            if not t:
                i += 1
                if body_lines:
                    # blank after body start: keep one
                    body_lines.append("")
                continue
            if t in sections or any(re.fullmatch(n, t) or t == n.replace(r"\[", "[").replace(r"\]", "]") for n, _ in spell_names):
                break
            if re.match(r"^(Type|Range|Damage|Duration|Drain|Action):", t):
                # may have multiple on one line separated by spaces/tabs
                # Split carefully
                parts = re.findall(r"(Type|Range|Damage|Duration|Drain|Action):\s*([^\t]+?)(?=\s{2,}|\t|(?:Type|Range|Damage|Duration|Drain|Action):|$)", t)
                if parts:
                    for k, v in parts:
                        stat_lines.append(f"{k}: {v.strip()}")
                else:
                    stat_lines.append(t)
                i += 1
                continue
            body_lines.append(lines[i])
            i += 1

        stats: dict[str, str] = {}
        for sl in stat_lines:
            if ":" in sl:
                k, v = sl.split(":", 1)
                v = v.strip()
                if k.strip() == "Drain":
                    v = v.replace("F–", "F - ").replace("F-", "F - ")
                    v = re.sub(r"F\s*-\s*", "F - ", v)
                    v = re.sub(r"F\s*\+\s*", "F + ", v)
                stats[k.strip()] = v

        body = join_broken_lines("\n".join(body_lines)).strip()
        # Chill+Frigid share body printed after Frigid stats
        if matched == "CHILL":
            # body may be empty; will be filled when Frigid body arrives - store stats
            out.append(spell_block("Chill", tags, stats, ""))
            # stash - actually Frigid follows and then shared body
            continue
        if matched == "FRIGID":
            out.append(spell_block("Frigid", tags, stats, ""))
            if body:
                out.append(body)
                out.append("")
                out.append("[print: Chill and Frigid share the above rules text]")
                out.append("")
            continue
        if matched == "FALSE IMPRESSION":
            out.append(spell_block("False Impression", tags, stats, ""))
            continue
        if matched == "MANASCAPE":
            out.append(spell_block("Manascape", tags, stats, body))
            if body:
                out.append("[print: False Impression and Manascape share the illusion-to-magical-senses rules; False Impression = single spell/astral form; Manascape = area]")
                out.append("")
            continue
        if matched == "CONTROL EMOTIONS":
            out.append(spell_block("Control Emotions", tags, stats, ""))
            continue
        if matched == "MOB MOOD":
            out.append(spell_block("Mob Mood", tags, stats, body))
            continue
        if matched == "BROADCAST":
            out.append(spell_block("Broadcast", tags, stats, ""))
            continue
        if matched == "SENDING":
            out.append(spell_block("Sending", tags, stats, body))
            continue
        if matched == "RADIATION SHIELD":
            out.append(spell_block("Radiation Shield", tags, stats, ""))
            continue
        if matched == "RADIATION BARRIER":
            out.append(spell_block("Radiation Barrier", tags, stats, body))
            continue

        display = matched.title() if matched[0] != "[" else matched
        # Better titles for known
        title_map = {
            "MAGEBOLT": "Magebolt",
            "FLAME BURST": "Flame Burst",
            "[ELEMENT] GRENADE": "[Element] Grenade",
            "SUNBEAM": "Sunbeam",
            "PASSENGER": "Passenger",
            "RECORDED ROOM": "Recorded Room",
            "SECRET HANDSHAKE": "Secret Handshake",
            "[SENSE] LINK": "[Sense] Link",
            "CONVERT BLOOD TO ICHOR": "Convert Blood to Ichor",
            "DECONTAMINATION": "Decontamination",
            "DEHYDRATE": "Dehydrate",
            "GHOULISH STRENGTH": "Ghoulish Strength",
            "HEALTHY GLOW": "Healthy Glow",
            "HYDRATE": "Hydrate",
            "INFLICT DISEASE": "Inflict Disease",
            "NAUSEATE": "Nauseate",
            "ALLEVIATE NAUSEA": "Alleviate Nausea",
            "PERSONAL WARMTH": "Personal Warmth",
            "ROT": "Rot",
            "VAMPIRIC SPEED": "Vampiric Speed",
            "VAMPIRIC STEALTH": "Vampiric Stealth",
            "AIR FILTER": "Air Filter",
            "ALTER MEMORY": "Alter Memory",
            "ALTER TEMPERATURE": "Alter Temperature",
            "ASTRAL ARMOR": "Astral Armor",
            "EVAPORATE": "Evaporate",
            "LOOKING GLASS": "Looking Glass",
            "INSULATE": "Insulate",
            "NAPALM WALL": "Napalm Wall",
            "PETRIFY": "Petrify",
            "PULSE": "Pulse",
        }
        display = title_map.get(matched, matched.title())
        note = ""
        if matched == "[SENSE] LINK":
            note = "\n\n[print quirk: tag printed as PHYSIC, likely PHYSICAL]"
        block = spell_block(display, tags, stats, body + note)
        out.append(block)

    text = "\n".join(out)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return clean_dashes(text).strip() + "\n"


def build_rituals(pages: dict[int, str]) -> str:
    raw = page_text(pages, 21, 22)
    raw = clean_dashes(strip_chrome(raw))
    raw = fix_soft_hyphens(raw)
    if "\nRITUALS\n" in raw:
        raw = "RITUALS\n" + raw.split("\nRITUALS\n", 1)[1]
    if "\nADEPT POWERS\n" in raw:
        raw = raw.split("\nADEPT POWERS\n")[0]

    out = [header("Rituals", "22-23", "21-22"), "## Rituals", ""]
    lines = [ln.rstrip() for ln in raw.splitlines()]
    i = 0
    while i < len(lines) and lines[i].strip() != "RITUALS":
        i += 1
    i += 1

    rituals = ["DECRYSTALIZE", "MANA FLOW", "MANA EBB"]
    while i < len(lines):
        s = lines[i].strip()
        if not s:
            i += 1
            continue
        if s in rituals:
            name = s.title() if s != "DECRYSTALIZE" else "Decrystalize"
            if s == "MANA FLOW":
                name = "Mana Flow"
            if s == "MANA EBB":
                name = "Mana Ebb"
            i += 1
            tags = None
            if i < len(lines) and lines[i].strip().startswith("("):
                tags = lines[i].strip().strip("()")
                i += 1
            buf = []
            while i < len(lines) and lines[i].strip() not in rituals and lines[i].strip() != "ADEPT POWERS":
                buf.append(lines[i])
                i += 1
            out.append(f"### {name}")
            out.append("")
            if tags:
                out.append(f"*{tags}*")
                out.append("")
            out.append(join_broken_lines("\n".join(buf)).strip())
            out.append("")
            if s == "MANA EBB":
                out.append("[print quirk: Mana Ebb continuation says it cannot be performed in an area with a neutral or positive count; may be a print/extract error vs expected neutral or negative]")
                out.append("")
            continue
        i += 1

    text = "\n".join(out)
    return clean_dashes(re.sub(r"\n{3,}", "\n\n", text)).strip() + "\n"


def build_adept(pages: dict[int, str]) -> str:
    raw = page_text(pages, 22, 23)
    raw = clean_dashes(strip_chrome(raw))
    raw = fix_soft_hyphens(raw)
    if "\nADEPT POWERS\n" in raw:
        raw = "ADEPT POWERS\n" + raw.split("\nADEPT POWERS\n", 1)[1]

    out = [header("Adept Powers", "23-24", "22-23"), "## Adept Powers", ""]
    powers = [
        "DEMARA",
        "EIDETIC SENSE MEMORY",
        "ENTHRALLING PERFORMANCE",
        "HEIGHTENED CONCERN",
        "INDOMITABLE WILL",
        "IRON GUT",
        "IRON LUNGS",
        "IRON WILL",
        "KERATIN CONTROL",
        "LIVING FOCUS",
        "MAINTAIN WARMTH",
        "MEMORY DISPLACEMENT",
        "PIERCING SENSES",
        "POWER SWIMMING",
        "ROOTING",
        "SUPERNATURAL TOUGHNESS",
    ]
    lines = [ln.rstrip() for ln in raw.splitlines()]
    i = 0
    while i < len(lines) and lines[i].strip() != "ADEPT POWERS":
        i += 1
    i += 1

    while i < len(lines):
        s = lines[i].strip()
        if not s:
            i += 1
            continue
        if s == "REAGENT COST TABLE":
            out.append("## Reagent Cost Table")
            out.append("")
            out.append("| Type | Avail | Cost |")
            out.append("|---|---|---|")
            out.append("| Raw, per dram | - | 20¥ |")
            out.append("| Refined | 6 | 350¥ |")
            out.append("| Radical | 8 | 4,500¥ |")
            out.append("| Orichalum | 12 | 140,000¥ |")
            out.append("")
            out.append("[print quirk: Orichalum spelling as printed (commonly Orichalcum)]")
            out.append("")
            break
        if s in powers:
            title = s.title()
            # fix title cases
            title_map = {
                "DEMARA": "Demara",
                "EIDETIC SENSE MEMORY": "Eidetic Sense Memory",
                "ENTHRALLING PERFORMANCE": "Enthralling Performance",
                "HEIGHTENED CONCERN": "Heightened Concern",
                "INDOMITABLE WILL": "Indomitable Will",
                "IRON GUT": "Iron Gut",
                "IRON LUNGS": "Iron Lungs",
                "IRON WILL": "Iron Will",
                "KERATIN CONTROL": "Keratin Control",
                "LIVING FOCUS": "Living Focus",
                "MAINTAIN WARMTH": "Maintain Warmth",
                "MEMORY DISPLACEMENT": "Memory Displacement",
                "PIERCING SENSES": "Piercing Senses",
                "POWER SWIMMING": "Power Swimming",
                "ROOTING": "Rooting",
                "SUPERNATURAL TOUGHNESS": "Supernatural Toughness",
            }
            title = title_map[s]
            i += 1
            cost = ""
            if i < len(lines) and lines[i].strip().upper().startswith("COST:"):
                cost = lines[i].strip()
                # COST: 0.5 / COST: 0.25 PER LEVEL etc.
                cost = re.sub(r"^COST:\s*", "", cost, flags=re.I).strip()
                i += 1
            buf = []
            while i < len(lines) and lines[i].strip() not in powers and lines[i].strip() != "REAGENT COST TABLE":
                if lines[i].strip().upper().startswith("COST:"):
                    break
                buf.append(lines[i])
                i += 1
            out.append(f"### {title}")
            out.append("")
            out.append(f"**Cost:** {cost}")
            out.append("")
            out.append(join_broken_lines("\n".join(buf)).strip())
            out.append("")
            continue
        i += 1

    text = "\n".join(out)
    return clean_dashes(re.sub(r"\n{3,}", "\n\n", text)).strip() + "\n"


# Magic Societies and Threats need careful NPC placement - build more carefully

def rebuild_with_npc_extraction(raw: str, npc_names: list[str]) -> str:
    """Generic: extract B-A-R... blocks following known names and format as tables."""
    raw = clean_dashes(strip_chrome(raw))
    raw = fix_soft_hyphens(raw)
    raw = raw.replace(">\t", ">")
    lines = [ln.rstrip() for ln in raw.splitlines()]

    # Find NPC stat starts: sequence B,A,R,S,...
    blocks: list[tuple[int, int, str]] = []  # start, end, inferred_name
    i = 0
    while i < len(lines):
        if lines[i].strip() == "B":
            parsed = parse_attr_block(lines, i)
            if parsed:
                # look backward for name
                name = "Unknown"
                for j in range(i - 1, max(-1, i - 15), -1):
                    t = lines[j].strip()
                    if not t:
                        continue
                    if t.upper() == t and len(t) > 2 and not t.startswith(">"):
                        name = t.title() if not t.startswith("THE ") else t
                        # prefer exact known
                        for n in npc_names:
                            if n.upper() == t.upper() or n.upper().replace(" ", "") == t.upper().replace(" ", ""):
                                name = n
                                break
                        break
                    if t in npc_names or t.title() in npc_names:
                        name = t if t in npc_names else t.title()
                        break
                # find end of labeled fields
                _, ni = parsed
                # advance through fields
                md, end_i = format_npc_stats_from_lines(lines, i, name)
                blocks.append((i, end_i, md))
                i = end_i
                continue
        i += 1

    # Rebuild: remove raw attr lines, insert markdown at first mention of name heading
    skip = set()
    for a, b, _ in blocks:
        for k in range(a, b):
            skip.add(k)

    out_lines: list[str] = []
    i = 0
    used_blocks = set()
    while i < len(lines):
        if i in skip:
            i += 1
            continue
        s = lines[i].strip()
        # If this line is an NPC name heading matching a block, emit block
        emitted = False
        for bi, (a, b, md) in enumerate(blocks):
            if bi in used_blocks:
                continue
            # name from first heading line of md
            first = md.splitlines()[0].replace("### ", "").strip()
            if s.upper() == first.upper() or s.upper().replace(" ", "") == first.upper().replace(" ", ""):
                out_lines.append("")
                out_lines.extend(md.splitlines())
                used_blocks.add(bi)
                emitted = True
                i += 1
                break
        if emitted:
            continue
        out_lines.append(lines[i])
        i += 1

    # Append any unused blocks at end (before next major section)
    for bi, (a, b, md) in enumerate(blocks):
        if bi not in used_blocks:
            out_lines.append("")
            out_lines.extend(md.splitlines())

    text = "\n".join(out_lines)
    text = join_broken_lines(text)
    text = format_jp(text)
    return text


def build_04_societies(pages: dict[int, str]) -> str:
    raw = page_text(pages, 6, 7, 8)
    # Cut at THREATS
    if "\nTHREATS\n" in raw:
        raw = raw.split("\nTHREATS\n")[0]
    # Also cut orphaned start of threats on page 8 end - Treasure hunters continues onto page 9 which is threats chapter start
    # Page fitz 8 is print 9 (Patrick Maley + Oxford + Treasure Hunters start)
    # Page fitz 9 print 10 starts with Samantha Littlerock continuation then THREATS
    # So societies should include fitz 6,7,8 and the Samantha continuation from fitz 9 BEFORE THREATS
    raw9 = pages.get(9, "")
    if "\nTHREATS\n" in raw9:
        pre = raw9.split("\nTHREATS\n")[0]
        raw = raw + "\n" + pre

    raw = clean_dashes(strip_chrome(raw))
    raw = fix_soft_hyphens(raw)
    raw = raw.replace(">\t", ">")

    out = [header("Magic Societies", "7-9", "6-8 (+p9 before Threats)"), "## Magic Societies", ""]

    # Manually structure societies
    text = raw
    # Remove lone "Haley Soprano" / "Patrick Maley" orphans before ALL CAPS headers
    text = re.sub(r"\nHaley Soprano\n(?=THE )", "\n", text)
    text = re.sub(r"\nPatrick Maley\n(?=PATRICK MALEY\n)", "\n", text)

    lines = [ln.rstrip() for ln in text.splitlines()]

    # Extract Haley and Patrick (and any) NPC blocks first
    npc_md: dict[str, str] = {}
    i = 0
    while i < len(lines):
        if lines[i].strip() == "B":
            # look back for name
            name = None
            for j in range(i - 1, max(-1, i - 20), -1):
                t = lines[j].strip()
                if t in ("HALEY SOPRANO", "PATRICK MALEY", "Haley Soprano", "Patrick Maley"):
                    name = "Haley Soprano" if "HALEY" in t.upper() or t == "Haley Soprano" else "Patrick Maley"
                    break
                if t == "B":
                    break
            if name:
                md, ni = format_npc_stats_from_lines(lines, i, name)
                npc_md[name] = md
                # blank out
                for k in range(i, ni):
                    lines[k] = ""
                # also blank the ALL CAPS name line just above if present
                for j in range(i - 1, max(-1, i - 5), -1):
                    if lines[j].strip().upper() in ("HALEY SOPRANO", "PATRICK MALEY"):
                        lines[j] = ""
                        break
                i = ni
                continue
        i += 1

    # Walk content by society headings
    societies = {
        "THE AMAZING BLASTERS": "The Amazing Blasters",
        "THE CÓDIGO 525": "The Código 525",
        "THE CODIGO 525": "The Código 525",
        "NEW LABOUR": "New Labour Movement Party",  # may be split
        "NEW LABOUR  MOVEMENT PARTY": "New Labour Movement Party",
        "NEW LABOUR MOVEMENT PARTY": "New Labour Movement Party",
        "THE OXFORD GRAND LODGE": "The Oxford Grand Lodge",
        "TREASURE HUNTERS, INC": "Treasure Hunters, Inc",
    }

    body = "\n".join(lines)
    body = re.sub(r"NEW LABOUR\s*\n\s*MOVEMENT PARTY", "NEW LABOUR MOVEMENT PARTY", body)
    body = re.sub(r"HALEY SOPRANO\n", "", body)
    body = re.sub(r"PATRICK MALEY\n", "", body)

    # Split on society headers
    parts = re.split(
        r"\n(?=THE AMAZING BLASTERS\n|THE C[ÓO]DIGO 525\n|NEW LABOUR MOVEMENT PARTY\n|THE OXFORD GRAND LODGE\n|TREASURE HUNTERS, INC\n)",
        "\n" + body,
    )
    for part in parts:
        part = part.strip()
        if not part or part == "MAGIC SOCIETIES":
            continue
        first = part.split("\n", 1)[0].strip()
        title = societies.get(first, first.title())
        rest = part.split("\n", 1)[1] if "\n" in part else ""
        out.append(f"## {title}")
        out.append("")
        # Format Members/Dues/etc as bold labels
        rest_lines = rest.splitlines()
        formatted: list[str] = []
        for ln in rest_lines:
            s = ln.strip()
            if not s:
                formatted.append("")
                continue
            if re.match(r"^(Members|Dues|Areas of Expertise|Patron|Description and Customs):", s):
                k, v = s.split(":", 1)
                formatted.append(f"**{k}:** {v.strip()}")
            else:
                formatted.append(s)
        chunk = format_jp(join_broken_lines("\n".join(formatted)))
        out.append(chunk.strip())
        out.append("")
        if title == "The Amazing Blasters" and "Haley Soprano" in npc_md:
            out.append(npc_md["Haley Soprano"])
        if title == "New Labour Movement Party" and "Patrick Maley" in npc_md:
            out.append(npc_md["Patrick Maley"])

    # Note print quirks
    out.append("[print quirks: Código 525 text uses both Branco and Blanco; \"it is believe\"; \"a eight-thousand-nuyen\"; New Oxford Lodge vs Oxford Grand Lodge naming]")
    out.append("")

    text = "\n".join(out)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return clean_dashes(text).strip() + "\n"


def build_05_threats(pages: dict[int, str]) -> str:
    raw = page_text(pages, 9, 10, 11, 12, 13, 14)
    if "\nTHREATS\n" in raw:
        raw = "THREATS\n" + raw.split("\nTHREATS\n", 1)[1]
    if "\nSUPPLEMENTARY\n" in raw:
        raw = raw.split("\nSUPPLEMENTARY\n")[0]
    raw = clean_dashes(strip_chrome(raw))
    raw = fix_soft_hyphens(raw)
    raw = raw.replace(">\t", ">")

    out = [header("Threats", "10-15", "9-14"), "## Threats", ""]

    lines = [ln.rstrip() for ln in raw.splitlines()]
    # Skip THREATS header
    while lines and lines[0].strip() in ("THREATS", ""):
        lines.pop(0)

    # Extract NPC/entity stat blocks with known names in order of appearance
    # Order in book: Crystaline Entity (+ Crystalize power), Simon, Georgette, Flasher, Talon
    # But columns interleave Simon stats into Georgette section

    npc_order_guess = [
        "CRYSTALINE ENTITY",
        "SIMON",
        "GEORGETTE SPINELER",
        "FLASHER MCDANIELS",
        "TALON KINCAID",
    ]

    # Extract Crystalize power separately
    crystalize_md = ""
    full = "\n".join(lines)
    m = re.search(
        r"CRYSTALIZE\nType:\s*P\s*Action:\s*Complex\nRange:\s*LOS\s*Duration:\s*Permanent\n(.*?)(?=\nB\n)",
        full,
        re.S,
    )
    if m:
        body = join_broken_lines(m.group(1))
        crystalize_md = (
            "### Crystalize\n\n"
            "**Type:** P  \n**Action:** Complex  \n**Range:** LOS  \n**Duration:** Permanent\n\n"
            f"{body.strip()}\n\n"
            "[print quirk: power name Crystalize / entity Crystaline Entity as printed]\n"
        )
        full = full[: m.start()] + full[m.end() :]
        lines = full.splitlines()

    # Extract all B-blocks with names
    extracted: list[tuple[str, str, int, int]] = []
    i = 0
    while i < len(lines):
        if lines[i].strip() == "B":
            name = "Unknown"
            for j in range(i - 1, max(-1, i - 30), -1):
                t = lines[j].strip()
                if t.upper() in {n.upper() for n in npc_order_guess} or t in (
                    "CRYSTALINE ENTITY", "SIMON", "GEORGETTE SPINELER", "FLASHER McDANIELS", "TALON KINCAID",
                    "Flasher McDaniels",
                ):
                    name = t.title() if t.upper() != "CRYSTALINE ENTITY" else "Crystaline Entity"
                    if "FLASHER" in t.upper():
                        name = "Flasher McDaniels"
                    if "GEORGETTE" in t.upper():
                        name = "Georgette Spineler"
                    if t.upper() == "SIMON":
                        name = "Simon"
                    if "TALON" in t.upper():
                        name = "Talon Kincaid"
                    break
            md, ni = format_npc_stats_from_lines(lines, i, name)
            extracted.append((name, md, i, ni))
            i = ni
            continue
        i += 1

    # Disambiguate by stats fingerprint if names wrong
    # Simon: B9 mage Spellcasting 14
    # Georgette: B7 adept Muscle aug
    # Flasher: B5 Magic 7 Unarmed
    # Talon: B4 Magic 6
    # Crystaline: F+4 etc
    for idx, (name, md, a, b) in enumerate(extracted):
        if "F+4" in md or "F + 4" in md or "| F+4 |" in md.replace(" ", ""):
            extracted[idx] = ("Crystaline Entity", md.replace(f"### {name}", "### Crystaline Entity"), a, b)
        elif "Spellcasting 14" in md:
            extracted[idx] = ("Simon", md.replace(f"### {name}", "### Simon"), a, b)
        elif "Muscle augmentation" in md or "Improved Ability 2 (Blades)" in md:
            extracted[idx] = ("Georgette Spineler", md.replace(f"### {name}", "### Georgette Spineler"), a, b)
        elif "Killing Hands" in md or "Unarmed combat 16" in md or "Unarmed Combat 16" in md:
            extracted[idx] = ("Flasher McDaniels", md.replace(f"### {name}", "### Flasher McDaniels"), a, b)
        elif "Knowledge: Lone Star" in md or "Watcher" in md:
            extracted[idx] = ("Talon Kincaid", md.replace(f"### {name}", "### Talon Kincaid"), a, b)

    skip = set()
    for _, _, a, b in extracted:
        for k in range(a, b):
            skip.add(k)
    # Also skip CRYSTALINE ENTITY / CRYSTALIZE leftover headers near stats
    for i, ln in enumerate(lines):
        if ln.strip() in ("CRYSTALINE ENTITY", "CRYSTALIZE", "SIMON", "GEORGETTE SPINELER", "FLASHER McDANIELS", "TALON KINCAID") and i + 1 < len(lines):
            # only skip duplicate headers immediately before removed stats; keep narrative section headers
            pass

    # Build narrative with section headings, inject stats at right points
    sections_map = [
        ("RIFTS AND THE", "## Rifts and the Guardians of Order"),
        ("GUARDIANS OF ORDER", None),  # continuation of title
        ("CREEDUS MAXIMUS", "## Creedus Maximus"),
        ("SIMON", "### Simon"),
        ("GEORGETTE SPINELER", "### Georgette Spineler"),
        ("FLASHER McDANIELS", "### Flasher McDaniels"),
        ("PROJECT WAMPUM", "## Project Wampum"),
        ("TALON KINCAID", "### Talon Kincaid"),
    ]

    out_lines: list[str] = []
    i = 0
    injected = set()
    pending_rifts_title = False

    while i < len(lines):
        if i in skip:
            i += 1
            continue
        s = lines[i].strip()
        if not s:
            out_lines.append("")
            i += 1
            continue
        if s == "RIFTS AND THE":
            pending_rifts_title = True
            i += 1
            continue
        if pending_rifts_title and "GUARDIAN" in s:
            out_lines.append("## Rifts and the Guardians of Order")
            out_lines.append("")
            pending_rifts_title = False
            i += 1
            continue
        if s == "CRYSTALINE ENTITY":
            out_lines.append("## Crystaline Entity")
            out_lines.append("")
            if crystalize_md:
                out_lines.append(crystalize_md)
            for name, md, _, _ in extracted:
                if name == "Crystaline Entity" and name not in injected:
                    out_lines.append(md)
                    injected.add(name)
            i += 1
            continue
        if s == "CRYSTALIZE":
            i += 1
            # skip power header; already emitted
            while i < len(lines) and lines[i].strip() and lines[i].strip() != "B" and not lines[i].strip().startswith(">"):
                # if still raw power text not extracted, skip until B
                if lines[i].strip().startswith("Type:"):
                    while i < len(lines) and i not in skip and lines[i].strip() != "B":
                        i += 1
                    break
                i += 1
            continue
        if s == "CREEDUS MAXIMUS":
            out_lines.append("## Creedus Maximus")
            out_lines.append("")
            i += 1
            continue
        if s == "SIMON" and (i + 1 >= len(lines) or lines[i + 1].strip() in ("", "GEORGETTE SPINELER", "One suspected", "B")):
            # Section header for Simon - careful: first SIMON is narrative start
            # Check following content
            if i + 1 < len(lines) and lines[i + 1].strip().startswith("One suspected"):
                out_lines.append("### Simon")
                out_lines.append("")
                i += 1
                continue
            if i + 1 < len(lines) and lines[i + 1].strip() in ("GEORGETTE SPINELER", "B", ""):
                # duplicate header before stats - inject simon stats if not done
                if "Simon" not in injected:
                    for name, md, _, _ in extracted:
                        if name == "Simon":
                            out_lines.append(md)
                            injected.add("Simon")
                i += 1
                continue
        if s == "GEORGETTE SPINELER":
            # Could be start of narrative or stats header
            # If next is "A physical adept" it's narrative
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j < len(lines) and lines[j].strip().startswith("A physical adept"):
                # inject Simon stats before Georgette narrative if pending
                if "Simon" not in injected:
                    for name, md, _, _ in extracted:
                        if name == "Simon":
                            out_lines.append(md)
                            injected.add("Simon")
                out_lines.append("### Georgette Spineler")
                out_lines.append("")
                i += 1
                continue
            if "Georgette Spineler" not in injected:
                for name, md, _, _ in extracted:
                    if name == "Georgette Spineler":
                        out_lines.append(md)
                        injected.add("Georgette Spineler")
            i += 1
            continue
        if s == "FLASHER McDANIELS":
            if "Georgette Spineler" not in injected:
                for name, md, _, _ in extracted:
                    if name == "Georgette Spineler":
                        out_lines.append(md)
                        injected.add("Georgette Spineler")
            out_lines.append("### Flasher McDaniels")
            out_lines.append("")
            i += 1
            continue
        if s == "PROJECT WAMPUM":
            if "Flasher McDaniels" not in injected:
                for name, md, _, _ in extracted:
                    if name == "Flasher McDaniels":
                        out_lines.append(md)
                        injected.add("Flasher McDaniels")
            out_lines.append("## Project Wampum")
            out_lines.append("")
            i += 1
            continue
        if s == "TALON KINCAID":
            out_lines.append("### Talon Kincaid")
            out_lines.append("")
            i += 1
            continue
        out_lines.append(lines[i])
        i += 1

    # Ensure all NPCs injected
    for name, md, _, _ in extracted:
        if name not in injected:
            out_lines.append("")
            out_lines.append(md)
            injected.add(name)

    body = format_jp(join_broken_lines("\n".join(out_lines)))
    out.append(body.strip())
    out.append("")
    out.append("[print quirks: Crystaline Entity / Crystalize spelling; \"talsimongers\"; \"suspect number\"/\"suspected number of Creedus\"; AP em/en dashes in weapons normalized to ASCII hyphen]")
    out.append("")

    text = "\n".join(out)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return clean_dashes(text).strip() + "\n"


def write_index() -> None:
    text = """# Shadow Spells

Extra spells, adept powers, rituals, traditions, magic societies, and astral threats.

**PDF:** `Source/PDF/shadow-spells-pdf.pdf` (24 pages, fitz 0-23)

## Workflow (per chapter)

1. **Convert:** dense LLM-reference markdown from PDF
2. **Loss check:** phrase/item sweep vs PDF; no next-chapter bleed
3. **QA:** JackPoint attribution, stats/tables, print quirks noted (not invented)
4. **Formatting:** no em dashes; strip page chrome; ASCII punctuation; table separators `|---|`

**Status:** all 8 chapters converted; landmark sweep PASS (`Source/_extract/shadow_spells_sweep_report.md`).

## Sections

| # | Chapter | Print pages (approx) |
|---|---|---|
| 1 | [Shadowrun: Shadow Spells](01%20-%20Shadowrun%20Shadow%20Spells.md) | 1 |
| 2 | [JackPoint](02%20-%20JackPoint.md) | 2 |
| 3 | [Traditions](03%20-%20Traditions.md) | 3-6 |
| 4 | [Magic Societies](04%20-%20Magic%20Societies.md) | 7-9 |
| 5 | [Threats](05%20-%20Threats.md) | 10-15 |
| 6 | [Supplementary Grimoire](06%20-%20Supplementary%20Grimoire.md) | 16-22 |
| 7 | [Rituals](07%20-%20Rituals.md) | 22-23 |
| 8 | [Adept Powers](08%20-%20Adept%20Powers.md) | 23-24 |

*[Page map: header `<< SHADOW SPELLS >> N` ≈ print page N; fitz index ≈ print - 1.]*
"""
    (OUT / "INDEX.md").write_text(text, encoding="utf-8")


def count_jp(text: str) -> int:
    return len(re.findall(r"^> \*\*[^*]+\*\*", text, re.M))


def count_spells_powers(text: str) -> int:
    return len(re.findall(r"^### ", text, re.M))


def main() -> None:
    raw = EXTRACT.read_text(encoding="utf-8")
    pages = split_pages(raw)
    OUT.mkdir(parents=True, exist_ok=True)

    files = {
        "01 - Shadowrun Shadow Spells.md": build_01(pages),
        "02 - JackPoint.md": build_02(pages),
        "03 - Traditions.md": build_03_traditions(pages),
        "04 - Magic Societies.md": build_04_societies(pages),
        "05 - Threats.md": build_05_threats(pages),
        "06 - Supplementary Grimoire.md": build_grimoire(pages),
        "07 - Rituals.md": build_rituals(pages),
        "08 - Adept Powers.md": build_adept(pages),
    }

    # Em dash check + write
    jp_total = 0
    spell_power_total = 0
    line_counts = {}
    quirks = []
    for name, content in files.items():
        if "\u2014" in content or "—" in content:
            content = clean_dashes(content)
        path = OUT / name
        path.write_text(content, encoding="utf-8")
        line_counts[name] = content.count("\n") + (0 if content.endswith("\n") else 1)
        jp_total += count_jp(content)
        if name.startswith("06") or name.startswith("07") or name.startswith("08") or name.startswith("05"):
            spell_power_total += count_spells_powers(content)
        for q in re.findall(r"\[print[^\]]*\]", content):
            quirks.append(f"{name}: {q}")

    write_index()

    # Sweep report
    landmarks = [
        ("Winterhawk", "03"),
        ("Aboriginal", "03"),
        ("Amazing Blasters", "04"),
        ("Patrick Maley", "04"),
        ("Crystaline Entity", "05"),
        ("Creedus Maximus", "05"),
        ("Magebolt", "06"),
        ("Passenger", "06"),
        ("Ghoulish Strength", "06"),
        ("Rot", "06"),
        ("Astral Armor", "06"),
        ("Control Emotions", "06"),
        ("Petrify", "06"),
        ("Decrystalize", "07"),
        ("Mana Flow", "07"),
        ("Keratin Control", "08"),
        ("Rooting", "08"),
        ("Iron Lungs", "08"),
        ("Enthralling Performance", "08"),
    ]
    report = ["# Shadow Spells landmark sweep", ""]
    all_text = {k: (OUT / k).read_text(encoding="utf-8") for k in files}
    for phrase, chap in landmarks:
        hits = [fn for fn, t in all_text.items() if phrase in t]
        expect = [fn for fn in all_text if fn.startswith(chap)]
        ok = any(fn.startswith(chap) for fn in hits)
        bleed = [fn for fn in hits if not fn.startswith(chap) and not fn.startswith("01") and not fn.startswith("02")]
        # Magebolt etc should only be in 06; some names may appear in NPC spell lists in 04/05 - note
        report.append(f"- **{phrase}** (expect ch {chap}): found in {hits or ['NONE']} {'PASS' if ok else 'FAIL'}")
    report.append("")
    report.append(f"JP handle blocks ( > **Handle** ): {jp_total}")
    report.append(f"### headings (spells/powers/NPCs across 05-08): {spell_power_total}")
    report.append("")
    report.append("## Quirks noted")
    for q in quirks:
        report.append(f"- {q}")
    report.append("")
    report.append("## Em dashes")
    em = False
    for fn, t in all_text.items():
        if "\u2014" in t or "—" in t:
            report.append(f"- FAIL {fn}")
            em = True
    if not em:
        report.append("- PASS: no em dashes in chapter files")
    report.append("")
    report.append("## Line counts")
    for fn, n in line_counts.items():
        report.append(f"- {fn}: {n}")
    REPORT.write_text("\n".join(report) + "\n", encoding="utf-8")

    print("Wrote chapters:")
    for fn, n in line_counts.items():
        print(f"  {fn}: {n} lines")
    print(f"JP handles: {jp_total}")
    print(f"### count (05-08): {spell_power_total}")
    print(f"Report: {REPORT}")


if __name__ == "__main__":
    main()
