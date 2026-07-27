# -*- coding: utf-8 -*-
"""Tighten formatters: only promote known headers, not every ALL CAPS line."""
from pathlib import Path
import re

EXTRACT = Path(r"c:\Users\admin\Desktop\Shadowrun\Source\_extract")
FILES = [
    "format_rigger5.py",
    "format_streetgrimoire.py",
    "format_forbiddenarcana.py",
    "format_runfaster.py",
    "format_streetlethal.py",
    "format_howlingshadows.py",
]

OLD = 'if s in KNOWN_HEADERS or (is_all_caps_title(s) and s.count(" ") <= 8):'
NEW = 'if s in KNOWN_HEADERS:'

for fname in FILES:
    p = EXTRACT / fname
    t = p.read_text(encoding="utf-8")
    if OLD not in t:
        print("pattern missing", fname)
        continue
    t = t.replace(OLD, NEW)
    # Also: when collecting caps runs under known headers only - the branch after
    # "if s in KNOWN_HEADERS: paras.append..." should not collect random caps.
    # Remove the fallback ALL CAPS place-title merge after known headers if present.
    t2 = re.sub(
        r"\n            # Place / subsection titles: merge consecutive ALL CAPS\n"
        r"            end_i, merged = collect_caps_run\(lines, i, s\)\n"
        r"            # Drop if merged is only a skip fragment\n"
        r"            if merged\.upper\(\) in SKIP_EXACT:\n"
        r"                i = end_i \+ 1\n"
        r"                continue\n"
        r"            paras\.append\(f\"## \{title_case_header\(merged\)\}\"\)\n"
        r"            i = end_i \+ 1\n"
        r"            continue\n",
        "\n            # Unknown ALL CAPS: keep as prose, do not promote to H2\n"
        "            buf.append(s)\n"
        "            i += 1\n"
        "            continue\n",
        t,
    )
    if t2 == t:
        # maybe already different structure; just write known-header tighten
        print("caps-run block not rewritten", fname)
    p.write_text(t2 if t2 != t else t, encoding="utf-8")
    print("patched", fname)
