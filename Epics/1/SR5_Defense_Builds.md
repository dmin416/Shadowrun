# SR5 Defense Builds

**Three layers, all separate:** Avoidance (not getting hit) · Resistance (absorbing the hit) · Magic defense (different problem entirely).

---

## THE CORE MECHANIC

```
Attacker: Weapon Skill + AGI [Accuracy]
Defender: REA + INT (free, no limit)
```
Attacker net hits → added to DV. Then BOD + Armor resists. For spells: direct spells skip the avoidance roll entirely.

---

## LAYER 1 — AVOIDANCE (REA + INT)

### What raises avoidance

| Source | REA bonus | Other | Conflicts |
|--------|-----------|-------|-----------|
| Wired Reflexes R1–3 | +R | +R Init Dice | Blocks all other REA/Init augs except wireless RE |
| Reaction Enhancers R1–3 | +R | — | Blocks wired except wireless stack |
| Synaptic Booster R1–3 | +R | +R Init Dice | Blocks ALL other REA/Init enhancements, no exceptions |
| Improved Reflexes L1–3 (adept) | +L | +L Init Dice | Blocks all cyber/bio REA/Init; adept-only lane |
| Reakt (Chrome Flesh transgenic) | — | +2 all defense rolls | Stacks with anything; different mechanism |
| Synaptic Acceleration (CF) | — | +1 all defense rolls | Stacks with anything |
| Running | — | +2 defense | Situational |
| Sprinting | — | +4 defense | Costs actions |
| Drop Prone vs ranged | — | +2 defense | Situational |
| Combat Sense (adept) | — | +1/level all defense | Stacks with everything |

### Stacking rules at a glance

| A | B | Stack? |
|---|---|--------|
| Wired Reflexes | Reaction Enhancers | NO (YES if both wireless) |
| Wired Reflexes | Synaptic Booster | NO |
| Wired Reflexes | Improved Reflexes | NO |
| Reaction Enhancers | Synaptic Booster | NO |
| Improved Reflexes | Synaptic Booster | NO |
| Any REA aug | Reakt | YES |
| Any REA aug | Synaptic Acceleration | YES |
| Any REA aug | Combat Sense | YES |
| Full Defense | Combat Sense | YES |
| Wired Reflexes (wireless) | Reaction Enhancers (wireless) | YES, can exceed +4 cap |

### Melee-only interrupt upgrades (cost Initiative Score)

| Option | Init cost | Pool |
|--------|-----------|------|
| Dodge | −5 | REA + INT + Gymnastics [Physical] |
| Parry | −5 | REA + INT + Melee Skill [Physical] |
| Block | −5 | REA + INT + Unarmed [Physical] |
| Full Defense | −10 | + WIL to all defenses this Combat Turn; stacks with above |

Full Defense applies to ranged attacks too (WIL added). Dodge/Parry/Block are melee only.

### Avoidance pools by build

| Build | REA | INT | Combat Sense | Base pool | Full Defense (WIL 6) |
|-------|-----|-----|-------------|-----------|----------------------|
| Untrained | 3 | 3 | — | 6 | 12 |
| Trained runner | 4 | 4 | — | 8 | 14 |
| Human peak, no ware | 6 | 6 | — | 12 | 18 |
| Wired R3 | 7 | 5 | — | 12 | 18 |
| Wired R3 + CS 3 | 7 | 5 | +3 | 15 | 21 |
| Wired R3 + Reakt + Synaptic Acc | 7 | 5 | — | 15 | 21 |
| Improved Reflexes L3 (adept) | 7 | 5 | — | 12 | 18 |
| Improved Reflexes L3 + CS 3 | 7 | 5 | +3 | 15 | 21 |
| Feathered Serpent dragon | 10 | 9 | — | 19 | — |
| Western dragon | 8 | 8 | — | 16 | — |

**To reliably out-roll a competent attacker (assume 4 avg hits):** need ~16+ defense dice.

---

## LAYER 2 — RESISTANCE (BOD + Armor)

### Armor values

| Armor | Description | Notes |
|-------|-------------|-------|
| 6 | Armor clothing | Concealable; light pistol territory |
| 9 | Armor vest / lined coat | Police grade; pistol coverage |
| 12 | Armor jacket | Runner standard |
| 15 | Full body armor | Military; rifle starts to become Stun |
| 18–20 | Mil-Spec Hardened | Hardened Armor rules; assault rifles bounce |

Accessories add to Armor but total bonus capped by STR. Every 2 points over STR = −1 AGI and REA.

### What raises resistance

| Source | Adds to | Notes |
|--------|---------|-------|
| Orthoskin R1–4 (bioware) | Armor +R | No dermal plating |
| Dermal Plating R1–6 (cyber) | Hardened Armor +R | No orthoskin |
| Bone Lacing Titanium (cyber) | BOD +3, Armor +3 | Also raises unarmed DV |
| Mystic Armor (adept power) | Armor +level | No encumbrance; works in astral; stacks freely |
| Attribute Boost BOD (adept) | BOD temporarily | Temporary; active power |
| Subdermal Armor (CF bioware) | Armor +R | Stacks with worn |

### Resistance pools by scenario

| Character | BOD | Armor | Pool | Heavy pistol hit (DV 10) | Assault rifle hit (DV 13) |
|-----------|-----|-------|------|--------------------------|---------------------------|
| Unarmored civilian | 3 | 0 | 3 | 9 Physical | 12 Physical → dead |
| Runner armor vest | 4 | 9 | 13 | 5 Stun | 10 Physical |
| Runner armor jacket | 4 | 12 | 16 | 5 Stun | 8 Physical |
| Tough runner jacket | 6 | 12 | 18 | 5 Stun | 7 Physical |
| Ork full body armor | 8 | 15 | 23 | 5 Stun | 5 Stun |
| Troll full body armor | 10 | 15 | 25 | 5 Stun | 4 Stun |
| Adept: Mystic Armor 4 + jacket | 5 | 16 | 21 | 5 Stun | 6 Physical |
| Mil-Spec Hardened 15 | any | 15H | — | DV 10 < 15 → zero damage | DV 13 < 15 → zero damage |

---

## LAYER 3 — MAGIC DEFENSE

### Spell types and what defends against them

| Spell type | Example | Avoidance roll | Resistance roll | Armor helps? |
|-----------|---------|---------------|-----------------|--------------|
| Indirect | Fireball, Lightning Bolt | REA + INT | BOD + Armor | YES |
| Direct Physical | Powerbolt, Shatter | BOD opposed | — (net hits = damage) | NO |
| Direct Mana | Manabolt, Stunbolt | WIL opposed | — (net hits = damage) | NO |

Direct spells have no avoidance step and no resistance step. The mage's casting hits become damage boxes directly, reduced only by BOD (physical) or WIL (mana).

### What raises magic defense

| Source | Effect | Applies to |
|--------|--------|-----------|
| High WIL | More dice vs mana direct spells | Mana direct only |
| High BOD | More dice vs physical direct spells | Physical direct only |
| Spell Resistance (adept) | +level dice to all spell resistance | All spells, preparations, rituals |
| Counterspelling (mage skill) | Adds skill dice to allies' defense; refreshes each turn; covers up to Magic-rating people simultaneously | All spells |
| Shielding (metamagic) | Personal Counterspelling-equivalent; requires Initiation | All spells, self only |
| Mystic Armor (adept) | Adds Armor vs indirect spells only | Indirect only |
| Full Defense | +WIL to avoidance vs indirect | Avoidance only |

### Practical magic defense numbers

| Character | vs Indirect (REA+INT) | vs Direct Mana (WIL) | vs Direct Physical (BOD) |
|-----------|----------------------|---------------------|--------------------------|
| Average (no magic investment) | 8 | 4 | 4 |
| Tough runner | 10 | 5 | 6 |
| Adept: Spell Resistance 3 | 10 + CS | 5 + 3 | 6 + 3 |
| Mage with CS 10 protecting ally | ally pool + 10 | ally pool + 10 | ally pool + 10 |

A mage with Counterspelling 10 next to you is the single best magic defense available. +10 dice to any spell, refreshes every turn, covers up to their Magic rating in allies.

---

## BUILD TEMPLATES

### Mundane Peak (no magic, no ware)
REA 6, INT 6, WIL 6, Armor jacket 12, BOD 6
- Avoidance: 12 base / 18 Full Defense
- Resistance: 18 (flips rifle to Stun)
- Magic: 6 vs direct mana / 6 vs direct physical — exposed

### Wired Street Samurai
REA 7 (wired R3), INT 5, WIL 4, Armor jacket 12, BOD 5
- Avoidance: 12 base / 16 Full Defense
- Resistance: 17
- Magic: 4 vs mana / 5 vs physical — exposed

### Wired + Reakt + Synaptic Acceleration
REA 7 (wired R3), INT 5, WIL 5, Armor jacket 12, BOD 5
- Avoidance: 12 + 2 (Reakt) + 1 (SA) = 15 base / 20 Full Defense
- Resistance: 17
- Magic: still exposed

### Adept Evader
Improved Reflexes L3 (+3 REA), REA 7, INT 5, Combat Sense 3, Mystic Armor 4, Armor jacket 12, Spell Resistance 3, BOD 4, WIL 5
- Avoidance: 12 + 3 CS = 15 base / 20 Full Defense
- Resistance: 4 BOD + 12 jacket + 4 Mystic = 20
- Magic: 8 vs indirect (Mystic helps) / 5 + 3 = 8 vs direct mana / 4 + 3 = 7 vs direct physical

### Mage Shield (protects the team)
Counterspelling 10, Magic 6, WIL 6
- Avoidance (self): standard
- Resistance (self): standard
- Magic (team): +10 dice to anyone in LOS vs any spell, every turn, up to 6 people simultaneously

### Mystic Adept (both worlds)
Improved Reflexes L2 (REA +2), REA 6, INT 5, Combat Sense 2, Spell Resistance 2, Counterspelling 6, Mystic Armor 3, Armor jacket 12, BOD 4, WIL 5
- Avoidance: 11 + 2 CS = 13 base / 18 Full Defense
- Resistance: 4 + 12 + 3 = 19
- Magic self: 11 + 2 SR + 6 CS = 19 vs any spell

---

## HARDENED ARMOR QUICK REFERENCE

If Modified DV < Hardened value → zero damage, no roll.
If Modified DV ≥ Hardened value → resist normally + auto-hits equal to half Hardened (after AP, round up).

| Source | Value | Assault rifle (Mod DV 11) | AV rocket (Mod DV 24) |
|--------|-------|--------------------------|----------------------|
| Mil-Spec Light | 15 | 11 < 15 → nothing | 24 > 15 → penetrates |
| Mil-Spec Heavy | 20 | 11 < 20 → nothing | 24 > 20 → penetrates |
| Eastern dragon scales | 17 | 11 < 17 → nothing | 24 > 17 → penetrates |
| Western dragon scales | 18 | 11 < 18 → nothing | 24 > 18 → penetrates |
