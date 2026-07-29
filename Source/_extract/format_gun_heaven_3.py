# -*- coding: utf-8 -*-
"""Formatting pass for Gun Heaven 3 Source Texts chapters."""
from __future__ import annotations

import re
from pathlib import Path

OUT = Path(r"c:\Users\admin\Desktop\Shadowrun\Source Texts\Gun Heaven 3")
SKIP = {"INDEX.md"}

DASHES = (("\u2014", "-"), ("\u2013", "-"), ("—", "-"), ("–", "-"))

SECTION_H2 = {
    "vintage",
    "cap & ball",
    "weapons accessories and modifications",
    "sporting rifles",
    "flamethrowers",
    "shadowrun, fifth edition",
    "shadowrun, twentieth anniversary edition",
    "jackpoint stats",
    "latest news",
    "personal alerts",
    "first degree",
    "today's heads up",
    "incoming",
    "top news items",
    "standard upgrades/accessories",
    "standard upgrades/accessories: none",
}

TABLE_HEADERS = {
    "gun",
    "acc",
    "dam",
    "ap",
    "mode",
    "rc",
    "ammo",
    "avail",
    "cost",
}

JUNK = re.compile(
    r"^(?:"
    r">>\s*SHADOWRUN\s*<<"
    r"|<<\s*GUN\s*H\(E\)AVEN\s*3.*"
    r"|GUN\s*H\(E\)AVEN\s*3\s+\d+"
    r"|GUN H\(E\)AVEN 3 STATS \(SR5\)"
    r"|GUN H\(E\)AVEN 3 STATS \(SR4A\)"
    r")$",
    re.I,
)

WEAPON_TYPE = re.compile(
    r"^\((HOLDOUT PISTOL|LIGHT PISTOL|HEAVY PISTOL|MACHINE PISTOL|"
    r"SUBMACHINE GUN|ASSAULT RIFLE|SHOTGUN|SPORTING RIFLE|"
    r"LIGHT MACHINE GUN|ASSAULT CANNON|FLAMETHROWER)\)\s*$",
    re.I,
)


def clean_dashes(s: str) -> str:
    for a, b in DASHES:
        s = s.replace(a, b)
    return s


def title_case(s: str) -> str:
    small = {"a", "an", "the", "and", "or", "of", "in", "on", "for", "to", "with"}
    keep = {"SR5", "SR4A", "UCAS", "FA", "BF", "SA", "SS", "RC", "AP", "DV"}
    words = s.split()
    out: list[str] = []
    for i, w in enumerate(words):
        bare = w.strip("():")
        if bare.upper() in keep:
            out.append(bare.upper())
            continue
        lw = bare.lower()
        if i > 0 and lw in small:
            out.append(lw)
        else:
            out.append(bare[:1].upper() + bare[1:].lower() if bare else bare)
    return " ".join(out)


def fix_soft_hyphens(text: str) -> str:
    text = re.sub(r"([A-Za-z]{2,})-\s*\n\s*([a-z]{2,})", r"\1\2", text)
    text = re.sub(r"([A-Za-z]{2,})-\s+([a-z]{2,})", r"\1\2", text)
    return text


def is_statish(s: str) -> bool:
    t = s.strip()
    if not t:
        return False
    if t.lower() in TABLE_HEADERS:
        return True
    if re.match(r"^[\d.,+\-()/¥RFAPSxXL]+\s*$", t):
        return True
    if "¥" in t:
        return True
    if re.match(r"^\d+[PRF]\b", t):
        return True
    if re.match(r"^\(?\d+\)?[CPBDMYML]+", t, re.I):
        return True
    return False


def is_handle(s: str) -> bool:
    t = s.strip().lstrip(">").strip()
    if not t or len(t) > 40:
        return False
    if t.endswith(".") or t.endswith("?"):
        return False
    words = t.split()
    if len(words) > 4:
        return False
    return True


def reflow_prose(lines: list[str]) -> str:
    if not lines:
        return ""
    paras: list[str] = []
    buf = lines[0].strip()
    for line in lines[1:]:
        s = line.strip()
        if not s:
            continue
        if buf.endswith("-") and s and s[0].islower():
            buf = buf[:-1] + s
            continue
        if re.search(r'[.!?]"?$', buf) and (s[0].isupper() or s[0] in "\"'>"):
            paras.append(buf)
            buf = s
            continue
        buf = buf + " " + s
    if buf:
        paras.append(buf)
    return "\n\n".join(paras)


def format_jp(lines: list[str]) -> list[str]:
    """Convert orphan '>' comment blocks into markdown quotes + handles."""
    out: list[str] = []
    i = 0
    while i < len(lines):
        s = lines[i].strip()
        if s != ">":
            out.append(lines[i])
            i += 1
            continue
        chunk: list[str] = []
        i += 1
        while i < len(lines):
            t = lines[i].strip()
            if t == ">":
                break
            if t.startswith("##") or t.startswith("###"):
                break
            if is_handle(t) and not t.startswith("Standard"):
                # peek: if next is blank or another > or heading, treat as handle
                break
            chunk.append(t)
            i += 1
        body = " ".join(c for c in chunk if c)
        handle = ""
        if i < len(lines) and is_handle(lines[i].strip()):
            handle = lines[i].strip().lstrip(">").strip()
            i += 1
        if body:
            out.append("> " + body)
        if handle:
            out.append("> **" + handle.lstrip(">").strip() + "**")
        continue
    return out


def format_stats_table(lines: list[str], sr5: bool) -> str:
    """Build a markdown table from column-per-line dump when possible."""
    # Keep as structured lines with ## headers; full table rebuild is fragile
    # because ammo wraps. Prefer readable labeled blocks after header row.
    text = "\n".join(lines)
    return text


def format_body(body: str, fname: str) -> str:
    body = clean_dashes(body)
    body = fix_soft_hyphens(body)
    raw = [ln.rstrip() for ln in body.splitlines()]

    blocks: list[str] = []
    prose: list[str] = []
    stats_mode = False
    stats_buf: list[str] = []

    def flush_prose() -> None:
        nonlocal prose
        if prose:
            blocks.append(reflow_prose(prose))
            prose = []

    def flush_stats() -> None:
        nonlocal stats_buf, stats_mode
        if stats_buf:
            blocks.append("\n".join(stats_buf))
            stats_buf = []
        stats_mode = False

    i = 0
    while i < len(raw):
        s = raw[i].strip()
        if not s:
            if not stats_mode:
                flush_prose()
            i += 1
            continue
        if JUNK.match(s):
            i += 1
            continue

        key = s.lower().rstrip(":")
        if key in SECTION_H2 or key.startswith("standard upgrades"):
            flush_stats()
            flush_prose()
            if key.startswith("shadowrun, fifth"):
                blocks.append("## Shadowrun, Fifth Edition")
                stats_mode = True
                i += 1
                continue
            if key.startswith("shadowrun, twentieth"):
                blocks.append("## Shadowrun, Twentieth Anniversary Edition")
                stats_mode = True
                i += 1
                continue
            if key.startswith("standard upgrades"):
                blocks.append("## Standard Upgrades/Accessories")
                rest = s.split(":", 1)
                if len(rest) == 2 and rest[1].strip():
                    blocks.append(rest[1].strip())
                i += 1
                continue
            blocks.append(f"## {title_case(s)}")
            i += 1
            continue

        if WEAPON_TYPE.match(s):
            flush_stats()
            flush_prose()
            blocks.append(f"**{s}**")
            i += 1
            continue

        if s == ">" or (s.startswith(">") and len(s) <= 2):
            flush_stats()
            flush_prose()
            # PDF JackPoint: > \n comment \n > \n Handle
            i += 1
            chunk: list[str] = []
            while i < len(raw) and raw[i].strip() != ">":
                t = raw[i].strip()
                if t.startswith("##") or WEAPON_TYPE.match(t):
                    break
                if t:
                    chunk.append(t)
                i += 1
            if i < len(raw) and raw[i].strip() == ">":
                i += 1
            while i < len(raw) and not raw[i].strip():
                i += 1
            handle = ""
            if i < len(raw) and is_handle(raw[i]) and not raw[i].strip().startswith("##"):
                handle = raw[i].strip().lstrip(">").strip()
                i += 1
            body_c = " ".join(chunk)
            if body_c:
                blocks.append("> " + body_c)
            if handle:
                blocks.append("> **" + handle + "**")
            continue

        if s.lower() in TABLE_HEADERS or (stats_mode and is_statish(s)):
            flush_prose()
            stats_mode = True
            stats_buf.append(s)
            i += 1
            continue

        if stats_mode and not is_statish(s):
            flush_stats()

        prose.append(s)
        i += 1

    flush_stats()
    flush_prose()

    text = "\n\n".join(blocks)
    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"

    if "Gun Stats" in fname:
        text = format_stats_page(text, "SR5" in fname)

    return clean_dashes(text)


def format_stats_page(text: str, sr5: bool) -> str:
    """Turn column dump into markdown table rows when columns align."""
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    # Find header markers
    try:
        gun_i = next(i for i, ln in enumerate(lines) if ln.upper() == "GUN")
    except StopIteration:
        return text

    headers = []
    i = gun_i
    while i < len(lines) and lines[i].upper() in {
        "GUN", "ACC", "DAM", "AP", "MODE", "RC", "AMMO", "AVAIL", "COST"
    }:
        headers.append(lines[i].upper())
        i += 1

    if "GUN" not in headers or "COST" not in headers:
        return text

    ncols = len(headers)
    cells = lines[i:]
    # Ammo sometimes wraps "50(D) OR" / "100(BELT)" - join those
    joined: list[str] = []
    j = 0
    while j < len(cells):
        c = cells[j]
        if c.endswith(" OR") and j + 1 < len(cells):
            joined.append(c + " " + cells[j + 1])
            j += 2
            continue
        joined.append(c)
        j += 1

    if len(joined) % ncols != 0:
        # leave raw if can't align cleanly
        return text

    rows = []
    for r in range(0, len(joined), ncols):
        rows.append(joined[r : r + ncols])

    out = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * ncols) + " |",
    ]
    for row in rows:
        out.append("| " + " | ".join(row) + " |")
    return "\n".join(out) + "\n"


def split_header(text: str) -> tuple[str, str]:
    lines = text.splitlines()
    if not lines:
        return "", ""
    header: list[str] = []
    i = 0
    if lines[0].startswith("# "):
        header.append(lines[0])
        i = 1
        while i < len(lines) and not lines[i].strip():
            header.append(lines[i])
            i += 1
        if i < len(lines) and lines[i].startswith("**Source:**"):
            header.append(lines[i])
            i += 1
            while i < len(lines) and not lines[i].strip():
                header.append(lines[i])
                i += 1
    return "\n".join(header).rstrip() + "\n\n", "\n".join(lines[i:])


def main() -> None:
    for path in sorted(OUT.glob("*.md")):
        if path.name in SKIP:
            continue
        raw = path.read_text(encoding="utf-8")
        header, body = split_header(raw)
        formatted = format_body(body, path.name)
        path.write_text(clean_dashes(header + formatted), encoding="utf-8")
        print("formatted", path.name, "bytes", path.stat().st_size)

    idx = OUT / "INDEX.md"
    if idx.exists():
        t = idx.read_text(encoding="utf-8")
        t = t.replace("- [ ] Format", "- [x] Format")
        idx.write_text(clean_dashes(t), encoding="utf-8")


if __name__ == "__main__":
    main()
