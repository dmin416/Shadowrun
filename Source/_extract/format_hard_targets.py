# -*- coding: utf-8 -*-
"""Formatting pass for Hard Targets Source Texts chapters."""
from __future__ import annotations

import re
from pathlib import Path

import fitz

OUT = Path(r"c:\Users\admin\Desktop\Shadowrun\Source Texts\Hard Targets")
PDF = Path(r"c:\Users\admin\Desktop\Shadowrun\Source\PDF\Shadowrun_5E_Hard_Targets.pdf")
SKIP = {"INDEX.md"}

DASHES = (("\u2014", "-"), ("\u2013", "-"), ("—", "-"), ("–", "-"), ("\u2026", "..."))

BASE_H2: dict[str, str] = {
    "introduction": "Introduction",
    "jackpoint": "JackPoint",
    "justice for hire": "Justice for Hire",
    "desperate times": "Desperate Times",
    "...and desperate measures": "...And Desperate Measures",
    "and desperate measures": "...And Desperate Measures",
    "killers, saviors, and hunters": "Killers, Saviors, and Hunters",
    "slow and steady death": "Slow and Steady Death",
    "havana: dale a todo meter!": "Havana: Dale A Todo Meter!",
    "chameleon": "Chameleon",
    "becoming death": "Becoming Death",
    "the wetwork toolkit": "The Wetwork Toolkit",
    "game information": "Game Information",
    "on the line": "On the Line",
    "cfd": "CFD",
    "in the crosshairs": "In the Crosshairs",
    "neutral ground": "Neutral Ground",
    "hiring meatshields": "Hiring Meatshields",
    "hiring hitmen": "Hiring Hitmen",
    "hiring dupes": "Hiring Dupes",
    "who's who in the murder world": "Who's Who in the Murder World",
    "brief history of cuba": "Brief History of Cuba",
    "havana": "Havana",
    "a workman is only as good as his tools": "A Workman Is Only as Good as His Tools",
    "wetwork and teamwork": "Wetwork and Teamwork",
    "credits": "Credits",
    "table of contents": "Table of Contents",
}

JP_HANDLE_KEYS = {
    "riser", "sticks", "bull", "netcat", "slamm-0!", "slamm-0", "glitch",
    "clockwork", "kane", "pirate", "/dev/grrl", "dev/grrl", "butch",
    "sounder", "snopes", "2xl", "orkce0", "blackwing", "tortuga",
}


def clean_dashes(s: str) -> str:
    for a, b in DASHES:
        s = s.replace(a, b)
    return s


def norm_key(s: str) -> str:
    s = s.lower().strip()
    s = s.replace(""", '"').replace(""", '"').replace("'", "'")
    s = s.replace("…", "...").replace("\u2026", "...")
    s = re.sub(r"\s+", " ", s)
    return s


def toc_h2_map() -> dict[str, str]:
    out = dict(BASE_H2)
    try:
        doc = fitz.open(str(PDF))
        for lvl, title, _page in doc.get_toc() or []:
            if lvl > 2:
                continue
            title = clean_dashes(re.sub(r"\s+", " ", title)).strip()
            if not title or title.lower().startswith("shadowrun:"):
                continue
            out[norm_key(title)] = title
            out[norm_key(title.rstrip("."))] = title
        # Also scrape TOC text from early pages for subsection titles
        for i in range(2, 4):
            text = doc[i].get_text("text") or ""
            for ln in text.splitlines():
                s = clean_dashes(ln.strip())
                if not s or re.match(r"^\d+$", s):
                    continue
                # "Looking at a Lockdown" style lines before a page number line
                if re.match(r"^[A-Z(].{3,60}$", s) and not s.isupper() or (
                    s[:1].isupper() and len(s.split()) <= 10 and not s.endswith(".")
                ):
                    if re.search(r"\d{2,3}\s*$", s):
                        s = re.sub(r"\s+\d+\s*$", "", s).strip()
                    if 3 <= len(s) <= 70 and not re.match(r"^\d", s):
                        out.setdefault(norm_key(s), s)
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
    if is_mostly_upper(s):
        return True
    words = [w for w in re.split(r"\s+", s) if w]
    if 2 <= len(words) <= 12 and not s.endswith("."):
        caps = sum(1 for w in words if w[:1].isupper())
        if caps >= len(words) - 1:
            return True
    return False


def looks_like_jp_handle(t: str) -> bool:
    t = t.strip()
    if not t or t.startswith("#") or t.startswith(">") or t.endswith("."):
        return False
    if len(t) > 40 or len(t.split()) > 4:
        return False
    if not re.match(r"^[/A-Z0-9][\w .'!\"/-]*$", t):
        return False
    if is_mostly_upper(t) and len(t.split()) >= 2:
        return False
    return True


def fix_soft_hyphens(text: str) -> str:
    text = re.sub(r"([A-Za-z]{2,})-\s*\n\s*([A-Za-z]{2,})", r"\1\2", text)
    text = re.sub(r"([A-Za-z]{2,})-\s+([a-z]{2,})", r"\1\2", text)
    return text


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
                if re.match(r"^>\s*[A-Za-z0-9/]", t) and len(t) < 55:
                    break
                if looks_like_jp_handle(t):
                    break
                if t.startswith("##"):
                    break
                chunk.append(t)
                i += 1
            body = " ".join(c for c in chunk if c)
            handle = ""
            if i < len(lines):
                t = lines[i].strip()
                if re.match(r"^>\s*[A-Za-z0-9/]", t) and len(t) < 55:
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
    chapter_keys = {
        norm_key(chapter_title),
        norm_key(chapter_title.rstrip(".")),
        norm_key(chapter_title.replace("...", "")),
    }
    skip_headings = fname.startswith("01 -") or fname.startswith("02 -")

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
            key2 = norm_key(s.rstrip(".").rstrip("!"))
            if key in chapter_keys or key2 in chapter_keys:
                continue
            matched = key if key in h2 else (key2 if key2 in h2 else "")
            if matched:
                if matched in JP_HANDLE_KEYS and not is_mostly_upper(s):
                    pass
                else:
                    flush()
                    blocks.append(f"## {h2[matched]}")
                    continue

        if not skip_headings and looks_like_jp_handle(s):
            key = norm_key(s)
            if key in h2 and key not in JP_HANDLE_KEYS:
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
        chapter = raw.splitlines()[0][2:].strip() if raw.startswith("# ") else ""
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
