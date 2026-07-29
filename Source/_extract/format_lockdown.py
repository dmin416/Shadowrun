# -*- coding: utf-8 -*-
"""Formatting pass: reflow Lockdown Source Texts into readable markdown.

Run AFTER extract_lockdown.py (expects raw PDF line breaks).
Does not format INDEX.md.
"""
from pathlib import Path
import re

OUT = Path(r"c:\Users\admin\Desktop\Shadowrun\Source Texts\Lockdown")

KNOWN_HEADERS = {
    "INTRODUCTION",
    "CONTENTS",
    "CREDITS",
    "JACKPOINT",
    "HARBOR HEIST",
    "A RUNNER'S GUIDE TO BOSTON",
    "BOSTON: HISTORY ABOUNDS",
    "BOSTON: FROM THE GROUND UP",
    "POLITICAL AFFAIRS",
    "CORPORATE AFFAIRS",
    "DRACONIC AFFAIRS",
    "SECURITY CONCERNS",
    "UNDERWORLD INFO",
    "MAGICAL BEANTOWN",
    "MEDICAL MIRACLES",
    "LOCKING THE HUB",
    "THE COVER-UP: NEWS SO FAR ON THE QUARANTINE",
    "THE UNWAVERING TRUTH",
    "WHO'S INSIDE",
    "STREET LEGENDS OF BOSTON",
    "INSIDE THE QZ: A WANDERER'S GUIDE",
    "INSIDE THE QZ",
    "A WANDERER'S GUIDE",
    "FOUR CORNERS",
    "MEETING HOUSE HILL",
    "UPHAMS CORNER",
    "MISSION HILL",
    "ROXBURY",
    "FENWAY",
    "FENWAY COLLEGES",
    "CAMBRIDGE",
    "CHELSEA",
    "FOUR POINTS SHERATON",
    "WEST REVERE",
    "FRANKLIN PARK",
    "MARBLEHEAD",
    "NAHANT",
    "THE BLACK BAZAAR",
    "UPTOWN",
    "THE NUB",
    "THE DEEP",
    "THE LABYRINTH",
    "THE BRAINTRUST",
    "THE SQUARES",
    "HARVARD",
    "CHESTNUT HILL",
    "THE GOOD",
    "THE BAD",
    "THE UGLY",
    "BEANTOWN BOUND",
    "INTRODUCTION TO THE ADVENTURES",
    "WHAT'S UP, CHUMMER?",
    "TELL IT TO THEM STRAIGHT",
    "BEHIND THE SCENES",
    "CHARACTERS",
    "LOCATIONS",
    "PICKING UP THE PIECES",
    "TRAINYARD TROUBLES",
    "THE DARK SIDE",
    "HEROES OF FOUR CORNERS",
    "VOICES",
    "HEAD CASE",
    "CROSSING THE ROAD",
    "IT'S A WRAP",
    "DIGGING DEEPER",
    "INTRO",
    "SETUP",
    "EVENT 1",
    "EVENT 2",
    "EVENT 3",
    "EVENT 4",
    "EVENT 5",
    "EVENT 6",
    "SEQUELS",
    "BRINGING DOWN THE HOUSE",
    "CLIMAX",
    "GAME INFORMATION",
    "COGNITIVE FRAGMENTATION DISORDER VIRUS",
    "THE STANDARD CFD VIRUS",
    "LOCKDOWN CFD",
    "THE FORCES OF DARKNESS",
    "CHARACTER TROVE",
    "FAMILIAR FACES",
    "SPECIAL THANKS",
}

SKIP_EXACT = {
    "SHADOWRUN",
    "LOCKDOWN",
    "CONTENTS",
    "& CREDITS",
    "CONTENTS & CREDITS",
    "CONTENTS/CREDITS",
}


def title_case_header(s: str) -> str:
    small = {"a", "an", "the", "and", "or", "of", "in", "on", "for", "to", "vs", "at"}
    words = s.split()
    out = []
    for i, w in enumerate(words):
        lw = w.lower().strip("()")
        if i > 0 and lw in small:
            if w.startswith("("):
                out.append("(" + lw + (")" if w.endswith(")") else ""))
            else:
                out.append(lw)
        else:
            core = w.strip("()")
            fixed = core[:1].upper() + core[1:].lower() if core else core
            if w.startswith("(") and w.endswith(")"):
                out.append(f"({fixed})")
            elif w.startswith("("):
                out.append("(" + fixed)
            elif w.endswith(")"):
                out.append(fixed + ")")
            else:
                out.append(fixed)
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
        # Keep intentional spaced dashes between real words ("decks - any")
        vowel = re.compile(r"[aeiouy]", re.I)
        if len(a) >= 4 and len(b) >= 3 and vowel.search(a) and vowel.search(b):
            return m.group(0)
        if a.islower() and b.islower() and len(a) <= 12 and len(b) <= 12:
            return a + b
        if a[0].isupper() and a[1:].islower() and b.islower() and len(a) <= 10 and len(b) <= 12:
            return a + b
        return m.group(0)

    text = re.sub(r"([A-Za-z0-9]+)\s+-\s+([A-Za-z0-9]+)", spaced_hyphen, text)
    return text


def is_stat_or_table_line(s: str) -> bool:
    # Full attr header row (not mid-prose mentioning armor/skills)
    if re.search(r"\bB\s+A\s+R\s+S\b", s):
        return True
    if re.match(r"^[\d\s().+\-/AP]+$", s) and len(s) > 8:
        return True
    if s.count("|") >= 2:
        return True
    if re.match(
        r"^(Condition Monitor|Armor|Initiative|Limits|Skills|Qualities|Gear|Weapons|"
        r"Vehicles|Boxes|Augmentations|Metatype|Sex|Age|Active|Knowledge|Languages|"
        r"Powers|Spells|Std\.?\s*Upgrades|Modifications|Astral Initiative|"
        r"Physical Initiative|Matrix Initiative)\s*:",
        s,
        re.I,
    ):
        return True
    if re.match(
        r"^(Condition Monitor|Armor|Initiative|Limits|Skills|Qualities|Gear|Weapons|"
        r"Vehicles|Boxes|Augmentations|Metatype|Sex|Age|Active|Knowledge|Languages|"
        r"Powers|Spells|Std\.?\s*Upgrades|Modifications|Astral Initiative|"
        r"Physical Initiative|Matrix Initiative)\s*$",
        s,
        re.I,
    ):
        return True
    if re.match(r"^(Connection|Loyalty)\s+\d", s, re.I):
        return True
    return False


def looks_like_stat_continuation(s: str) -> bool:
    if is_stat_or_table_line(s):
        return True
    if re.match(r"^Boxes\s+\d", s, re.I):
        return True
    if re.match(r"^[\d(]", s):
        return True
    if re.match(r"^[a-z]", s) and len(s) < 60 and not s.endswith("."):
        if re.search(
            r"\b(DV|AP|Acc|RC|SA|BF|FA|Reach|w/|clips?|ammo|Rating|Essence|Initiative)\b",
            s,
        ):
            return True
        if s.count(",") >= 2:
            return True
    if re.search(r"\b(DV|AP|Acc|RC|SA|BF|FA|Reach|w/|clips?|ammo|Rating)\b", s):
        return True
    return False


def is_all_caps_title(s: str) -> bool:
    if not s or not s.isupper():
        return False
    if s.endswith(".") and len(s) > 40:
        return False
    if len(s) > 70:
        return False
    return True


def strip_noise(s: str) -> str | None:
    if not s:
        return None
    if s in {"SHADOWRUN", ">>", "<<", "<"}:
        return None
    # Keep lone ">" for JackPoint comment handling in reflow_body
    if re.match(r"^>>?\s*LOCKDOWN", s, re.I):
        return None
    if "InMediaRes Productions" in s:
        return None
    if re.match(r"^>>?\s*CONTENTS", s, re.I):
        return None
    if re.match(r"^CONTENTS & CREDITS\s*$", s, re.I):
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
    """Split very long prose blocks on sentence boundaries."""
    out: list[str] = []
    for block in text.split("\n\n"):
        if block.startswith("## ") or block.startswith("```") or block.startswith(">"):
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

        # JackPoint comments ("> text" or lone ">" then body/handle lines)
        if s == ">" or s.startswith(">") or s.startswith(">\t"):
            flush_all()
            comment = s.lstrip(">").strip()
            j = i + 1
            # Gather comment body until blank / new post / section
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
                if is_all_caps_title(nxt) and (
                    nxt in KNOWN_HEADERS or nxt.rstrip(":") in KNOWN_HEADERS
                ):
                    break
                if not comment:
                    comment = nxt
                else:
                    comment = comment + " " + nxt
                j += 1
                # Typical JP pattern: one comment line, then handle line, then stop
                # Keep gathering short handle-only followups
                peek = peek_nonempty(lines, j)
                if peek and (
                    peek[1] == ">"
                    or peek[1].startswith(">")
                    or peek[1].upper().startswith("POSTED BY:")
                    or peek[1] in KNOWN_HEADERS
                ):
                    break
                # If next looks like a short handle (1-3 words, no period), include then stop
                if peek and len(peek[1].split()) <= 3 and not peek[1].endswith((".", "!", "?")):
                    if not peek[1][0].islower() and len(peek[1]) < 40:
                        comment = comment + "\n> " + peek[1]
                        j = peek[0] + 1
                    break
                break
            comment = fix_soft_hyphens(re.sub(r"\s+", " ", comment.replace("\n> ", " | ")).strip())
            if comment:
                # Restore handle on own blockquote line if marked
                if " | " in comment:
                    body_c, handle = comment.rsplit(" | ", 1)
                    paras.append("> " + body_c.strip())
                    paras.append("> " + handle.strip())
                else:
                    paras.append("> " + comment)
            i = j
            continue

        # Posted-by banners
        if s.upper().startswith("POSTED BY:"):
            flush_all()
            paras.append("## " + s)
            i += 1
            continue

        # Known section headers
        if s in KNOWN_HEADERS or (is_all_caps_title(s) and s.rstrip(":") in KNOWN_HEADERS):
            key = s.rstrip(":")
            if key in SKIP_EXACT:
                i += 1
                continue
            peek = peek_nonempty(lines, i + 1)
            if (
                peek
                and re.match(r"^[a-z]", peek[1])
                and buf
                and not buf[-1].rstrip().endswith((".", "!", "?", ":", '"', "'"))
            ):
                i += 1
                continue
            flush_all()
            # Merge multi-line ALL CAPS title fragments
            parts = [key]
            j = i + 1
            while True:
                nxt = peek_nonempty(lines, j)
                if not nxt:
                    break
                nj, ns = nxt
                if ns in KNOWN_HEADERS or ns.rstrip(":") in KNOWN_HEADERS:
                    break
                if not is_all_caps_title(ns) or len(ns) > 48:
                    break
                parts.append(ns.rstrip(":"))
                j = nj + 1
            merged = " ".join(parts)
            # Prefer known full header if we built one
            if merged in KNOWN_HEADERS:
                header = merged
                i = j
            else:
                header = key
                i += 1
            paras.append(f"## {title_case_header(header)}")
            continue

        # Multi-line ALL CAPS known as "CARD AND PUZZLE" + "BACKGROUND"
        if is_all_caps_title(s) and len(s) <= 40:
            peek = peek_nonempty(lines, i + 1)
            if peek and is_all_caps_title(peek[1]) and len(peek[1]) <= 40:
                merged = f"{s} {peek[1]}".rstrip(":")
                if merged in KNOWN_HEADERS:
                    flush_all()
                    paras.append(f"## {title_case_header(merged)}")
                    i = peek[0] + 1
                    continue

        # Mid-line attribute header: "... HUMAN B A R S W L I C ..."
        bars = re.search(r"^(.*?\S)\s+(B\s+A\s+R\s+S\b.*)$", s)
        if bars and not s.startswith("B "):
            flush_all()
            bio = bars.group(1).strip()
            if bio:
                paras.append(bio)
            s = bars.group(2).strip()
            # fall through into BARS stat block handler below

        if is_stat_or_table_line(s) and re.search(r"\bB\s+A\s+R\s+S\b", s):
            flush_all()
            block = [s]
            j = i + 1
            while j < len(lines):
                nxt_raw = lines[j].strip()
                if not nxt_raw:
                    peek = peek_nonempty(lines, j + 1)
                    if not peek:
                        break
                    nj, ns = peek
                    if ns in KNOWN_HEADERS or (
                        is_all_caps_title(ns) and not looks_like_stat_continuation(ns)
                    ):
                        break
                    if (
                        not looks_like_stat_continuation(ns)
                        and len(ns) > 50
                        and (" is " in ns or " got " in ns or " spent " in ns)
                    ):
                        break
                    j += 1
                    continue
                nxt = strip_noise(nxt_raw)
                if nxt is None:
                    j += 1
                    continue
                if nxt in KNOWN_HEADERS:
                    break
                if is_all_caps_title(nxt) and nxt.count(" ") <= 6 and not re.search(
                    r"\b(DV|AP|Acc|RC|SA|BF|FA|Reach|Rating|Armor|Skills|Gear|Weapons)\b",
                    nxt,
                ):
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
            while j < len(lines):
                nxt_raw = lines[j].strip()
                if not nxt_raw:
                    peek = peek_nonempty(lines, j + 1)
                    if peek and looks_like_stat_continuation(peek[1]):
                        j += 1
                        continue
                    break
                nxt = strip_noise(nxt_raw)
                if nxt is None:
                    j += 1
                    continue
                if is_all_caps_title(nxt) and nxt in KNOWN_HEADERS:
                    break
                if looks_like_stat_continuation(nxt):
                    block.append(nxt)
                    j += 1
                    continue
                if nxt.endswith(".") and len(nxt) > 70:
                    break
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
        if p.startswith("## "):
            if out_lines and out_lines[-1] != "":
                out_lines.append("")
            out_lines.append(p)
            out_lines.append("")
        elif p.startswith("```"):
            if out_lines and out_lines[-1] != "":
                out_lines.append("")
            out_lines.append(p)
            out_lines.append("")
        elif p.startswith("> "):
            if out_lines and out_lines[-1] != "":
                out_lines.append("")
            out_lines.append(p)
            out_lines.append("")
        elif p.startswith("- "):
            out_lines.append(p)
        else:
            out_lines.append(p)
            out_lines.append("")

    text = "\n".join(out_lines).strip() + "\n"
    text = fix_soft_hyphens(text)
    text = break_giant_paras(text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text


def strip_duplicate_chapter_headers(title: str, body: str) -> str:
    """Drop ## headers that merely repeat the chapter H1."""
    h1 = title[2:].strip().lower()
    out: list[str] = []
    for block in body.split("\n\n"):
        if block.startswith("## "):
            h = block[3:].strip().lower()
            if h == h1 or h.replace(":", "") == h1.replace(":", ""):
                continue
        out.append(block)
    return "\n\n".join(out)


def format_file(path: Path) -> None:
    if path.name == "INDEX.md":
        return
    raw = path.read_text(encoding="utf-8")
    lines = raw.splitlines()
    if not lines or not lines[0].startswith("# "):
        return
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
    if body.startswith("(No extractable text"):
        path.write_text(f"{title}\n\n{src}\n\n{body.strip()}\n", encoding="utf-8")
        print("kept image stub", path.name)
        return
    formatted = reflow_body(body)
    formatted = strip_duplicate_chapter_headers(title, formatted)
    for a, b in (("\u2014", "-"), ("\u2013", "-"), ("—", "-"), ("–", "-")):
        formatted = formatted.replace(a, b)
        title = title.replace(a, b)
        src = src.replace(a, b)
    path.write_text(f"{title}\n\n{src}\n\n{formatted}", encoding="utf-8")
    print("formatted", path.name, "bytes", path.stat().st_size)


def main():
    for p in sorted(OUT.glob("*.md")):
        format_file(p)


if __name__ == "__main__":
    main()
