# Healing and Injuries

Agent reference (SR5). LLM layout; First Aid, Medicine, natural recovery, magical Heal, overflow, stabilization.

**Src PDFs:** `Source/PDF/shadowrunfiftheditioncorerulebook_V2.pdf`
**Printed:** Healing ~p.205-209; Condition overflow ~p.170; First Aid skill ~p.145
**Source Text:** `11 - Combat.md` · First Aid / Medicine in `09 - Skills.md`
**See also:** [Combat/Damage Armor and Wounds](Combat/Damage%20Armor%20and%20Wounds.md) · [Dice and Tests](Dice%20and%20Tests.md) · [Actions Outside Combat](Actions%20Outside%20Combat.md) · Encyclopedia Medical Gear · Magic Basics (Heal / Stabilize spells)

**Scope:** First Aid; Medicine; medkit/autodoc; natural Stun/Physical recovery; Heal spell interaction; Healing Modifiers; overflow death; Stabilization
**Out of scope:** Full toxin/disease tables (Encyclopedia / Toxins play page); full Heal spell Force/Drain text (Magic); implant surgery Essence rules

## Inventory (completeness checklist)

- [x] First Aid / Medicine / medkit; Heal spell
- [x] Natural recovery Stun/Physical tables; glitches
- [x] Stabilization; overflow death

---

## Schema

| Token | Meaning |
| --- | --- |
| First Aid | First Aid + Logic [Mental] (2); needs medkit; within 1 hour |
| Medicine | Medicine + Logic [Mental]; bonus dice to rest Recovery |
| Heal spell | Spellcasting hits heal Physical boxes (max Force); not Drain damage |
| Stabilize | First Aid or Medicine [Mental] (3); or Stabilize spell |
| Overflow | Physical track full → Body boxes of overflow, then death |

---

## Tracks reminder

| Rule | Detail |
| --- | --- |
| Stun / Physical | Separate monitors |
| Wound mods | -1 DP (and Init Attr) per 3 boxes **per track**, stack |
| Physical full | Enter overflow; death if overflow > Body |

---

## First Aid

| Rule | Detail |
| --- | --- |
| Need | Medkit (even empty of supplies counts as having one) |
| Window | Within **1 hour** of the damage |
| Test | First Aid + Logic [Mental] **(2)** + Healing Modifiers; apply wound mods |
| Effect | Each **net hit** removes 1 box (Stun or Physical). Cap healed = **First Aid skill rating** |
| Armor | Full-body armor on patient → halve net effect (round up) |
| Once | Once per **set of wounds**; **cannot** use if Heal spell already applied to that set |
| Combat time | Complex Action to start; healing takes **1 Combat Turn per box** healed (Complex Action each of those Turns; other Actions OK in remaining Phases) |
| Crit glitch | +1D3 (1D6÷2) boxes damage |
| Diagnose | GM sets threshold; net hits = info |

Medkit in combat: Complex Action to apply → then +Rating dice (wireless) or autodoc autosoft; Limit also gains medkit Rating. Untrained: Logic -1 + device Rating as skill. Unattended wireless medkit: Rating × 2.

---

## Magical healing (Heal)

| Rule | Detail |
| --- | --- |
| Effect | Each Spellcasting hit heals 1 Physical box, max = Force |
| Ban | Cannot heal Drain damage |
| Stacking | Heal and First Aid each **once** per injury set. First Aid **blocked** after Heal. Heal **OK after** First Aid |

SOP (Core): First Aid → Heal in field → Medicine at clinic for Recovery bonuses.

Stabilize spell can stabilize; **Heal cannot** stabilize overflow.

---

## Medicine

| Rule | Detail |
| --- | --- |
| Test | Medicine + Logic [Mental] + Healing Modifiers |
| Effect | Each hit = **+1 die** on patient's subsequent **natural Recovery** tests while tended |
| Tend time | Physical: ≥30 min/day. Stun: ≥10 min/hour |
| Once | Once per wound set; OK after First Aid and/or Heal |
| Combat | **Cannot** use Medicine in combat |
| Diagnose | Same idea as First Aid |

---

## Natural recovery

Extended Tests; record hits per interval if interrupted.

| Damage | Test | Interval | Rest | Effect |
| --- | --- | --- | --- | --- |
| Stun | Body + Willpower | 1 hour | Full hour (sleep/unconscious OK) | 1 box per hit |
| Physical | Body × 2 | 1 day | Full day | 1 box per hit |

Physical rest healing **blocked** while any Stun remains; heal Stun first.

| Glitch | Effect |
| --- | --- |
| Glitch | Damage still heals; resting time **doubles** |
| Critical glitch | +1D3 boxes damage **and** double rest time |

Medkits/autodocs can bolster Recovery (same device rules as aid).

---

## Healing Modifiers Table

| Situation | Modifier |
| --- | --- |
| Good conditions (sterilized med facility) | +0 |
| Average conditions (indoors) | -1 |
| Poor conditions (street or wilderness) | -2 |
| Bad conditions (combat, bad weather, swamp) | -3 |
| Terrible conditions (fire, severe storm) | -4 |
| No medical supplies | -3 |
| Improvised medical supplies | -1 |
| Wireless medkit/autodoc | +Rating |
| Applying care remotely through medkit/autodoc | -2 |
| Assistance | Teamwork Test |
| Uncooperative patient | -2 |
| Patient is Awakened or Emerged | -2 |
| Patient has implants | -1 per 2 full points of lost Essence |

---

## Overflow and death

Exceed Physical monitor → overflow boxes. Automatic death when overflow exceeds **Body**. Until stabilized, take **+1 box every (Body) minutes** (blood loss/shock).

---

## Stabilization

| Rule | Detail |
| --- | --- |
| Test | First Aid + Logic [Mental] **(3)** or Medicine + Logic [Mental] **(3)** (+ Healing Modifiers); medkit/autodoc OK |
| Success | No more automatic overflow ticks |
| Fail | Keep ticking; retry at **cumulative -2** per prior attempt |
| Magic | Stabilize spell OK; Heal spell **not** |
| After | First Aid / Medicine / Heal apply normally once stable |

---

## Quick order of care

1. Stabilize if in overflow.
2. First Aid (≤1 hour, once).
3. Heal spell (once; after First Aid OK).
4. Medicine for Recovery dice.
5. Rest Extended Tests (Stun then Physical).
