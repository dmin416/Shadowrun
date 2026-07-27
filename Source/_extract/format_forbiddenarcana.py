# -*- coding: utf-8 -*-
"""Formatting pass: reflow Forbidden Arcana Source Texts into readable markdown.

Run AFTER extract_forbiddenarcana.py (expects raw PDF line breaks).
Does not format INDEX.md.
"""
from pathlib import Path
import re

OUT = Path(r"c:\Users\admin\Desktop\Shadowrun\Source Texts\Forbidden Arcana")

KNOWN_HEADERS = {
    "ADVANCED ALCHEMY",
    "BLOOD MAGIC",
    "COMBAT SPELLS",
    "CONJURING",
    "CONTENTS",
    "CREDITS",
    "DETECTION SPELLS",
    "ENCHANTING",
    "EXPANDED ASPECTS",
    "FOCUSED AWAKENED",
    "GAME INFORMATION",
    "HEALTH SPELLS",
    "IDEALS",
    "ILLUSION SPELLS",
    "INTRODUCTION",
    "MAGIC MASTERY",
    "MANIPULATION SPELLS",
    "NEW METAMAGICS",
    "NEW RITUALS",
    "NEW SPELLS",
    "NOTABLE TEACHERS",
    "PREFERRED SPELLS",
    "RELATED MENTOR SPIRITS",
    "RULES",
    "SEEING THE INVISIBLE WORLD",
    "SORCERY",
    "TEA & SYMPATHY",
    "TEA AND SYMPATHY",
    "TRADITION UPDATES",
    "TRADITIONS",
    "WHERE THE WILD THINGS ARE",
}

SKIP_EXACT = {
    "SHADOWRUN",
    "Forbidden Arcana",
    "CONTENTS",
    "& CREDITS",
}


def title_case_header(s: str) -> str:
    small = {"a", "an", "the", "and", "or", "of", "in", "on", "for", "to", "vs", "at"}
    words = s.split()
    out = []
    for i, w in enumerate(words):
        lw = w.lower().strip("()")
        if i > 0 and lw in small:
            # preserve surrounding punctuation like (Trouble)
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







def is_stat_or_table_line(s: str) -> bool:
    if re.search(r"\bB\s+A\s+R\s+S\b", s):
        return True
    if re.match(r"^[\d\s().+\-/AP]+$", s) and len(s) > 8:
        return True
    if s.count("|") >= 2:
        return True
    if re.match(
        r"^(Condition Monitor|Armor|Initiative|Limits|Skills|Qualities|Gear|Weapons|Vehicles|Boxes|Augmentations|Metatype|Sex|Age|Active|Knowledge|Languages|Powers|Spells|Std\.?\s*Upgrades|Modifications)\b",
        s,
        re.I,
    ):
        return True
    # Contact sheet numbers only (avoid "Connection + Connection Test")
    if re.match(r"^(Connection|Loyalty)\s+\d", s, re.I):
        return True
    return False


def looks_like_stat_continuation(s: str) -> bool:
    """Lines that continue a split NPC sheet after a soft wrap."""
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
    if re.search(
        r"\b(DV|AP|Acc|RC|SA|BF|FA|Reach|w/|clips?|ammo|Rating)\b",
        s,
    ):
        return True
    return False



def is_all_caps_title(s: str) -> bool:
    if not s or not s.isupper():
        return False
    if s.endswith(".") and len(s) > 40:
        return False
    if len(s) > 60:
        return False
    return True


def strip_noise(s: str) -> str | None:
    if not s:
        return None
    if s == "SHADOWRUN":
        return None
    if re.match(r"^>>?\s*Forbidden Arcana", s, re.I):
        return None
    if "InMediaRes Productions LLC" in s:
        return None
    if re.match(r"^>>?\s*CONTENTS", s, re.I):
        return None
    if re.match(r"^<<?\s*", s) and "<<" in s:
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


def collect_caps_run(lines: list[str], i: int, first: str) -> tuple[int, str]:
    """Merge consecutive ALL-CAPS title fragments into one heading."""
    parts = [first.rstrip(":")]
    j = i + 1
    while True:
        nxt = peek_nonempty(lines, j)
        if not nxt:
            break
        nj, ns = nxt
        # stop at known section headers that start a new block
        if ns in KNOWN_HEADERS:
            break
        if not is_all_caps_title(ns):
            break
        # Don't swallow Karma cost lines or digit-bearing titles
        if re.match(r"^\d+\s+KARMA\b", ns, re.I) or re.search(r"\d", ns):
            break
        # Don't swallow long prose ALL CAPS
        if len(ns) > 48:
            break
        parts.append(ns.rstrip(":"))
        j = nj + 1
    return j - 1, " ".join(parts)


def reflow_body(body: str) -> str:
    # Soft-hyphen join before line split so "word-\nword" is fixed early
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
        if text.startswith("â€¢"):
            text = "- " + text.lstrip("â€¢ ").strip()
        elif not text.startswith("- "):
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
            # Page-break blanks often land mid-sentence; do not flush prose.
            # End an open bullet on a blank so list items stay separate.
            if bullet_buf is not None:
                flush_bullet()
            i += 1
            continue

        s = strip_noise(stripped)
        if s is None:
            i += 1
            continue

        # Multi-line "WHEN ..., READ THE FOLLOWING:"
        if s.isupper() and s.startswith("WHEN "):
            flush_all()
            parts = [s.rstrip(":")]
            j = i + 1
            while j < len(lines):
                nxt = strip_noise(lines[j].strip()) if lines[j].strip() else None
                if nxt is None:
                    if lines[j].strip() == "":
                        break
                    j += 1
                    continue
                if nxt.isupper() or "FOLLOWING" in nxt.upper():
                    parts.append(nxt.rstrip(":"))
                    if "FOLLOWING" in nxt.upper():
                        i = j
                        break
                    j += 1
                    continue
                break
            paras.append("## " + title_case_header(" ".join(parts)))
            i += 1
            continue

        # Mastery quality: ALL-CAPS name line(s), then a "N KARMA" line
        if (
            s.isupper()
            and 3 <= len(s) <= 60
            and not s.endswith(".")
            and not re.match(r"^\d+\s+KARMA\b", s, re.I)
            and not re.search(r"\d", s)  # names don't include digits
        ):
            end_i, merged = collect_caps_run(lines, i, s)
            nxt = peek_nonempty(lines, end_i + 1)
            if nxt and re.match(r"^\d+\s+KARMA\b", nxt[1], re.I):
                flush_all()
                paras.append(f"### {title_case_header(merged)}")
                paras.append(f"**{nxt[1]}**")
                i = nxt[0] + 1
                continue

        # Known section headers
        if s in KNOWN_HEADERS:
            if s in SKIP_EXACT:
                i += 1
                continue
            # Running page header mid-sentence (next line continues lowercase)
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
            paras.append(f"## {title_case_header(s)}")
            i += 1
            continue

        if is_stat_or_table_line(s) and re.search(r"\bB\s+A\s+R\s+S\b", s):
            # Full NPC attribute sheet: keep everything until next NPC/section
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
                    # New section / NPC heading
                    if ns in KNOWN_HEADERS or (
                        is_all_caps_title(ns) and not looks_like_stat_continuation(ns)
                    ):
                        break
                    # New NPC bio paragraph
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

        # Bullets
        if s.startswith("â€¢") or s.startswith("- "):
            flush_buf()
            if bullet_buf is not None:
                flush_bullet()
            bullet_buf = [s.lstrip("â€¢").strip() if s.startswith("â€¢") else s[2:].strip()]
            i += 1
            continue

        # Continuation of a bullet (next line not a new section / bullet)
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
        elif p.startswith("- "):
            out_lines.append(p)
        else:
            out_lines.append(p)
            out_lines.append("")

    text = "\n".join(out_lines).strip() + "\n"
    text = fix_soft_hyphens(text)
    # Common PDF digit splits / OCR artifacts
    text = text.replace("kill 1 1 HN", "kill 11 HN")
    text = re.sub(r"\bp\.\s*(\d)\s+(\d{2})\b", r"p. \1\2", text)
    text = re.sub(r"\b(20\d)\s+(\d)\b", r"\1\2", text)
    text = text.replace("Jack - Pointers", "JackPointers")
    text = text.replace("Jack - Point", "JackPoint")
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text


def format_file(path: Path) -> None:
    if path.name.startswith("00 -") or path.name == "INDEX.md":
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
    formatted = reflow_body(body)
    for a, b in (("\u2014", "-"), ("\u2013", "-"), ("â€”", "-"), ("â€“", "-")):
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

