# Completed (audited)

Re-checked against the files themselves on 2026-07-26. Prior “perfectly completed” claims were too optimistic. This file only keeps what survived a substance audit.

**Error fixes applied the same day:**
- Replaced 443 em/en dashes in Encyclopedia + Mechanics with ASCII `-` (workspace rule)
- Recovered Forbidden Arcana chapters (git HEAD had empty stubs; working tree was wiped by checkout; re-extracted + reformatted from PDF)
- Promoted Magic Mastery quality headings (`### Adept Healer`, etc.)
- Clarified Serrated Edge image-only map stubs

**Method:** file size / table-or-entry density; Mechanics Inventory checklists; Core quality-name spot check; Source Texts INDEX pipeline flags; Run & Gun chapter report; `qa_six_books.py` re-run; Encyclopedia UNVERIFIED / no-local-PDF callout scan; Serrated Edge per-chapter char counts.

---

## Verified: Mechanics pages

These have full Inventory scope closed (checkbox or prose inventory), Schema, and substantial tables/rules body. Safe to treat as done for their stated scope.

### Core resolution

- [Dice and Tests](Mechanics/Dice%20and%20Tests.md)
- [Edge](Mechanics/Edge.md)

### Character Creation (entire tree)

- [Overview](Mechanics/Character%20Creation/Overview.md)
- [Priority System](Mechanics/Character%20Creation/Priority%20System.md)
- [Metatype](Mechanics/Character%20Creation/Metatype.md)
- [Attributes](Mechanics/Character%20Creation/Attributes.md)
- [Magic and Resonance](Mechanics/Character%20Creation/Magic%20and%20Resonance.md)
- [Skills](Mechanics/Character%20Creation/Skills.md)
- [Resources and Gear](Mechanics/Character%20Creation/Resources%20and%20Gear.md)
- [Qualities](Mechanics/Character%20Creation/Qualities.md) (Core Positive/Negative tables present; e.g. Double-Jointed, Low Pain Tolerance)
- [Contacts](Mechanics/Character%20Creation/Contacts.md)
- [Finishing Touches](Mechanics/Character%20Creation/Finishing%20Touches.md)

Note: Finishing Touches still has unchecked boxes under **Sheet checklist (must pass)**. Those are player-facing chargen checks, not unfinished Inventory work.

### Combat (these three pages only)

- [Overview](Mechanics/Combat/Overview.md)
- [Initiative](Mechanics/Combat/Initiative.md)
- [Action Economy](Mechanics/Combat/Action%20Economy.md) (Free/Simple/Complex/Interrupt tables present)

Sibling Combat pages (Ranged, Melee, Damage, Movement, Surprise, Called Shots) are **not** done.

---

## Verified: Source Texts (full pipeline)

Extract + format + loss-check + done-check. Re-validated where a report/script exists.

| Book | Evidence | Caveat |
| --- | --- | --- |
| [Run & Gun](Source%20Texts/Run%20and%20Gun/) | INDEX all `[x]`; `Source/_extract/rng_chapter_check_report.md` all chapters PASS | Residual format polish possible (caption interleave); not content loss |
| [Rigger 5](Source%20Texts/Rigger%205/) | `qa_six_books.py` PASS | |
| [Street Grimoire](Source%20Texts/Street%20Grimoire/) | `qa_six_books.py` PASS | |
| [Run Faster](Source%20Texts/Run%20Faster/) | `qa_six_books.py` PASS | INDEX phantoms noted in book INDEX |
| [Street Lethal](Source%20Texts/Street%20Lethal/) | `qa_six_books.py` PASS | |
| [Howling Shadows](Source%20Texts/Howling%20Shadows/) | `qa_six_books.py` PASS | |
| [Forbidden Arcana](Source%20Texts/Forbidden%20Arcana/) | Re-extracted + reformatted; `qa_six_books.py` PASS; Magic Mastery qualities are `###` headings | Tradition subsection labels are dense `##`; residual running-header glue may remain in a few prose blocks |

---

## Demoted: not “perfect”

### Encyclopedia catalogs

**Demoted from perfect.** Catalogs are large and usable, but many files still contain `UNVERIFIED` / `no local PDF` rows or print-conflict notes. That is filled-with-gaps, not PDF-perfect. Em/en dashes in these files were fixed.

Highest gap density in this audit:

- Projectile Weapons (~17 callouts; Hard Targets PDF missing)
- Ammunition, Armor / Armor Mods, Cyberware, Bioware (HT / no-PDF rows)
- Drones (e.g. Dustoff secondary reprint)
- Vehicles (HT* table-only notes)

Treat Encyclopedia as **catalog complete for available PDFs**, not as fully verified against every cited book.

### Serrated Edge

**Demoted from perfect.** Adventure scenes + GM brief are substantial, and INDEX marks extract/format/brief/gear audit done, but:

- No formal PDF loss-check like RnG / six-book QA
- Map chapters are intentionally image-only stubs (caption/notes only); open the PDF for the art

### Removed / never verified

- Separate “Qualities Reference” line (duplicate of Qualities.md; nothing extra to audit)
- Claim that Encyclopedia setup alone equals perfect catalogs

---

## Still open

- Living the Shadows + Matrix/Magic/Rigging Basics Mechanics
- Encyclopedia polish (cross-links, source tags, layout)
- Seattle Sprawl done-check
- Chrome Flesh and other incomplete Source Texts
- Core back-matter thins (Random Run Generator, Character Sheet, cityscapes, cover scenes) if you care about those pages

Audit / fix scripts: `Source/_extract/audit_completed*.py`, `qa_six_books.py`, `fix_audit_errors.py`, `extract_forbiddenarcana.py`, `format_forbiddenarcana.py`.
