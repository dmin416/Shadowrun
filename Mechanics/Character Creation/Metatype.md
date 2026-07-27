# Character Creation - Metatype

Agent reference (SR5). LLM layout; full metatype mins/maxes and racial traits.

**Src PDFs:** `Source/PDF/shadowrunfiftheditioncorerulebook_V2.pdf`
**Printed:** Metatype Attribute Table p.66; Priority Metatype column p.65; racial notes in Concepts / chargen
**Source Text:** `08 - Creating A Shadowrunner.md` · Concepts metatype blurbs
**See also:** [Overview](Overview.md) · [Priority System](Priority%20System.md) · [Attributes](Attributes.md)

**Scope:** five Core metatypes; Attr min/max; Edge start; racial abilities; lifestyle cost mods; Priority row availability
**Out of scope:** Run Faster metavariants (hobgoblin, etc.); movement rate formulas (Combat Movement); qualities that alter metatype

## Inventory (completeness checklist)

- [x] Metatype Attribute Table (all Physical/Mental + Edge + Ess + Init)
- [x] Racial abilities (vision, Reach, dermal armor, toxin +2, lifestyle %)
- [x] Starting Edge; special Attr spend pointer
- [x] Which Priority rows allow which metatypes
- [x] Chargen: attrs start at min free; 1 point = +1

---

## Schema

| Token | Meaning |
| --- | --- |
| min/max | Racial attribute floor / natural ceiling |
| Special Attr pts | Metatype Priority (N); Edge/Magic/Resonance only |
| Lifestyle mod | Extra % on Lifestyle yen (dwarf/troll) |

---

## Priority availability

| Metatype | A | B | C | D | E |
| --- | --- | --- | --- | --- | --- |
| Human | yes (9) | yes (7) | yes (5) | yes (3) | yes (1) |
| Elf | yes (8) | yes (6) | yes (3) | yes (0) | no |
| Dwarf | yes (7) | yes (4) | yes (1) | no | no |
| Ork | yes (7) | yes (4) | yes (0) | no | no |
| Troll | yes (5) | yes (0) | no | no | no |

**(N)** = special attribute points at that Priority (Edge / Magic / Resonance only). See [Priority System](Priority%20System.md).

---

## Metatype Attribute Table (Core)

Format **min/max**. Characters start at **min** for free; spend Attributes-column points to raise (1 point = +1). Edge starts at min; Magic/Resonance start at **0** then add Priority + special points.

| Race | BOD | AGI | REA | STR | WIL | LOG | INT | CHA | EDG | ESS | Init |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Human | 1/6 | 1/6 | 1/6 | 1/6 | 1/6 | 1/6 | 1/6 | 1/6 | **2/7** | 6 | REA+INT |
| Elf | 1/6 | 2/7 | 1/6 | 1/6 | 1/6 | 1/6 | 1/6 | 3/8 | 1/6 | 6 | REA+INT |
| Dwarf | 3/8 | 1/6 | 1/5 | 3/8 | 2/7 | 1/6 | 1/6 | 1/6 | 1/6 | 6 | REA+INT |
| Ork | 4/9 | 1/6 | 1/6 | 3/8 | 1/6 | 1/5 | 1/6 | 1/5 | 1/6 | 6 | REA+INT |
| Troll | 5/10 | 1/5 | 1/6 | 5/10 | 1/6 | 1/5 | 1/5 | 1/4 | 1/6 | 6 | REA+INT |

### Natural max notes

| Race | Attrs below human-typical 6 max |
| --- | --- |
| Dwarf | REA max **5** |
| Ork | LOG max **5**; CHA max **5** |
| Troll | AGI max **5**; LOG max **5**; INT max **5**; CHA max **4** |
| Elf | AGI max **7**; CHA max **8** |
| Human | Edge max **7** (others Edge max **6**) |

Chargen: only **one** Mental or Physical attr may sit at its natural maximum (Exceptional Attribute can push one higher with GM OK). Edge / Magic / Resonance exempt.

---

## Racial abilities

| Race | Abilities / modifiers |
| --- | --- |
| **Human** | None. Higher Edge floor/ceiling (2/7) |
| **Elf** | **Low-Light Vision** |
| **Dwarf** | **Thermographic Vision**; **+2** dice pathogen and toxin resistance; **+20%** Lifestyle cost |
| **Ork** | **Low-Light Vision** |
| **Troll** | **Thermographic Vision**; **+1 Reach**; **+1 dermal armor** (Armor); **+100%** Lifestyle cost |

Vision rules in play: Combat / Perception environmental mods when those pages are filled. Reach: Melee. Dermal armor: stacks with worn armor as Armor rating +1 (Damage/Armor when filled).

### Lifestyle cost (chargen Resources)

| Race | Lifestyle ¥ multiplier |
| --- | --- |
| Dwarf | ×1.20 |
| Troll | ×2.00 |
| Others | ×1.00 |

Pay the modified cost when buying months of Lifestyle at creation.

---

## Special attributes (metatype-linked)

| Attr | Start | Raised by |
| --- | --- | --- |
| Edge | Metatype min | Special Attr points; Karma |
| Magic | 0 | Mag/Res Priority rating + special Attr points; Karma |
| Resonance | 0 | Mag/Res Priority rating + special Attr points; Karma |
| Essence | 6 | Reduced by ware (not raised by metatype) |

Special Attr points: only from Metatype Priority cell; only Edge/Magic/Resonance; unused lost. Details: [Priority System](Priority%20System.md) · [Attributes](Attributes.md).

---

## Chargen procedure (metatype slice)

1. Choose metatype that fits concept and available Priority row.
2. Record racial abilities and lifestyle multiplier on sheet.
3. Set all Physical/Mental attrs to racial **min**.
4. Set Edge to racial **min**; Magic/Resonance = 0 until Mag/Res Priority + special points.
5. Spend Metatype-column special Attr points (if any).
6. Spend Attributes-column points (separate Priority).

---

## Coverage notes

- Table and racial lines matched to Core PDF p.66.
- PDF chargen example once said troll “+50% gear and Lifestyle”; **table** is +100% Lifestyle only (no gear % on the Metatype Attribute Table). Use table.
- Metavariants / SURGE: not in Core chargen table; defer to Run Faster when sourced.
