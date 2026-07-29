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
| [Chrome Flesh](Source%20Texts/Chrome%20Flesh/) | All 13 chapters + INDEX; `qa_chrome_flesh.py` / `chrome_flesh_qa_report.md` PASS; polish via `polish_six_books.py` | Residual long prose paras (~800-900 chars) acceptable; optional table re-audit |
| [Kill Code](Source%20Texts/Kill%20Code/) | All 16 chapters + INDEX; `killcode_sweep_report.md` landmark/JP PASS | Ch13 JP handle order fixed in sweep; Denial of Service / Power Munger print quirks noted in-file |
| [Data Trails](Source%20Texts/Data%20Trails/) | All 16 chapters + INDEX; `datatrails_sweep_report.md` landmark PASS | Print quirks noted in-file (Insansity, Emporer, etc.); optional deeper table re-audit |
| [Gun Heaven 3](Source%20Texts/Gun%20Heaven%203/) | All 39 sections + INDEX; `gun_heaven_3_qa_report.md` PASS | Dual SR5/SR4A stats; page 3 split for upgrades vs using-this-book |
| [Book of the Lost](Source%20Texts/Book%20of%20the%20Lost/) | All 16 chapters + INDEX; `book_of_the_lost_qa_report.md` PASS | Residual JP wrapping / Character Trove table polish possible; PDF typo "shadowurns" preserved |
| [Better Than Bad](Source%20Texts/Better%20Than%20Bad/) | All 12 chapters + INDEX; `better_than_bad_qa_report.md` PASS | Residual inline gear tables / JP handles in Building a Hooder; Hooder Runs dice tables are fenced lists |
| [Cutting Aces](Source%20Texts/Cutting%20Aces/) | All 11 chapters + INDEX; `cutting_aces_qa_report.md` PASS | Residual JP wrapping; some gear/NPC tables still prose-ish |
| [Aetherology](Source%20Texts/Aetherology/) | All 6 chapters + INDEX; `aetherology_qa_report.md` PASS | Mid-page splits for Greater Beings / Rules; spirit stat blocks still column-per-line |
| [Splintered State](Source%20Texts/Splintered%20State/) | All 18 chapters + INDEX; `splintered_state_qa_report.md` PASS | Cover image-only; mid-page scene splits; NPC stat blocks mostly fenced/columnar |
| [Dark Terrors](Source%20Texts/Dark%20Terrors/) | All 16 chapters + INDEX; `dark_terrors_qa_report.md` PASS | Cover image-only; Credits/Introduction split on idx 5; residual Game Information heading density in bug section |
| [Assassin's Primer](Source%20Texts/Assassin's%20Primer/) | All 7 chapters + INDEX; `assassins_primer_sweep_report.md` landmark PASS | Short PDF (17 pp); print quirks noted in-file (`has lead`, plural Disadvantages) |
| [Shadow Spells](Source%20Texts/Shadow%20Spells/) | All 8 chapters + INDEX; `shadow_spells_sweep_report.md` landmark PASS | 41 spells / 3 rituals / 16 adept powers; print quirks noted (Crystaline, Orichalum, Mana Ebb wording) |
| [Lockdown](Source%20Texts/Lockdown/) | All 15 chapters + INDEX; `lockdown_qa_report.md` PASS | Dense QZ diary / CFD rules; residual date-stamp headers and table polish possible |
| [Stolen Souls](Source%20Texts/Stolen%20Souls/) | All 17 chapters + INDEX; `stolen_souls_qa_report.md` PASS | Compiled tables chapter still flattened prose rows; CFD Game Info dense |
| [Market Panic](Source%20Texts/Market%20Panic/) | All 14 chapters + INDEX; `market_panic_qa_report.md` PASS | Big Ten corp book (210 pp); residual JP polish / table formatting possible |
| [Seattle Sprawl](Source%20Texts/Seattle%20Sprawl/) | All 16 chapters + INDEX; `seattle_sprawl_qa_report.md` PASS | Ch.01 condensed TOC intentional; Council Island has no Help Wanted in print |
| [Serrated Edge](Source%20Texts/Serrated%20Edge/) | 16 PDF chapters + GM brief + INDEX; `serrated_edge_qa_report.md` PASS | Denver Map / Medical Center Map are image-only stubs; open PDF for art |

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

### Removed / never verified

- Separate “Qualities Reference” line (duplicate of Qualities.md; nothing extra to audit)
- Claim that Encyclopedia setup alone equals perfect catalogs

---

## Still open

- Encyclopedia polish (cross-links, source tags, layout)
- Core Source Texts: rules chapters filled (volume ≈ PDF); art back-matter stubs intentional; formal Core QA / em-dash scrub still open (see TODO)

Living the Shadows Mechanics filled 2026-07-26: Actions Outside Combat, Healing and Injuries, Gig Rewards, Housing and Lifestyle, Vehicles.

Specialized Basics filled 2026-07-26: Matrix Basics, Magic Basics, Rigging Basics (Core; DT/SG/R5 as pointers).

Chrome Flesh Source Texts QA PASS 2026-07-26: format/polish + loss/done (`chrome_flesh_qa_report.md`).

Book of the Lost Source Texts QA PASS 2026-07-28: extract/format + loss/done (`book_of_the_lost_qa_report.md`).

Better Than Bad Source Texts QA PASS 2026-07-28: extract/format + loss/done (`better_than_bad_qa_report.md`).

Cutting Aces Source Texts QA PASS 2026-07-28: extract/format + loss/done (`cutting_aces_qa_report.md`).

Lockdown Source Texts QA PASS 2026-07-28: extract/format + loss/done (`lockdown_qa_report.md`).

Stolen Souls Source Texts QA PASS 2026-07-28: extract/format + loss/done (`stolen_souls_qa_report.md`).

Market Panic Source Texts QA PASS 2026-07-28: extract/format + loss/done (`market_panic_qa_report.md`).

Seattle Sprawl Source Texts done-check PASS 2026-07-28 (`seattle_sprawl_qa_report.md`).

Serrated Edge Source Texts loss/done QA PASS 2026-07-28 (`serrated_edge_qa_report.md`).

Audit / fix scripts: `Source/_extract/audit_completed*.py`, `qa_six_books.py`, `qa_chrome_flesh.py`, `qa_book_of_the_lost.py`, `qa_better_than_bad.py`, `qa_cutting_aces.py`, `qa_lockdown.py`, `qa_stolen_souls.py`, `qa_seattle_sprawl.py`, `qa_serrated_edge.py`, `fix_audit_errors.py`, `extract_forbiddenarcana.py`, `format_forbiddenarcana.py`, `extract_book_of_the_lost.py`, `format_book_of_the_lost.py`, `extract_better_than_bad.py`, `format_better_than_bad.py`, `extract_cutting_aces.py`, `format_cutting_aces.py`, `extract_lockdown.py`, `format_lockdown.py`, `extract_stolen_souls.py`, `format_stolen_souls.py`, `killcode_sweep.py`, `killcode_landmark_sweep.py`, `killcode_sweep_report.md`, `chrome_flesh_qa_report.md`, `book_of_the_lost_qa_report.md`, `better_than_bad_qa_report.md`, `cutting_aces_qa_report.md`, `lockdown_qa_report.md`, `stolen_souls_qa_report.md`, `seattle_sprawl_qa_report.md`, `serrated_edge_qa_report.md`.
