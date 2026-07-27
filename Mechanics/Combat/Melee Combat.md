# Combat - Melee Combat

Agent reference (SR5). LLM layout; close combat Opposed Tests, Reach, modifiers.

**Src PDFs:** `Source/PDF/shadowrunfiftheditioncorerulebook_V2.pdf`
**Printed:** Melee ~p.186-188; Defense melee options ~p.188-191; Intercept ~p.194
**Source Text:** `11 - Combat.md`
**See also:** [Overview](Overview.md) · [Ranged Combat](Ranged%20Combat.md) · [Action Economy](Action%20Economy.md) · [Movement](Movement.md) · [Called Shots and Special](Called%20Shots%20and%20Special.md) · [Damage Armor and Wounds](Damage%20Armor%20and%20Wounds.md)

**Scope:** Melee Opposed; Reach; charge; friends in melee / teamwork; guns in melee; multiple attackers; touch-only; Melee Modifiers table
**Out of scope:** Full called-shot list (Called Shots and Special); astral melee (Magic)

## Inventory (completeness checklist)

- [x] Melee Opposed; Reach; charge; friends in melee
- [x] Guns in melee; multiple attackers; touch-only
- [x] Melee modifiers table

---

## Schema

| Token | Meaning |
| --- | --- |
| Attack | Melee skill + Agility [Accuracy] (unarmed: Unarmed + Agility [Physical]) |
| Defense | Rea+Int free; or Block/Parry/Dodge Interrupt; Full Defense |
| Reach | Weapon 1-4; troll natural +1; compare net → Defense mod |

---

## Basic Opposed Test

```
Attacker: Melee Skill + Agility ± mods [Accuracy]
vs
Defender: Reaction + Intuition ± mods
```

Unarmed / implant weapons as Unarmed: Limit = **Physical** (no Accuracy). Net hits → +DV. Then Damage Resistance ([Overview](Overview.md) DADA).

### Defense options (melee)

| Option | Cost | Pool |
| --- | --- | --- |
| Standard | Free | Reaction + Intuition |
| Dodge | Interrupt -5 Init | Rea + Int + Gymnastics [Physical] |
| Parry | Interrupt -5 | Rea + Int + melee weapon skill [Physical] (that weapon in hand) |
| Block | Interrupt -5 | Rea + Int + Unarmed [Physical] (empty hands) |
| Full Defense | Interrupt -10 | +Willpower to Defense whole Turn (stacks with Block/Dodge/Parry) |

---

## Reach

| Rule | Detail |
| --- | --- |
| Weapon Reach | 1-4 on weapon |
| Troll | Natural Reach **1**, stacks with weapon |
| Compare | Net Reach difference → mod on **defender's** pool |
| Attacker longer | Defender -1 per net Reach |
| Defender longer | Defender +1 per net Reach |

Reach does not add to attack pool; it changes how hard it is to defend.

---

## Melee Modifiers Table

| Situation | Dice pool mod |
| --- | --- |
| Attacker charging (running) | +2 attack; ignore usual -2 running skill penalty |
| Attacker prone | -1 |
| Called Shot | -4 (+ Free Action) |
| Multiple targets | Split dice pool |
| Superior position | +2 |
| Off-hand weapon | -2 (Ambidextrous: no off-hand) |
| Attacker wounded | -wound |
| Defender receiving a charge | +1 Defense (if Delayed Action ready) |
| Environmental | Light + Visibility columns only ([Ranged](Ranged%20Combat.md) env table) |
| Friends in melee | +1 attack (flat; not per friend) **or** Melee Teamwork |
| Opponent prone | +1 attack |
| Touch-only attack | +2; on **tie**, attacker succeeds (contact) |

### Charge

Melee attack while attacker is **Running** this Turn: +2 and no -2 running penalty on that melee attack.

### Friends in melee / teamwork

| Mode | Rule |
| --- | --- |
| Simple | +1 if ≥1 ally also in that melee |
| Teamwork | Ally Complex: Opposed Combat Skill + Agi [Accuracy] vs foe's Intuition (incl. Friends mod). Net hits → dice for next ally attack (or next teamwork). Max 3 teamwork assists before a real attack must land |

### Touch-only

Intent is contact (spell discharge, RFID tag, tag): +2 DP; ties go to **attacker**.

### Changing lethal ↔ nonlethal

| Case | Rule |
| --- | --- |
| Armored target | Called Shots: Harder Knock (S→P) or Splitting the Damage as applicable |
| Unarmored | Use as club (Clubs skill), Accuracy 3; blades as club lose Reach (pommel) |

### Unarmed DV

Default unarmed: **(STR)S**. Other weapons: listed DV (often STR+x).

---

## Guns in melee

| Rule | Detail |
| --- | --- |
| Ranged while in melee | Attacker -3 ([Ranged](Ranged%20Combat.md) situational) |
| Defender in melee vs gun | Defender -3 vs that ranged attack |
| Break melee | Risk Intercept |
| Pistol-whip / smash | Use Clubs (or appropriate) as melee instead |

### Intercept (Interrupt -5 Init)

If someone moves past within **1 + your Reach** meters or tries to leave melee: make a melee attack out of turn (need enough Init Score). Full: [Called Shots and Special](Called%20Shots%20and%20Special.md).

---

## Multiple attackers / targets

| Case | Rule |
| --- | --- |
| Multi-target | Multiple Attacks Free; split attack pool |
| Ganging up | Friends +1 or Teamwork (above) |
| Superior position | Behind, above, mounted grapple, etc. → +2 |

---

## Coverage notes

- Core melee modifiers + Reach + defense Interrupt options: complete for this page.
- Subduing / clinch: [Called Shots and Special](Called%20Shots%20and%20Special.md).
- Shooting into melee friendly-fire: [Ranged Combat](Ranged%20Combat.md).
