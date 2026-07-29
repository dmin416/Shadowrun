# -*- coding: utf-8 -*-
"""Formatting pass: reflow Splintered State Source Texts into readable markdown.

Run AFTER extract_splintered_state.py (expects raw PDF line breaks).
Does not format INDEX.md.
"""
from pathlib import Path
import re

OUT = Path(r"c:\Users\admin\Desktop\Shadowrun\Source Texts\Splintered State")

KNOWN_HEADERS = {
    "SCAN THIS",
    "TELL IT TO THEM STRAIGHT",
    "HOOKS",
    "BEHIND THE SCENES",
    "PUSHING THE ENVELOPE",
    "DEBUGGING",
    "PLACES OF INTEREST",
    "GRUNTS AND MOVING TARGETS",
    "PICKING UP THE PIECES",
    "MONEY",
    "KARMA",
    "REPUTATION",
    "CONTACTS",
    "CAST OF SHADOWS",
    "PLOT SYNOPSIS",
    "ADVENTURE BACKGROUND",
    "POLITICS & PAYDATA",
    "POLITICS AND PAYDATA",
    "LEGWORK",
    "MATRIX LEGWORK",
    "PLAYER HANDOUTS",
    "CONTENTS",
    "CREDITS",
    "OTHER CONTACTS",
    "THE ARES OFFER",
    "PHYSICAL SECURITY FEATURES",
    "MATRIX SECURITY",
    "NOVELTY HILLS SLEEP AND EAT",
    "HANDOUT #1: FRAGMENTED FILES FROM DIETRICH'S COMMLINK",
    "HANDOUT #2: REASSEMBLED PROJECT DAYBREAK FILES",
    "FORT LEWIS ZOO MAP",
    "BRACKHAVEN INVESTMENTS MAP",
    "AGENT SETH DIETRICH",
    "'IMAGINARY' ANNIE GOLDSMITH, INVISIBLE ESQUIRE",
    "DISTRICT ATTORNEY DANA OAKS",
    "ELIZA BLOOM",
    "GREGORY ZANE",
    "KAREN KING",
    "TAUREN",
    "SETH DIETRICH",
    "OPERATION DAYBREAK",
    "DANA OAKS' ANTI-GANG TASK FORCE",
    "SHOTOZUMI GUMI NINJA",
}

SKIP_EXACT = {
    "SHADOWRUN",
    "SPLINTERED",
    "STATE",
    "SPLINTERED STATE",
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
    # "Har-\nvard" / "Har- vard"
    text = re.sub(r"([A-Za-z]{2,})-\s+([A-Za-z]{2,})", r"\1\2", text)

    # "Har - vard" / "ster - ile" but NOT legwork "3 - Whispers" / "5 - The"
    def spaced_hyphen(m: re.Match) -> str:
        a, b = m.group(1), m.group(2)
        if a.isdigit() or b.isdigit():
            return m.group(0)
        # Syllable fragments are short; keep intentional spaced dashes otherwise
        if len(a) <= 5 and len(b) <= 6 and a.isalpha() and b.isalpha():
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
    # Skill/gear wrap: "6, Etiquette 3, ..." or "helmet, and non-conductivity"
    if re.match(r"^[\d(]", s):
        return True
    if re.match(r"^[a-z]", s):
        return True
    # Weapon / gear lines often start with brand names mid-list
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
    if re.match(r"^>>?\s*SPLINTERED STATE", s, re.I):
        return None
    if re.match(r"^\d+\s+SCENE \d+", s, re.I):
        return None
    if re.match(r"^SCENE \d+:.+\s+\d+\s*$", s, re.I):
        return None
    if re.match(r"^SCENE \d+:\s*$", s, re.I):
        return None
    if re.match(r"^\d+\s+(?:LEGWORK|CAST OF SHADOWS|PLOT SYNOPSIS|PICKING UP)", s, re.I):
        return None
    if re.match(r"^(?:LEGWORK|CAST OF SHADOWS|PLOT SYNOPSIS|PICKING UP THE PIECES)\s+\d+\s*$", s, re.I):
        return None
    if re.match(r"^\d+\s+CONTENTS", s, re.I):
        return None
    if re.match(r"^CONTENTS?\s*&\s*CREDITS\s+\d+$", s, re.I):
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
        if text.startswith("•"):
            text = "- " + text.lstrip("• ").strip()
        elif text.startswith("*"):
            text = "- " + text.lstrip("* ").strip()
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

        # Known section headers
        if s in KNOWN_HEADERS or (is_all_caps_title(s) and s.count(" ") <= 8):
            # Skip redundant SCENE N banners (title is in H1)
            if re.match(r"^SCENE \d+", s, re.I):
                end_i, _ = collect_caps_run(lines, i, s)
                i = end_i + 1
                continue
            if s in SKIP_EXACT:
                i += 1
                continue
            flush_all()
            if s in KNOWN_HEADERS:
                paras.append(f"## {title_case_header(s)}")
                i += 1
                continue
            # Place / subsection titles: merge consecutive ALL CAPS
            end_i, merged = collect_caps_run(lines, i, s)
            # Drop if merged is only a skip fragment
            if merged.upper() in SKIP_EXACT:
                i = end_i + 1
                continue
            paras.append(f"## {title_case_header(merged)}")
            i = end_i + 1
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

        # Bullets (* from extract of •)
        if s.startswith("•") or s.startswith("*") or s.startswith("- "):
            flush_buf()
            if bullet_buf is not None:
                flush_bullet()
            if s.startswith("•"):
                bullet_buf = [s.lstrip("•").strip()]
            elif s.startswith("*"):
                bullet_buf = [s.lstrip("*").strip()]
            else:
                bullet_buf = [s[2:].strip()]
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
    # Common PDF digit splits
    text = text.replace("kill 1 1 HN", "kill 11 HN")
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text


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
    if body.strip().startswith("(No extractable text"):
        return
    formatted = reflow_body(body)
    for a, b in (("\u2014", "-"), ("\u2013", "-"), ("—", "-"), ("–", "-")):
        formatted = formatted.replace(a, b)
        title = title.replace(a, b)
        src = src.replace(a, b)
    path.write_text(f"{title}\n\n{src}\n\n{formatted}", encoding="utf-8")
    print("formatted", path.name, "bytes", path.stat().st_size)


def main():
    for p in sorted(OUT.glob("*.md")):
        format_file(p)
    idx = OUT / "INDEX.md"
    if idx.exists():
        t = idx.read_text(encoding="utf-8")
        t = t.replace("- [ ] Format", "- [x] Format")
        for a, b in (("\u2014", "-"), ("\u2013", "-"), ("—", "-"), ("–", "-")):
            t = t.replace(a, b)
        idx.write_text(t, encoding="utf-8")


if __name__ == "__main__":
    main()
