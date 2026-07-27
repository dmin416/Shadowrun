# Character Creation - Overview

Agent reference (SR5). LLM layout; full mechanical detail for the chargen pipeline. Prefer sibling pages for deep tables.

**Src PDFs:** `Source/PDF/shadowrunfiftheditioncorerulebook_V2.pdf`
**Printed:** Creating a Shadowrunner ~p.62-101 (steps); Alternate Gameplay sidebar; Final Calculations Table p.101; Character Creation Checklist
**Source Text:** `08 - Creating A Shadowrunner.md`
**See also:** [Priority System](Priority%20System.md) · [Metatype](Metatype.md) · [Attributes](Attributes.md) · [Magic and Resonance](Magic%20and%20Resonance.md) · [Skills](Skills.md) · [Resources and Gear](Resources%20and%20Gear.md) · [Qualities](Qualities.md) · [Contacts](Contacts.md) · [Finishing Touches](Finishing%20Touches.md) · `Mechanics/Dice and Tests.md` · `Mechanics/Edge.md`

**Scope:** step order; play levels; global Karma/gear caps; Final Calculations; Core creation checklist; concept roles (pointer)
**Out of scope:** full Priority table cells (Priority System); quality catalog; skill lists; gear catalogs (Encyclopedia)

## Inventory (completeness checklist)

**Core steps 1-9:** Concept → Metatype/Attrs → Magic/Resonance → Qualities → Skills → Resources → Leftover Karma → Final Calculations → Final Touches  
**Play levels:** Experienced (default); Street-Level; Prime Runner  
**Global caps:** 25 Karma start; ±25 Karma qualities; Avail ≤12 / Device Rating ≤6 (experienced); aug +4 Attr; 1 Mental/Physical at natural max; Knowledge free points; contacts Cha×3; carryover Karma ≤7; leftover ¥ ≤5,000 → starting nuyen  
**Final Calculations Table:** Init forms; Limits; Condition Monitors; Living Persona; Reputation blanks  
**Core checklist bullets:** all (see end)

---

## Schema

| Token | Meaning |
| --- | --- |
| Play level | Street / Experienced / Prime (sets yen, Karma, Avail) |
| Priority | A-E assignment across five columns |
| Final Calculations | Derived Init, Limits, Condition Monitors, Living Persona |

---

## Play level (pick one)

Default = **Experienced**. Alternate Gameplay sidebar:

| Rule | Street-Level | Experienced (default) | Prime Runner |
| --- | --- | --- | --- |
| Resources Priority A-E ¥ | 75k / 50k / 25k / 15k / 6k | 450k / 275k / 140k / 50k / 6k | 500k / 325k / 210k / 150k / 100k |
| Starting Karma | 13 (max usable 26) | **25** | 35 (max usable 70) |
| Max Availability | ≤10 | **≤12** | ≤15 |
| Max Device Rating | ≤4 | **≤6** | ≤6 |
| Karma → ¥ | ≤5 Karma → ≤10,000¥ | ≤10 Karma → ≤20,000¥ (2,000¥/Karma) | ≤25 Karma → ≤50,000¥ |
| Contacts free Karma | Cha × 3 | **Cha × 3** | Cha × **6** |
| Initiation / Submersion at chargen | No | **No** | **Yes** |

Other chargen rules (priority assignment, attribute max rules, etc.) still apply unless the row above overrides.

---

## Step order (Core)

| Step | Name | Do | Deep page |
| --- | --- | --- | --- |
| 1 | Choose Concept | Role, background, team niche. Note desired qualities early | this file (roles) |
| 2 | Metatype + Attributes | Assign **each** Priority column A-E once. Pick metatype; spend Metatype special Attr points (Edge / Magic / Resonance only). Spend **all** Attributes-column points on Mental/Physical | Priority · Metatype · Attributes |
| 3 | Magic or Resonance | If Priority grants Mag/Res: tradition, type (mage / adept / mystic adept / aspected / techno), free skills/spells/forms as listed | Magic and Resonance · Priority |
| 4 | Qualities | Spend from play-level Karma pool (Street 13 / Exp **25** / Prime 35). Cap **≤25 Karma** Positive and **≤25 Karma** Negative at creation | Qualities |
| 5 | Skills | Spend Skills-column points (individual / groups). Free Knowledge+Language = **(Int + Log) × 2**. 1 native Language **N** free (Bilingual → 2nd native free) | Skills |
| 6 | Resources | Spend Priority ¥ on gear, lifestyle, SINs, etc. Hold ≤**5,000¥** into starting nuyen; rest of unspent ¥ lost. Optional Karma→¥ (rate above) | Resources and Gear |
| 7 | Leftover Karma | Raise skills/attrs; spells/forms; bond foci; bind spirits / register sprites; contacts (free Cha×3 plus extra Karma); mystic adept Power Points (**5 Karma / PP**, max PP = Magic). Carry ≤**7** Karma into play | Finishing Touches · Contacts |
| 8 | Final Calculations | Initiative forms, Limits, Condition Monitors, Living Persona, list Init Dice | this file + Finishing Touches |
| 9 | Final Touches | Story, appearance, GM approval | Finishing Touches |

**Note:** Core numbers Steps as Concept → Metatype (attrs) → Magic/Resonance → Qualities → Skills → Resources → Karma → Final Calculations → Final Touches. Qualities are Step Four in Core (before Skills), not after Resources.

---

## Global creation caps (experienced unless noted)

| Cap | Rule |
| --- | --- |
| Priority rows | Each of A-E used **exactly once** across the five columns |
| Attribute points | Spend **all** Attributes-column points; not on special attrs |
| Special Attr points | From Metatype column only; Edge / Magic / Resonance only; unused lost after chargen |
| Natural max | **Only one** Mental or Physical Attr at natural metatype max (Exceptional Attribute can push +1). Edge / Magic / Resonance **exempt** |
| Augmented Attr | From all sources: **+4** max to any Mental/Physical Attr |
| Active skills / groups | Max **6** at creation (skill can hit **7** with Aptitude; groups cannot). Post-chargen max 12 (13 with Aptitude for skills) |
| Knowledge / Language | Max rating **6** at creation; native = **N** |
| Gear | Avail ≤**12**, Device Rating ≤**6** (experienced); GM veto always |
| Qualities | ≤25 Karma Positive; ≤25 Karma Negative |
| Karma carry into play | ≤**7** |
| Unspent Resources ¥ | ≤**5,000** kept as starting nuyen add-on; excess lost |
| Initiation / Submersion | **Forbidden** at creation except Prime Runner |
| Knowledge / Contact math | Use **unaugmented** Int/Log/Cha (ware bonuses do not raise free Knowledge points or free contact Karma) |

### Essence / Magic / Resonance

| Rule | Detail |
| --- | --- |
| Start Essence | 6 |
| Ware | Cyber/bioware reduce Essence |
| Mag/Res loss | Any fraction of Essence loss → **-1** Magic or Resonance (per full point-crossing; see Magic/Resonance page). Example: 6.0→5.5 costs -1 Magic |
| Social Limit | Round Essence **up** to whole number before Social Limit formula |

### Mystic adept Power Points

Adepts: PP = Magic (free). Mystic adepts: **no** free PP; buy **5 Karma per full PP**, max PP = Magic (usually Step 7 / leftover Karma).

---

## Concept roles (Core gallery; not mechanical locks)

| Role | Core focus attrs (guide) |
| --- | --- |
| Face | Cha, Wil; social / Con / Negotiation |
| Spellcaster | Mag Priority; Cha or Int (tradition) + Wil (Drain) |
| Decker | Log, Int, Wil; cyberdeck |
| Technomancer | Resonance Priority; Log, Int, Wil |
| Rigger | Reaction; vehicles/drones |
| Street Samurai | Bod, Str, Agi; ware + combat |

Any concept allowed; team coverage is a play concern, not a rule.

---

## Final Calculations Table (Core)

Compute after ware/attrs locked. Round Limits **up**. Condition Monitors: round up final boxes.

| Mechanic | Formula | Aug notes |
| --- | --- | --- |
| Initiative | (Intuition + Reaction) + **1D6** | Add Attr and Init Dice bonuses; note as `9 (11) + 2D6` style |
| Astral Initiative | (Intuition × 2) + **2D6** | - |
| Matrix AR Initiative | (Intuition + Reaction) + **1D6** | - |
| Matrix VR Cold-Sim | (Data Processing + Intuition) + **3D6** | - |
| Matrix VR Hot-Sim | (Data Processing + Intuition) + **4D6** | - |
| Mental Limit | [(Logic × 2) + Intuition + Willpower] / 3 | round up |
| Physical Limit | [(Strength × 2) + Body + Reaction] / 3 | round up |
| Social Limit | [(Charisma × 2) + Willpower + Essence] / 3 | Essence rounded **up** first |
| Physical Condition Monitor | [Body / 2] + 8 | include Body bonuses before calc; round up |
| Stun Condition Monitor | [Willpower / 2] + 8 | include Wil bonuses; round up |
| Overflow | Body + augmentation bonuses | - |
| Living Persona Attack | Charisma | techno |
| Living Persona Data Processing | Logic | |
| Living Persona Device Rating | Resonance | |
| Living Persona Firewall | Willpower | |
| Living Persona Sleaze | Intuition | |
| Reputation | Street Cred / Notoriety / Public Awareness | start usually 0 unless qualities |

Also list: Composure, Judge Intentions, Lift/Carry, Memory (see Dice and Tests); Movement (Combat Movement when filled).

---

## Leftover Karma purchases (creation table summary)

Full costs/restrictions: Finishing Touches. Caps at creation:

| Item | Karma | Cap at creation |
| --- | --- | --- |
| Contact | 1 per Connection + 1 per Loyalty (min 2) | ≤**7** Karma on any one contact; free pool Cha×3 (or ×6 Prime) |
| Spell / ritual / prep | 5 each | **Each** group ≤ Magic × 2 (e.g. Magic 4 → 8 spells **and** 8 rituals **and** 8 preps) |
| Complex Form | 4 each | ≤ Resonance × 2 |
| Bound spirit | 1 per service (Force = Magic) | Number ≤ Charisma |
| Registered sprite | 1 per task (Level = Resonance) | Number ≤ Charisma |
| Bond foci | per Magic rules | Total Force bonded ≤ Magic × 2 |
| Mystic adept PP | 5 per PP | PP ≤ Magic |

---

## Core Character Creation Checklist (must pass)

1. Each Priority Table row A-E chosen **once**.
2. Racial advantages/disadvantages noted (vision, Reach, lifestyle cost, toxin dice, etc.).
3. Metatype special Attr points spent on Edge and/or Magic/Resonance (or consciously left to later Karma if 0 points).
4. **All** Mental/Physical attribute points spent; ≤1 Mental/Physical at natural max (special attrs exempt).
5. Magic/Resonance Priority benefits recorded (skills, spells, forms, aspected category only, mystic adept PP Karma).
6. Qualities applied; sheet mods noted; ±25 Karma caps.
7. All skill + skill group points spent; no group/individual duplication; desired specializations from priority.
8. Gear complete (commlink/deck, ammo, vehicles, lifestyle, fake SIN/licenses); dwarf/troll **lifestyle** cost mods (+20% / +100%); Karma→¥ ≤ cap; ≤5,000¥ carry to starting nuyen.
9. Essence, Initiative (all forms used), Inherent Limits, contacts calculated.
10. GM approval.

---

## Coverage notes

- Pipeline + caps + Final Calculations + Core checklist: complete for Overview.
- Sibling Character Creation pages are filled for Core Priority chargen (see those files for deep tables).
- Run Faster / Chrome Flesh chargen options (Sum-to-Ten, metavariants, extra qualities): not in this Core Overview.
