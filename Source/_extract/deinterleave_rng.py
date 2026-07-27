# -*- coding: utf-8 -*-
"""Fix PDF reading-order interleaves in Run & Gun Source Texts.

1) Stitch lowercase continuations back onto incomplete sentences.
2) Park interrupting caption/stat/sidebar chunks and reinsert after the
   matching item title (or at end of current section).
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(r"c:\Users\admin\Desktop\Shadowrun\Source Texts\Run and Gun")

STAT_HEADERS = {
    "ACC",
    "REACH",
    "DV",
    "AP",
    "AVAIL",
    "COST",
    "MODE",
    "AMMO",
    "RC",
    "NAME",
    "ARMOR",
    "ARMOR RATING",
    "CAPACITY",
    "SIZE",
    "MODIFIER",
    "EXAMPLES",
    "THRESHOLD",
    "PRICE",
    "ITEM",
    "PAGE",
    "RATING",
    "DAMAGE",
    "DAM",
    "TYPE",
    "SKILL",
    "AVAILABILITY",
    "WIRELESS",
    "ESSENCE",
    "SLOTS",
}

TABLE_CELL_WORDS = {
    "Minuscule",
    "Tiny",
    "Small",
    "Average",
    "Bulky",
    "Large",
    "Huge",
}

SIDEBAR_TITLES = {
    "REALISM VS. COMBAT ABSTRACTION:",
    "STRIKING A BALANCE",
    "THE LITTLE THINGS",
    "MODIFIERS, MODIFIERS, MODIFIERS!",
    "ALL ABOUT FLAMETHROWERS",
    "TARGET SIZE MODIFIERS",
    "MOVEMENT PENALTIES BY SPEED",
}


def is_table_cell_label(s: str) -> bool:
    return s.strip() in TABLE_CELL_WORDS


def clean_em(s: str) -> str:
    for a, b in (("\u2014", "-"), ("\u2013", "-"), ("—", "-"), ("–", "-")):
        s = s.replace(a, b)
    return s


def is_blank(s: str) -> bool:
    return not s.strip()


def is_heading(s: str) -> bool:
    return s.startswith("#")


def is_source(s: str) -> bool:
    return s.startswith("**Source:**")


def is_comment_marker(s: str) -> bool:
    return s.strip() == ">" or s.startswith("> ")


def is_stat_header(s: str) -> bool:
    return s.strip().upper() in STAT_HEADERS


def is_statish(s: str) -> bool:
    t = s.strip()
    if not t:
        return False
    if is_stat_header(t):
        return True
    if re.match(r"^[\d.,+\-()/¥RFAPSxXL]+\s*$", t):
        return True
    if re.match(r"^\(?STR\s*[+x]", t, re.I):
        return True
    if re.match(r"^\d+[PRF]\b", t):
        return True
    if "¥" in t or t.endswith("SR5"):
        return True
    return False


def is_allcaps_title(s: str) -> bool:
    t = s.strip()
    if not t or len(t) > 80:
        return False
    if t.upper() != t:
        return False
    if not any(c.isalpha() for c in t):
        return False
    if is_stat_header(t):
        return False
    words = t.split()
    if len(words) < 1:
        return False
    return all(re.match(r"^[A-Z0-9][A-Z0-9'\"\-./:&]*$", w) for w in words)


def is_item_title_line(s: str) -> bool:
    if is_allcaps_title(s) or s.startswith("## ") or s.startswith("### "):
        return True
    t = s.strip()
    m = re.match(
        r"^((?:[A-Z0-9][A-Z0-9'\"\-./:&]*\s+){0,8}[A-Z0-9][A-Z0-9'\"\-./:&]*)\s+",
        t,
    )
    if not m:
        return False
    title = m.group(1).strip()
    if not title or not is_allcaps_title(title):
        return False
    rest = t[m.end() :]
    if not rest:
        return True
    # Glued prose after the title (sentence, quoted slogan, etc.)
    return rest[0].islower() or rest[0] in "'\"" or any(c.islower() for c in rest[:24])


def is_continuation(s: str) -> bool:
    t = s.strip()
    if not t or is_heading(t) or is_comment_marker(t) or t.startswith("|"):
        return False
    if is_allcaps_title(t) or is_statish(t):
        return False
    # lowercase start, or mid-word hyphenation residue like "mine their"
    if t[0].islower():
        return True
    return False


def is_incomplete(s: str) -> bool:
    t = s.strip()
    if not t or is_heading(t) or is_source(t) or is_comment_marker(t):
        return False
    if is_allcaps_title(t) or is_statish(t):
        return False
    # JackPoint handles
    if len(t) < 40 and not any(ch in t for ch in ".!?"):
        words = t.split()
        if 1 <= len(words) <= 4 and t[0].isupper():
            # likely a handle, not incomplete prose
            if not t.endswith(("-", ",")):
                return False
    if t.endswith((".", "!", "?", '"', "¥")):
        return False
    if t.endswith((")", "]")) and not t.endswith(("-", ",")):
        # could still be incomplete mid-paren; treat complete if ends with )
        return False
    if t.endswith(("-", ",", ";", ":")):
        return True
    # ends with a letter/digit -> often mid-sentence after reflow cut
    if t[-1].isalnum() or t[-1] in "'\"":
        return True
    return False


def looks_like_interrupt(chunk: list[str]) -> bool:
    """True if chunk is captions/stats/sidebar rather than normal prose."""
    body = [ln for ln in chunk if ln.strip()]
    if not body:
        return False
    caps = sum(1 for ln in body if is_allcaps_title(ln) or is_statish(ln) or ln.strip().upper() in SIDEBAR_TITLES)
    if caps >= max(1, len(body) // 3):
        return True
    # starts with caption / sidebar
    head = body[0].strip().upper()
    if is_allcaps_title(body[0]) or head in SIDEBAR_TITLES or is_stat_header(body[0]):
        return True
    return False


def extract_item_name(chunk: list[str]) -> str | None:
    """Best-effort item name from an interrupting stat chunk."""
    titles: list[str] = []
    for ln in chunk:
        t = ln.strip()
        if is_stat_header(t):
            break
        if is_allcaps_title(t):
            titles.append(t)
        elif titles:
            break
    if not titles:
        return None
    multi = [t for t in titles if len(t.split()) > 1]
    return max(multi, key=len) if multi else max(titles, key=len)


def normalize_name(s: str) -> str:
    s = s.upper()
    s = s.replace('"', "").replace("'", "")
    s = re.sub(r"\s+", " ", s).strip()
    return s


def names_match(a: str, b: str) -> bool:
    na, nb = normalize_name(a), normalize_name(b)
    if not na or not nb:
        return False
    if na == nb:
        return True
    short, long_ = (na, nb) if len(na) <= len(nb) else (nb, na)
    # Require a real product-name prefix/suffix, not a generic
    # single token like "BLADES" inside "COUGAR FINEBLADES".
    if len(short.split()) < 2 and len(short) < 10:
        return False
    return long_.startswith(short + " ") or long_.endswith(" " + short)


def deinterleave(lines: list[str]) -> list[str]:
    out: list[str] = []
    parked: list[tuple[str | None, list[str]]] = []  # (item_name, chunk)
    i = 0
    n = len(lines)

    while i < n:
        line = lines[i]

        # Join across blanks when the previous prose line is clearly
        # incomplete (PDF wrap or soft hyphen), including capitalized
        # continuations like "Initiative Scores...".
        blank_join_idx = None
        right0 = line.strip()
        if right0 and not (
            is_heading(right0)
            or is_source(right0)
            or is_statish(right0)
            or is_allcaps_title(right0)
            or is_comment_marker(right0)
            or is_table_cell_label(right0)
            or right0.startswith("|")
        ):
            for j in range(len(out) - 1, -1, -1):
                s = out[j]
                if is_blank(s):
                    continue
                intervening = out[j + 1 :]
                if not all(is_blank(x) for x in intervening):
                    break
                if is_heading(s) or is_source(s) or is_statish(s) or is_allcaps_title(s):
                    break
                if not is_incomplete(s):
                    break
                left = s.rstrip()
                last = left.split()[-1].lower() if left.split() else ""
                # Soft-hyphen joins only to lowercase residue ("deter-"+"mine").
                # Function-word / possessive cuts may continue with capitals.
                if left.endswith("-"):
                    ok = bool(right0) and right0[0].islower()
                else:
                    ok = (
                        right0[0].islower()
                        or left.endswith("'")
                        or last
                        in {
                            "a",
                            "an",
                            "the",
                            "to",
                            "of",
                            "for",
                            "and",
                            "or",
                            "with",
                            "their",
                            "all",
                            "players'",
                        }
                    )
                if ok:
                    blank_join_idx = j
                break
        if blank_join_idx is not None:
            left = out[blank_join_idx].rstrip()
            right = right0
            if left.endswith("-") and right and right[0].islower():
                merged = left[:-1] + right
            else:
                merged = left + " " + right
            out = out[: blank_join_idx + 1]
            out[blank_join_idx] = merged
            i += 1
            continue

        prose_line = bool(
            line.strip()
            and not is_heading(line)
            and not is_source(line)
            and not is_statish(line)
            and not is_allcaps_title(line)
            and not is_comment_marker(line)
            and not is_table_cell_label(line)
            and not line.strip().startswith("|")
        )

        if is_continuation(line) or prose_line:
            # Find nearest incomplete prose that has an interrupting
            # caption/stat/sidebar chunk between it and this continuation.
            inc_idx = None
            for j in range(len(out) - 1, -1, -1):
                s = out[j]
                if is_blank(s):
                    continue
                if is_heading(s) or is_source(s):
                    break
                if is_statish(s) or is_allcaps_title(s) or is_comment_marker(s):
                    continue
                st = s.strip()
                if (
                    len(st) < 40
                    and st
                    and st[0].isupper()
                    and "." not in st
                    and not is_incomplete(s)
                ):
                    continue
                if is_incomplete(s):
                    intervening = out[j + 1 :]
                    body = [ln for ln in intervening if ln.strip()]
                    if not body:
                        continue
                    head = body[0]
                    head_u = head.strip().upper().rstrip(":")
                    sidebar_keys = {x.rstrip(":") for x in SIDEBAR_TITLES}
                    head_ok = (
                        is_allcaps_title(head)
                        or is_stat_header(head)
                        or head_u in sidebar_keys
                        or head.strip().upper() in SIDEBAR_TITLES
                    )
                    if not head_ok:
                        # mid-table / mid-prose - keep looking further back
                        continue
                    has_acc = any(
                        is_stat_header(ln) and ln.strip().upper() == "ACC"
                        for ln in intervening
                    )
                    has_sidebar = any(
                        ln.strip().upper().rstrip(":") in sidebar_keys
                        or ln.strip().upper() in SIDEBAR_TITLES
                        for ln in intervening
                    )
                    has_table = any(
                        is_stat_header(ln)
                        and ln.strip().upper()
                        in {
                            "SIZE",
                            "MODIFIER",
                            "EXAMPLES",
                            "THRESHOLD",
                            "ACC",
                        }
                        for ln in intervening
                    )
                    if has_acc or has_sidebar or has_table:
                        if not is_continuation(line):
                            left = s.rstrip()
                            last = left.split()[-1].lower() if left.split() else ""
                            if left.endswith("-"):
                                # soft-hyphen incomplete needs lowercase continuation
                                if not line.strip() or not line.strip()[0].islower():
                                    continue
                            elif not (
                                left.endswith("'")
                                or last
                                in {
                                    "a",
                                    "an",
                                    "the",
                                    "to",
                                    "of",
                                    "for",
                                    "and",
                                    "or",
                                    "with",
                                    "their",
                                    "all",
                                    "players'",
                                }
                            ):
                                continue
                        inc_idx = j
                        break
                    continue
                # complete prose: keep scanning further back for an incomplete
                continue

            if inc_idx is not None:
                intervening = out[inc_idx + 1 :]
                name = extract_item_name(intervening)
                left = out[inc_idx].rstrip()
                right = line.strip()
                if left.endswith("-") and right and right[0].islower():
                    merged = left[:-1] + right
                else:
                    merged = left + " " + right
                out = out[: inc_idx + 1]
                out[inc_idx] = merged
                has_weapon_stats = any(
                    is_stat_header(ln) and ln.strip().upper() == "ACC" for ln in intervening
                )
                if has_weapon_stats:
                    parked.append((name, intervening))
                else:
                    # Sidebar / rules table: keep adjacent to the stitched paragraph
                    if out and out[-1].strip():
                        out.append("")
                    out.extend(intervening)
                    if out and out[-1].strip():
                        out.append("")
                i += 1
                continue

            out.append(line)
            i += 1
            continue

        out.append(line)
        i += 1

    # Reinsert parked chunks after the matching earlier item title
    def clean_chunk(chunk: list[str], title: str) -> list[str]:
        nt = normalize_name(title)
        cleaned: list[str] = []
        for ln in chunk:
            if is_allcaps_title(ln) and names_match(ln, title):
                continue
            cleaned.append(ln)
        # trim blanks
        while cleaned and not cleaned[0].strip():
            cleaned.pop(0)
        while cleaned and not cleaned[-1].strip():
            cleaned.pop()
        return cleaned

    def item_end(lines: list[str], title_idx: int) -> int:
        for j in range(title_idx + 1, len(lines)):
            if is_item_title_line(lines[j]):
                return j
        return len(lines)

    # Insert from last parked to first so earlier indices stay valid when we rebuild via pieces
    leftovers: list[tuple[str | None, list[str]]] = []
    # Work on a mutable copy
    body = list(out)
    # Process parked in reverse so insertions at later positions first don't affect earlier finds... 
    # Actually inserting after earlier titles shifts later indices. Rebuild instead.

    insertions: dict[int, list[list[str]]] = {}  # title_idx -> list of chunks
    for name, chunk in parked:
        if not name:
            leftovers.append((name, chunk))
            continue
        title_idx = None
        for i, ln in enumerate(body):
            if is_allcaps_title(ln) or ln.startswith("## ") or ln.startswith("### "):
                t = ln.lstrip("#").strip()
                if names_match(t, name):
                    title_idx = i
                    break
        if title_idx is None:
            leftovers.append((name, chunk))
            continue
        insertions.setdefault(title_idx, []).append(clean_chunk(chunk, name))

    final: list[str] = []
    i = 0
    while i < len(body):
        if is_allcaps_title(body[i]) or body[i].startswith("## ") or body[i].startswith("### "):
            title_i = i
            final.append(body[i])
            i += 1
            end = item_end(body, title_i)
            while i < end:
                final.append(body[i])
                i += 1
            if title_i in insertions:
                for chunk in insertions[title_i]:
                    if final and final[-1].strip():
                        final.append("")
                    final.extend(chunk)
                    if final and final[-1].strip():
                        final.append("")
            continue
        final.append(body[i])
        i += 1

    for name, chunk in leftovers:
        if final and final[-1].strip():
            final.append("")
        if name:
            final.append(name)
        final.extend(chunk)

    cleaned: list[str] = []
    blank = 0
    for ln in final:
        if not ln.strip():
            blank += 1
            if blank <= 2:
                cleaned.append("")
            continue
        blank = 0
        cleaned.append(ln)
    while cleaned and not cleaned[0].strip():
        cleaned.pop(0)
    while cleaned and not cleaned[-1].strip():
        cleaned.pop()
    return relocate_misplaced_stat_blocks(move_misplaced_item_notes(cleaned))


def find_acc_blocks(lines: list[str]) -> list[tuple[int, int, str]]:
    """Return (start, end, name) for weapon/item ACC stat blocks."""
    blocks: list[tuple[int, int, str]] = []
    i = 0
    while i < len(lines):
        if lines[i].strip().upper() != "ACC":
            i += 1
            continue
        start = i
        while start > 0 and is_allcaps_title(lines[start - 1]):
            start -= 1
        titles = [ln.strip() for ln in lines[start:i] if is_allcaps_title(ln)]
        if not titles:
            i += 1
            continue
        # Prefer the most specific multi-word product title over
        # subtype labels like SWORD / DAGGER / SHORT.
        multi = [t for t in titles if len(t.split()) > 1]
        name = max(multi, key=len) if multi else max(titles, key=len)
        end = i + 1
        saw_costish = False
        while end < len(lines):
            s = lines[end]
            if is_blank(s):
                # peek: trailing rules note after blank?
                if end + 1 < len(lines) and not is_statish(lines[end + 1]) and not is_allcaps_title(lines[end + 1]):
                    nxt = lines[end + 1].strip()
                    if (
                        saw_costish
                        and nxt
                        and nxt[0].isupper()
                        and nxt.endswith(".")
                        and len(nxt) < 160
                        and any(
                            k in nxt.lower()
                            for k in ("scabbard", "ready weapon")
                        )
                    ):
                        end += 2
                    break
                end += 1
                continue
            if is_stat_header(s) or is_statish(s):
                if "¥" in s or s.strip().upper() in {"COST", "AVAIL"}:
                    saw_costish = True
                end += 1
                continue
            if is_allcaps_title(s) or is_heading(s):
                break
            # trailing one-line rules note glued without blank
            st = s.strip()
            if (
                saw_costish
                and st
                and st[0].isupper()
                and st.endswith(".")
                and len(st) < 160
                and any(
                    k in st.lower()
                    for k in ("scabbard", "ready weapon")
                )
            ):
                end += 1
                break
            break
        blocks.append((start, end, name))
        i = end
    return blocks


GENERIC_STAT_LABELS = {
    "SHORT",
    "LONG",
    "SWORD",
    "DAGGER",
    "BELT",
    "BRACELET",
    "STANDARD",
    "HEAVY",
    "LIGHT",
    "MINI",
    "MICRO",
}


def relocate_misplaced_stat_blocks(lines: list[str]) -> list[str]:
    """Move ACC blocks that sit under the wrong item back to their title."""
    lines = move_misplaced_item_notes(lines)
    blocks = find_acc_blocks(lines)
    if not blocks:
        return lines

    moves: list[tuple[int, int, str, list[str]]] = []
    for start, end, name in blocks:
        # Subtype-only labels (SHORT/LONG/SWORD) must stay with their
        # parent item; moving them orphans stats at the chapter head.
        if normalize_name(name) in GENERIC_STAT_LABELS or len(name.split()) < 2:
            continue
        # Walk back past the block's own titles to the prior item title
        j = start - 1
        while j >= 0 and (is_blank(lines[j]) or is_allcaps_title(lines[j])):
            j -= 1
        prior_title = None
        k = j
        while k >= 0:
            if is_allcaps_title(lines[k]):
                prior_title = lines[k].strip()
                break
            if is_heading(lines[k]):
                break
            k -= 1
        if prior_title and names_match(prior_title, name):
            continue  # already under the right item
        moves.append((start, end, name, lines[start:end]))

    if not moves:
        return lines

    # Remove from the end so indices stay valid
    body = list(lines)
    extracted: list[tuple[str, list[str]]] = []
    for start, end, name, chunk in sorted(moves, key=lambda x: x[0], reverse=True):
        extracted.append((name, chunk))
        del body[start:end]

    # Insert after matching title section
    def item_end(ls: list[str], title_idx: int) -> int:
        for j in range(title_idx + 1, len(ls)):
            if is_item_title_line(ls[j]):
                return j
        return len(ls)

    for name, chunk in reversed(extracted):
        title_idx = None
        for i, ln in enumerate(body):
            if is_allcaps_title(ln) or ln.startswith("## ") or ln.startswith("### "):
                t = ln.lstrip("#").strip()
                if names_match(t, name):
                    title_idx = i
                    break
        if title_idx is None:
            if body and body[-1].strip():
                body.append("")
            body.extend(chunk)
            continue
        # Avoid duplicate if identical ACC already present in section
        end = item_end(body, title_idx)
        section = body[title_idx:end]
        if any(ln.strip().upper() == "ACC" for ln in section):
            continue
        insert_at = end
        # strip duplicate title lines from chunk
        cleaned_chunk = [
            ln
            for ln in chunk
            if not (is_allcaps_title(ln) and names_match(ln, name))
        ]
        while cleaned_chunk and not cleaned_chunk[0].strip():
            cleaned_chunk.pop(0)
        while cleaned_chunk and not cleaned_chunk[-1].strip():
            cleaned_chunk.pop()
        piece = []
        if insert_at > 0 and body[insert_at - 1].strip():
            piece.append("")
        piece.extend(cleaned_chunk)
        piece.append("")
        body[insert_at:insert_at] = piece

    # collapse blanks
    cleaned: list[str] = []
    blank = 0
    for ln in body:
        if not ln.strip():
            blank += 1
            if blank <= 2:
                cleaned.append("")
            continue
        blank = 0
        cleaned.append(ln)
    while cleaned and not cleaned[0].strip():
        cleaned.pop(0)
    while cleaned and not cleaned[-1].strip():
        cleaned.pop()
    return cleaned


def move_misplaced_item_notes(lines: list[str]) -> list[str]:
    """Move rules notes that clearly belong to a named item."""
    NOTE_OWNERS = [
        ("memory blade", "VICTORINOX MEMORY BLADE"),
    ]

    def item_end(ls: list[str], title_idx: int) -> int:
        for j in range(title_idx + 1, len(ls)):
            if is_item_title_line(ls[j]):
                return j
        return len(ls)

    body = list(lines)
    for needle, owner in NOTE_OWNERS:
        moves: list[int] = []
        for i, ln in enumerate(body):
            if needle in ln.lower() and not is_allcaps_title(ln):
                # skip if already under owner
                k = i - 1
                prior = None
                while k >= 0:
                    if is_allcaps_title(body[k]):
                        prior = body[k].strip()
                        break
                    if is_heading(body[k]):
                        break
                    k -= 1
                if prior and names_match(prior, owner):
                    continue
                moves.append(i)
        for i in reversed(moves):
            note = body.pop(i)
            title_idx = None
            for j, ln in enumerate(body):
                if is_allcaps_title(ln) and names_match(ln, owner):
                    title_idx = j
                    break
            if title_idx is None:
                body.append(note)
                continue
            insert_at = item_end(body, title_idx)
            if insert_at > 0 and body[insert_at - 1].strip():
                body.insert(insert_at, "")
                insert_at += 1
            body.insert(insert_at, note)
            body.insert(insert_at + 1, "")
    cleaned: list[str] = []
    blank = 0
    for ln in body:
        if not ln.strip():
            blank += 1
            if blank <= 2:
                cleaned.append("")
            continue
        blank = 0
        cleaned.append(ln)
    while cleaned and not cleaned[0].strip():
        cleaned.pop(0)
    while cleaned and not cleaned[-1].strip():
        cleaned.pop()
    return cleaned


def process_file(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines:
        return
    # keep header
    header: list[str] = []
    body_start = 0
    if lines[0].startswith("# "):
        header.append(lines[0])
        body_start = 1
        while body_start < len(lines) and not lines[body_start].strip():
            header.append(lines[body_start])
            body_start += 1
        if body_start < len(lines) and lines[body_start].startswith("**Source:**"):
            header.append(lines[body_start])
            body_start += 1
            header.append("")
            while body_start < len(lines) and not lines[body_start].strip():
                body_start += 1

    body = deinterleave(lines[body_start:])
    md = "\n".join(header + body).strip() + "\n"
    md = clean_em(md)
    path.write_text(md, encoding="utf-8")
    print("deinterleaved", path.name)


def main() -> None:
    targets = [
        "05 - Arsenal.md",
        "06 - Armor and Protection.md",
        "08 - Killshots and More.md",
    ]
    for name in targets:
        process_file(ROOT / name)


if __name__ == "__main__":
    main()
