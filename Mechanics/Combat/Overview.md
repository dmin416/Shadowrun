# Combat - Overview

Agent reference (SR5). LLM layout; Combat Turn pipeline + universal attack resolution (DADA).

**Src PDFs:** `Source/PDF/shadowrunfiftheditioncorerulebook_V2.pdf`
**Printed:** Combat Basics ~p.158-173; Combat Sequence (DADA) ~p.173
**Source Text:** `11 - Combat.md`
**See also:** [Initiative](Initiative.md) · [Action Economy](Action%20Economy.md) · [Ranged Combat](Ranged%20Combat.md) · [Melee Combat](Melee%20Combat.md) · [Damage Armor and Wounds](Damage%20Armor%20and%20Wounds.md) · [Movement](Movement.md) · [Surprise](Surprise.md) · [Called Shots and Special](Called%20Shots%20and%20Special.md) · `../Dice and Tests.md` · `../Edge.md`

**Scope:** Combat Turn / Pass / Action Phase; attack sequence Declare→Attack→Defend→Apply; wound timing; mid-fight entry; sibling index
**Out of scope:** Full fire-mode/recoil tables (Ranged); Reach/melee mods (Melee); elemental secondaries (Damage); full action lists (Action Economy)

## Inventory (completeness checklist)

- [x] Combat Turn / Action Phase / Pass structure
- [x] Attack sequence: Attack → Defense → DV/AP → Damage Resistance
- [x] Wound mods timing; entering mid-fight Init -10/Pass
- [x] Link to all Combat siblings

---

## Schema

| Token | Meaning |
| --- | --- |
| Combat Turn | ~3 seconds (20 Turns = 1 minute) |
| Initiative Pass | Slice of the Turn; act if Score > 0 |
| Action Phase | One character's turn in a Pass |
| Initiative Score | Attr + face sum of Init Dice; order high→low |
| DADA | Declare → Attack → Defend → Apply Effect |

---

## Hierarchy

```
Combat Turn (~3 sec)
  └─ Initiative Pass(es)
       └─ Action Phase (each combatant with Score > 0, high to low)
            └─ Actions (1 Complex or 2 Simple + Free; movement declared)
```

After everyone with Score > 0 has acted in a Pass: all Scores **-10**. Repeat Passes until all Scores ≤ 0, then new Combat Turn (re-roll Initiative).

---

## Combat Turn sequence (Core)

| Step | Name | Do |
| --- | --- | --- |
| 1 | Roll Initiative | Everyone rolls Init Score ([Initiative](Initiative.md)). Highest acts first. Wound mods already affect Score as soon as wounds land |
| 2 | Begin Initiative Pass | Acting character = highest Score still eligible |
| 3 | Action Phase | 3A Declare (incl. delayed interveners); 3B Resolve |
| 4 | Remaining characters | Next-highest Score; when all acted → Scores -10; if anyone > 0 → back to Step 2 |
| 5 | New Combat Turn | All Scores ≤ 0 → Step 1 again until fight ends |

### Action Phase package (summary)

| You get | Detail |
| --- | --- |
| Actions | **1 Complex** **or** **2 Simple** (only **one** Simple may be an attack) |
| Free | Normally **1 Free Action** per Initiative Pass (own Phase or later in that Pass) |
| Movement | Declared in 3A; Walk/Run budget for whole Turn ([Movement](Movement.md)) |
| Delay | May delay instead of acting ([Initiative](Initiative.md)) |
| Defend | Always may use free Defense vs attacks; Interrupts cost Init Score ([Action Economy](Action%20Economy.md)) |

Score ≤ 0 this Pass: no Action Phase; still **1 Free** and may defend. Full lists: [Action Economy](Action%20Economy.md).

### Entering mid-fight

Roll Init normally, then **-10 per Initiative Pass already completed** this Combat Turn. May or may not get a Phase this Turn.

### Wound timing (critical)

| When | Effect |
| --- | --- |
| Wound taken | Wound modifier applies to **Initiative attribute** and thus **Initiative Score immediately** (even mid-Pass) |
| Does not | Grant an extra Action Phase |
| Also | Wound mods on later tests (not Damage Resistance / toxin resist / etc.) |

---

## Combat resolution (DADA)

Same skeleton for ranged, melee, astral, cybercombat (pools differ by type).

### Step 1: Declare

| Side | Declare |
| --- | --- |
| Attacker | Attack as part of Action Phase declare |
| Defender | Defense method: free **Reaction + Intuition**, or **Full Defense** (any attack). Melee also: **Dodge / Parry / Block** Interrupts ([Called Shots and Special](Called%20Shots%20and%20Special.md) / Action Economy) |

### Step 2: Attack

`Combat Skill + Attribute ± mods [Limit]`

Limit usually weapon **Accuracy** (melee/unarmed often **Physical**). Apply wound, environment, recoil, situational mods.

### Step 3: Defend

**A. Opposed hits**

| Result | Outcome |
| --- | --- |
| Attacker hits > defender | Hit; **net hits** = difference → Step 3B |
| Tie | **Grazing hit**: **no damage** (no Condition Monitor boxes); contact still occurs (toxin, shock glove, touch spell, etc. may still apply) |
| Defender hits > attacker | Miss; stop |

Standard Defense: Reaction + Intuition ± mods, **no Limit** (unless a skill is added via Dodge/Parry/Block).

**B. Damage math**

1. Modified DV = weapon DV + attacker's **net hits**
2. Modified Armor = Armor + attack **AP** (AP often negative)
3. **P vs S (Step 3B):** modified DV **≥** modified Armor → **Physical**; modified DV **<** modified Armor → **Stun**. This page follows Step 3B (either direction). Armor intro only describes Physical→Stun; Harder Knock forces P from Stun weapons. Table may choose Armor-intro-only if preferred.
4. Damage Resistance: Body + modified Armor (or Body only if modified Armor ≤ 0). Each hit -1 modified DV
5. If DV ≤ 0 after resist → no damage marked

### Step 4: Apply Effect

| Effect | Rule |
| --- | --- |
| Boxes | Remaining DV = boxes on Physical or Stun track |
| Wounds | Wound mods may update immediately (incl. Init Score) |
| Knockdown | Check if needed ([Called Shots and Special](Called%20Shots%20and%20Special.md) / Damage) |
| Secondaries | Electricity, fire, etc. ([Damage Armor and Wounds](Damage%20Armor%20and%20Wounds.md)) |

---

## Sheet checklist (combat)

- Initiative Attr + Dice (all forms used)
- Attack pools; weapon DV / AP / Accuracy / modes
- Armor (+ accessories, encumbrance)
- Condition Monitors; current wound mod
- Edge points remaining
- Reach / Cover / Recoil tracking as needed

---

## Sibling index

| File | Use for |
| --- | --- |
| [Initiative](Initiative.md) | Score, ERIC, -10/Pass, Edge Seize/Blitz, delay, form chart, wounds to Init |
| [Action Economy](Action%20Economy.md) | Free/Simple/Complex/Interrupt tables + combine rules |
| [Ranged Combat](Ranged%20Combat.md) | Modes, recoil, range, cover, Take Aim |
| [Melee Combat](Melee%20Combat.md) | Reach, charge, friends in melee, guns in melee |
| [Damage Armor and Wounds](Damage%20Armor%20and%20Wounds.md) | P/S, overflow, wound -1/3, elementals |
| [Movement](Movement.md) | Walk/Run/Sprint, running mods |
| [Surprise](Surprise.md) | Surprise Test, Ambush |
| [Called Shots and Special](Called%20Shots%20and%20Special.md) | Called shots, suppression, Full Defense / Block / Parry / Dodge |

Also: `../Healing and Injuries.md` · Matrix/Magic/Rigging Basics for non-meat attacks.
