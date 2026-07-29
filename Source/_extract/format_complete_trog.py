# -*- coding: utf-8 -*-
"""Formatting pass for The Complete Trog Source Texts chapters."""
from __future__ import annotations

import re
from pathlib import Path

import fitz

OUT = Path(r"c:\Users\admin\Desktop\Shadowrun\Source Texts\Complete Trog")
PDF = Path(r"c:\Users\admin\Desktop\Shadowrun\Source\PDF\completetrog.pdf")
SKIP = {"INDEX.md"}

DASHES = (("\u2014", "-"), ("\u2013", "-"), ("—", "-"), ("–", "-"))

# Always-available chapter-level / rules H2s
BASE_H2: dict[str, str] = {
    "contents & credits": "Contents & Credits",
    "introduction": "Introduction",
    "jackpoint": "JackPoint",
    "belinda": "Belinda",
    "what are you?": "What Are You?",
    "living as a trog in...": "Living as a Trog In...",
    "true blue trog": "True Blue Trog",
    "working as a trog in...": "Working As a Trog In...",
    "trog heroes": "Trog Heroes",
    "trog enemies": "Trog Enemies",
    "trog runners": "Trog Runners",
    "united we stomp": "United We Stomp",
    "everything trog": "Everything Trog",
    "gear": "Gear",
    "qualities": "Qualities",
    "life modules": "Life Modules",
    "making a trog runner": "Making a Trog Runner",
    "shadowrun: anarchy trog characters": "Shadowrun: Anarchy Trog Characters",
    "or'zet glossary": "Or'zet Glossary",
    "a call to arms": "A Call to Arms",
    # local subsection banners not always in PDF TOC
    "breeding of a kingdom": "Breeding of a Kingdom",
    "troll politics": "Troll Politics",
    "the troll thing": "The Troll Thing",
    "shadows of freiburg": "Shadows of Freiburg",
    "the awakened black forest": "The Awakened Black Forest",
    "positive qualities": "Positive Qualities",
    "negative qualities": "Negative Qualities",
    "formative years": "Formative Years",
    "teen years": "Teen Years",
    "further education": "Further Education",
    "real life": "Real Life",
}


def clean_dashes(s: str) -> str:
    for a, b in DASHES:
        s = s.replace(a, b)
    return s


def norm_key(s: str) -> str:
    s = s.lower().strip()
    s = s.replace(""", '"').replace(""", '"').replace("'", "'")
    s = re.sub(r"\s+", " ", s)
    s = s.replace("�", "...")
    return s


def toc_h2_map() -> dict[str, str]:
    """Build H2 whitelist from PDF TOC (level 1-2)."""
    out = dict(BASE_H2)
    try:
        doc = fitz.open(str(PDF))
        for lvl, title, _page in doc.get_toc() or []:
            if lvl > 2:
                continue
            title = clean_dashes(re.sub(r"\s+", " ", title)).strip()
            if not title or title.lower().startswith("shadowrun:"):
                continue
            # display: keep reasonable casing from TOC
            key = norm_key(title)
            # TOC already title-ish
            out[key] = title
            # also without trailing ellipsis variants
            out[norm_key(title.rstrip("."))] = title
        doc.close()
    except Exception as exc:  # noqa: BLE001
        print("TOC load warning:", exc)
    return out


def is_mostly_upper(line: str) -> bool:
    letters = [c for c in line if c.isalpha()]
    if len(letters) < 3:
        return False
    return sum(1 for c in letters if c.isupper()) / len(letters) >= 0.85


def is_heading_candidate(line: str) -> bool:
    s = line.strip()
    if not s or len(s) > 90:
        return False
    if s.startswith("#") or s.startswith(">") or s.startswith("**") or s.startswith("|"):
        return False
    if s.upper().startswith("POSTED BY"):
        return False
    if re.match(r"^\d", s):
        return False
    letters = [c for c in s if c.isalpha()]
    if len(letters) < 3:
        return False
    # Prefer ALL CAPS banners. Title Case only for multi-word TOC hits.
    if is_mostly_upper(s):
        return True
    words = [w for w in re.split(r"\s+", s) if w]
    if len(words) >= 2 and len(words) <= 12 and not s.endswith("."):
        caps = sum(1 for w in words if w[:1].isupper())
        if caps >= len(words) - 1:
            return True
    return False


# Single-token TOC entries that are also JackPoint handles / names.
# Only promote these when the PDF line is ALL CAPS (profile section banners).
JP_HANDLE_KEYS = {
    "2xl",
    "clockwork",
    "snopes",
    "butch",
    "sounder",
    "sunshine",
    "beaker",
    "netcat",
    "slamm-0!",
    "slamm-0",
}


def fix_soft_hyphens(text: str) -> str:
    text = re.sub(r"([A-Za-z]{2,})-\s*\n\s*([A-Za-z]{2,})", r"\1\2", text)
    text = re.sub(r"([A-Za-z]{2,})-\s+([a-z]{2,})", r"\1\2", text)
    return text


def join_known_multiline(text: str, h2: dict[str, str]) -> str:
    text = re.sub(
        r"(?im)^THE BLACK FOREST\s*\nTROLL REPUBLIC\s*$",
        "THE BLACK FOREST TROLL REPUBLIC",
        text,
    )
    text = re.sub(
        r"(?im)^THE AWAKENED\s*\nBLACK FOREST\s*$",
        "THE AWAKENED BLACK FOREST",
        text,
    )
    text = re.sub(
        r"(?im)^ATLANTA\s*[.\u2026]*\s*\nKINDA SORTA\s*$",
        "ATLANTA ... KINDA SORTA",
        text,
    )
    text = re.sub(
        r"(?im)^KINGDOMS OF NIGERIA AND\s*\nTHE CONGO TRIBAL LANDS\s*$",
        "KINGDOMS OF NIGERIA AND THE CONGO TRIBAL LANDS",
        text,
    )
    text = re.sub(
        r"(?im)^KINGDOMS OF\s*\nNIGERIA AND\s*\nTHE CONGO\s*\nTRIBAL LANDS\s*$",
        "KINGDOMS OF NIGERIA AND THE CONGO TRIBAL LANDS",
        text,
    )
    text = re.sub(
        r"(?im)^YAKUT'A TOLD ME THIS PLACE WAS SO COLD\s*$",
        "YAKUT'A TOLD ME THIS PLACE WAS SO COLD",
        text,
    )
    text = re.sub(
        r"(?im)^YAKUT'A TOLD\s*\nME THIS PLACE\s*\nWAS SO COLD\s*$",
        "YAKUT'A TOLD ME THIS PLACE WAS SO COLD",
        text,
    )
    # Join 2-4 consecutive ALL CAPS short lines when combo matches TOC
    lines = text.splitlines()
    out: list[str] = []
    i = 0
    while i < len(lines):
        cur = lines[i].strip()
        if cur and is_mostly_upper(cur):
            parts = [cur]
            j = i + 1
            matched_at = -1
            while j < len(lines) and len(parts) < 4:
                nxt = lines[j].strip()
                if not nxt or not is_mostly_upper(nxt):
                    break
                parts.append(nxt)
                combo = " ".join(parts)
                if norm_key(combo) in h2:
                    matched_at = j
                    break
                j += 1
            if matched_at >= 0:
                out.append(" ".join(parts))
                i = matched_at + 1
                continue
        out.append(lines[i])
        i += 1
    return "\n".join(out)


def reflow_prose(lines: list[str]) -> str:
    if not lines:
        return ""
    paras: list[str] = []
    buf = lines[0].strip()
    for line in lines[1:]:
        s = line.strip()
        if not s:
            continue
        if buf.endswith("-") and s and s[0].isalpha():
            buf = buf[:-1] + s
            continue
        if s.startswith("*") or s.upper().startswith("POSTED BY"):
            if buf:
                paras.append(buf)
            buf = s
            continue
        if re.search(r'[.!?]"?$', buf) and (s[0].isupper() or s[0] in "\"'>"):
            paras.append(buf)
            buf = s
            continue
        buf = buf + " " + s
    if buf:
        paras.append(buf)
    return "\n\n".join(paras)


def looks_like_jp_handle(t: str) -> bool:
    t = t.strip()
    if not t or t.startswith("#") or t.startswith(">") or t.endswith("."):
        return False
    if len(t) > 45 or len(t.split()) > 5:
        return False
    if not re.match(r"^[A-Z0-9][\w .'!\"-]*$", t):
        return False
    # avoid ALL CAPS section banners
    if is_mostly_upper(t) and len(t.split()) >= 2:
        return False
    return True


def format_jp_blocks(lines: list[str]) -> list[str]:
    out: list[str] = []
    i = 0
    while i < len(lines):
        s = lines[i].strip()
        if s == ">":
            chunk: list[str] = []
            i += 1
            while i < len(lines):
                t = lines[i].strip()
                if not t:
                    i += 1
                    continue
                if t == ">":
                    break
                if re.match(r"^>\s*[A-Za-z0-9]", t) and len(t) < 55:
                    break
                if looks_like_jp_handle(t):
                    break
                if t.startswith("##") or t.startswith("###"):
                    break
                chunk.append(t)
                i += 1
            body = " ".join(c for c in chunk if c)
            handle = ""
            if i < len(lines):
                t = lines[i].strip()
                if re.match(r"^>\s*[A-Za-z0-9]", t) and len(t) < 55:
                    handle = t if t.startswith(">") else "> " + t
                    i += 1
                elif looks_like_jp_handle(t):
                    handle = "> " + t
                    i += 1
            if body:
                out.append("> " + body)
            if handle:
                out.append(handle)
            continue
        out.append(lines[i])
        i += 1
    return out


def format_body(
    body: str, h2: dict[str, str], chapter_title: str = "", fname: str = ""
) -> str:
    body = clean_dashes(body)
    body = fix_soft_hyphens(body)
    body = join_known_multiline(body, h2)
    chapter_keys = {
        norm_key(chapter_title),
        norm_key(chapter_title.rstrip(".")),
        norm_key(chapter_title.replace("...", "")),
    }
    # Contents pages list every TOC title; do not promote those lines to H2.
    skip_headings = fname.startswith("01 -")
    # Character-sheet labels that collide with Everything Trog TOC entries
    sheet_labels = {"qualities", "gear"}
    allow_sheet_labels = fname.startswith("13 -")

    raw_lines = [ln.rstrip() for ln in body.splitlines()]
    blocks: list[str] = []
    prose_buf: list[str] = []

    def flush() -> None:
        nonlocal prose_buf
        if prose_buf:
            blocks.append(reflow_prose(prose_buf))
            prose_buf = []

    for ln in raw_lines:
        s = ln.strip()
        if not s:
            flush()
            continue
        if s.startswith(">") or s == ">":
            flush()
            blocks.append(s)
            continue
        if s.upper().startswith("POSTED BY"):
            flush()
            blocks.append(f"**{s}**")
            continue

        if not skip_headings and is_heading_candidate(s):
            key = norm_key(s)
            key2 = norm_key(s.rstrip("."))
            if key in chapter_keys or key2 in chapter_keys:
                continue
            matched = key if key in h2 else (key2 if key2 in h2 else "")
            if matched:
                if matched in sheet_labels and not allow_sheet_labels:
                    prose_buf.append(s)
                    continue
                if matched in JP_HANDLE_KEYS and not is_mostly_upper(s):
                    pass
                else:
                    flush()
                    blocks.append(f"## {h2[matched]}")
                    continue

        # Bare JackPoint handles (after TOC heading check so Dubai etc. win)
        if not skip_headings and looks_like_jp_handle(s):
            key = norm_key(s)
            if key in h2 and key not in JP_HANDLE_KEYS and (
                key not in sheet_labels or allow_sheet_labels
            ):
                flush()
                blocks.append(f"## {h2[key]}")
                continue
            flush()
            blocks.append("> " + s)
            continue

        prose_buf.append(s)

    flush()

    expanded: list[str] = []
    for b in blocks:
        expanded.extend(b.splitlines() if b else [])
        expanded.append("")
    fixed = format_jp_blocks([ln for ln in expanded])
    text = "\n".join(fixed)
    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"
    return clean_dashes(text)


def split_header(text: str) -> tuple[str, str]:
    lines = text.splitlines()
    if not lines:
        return "", ""
    header_lines: list[str] = []
    i = 0
    if lines[0].startswith("# "):
        header_lines.append(lines[0])
        i = 1
        while i < len(lines) and not lines[i].strip():
            header_lines.append(lines[i])
            i += 1
        if i < len(lines) and lines[i].startswith("**Source:**"):
            header_lines.append(lines[i])
            i += 1
            while i < len(lines) and not lines[i].strip():
                header_lines.append(lines[i])
                i += 1
    header = "\n".join(header_lines).rstrip() + "\n\n"
    return header, "\n".join(lines[i:])


def main() -> None:
    h2 = toc_h2_map()
    print("H2 keys", len(h2))
    for path in sorted(OUT.glob("*.md")):
        if path.name in SKIP:
            continue
        raw = path.read_text(encoding="utf-8")
        header, body = split_header(raw)
        chapter = ""
        if raw.startswith("# "):
            chapter = raw.splitlines()[0][2:].strip()
        formatted = format_body(body, h2, chapter_title=chapter, fname=path.name)
        path.write_text(clean_dashes(header + formatted), encoding="utf-8")
        print("formatted", path.name, "bytes", path.stat().st_size)

    idx = OUT / "INDEX.md"
    if idx.exists():
        t = idx.read_text(encoding="utf-8")
        t = t.replace("- [ ] Format", "- [x] Format")
        idx.write_text(clean_dashes(t), encoding="utf-8")


if __name__ == "__main__":
    main()
