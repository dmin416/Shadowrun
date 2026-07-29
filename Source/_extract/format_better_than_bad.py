# -*- coding: utf-8 -*-
"""Formatting pass: reflow Better Than Bad Source Texts into readable markdown.

Run AFTER extract_better_than_bad.py (expects raw PDF line breaks).
Does not format INDEX.md.
"""
from __future__ import annotations

import re
from pathlib import Path

OUT = Path(r"c:\Users\admin\Desktop\Shadowrun\Source Texts\Better Than Bad")

# Full section banners (after multi-line joins)
KNOWN_HEADERS = {
    "JACKPOINT",
    "INTRODUCTION",
    "BETTER THAN BAD CREDITS",
    "FRIENDS WILL BE FRIENDS",
    "LIGHTS IN THE DARKNESS",
    "ROBBING HOODS",
    "A GREAT CLOUD OF HOODERS PAST",
    "A COMMUNION OF REBELS, REVOLUTIONARIES, AND RUINED",
    "WHAT'S HOODING NOW?",
    "NEO-ANARCHISTS AND ANTI-CORPS",
    "MINORITY RIGHTS GROUPS",
    "ENVIRONMENTALISTS",
    "NATIONAL/LOCAL REVOLUTIONARIES",
    "DO-GOODERS/VIGILANTES/ANTIFAS",
    "SHADOWRUNNERS AND HOODERS: A MATCH MADE JUST FOR US",
    "FIXER-UPPER OPPORTUNITIES",
    "FIXER UPPER OPPORTUNITIES",
    "IT'S ALL ABOUT POWER",
    "BLACK STAR",
    "ON THE FRINGES",
    "INFECTED VIGILANTES",
    "ASAMANDO",
    "CHICAGO",
    "TURNING A PROFIT WITHOUT CHARGING MONEY",
    "THE INMATES ARE RUNNING THE ASYLUM",
    "A GLOBAL CONSPIRACY - FOR GOOD! (MOSTLY)",
    "A GLOBAL CONSPIRACY FOR GOOD! (MOSTLY)",
    "DRACO FOUNDATION: BIG D'S FOUNDATION FOR CHANGE",
    "DRACO FOUNDATION GLOBAL INITIATIVES",
    "ARLEESH: OUR NEW GUARDIAN DRAGON-MOTHER?",
    "SHADOWCASTERS: ACTS OF INFORMATION FREEDOM",
    "NEW UNDERGROUND RAILROAD: THE MORE THINGS CHANGE",
    "WARREN'S WAVERIDERS: SAILING THE FRIENDLY SEAS",
    "FIRST, YOU NEED A JOB",
    "MEET MS. SMITH",
    "CRY FOR HELP",
    "FIDES, SPES, ET CARITAS",
    "HOODING RUNS FOR THE DISCERNING GAMEMASTER",
    "PRETORIA, HURRAH",
    "PRETORIA-WITWATERSRAND-VAAL METROPLEX",
    "CULTURAL OVERVIEW, OR PERHAPS CLASH",
    "HISTORY",
    "PRESENT",
    "THE HAVES: TSHWANE AND KUNGWINI",
    "THE HAVE-NOTS",
    "THE MIXING POTS",
    "BENEATH THE SURFACE",
    "THE WILD SIDE",
    "ARCANE AFRICA",
    "CORPORATE BRIEFING",
    "POLITICAL BRIEFING",
    "SECURITY BRIEFING",
    "UNDERWORLD BRIEFING",
    "ALL THE COLORS OF A DEADLY RAINBOW",
    "GAME INFORMATION",
    "BUYING A FAKE",
    "MINING FOR GOLD",
    "JACARANDA CITIZENS",
    "JACARANDA CITIZENS: PEOPLE OF PRETORIA",
    "AIKSHE",
    "HASHTU OJIMBWE",
    "SARU OWEMAWAI",
    "KURT KOENIG",
    "WOLFGANG SCHMIDT/THE FOX",
    "LINCOLN THOMAS ASTERMOORE IV",
    "LEEKA MONTCLAIR",
    "GARIK \"HEAVY\" BRECKWORTH",
    "GARIK HEAVY BRECKWORTH",
    "HESHAM \"ACHE\" KURGTOREK",
    "HESHAM ACHE KURGTOREK",
    "THE RUBY SLIPPER NETWORK",
    "OZ",
    "COUGAR",
    "FULL THROTTLE",
    "REAPER",
    "BIANCA",
    "LIFER",
    "RULES",
    "SOCIAL CHAMELEON (POSITIVE QUALITY)",
    "QUADRIPLEGIC (NEGATIVE QUALITY)",
    "GUANYIN (MENTOR SPIRIT)",
    "BEING LESS BAD: THE FINE ART OF HOODING",
    "THE FINE ART OF HOODING",
    "DOING GOOD",
    "EXPOSING YOURSELF",
    "COPS ARE PEOPLE, TOO",
    "GOOD DEEDS",
    "NEIGHBORHOOD, WATCH",
    "BEING A BETTER PERSON",
    "LIVING THE HOOD LIFE",
    "A GOOD START",
    "GOOD PEOPLE",
    "WHAT HOODING ISN'T, OR \"WHY OLD CROW IS WRONG\"",
    "CONCLUSION",
    "BUILDING A HOODER",
    "NEW GEAR",
    "NEW ARMOR MODIFICATIONS",
    "GREY MANA TATTOOS",
    "NEW TOXIN",
    "BLIGHT",
    "NEW CYBERWARE GRADE",
    "GREYWARE",
    "NEW SPELLS AND ADEPT POWERS",
    "NEW MANIPULATION SPELLS",
    "NEW ADEPT POWERS",
    "MYSTIC APTITUDE",
    "STATE OF PURITY",
    "NEW QUALITIES",
    "NEW POSITIVE QUALITIES",
    "NEW MASTERY QUALITIES",
    "NEW NEGATIVE QUALITIES",
    "NEW LIFE MODULES",
    "NATIONALITIES",
    "FORMATIVE YEARS",
    "FURTHER EDUCATION",
    "REAL LIFE",
    "NEW USES FOR KARMA AND STRET CRED",
    "HOODER RUNS",
    "THE PAY OFFERED IS...",
    "IF YOU CAN'T GET WHAT YOU WANT, TRY FOR WHAT YOU NEED",
}

SKIP_EXACT = {
    "BETTER THAN BAD",
    "CONTENTS",
    "& CREDITS",
    "CONTENTS & CREDITS",
    "BY PATRICK GOODMAN",
    "BY JASON M. HARDY",
}

JOIN_TITLES = [
    (r"(?im)^FRIENDS WILL\s*\nBE FRIENDS\s*$", "FRIENDS WILL BE FRIENDS"),
    (r"(?im)^MINING\s*\nFOR GOLD\s*$", "MINING FOR GOLD"),
    (r"(?im)^THE FINE\s*\nART OF HOODING\s*$", "THE FINE ART OF HOODING"),
    (r"(?im)^BEING LESS BAD:\s*\nTHE FINE ART OF HOODING\s*$", "BEING LESS BAD: THE FINE ART OF HOODING"),
    (r"(?im)^A GREAT CLOUD\s*\nOF HOODERS PAST\s*$", "A GREAT CLOUD OF HOODERS PAST"),
    (r"(?im)^A COMMUNION OF\s*\nREBELS, REVOLUTIONARIES,\s*\nAND RUINED\s*$",
     "A COMMUNION OF REBELS, REVOLUTIONARIES, AND RUINED"),
    (r"(?im)^WHAT'?S\s*\nHOODING NOW\?\s*$", "WHAT'S HOODING NOW?"),
    (r"(?im)^NEO-ANARCHISTS\s*\nAND ANTI-CORPS\s*$", "NEO-ANARCHISTS AND ANTI-CORPS"),
    (r"(?im)^NATIONAL/LOCAL\s*\nREVOLUTIONARIES\s*$", "NATIONAL/LOCAL REVOLUTIONARIES"),
    (r"(?im)^SHADOWRUNNERS AND HOODERS:\s*\nA MATCH MADE JUST FOR US\s*$",
     "SHADOWRUNNERS AND HOODERS: A MATCH MADE JUST FOR US"),
    (r"(?im)^IT'?S ALL\s*\nABOUT POWER\s*$", "IT'S ALL ABOUT POWER"),
    (r"(?im)^TURNING A PROFIT WITHOUT\s*\nCHARGING MONEY\s*$", "TURNING A PROFIT WITHOUT CHARGING MONEY"),
    (r"(?im)^THE INMATES ARE\s*\nRUNNING THE ASYLUM\s*$", "THE INMATES ARE RUNNING THE ASYLUM"),
    (r"(?im)^A GLOBAL CONSPIRACY.?\s*\nFOR GOOD! \(MOSTLY\)\s*$",
     "A GLOBAL CONSPIRACY - FOR GOOD! (MOSTLY)"),
    (r"(?im)^NEW ARMOR\s*\nMODIFICATIONS\s*$", "NEW ARMOR MODIFICATIONS"),
    (r"(?im)^NEW SPELLS AND\s*\nADEPT POWERS\s*$", "NEW SPELLS AND ADEPT POWERS"),
    (r"(?im)^NEW USES FOR KARMA\s*\nAND STRET CRED\s*$", "NEW USES FOR KARMA AND STRET CRED"),
    (r"(?im)^THE HAVES: TSHWANE\s*\nAND KUNGWINI\s*$", "THE HAVES: TSHWANE AND KUNGWINI"),
    (r"(?im)^ALL THE COLORS OF A\s*\nDEADLY RAINBOW\s*$", "ALL THE COLORS OF A DEADLY RAINBOW"),
    (r"(?im)^JACARANDA CITIZENS:\s*\nPEOPLE OF PRETORIA\s*$", "JACARANDA CITIZENS: PEOPLE OF PRETORIA"),
    (r"(?im)^PRETORIA-WITWA-?\s*\nTERSRAND-VAAL\s*\nMETROPLEX\s*$",
     "PRETORIA-WITWATERSRAND-VAAL METROPLEX"),
    (r"(?im)^IF YOU CAN'T GET\s*\nWHAT YOU WANT,\s*\nTRY FOR WHAT YOU NEED\s*$",
     "IF YOU CAN'T GET WHAT YOU WANT, TRY FOR WHAT YOU NEED"),
    (r"(?im)^BETTER THAN BAD\s*\nHOODER\s*\nRUNS\s*$", "HOODER RUNS"),
]


def title_case_header(s: str) -> str:
    small = {"a", "an", "the", "and", "or", "of", "in", "on", "for", "to", "vs", "at", "et"}
    keep = {"PWV", "AAA", "AA", "AI", "IV", "Ms", "MS"}
    # Preserve punctuation attached to words
    words = re.findall(r"\S+", s)
    out: list[str] = []
    for i, w in enumerate(words):
        # Keep pure punctuation tokens
        if not any(c.isalpha() for c in w):
            out.append(w)
            continue
        m = re.match(r"^([(\"']*)(.*?)([,.!?:;\"')]*)$", w)
        if not m:
            out.append(w)
            continue
        pre, bare, post = m.group(1), m.group(2), m.group(3)
        if bare.upper() in keep:
            core = bare.upper() if bare.upper() in {"PWV", "AAA", "AA", "AI", "IV"} else bare
        else:
            lw = bare.lower()
            if i > 0 and lw in small:
                core = lw
            else:
                core = bare[:1].upper() + bare[1:].lower() if bare else bare
        out.append(pre + core + post)
    return " ".join(out)


def fix_soft_hyphens(text: str) -> str:
    def join_hyphen(m: re.Match) -> str:
        a, b = m.group(1), m.group(2)
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
        if a.islower() and b.islower() and len(a) <= 12 and len(b) <= 12:
            return a + b
        if a[0].isupper() and a[1:].islower() and b.islower() and len(a) <= 10 and len(b) <= 12:
            return a + b
        return m.group(0)

    text = re.sub(r"([A-Za-z0-9]+)\s+-\s+([A-Za-z0-9]+)", spaced_hyphen, text)
    return text


def is_stat_or_table_line(s: str) -> bool:
    if re.search(r"\bB\s+A\s+R\s+S\b", s):
        return True
    if s.count("|") >= 2:
        return True
    if re.match(
        r"^(Condition Monitor|Armor|Initiative|Limits|Skills|Qualities|Gear|Weapons|"
        r"Vehicles|Boxes|Augmentations|Metatype|Sex|Age|Active|Knowledge|Languages|"
        r"Powers|Spells|Connection|Loyalty|Availability|Cost|Essence|Capacity|"
        r"Physical Initiative|Matrix Initiative|Astral Initiative)\s*:",
        s,
        re.I,
    ):
        return True
    if re.match(r"^(Connection|Loyalty)\s+\d", s, re.I):
        return True
    if re.match(r"^(2D6|1D6)\s+RESULT\s*$", s, re.I):
        return True
    return False


def looks_like_stat_continuation(s: str) -> bool:
    if is_stat_or_table_line(s):
        return True
    if re.match(r"^[\d(]", s):
        return True
    if re.search(r"\b(DV|AP|Acc|RC|SA|BF|FA|Reach|Rating|Essence|¥|Karma)\b", s):
        return True
    return False


def is_all_caps_title(s: str) -> bool:
    if not s or len(s) > 70:
        return False
    letters = [c for c in s if c.isalpha()]
    if len(letters) < 3:
        return False
    if s.endswith(".") and len(s) > 40:
        return False
    return all(c.isupper() for c in letters)


def strip_noise(s: str) -> str | None:
    if not s:
        return None
    if s in {"SHADOWRUN", ">", ">>", "<", "<<"}:
        return None
    if re.match(r"^>>?\s*BETTER THAN BAD", s, re.I):
        return None
    if "InMediaRes Productions" in s:
        return None
    if re.match(r"^<<?\s*", s) and ("<<" in s or s.startswith("<<")):
        return None
    if re.match(r"^\d+\s+>>?", s):
        return None
    if re.match(r"^>>?\s*.*<<\s*\d*\s*$", s):
        return None
    if s in SKIP_EXACT:
        return None
    if re.match(r"^\d{1,3}$", s):
        return None
    return s


def peek_nonempty(lines: list[str], start: int) -> tuple[int, str] | None:
    j = start
    while j < len(lines):
        raw = lines[j].strip()
        if not raw:
            j += 1
            continue
        s = strip_noise(raw)
        if s is None:
            j += 1
            continue
        return j, s
    return None


def break_giant_paras(text: str, limit: int = 900) -> str:
    out: list[str] = []
    for block in text.split("\n\n"):
        if block.startswith(("## ", "```", ">")):
            out.append(block)
            continue
        if len(block) <= limit:
            out.append(block)
            continue
        parts: list[str] = []
        cur = ""
        for sent in re.split(r"(?<=[.!?])\s+", block):
            if not cur:
                cur = sent
            elif len(cur) + 1 + len(sent) <= limit:
                cur = cur + " " + sent
            else:
                parts.append(cur)
                cur = sent
        if cur:
            parts.append(cur)
        out.extend(parts)
    return "\n\n".join(out)


def reflow_body(body: str) -> str:
    body = re.sub(r"(\w)-\n(\w)", r"\1\2", body)
    for pat, repl in JOIN_TITLES:
        body = re.sub(pat, repl, body)

    lines = [ln.rstrip() for ln in body.splitlines()]
    paras: list[str] = []
    buf: list[str] = []
    bullet_buf: list[str] | None = None

    def flush_buf():
        nonlocal buf
        if not buf:
            return
        text = " ".join(x.strip() for x in buf)
        text = re.sub(r"\s+", " ", text).strip()
        text = fix_soft_hyphens(text)
        if text:
            paras.append(text)
        buf = []

    def flush_bullet():
        nonlocal bullet_buf
        if not bullet_buf:
            return
        text = " ".join(x.strip() for x in bullet_buf)
        text = re.sub(r"\s+", " ", text).strip()
        text = fix_soft_hyphens(text)
        if not text.startswith("- "):
            text = "- " + text
        paras.append(text)
        bullet_buf = None

    def flush_all():
        flush_bullet()
        flush_buf()

    i = 0
    while i < len(lines):
        raw = lines[i]
        stripped = raw.strip()
        if not stripped:
            if bullet_buf is not None:
                flush_bullet()
            i += 1
            continue

        s = strip_noise(stripped)
        if s is None:
            i += 1
            continue

        if s == ">" or s.startswith(">"):
            flush_all()
            comment = s.lstrip(">").strip()
            j = i + 1
            while j < len(lines):
                nxt_raw = lines[j].strip()
                if not nxt_raw:
                    if comment:
                        break
                    j += 1
                    continue
                nxt = strip_noise(nxt_raw)
                if nxt is None:
                    j += 1
                    continue
                if nxt == ">" or nxt.startswith(">"):
                    break
                if nxt.upper().startswith("POSTED BY:") or nxt in KNOWN_HEADERS:
                    break
                if is_all_caps_title(nxt) and nxt.rstrip(":") in KNOWN_HEADERS:
                    break
                if not comment:
                    comment = nxt
                else:
                    comment = comment + " " + nxt
                j += 1
                peek = peek_nonempty(lines, j)
                if peek and (
                    peek[1] == ">"
                    or peek[1].startswith(">")
                    or peek[1].upper().startswith("POSTED BY:")
                    or peek[1] in KNOWN_HEADERS
                ):
                    break
                if peek and len(peek[1].split()) <= 3 and not peek[1].endswith((".", "!", "?")):
                    if not peek[1][0].islower() and len(peek[1]) < 40:
                        comment = comment + "\n> " + peek[1]
                        j = peek[0] + 1
                    break
                break
            comment = fix_soft_hyphens(re.sub(r"\s+", " ", comment.replace("\n> ", " | ")).strip())
            if comment:
                if " | " in comment:
                    body_c, handle = comment.rsplit(" | ", 1)
                    paras.append("> " + body_c.strip())
                    paras.append("> **" + handle.strip() + "**")
                else:
                    paras.append("> " + comment)
            i = j
            continue

        if s.upper().startswith("POSTED BY:"):
            flush_all()
            paras.append("## " + s)
            i += 1
            continue

        key = s.rstrip(":")
        if key in KNOWN_HEADERS or (is_all_caps_title(s) and key in KNOWN_HEADERS):
            if key in SKIP_EXACT:
                i += 1
                continue
            flush_all()
            paras.append(f"## {title_case_header(key)}")
            i += 1
            continue

        # Promote short ALL CAPS banners that look like section titles
        if is_all_caps_title(s) and 3 <= len(s.split()) <= 8 and len(s) <= 55:
            if not re.search(r"[.!?]$", s) and key not in SKIP_EXACT:
                peek = peek_nonempty(lines, i + 1)
                # Avoid promoting mid-sentence ALL CAPS quotes fragments
                if not s.startswith('"') and not s.startswith("("):
                    if peek and (
                        peek[1][0].islower()
                        or peek[1].startswith(">")
                        or peek[1].upper().startswith("POSTED BY:")
                        or is_stat_or_table_line(peek[1])
                    ):
                        flush_all()
                        paras.append(f"## {title_case_header(key)}")
                        i += 1
                        continue

        if is_stat_or_table_line(s) and re.search(r"\bB\s+A\s+R\s+S\b", s):
            flush_all()
            block = [s]
            j = i + 1
            while j < len(lines):
                nxt_raw = lines[j].strip()
                if not nxt_raw:
                    peek = peek_nonempty(lines, j + 1)
                    if not peek or not looks_like_stat_continuation(peek[1]):
                        break
                    j += 1
                    continue
                nxt = strip_noise(nxt_raw)
                if nxt is None:
                    j += 1
                    continue
                if nxt in KNOWN_HEADERS:
                    break
                if is_all_caps_title(nxt) and nxt.count(" ") <= 6 and not looks_like_stat_continuation(nxt):
                    break
                block.append(nxt)
                j += 1
            paras.append("```\n" + "\n".join(block) + "\n```")
            i = j
            continue

        if is_stat_or_table_line(s):
            flush_all()
            block = [s]
            j = i + 1
            # For dice-result tables, keep gathering until a clear prose sentence
            dice_table = bool(re.match(r"^(2D6|1D6|5D6)\s+RESULT", s, re.I))
            while j < len(lines):
                nxt_raw = lines[j].strip()
                if not nxt_raw:
                    peek = peek_nonempty(lines, j + 1)
                    if peek and (looks_like_stat_continuation(peek[1]) or dice_table):
                        # blank inside dice table: keep going unless next is a new section banner
                        if peek[1] in KNOWN_HEADERS or (
                            is_all_caps_title(peek[1]) and len(peek[1].split()) >= 3
                            and peek[1] not in block
                            and not re.match(r"^[\d\-]", peek[1])
                        ):
                            break
                        j += 1
                        continue
                    break
                nxt = strip_noise(nxt_raw)
                if nxt is None:
                    j += 1
                    continue
                if nxt in KNOWN_HEADERS:
                    break
                if dice_table:
                    # Stop at next ALL CAPS table title like THE MEET OCCURS AT...
                    if (
                        is_all_caps_title(nxt)
                        and len(nxt) > 12
                        and not re.match(r"^[\d\-]", nxt)
                        and "RESULT" not in nxt
                    ):
                        break
                    block.append(nxt)
                    j += 1
                    continue
                if looks_like_stat_continuation(nxt):
                    block.append(nxt)
                    j += 1
                    continue
                break
            paras.append("```\n" + "\n".join(block) + "\n```")
            i = j
            continue

        if s.startswith("- "):
            flush_buf()
            if bullet_buf is not None:
                flush_bullet()
            bullet_buf = [s[2:].strip()]
            i += 1
            continue

        if bullet_buf is not None:
            bullet_buf.append(s)
            i += 1
            continue

        buf.append(s)
        i += 1

    flush_all()

    out_lines: list[str] = []
    for p in paras:
        if p.startswith(("## ", "```", "> ")):
            if out_lines and out_lines[-1] != "":
                out_lines.append("")
            out_lines.append(p)
            out_lines.append("")
        else:
            out_lines.append(p)
            out_lines.append("")

    text = "\n".join(out_lines)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = break_giant_paras(text)
    text = fix_soft_hyphens(text)
    for a, b in (("\u2014", "-"), ("\u2013", "-"), ("—", "-"), ("–", "-"), ("\u00ad", "")):
        text = text.replace(a, b)
    return text.strip() + "\n"


def reflow_toc(body: str) -> str:
    """Contents page: reflow only; do not promote TOC lines to ##."""
    body = re.sub(r"(\w)-\n(\w)", r"\1\2", body)
    lines = [ln.strip() for ln in body.splitlines() if ln.strip()]
    cleaned: list[str] = []
    for s in lines:
        s2 = strip_noise(s)
        if s2 is None:
            continue
        if s2 in SKIP_EXACT:
            continue
        cleaned.append(s2)
    # Pair title + page number when possible
    out: list[str] = []
    i = 0
    while i < len(cleaned):
        cur = cleaned[i]
        if i + 1 < len(cleaned) and re.match(r"^\d{1,3}$", cleaned[i + 1]):
            out.append(f"- {cur} — {cleaned[i + 1]}".replace("—", "-"))
            i += 2
            continue
        # Credits blocks stay as paragraphs
        if cur.upper().startswith("WRITING:") or cur.upper().startswith("BETTER THAN BAD CREDITS"):
            flush = [cur]
            i += 1
            while i < len(cleaned) and not re.match(r"^\d{1,3}$", cleaned[i]):
                if cleaned[i] in KNOWN_HEADERS and len(cleaned[i].split()) <= 4:
                    break
                flush.append(cleaned[i])
                i += 1
            out.append("")
            out.append(" ".join(flush))
            out.append("")
            continue
        out.append(cur)
        i += 1
    text = "\n".join(out)
    text = re.sub(r"\n{3,}", "\n\n", text)
    for a, b in (("\u2014", "-"), ("\u2013", "-"), ("—", "-"), ("–", "-"), ("\u00ad", "")):
        text = text.replace(a, b)
    return text.strip() + "\n"


def format_file(path: Path) -> bool:
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
    while body_start < len(lines) and not lines[body_start].strip():
        body_start += 1
    body = "\n".join(lines[body_start:])
    if path.name.startswith("01 -"):
        new_body = reflow_toc(body)
    else:
        new_body = reflow_body(body)
        # Drop leftover running headers smashed into prose
        new_body = re.sub(
            r"\b(?:LIGHTS IN THE DARKNESS|FIXER-UPPER OPPORTUNITIES|PRETORIA, HURRAH|"
            r"BUILDING A HOODER|BEING LESS BAD|JACARANDA CITIZENS|MINING FOR GOLD|"
            r"FRIENDS WILL BE FRIENDS)\b",
            "",
            new_body,
            flags=re.I,
        )
        new_body = re.sub(r" {2,}", " ", new_body)
        new_body = re.sub(r"\n{3,}", "\n\n", new_body)
    new = f"{title}\n\n{src}\n\n{new_body}" if src else f"{title}\n\n{new_body}"
    for a, b in (("\u2014", "-"), ("\u2013", "-"), ("—", "-"), ("–", "-")):
        new = new.replace(a, b)
    if new != raw:
        path.write_text(new, encoding="utf-8")
        return True
    return False


def main() -> None:
    changed = 0
    for p in sorted(OUT.glob("[0-9]*.md")):
        if format_file(p):
            changed += 1
            print("formatted", p.name, p.stat().st_size)
        else:
            print("unchanged", p.name)
    print(f"done: {changed} files")


if __name__ == "__main__":
    main()
