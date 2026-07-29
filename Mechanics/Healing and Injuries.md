# Healing and Injuries

Agent reference (SR5). LLM layout; First Aid, Medicine, natural recovery, magical Heal, overflow, stabilization.

**Src PDFs:** `Source/PDF/shadowrunfiftheditioncorerulebook_V2.pdf`
**Printed:** Healing ~p.205-209; Condition overflow ~p.170; First Aid skill ~p.145
**Source Text:** `11 - Combat.md` · First Aid / Medicine in `09 - Skills.md`
**See also:** [Combat/Damage Armor and Wounds](Combat/Damage%20Armor%20and%20Wounds.md) · [Dice and Tests](Dice%20and%20Tests.md) · [Actions Outside Combat](Actions%20Outside%20Combat.md) · [Toxins and Drugs Play](Toxins%20and%20Drugs%20Play.md) · Encyclopedia Medical Gear · [Magic](Magic.md) (Heal / Stabilize)

**Scope:** First Aid; Medicine; natural recovery; Heal; overflow; Stabilization; **Care Under Fire** (*Bullets & Bandages*)
**Out of scope:** Full toxin/disease catalogs (Encyclopedia); toxin Resistance procedure ([Toxins and Drugs Play](Toxins%20and%20Drugs%20Play.md)); full Heal spell Force/Drain text (Magic); implant surgery Essence rules

## Inventory (completeness checklist)

- [x] First Aid / Medicine / medkit; Heal spell
- [x] Natural recovery Stun/Physical tables; glitches
- [x] Care Under Fire (B&B): progression, stabilization, diagnosis, treatment

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

## Stabilization (Core)

| Rule | Detail |
| --- | --- |
| Test | First Aid + Logic [Mental] **(3)** or Medicine + Logic [Mental] **(3)** (+ Healing Modifiers); medkit/autodoc OK |
| Success | No more automatic overflow ticks |
| Fail | Keep ticking; retry at **cumulative -2** per prior attempt |
| Magic | Stabilize spell OK; Heal spell **not** |
| After | First Aid / Medicine / Heal apply normally once stable |

---

## Care Under Fire (*Bullets & Bandages*, optional)

**Verified from:** `Bullets and Bandages Condensed.md`

Ideal order: **Stabilize → Diagnose → Treat**. Under fire, often stabilize only until safe.

### Damage progression

If a single attack deals **5+ Physical boxes**, damage progresses **+1 box every (Body) Combat Turns** until Stabilized (like Overflow timing). Wound mods accrue; death if Overflow > Body before Stabilization.

### Stabilization (Care Under Fire)

| Rule | Detail |
| --- | --- |
| Test | First Aid + Logic **Extended** (Complex); threshold = total Physical boxes (incl. progression + Overflow) |
| Success | Stops progression/overflow; does **not** remove damage. Each net hit reduces wound modifiers by 1 for (First Aid skill) hours |
| Non-progressive | Threshold = total boxes on both monitors; can negate wound mods |
| Stabilize spell | Force >= Progressive + Overflow boxes; DV = (Progressive + Overflow)/2 round up; sustain turns = those boxes |
| Trauma patch / **Crash** | Patient rolls Stabilization with **Body** at end of each CT. Medic dosing first adds patient Body to medic pool |

### Diagnosis (Care Under Fire)

Complex Action; Medicine + Logic or First Aid + Logic vs threshold. Biomonitor: +1 (not stackable with medkit). Success: **+2** to subsequent Stabilization/Treatment. Magic: Assensing + Intuition or **Diagnose** spell (same +2).

| Threshold | Injuries | Illness / intoxication |
| --- | --- | --- |
| 1 | Light (1-2 boxes) | Obvious etiology or toxin |
| 2 | Moderate (3-5 boxes) | Common etiology or toxin |
| 3 | Severe (6-9 boxes) | Rare etiology or toxin |
| 5+ | Critical (10+ boxes) | Exotic etiology or toxin |

### Treatment (Care Under Fire)

First Aid + Logic (2) per Core, with exceptions:

- If Physical CM not exceeded: success also **Stabilizes** (stops progression).
- If in Overflow: still need separate Stabilization.
- If previously Stabilized: each net hit removes **2** boxes (max net hits = First Aid or Medkit rating, higher).
- **Heal spell:** success also Stabilizes unless already in Overflow.

### Combat medical actions (summary)

| Action | Type | Notes |
| --- | --- | --- |
| Apply slap patch / dressing | Simple | Trauma patch, HemostatiX, etc. |
| Attach biomonitor | Simple | |
| Rapid assessment | Simple | First Aid + Intuition (2); not full Diagnosis |
| Attach medkit / Start IV | Complex | IV inject then Simple |
| Diagnose / Treat / Stabilize | Complex | Care Under Fire tests |
| Inject drug/toxin | Complex | Simple if IV running |

Medkit dice pools, autodoc Pilot rules, supply expenditure: *Bullets & Bandages* Ch. 07.

---

## Quick order of care

1. Stabilize if in overflow.
2. First Aid (≤1 hour, once).
3. Heal spell (once; after First Aid OK).
4. Medicine for Recovery dice.
5. Rest Extended Tests (Stun then Physical).
