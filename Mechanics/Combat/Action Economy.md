# Combat - Action Economy

Agent reference (SR5). LLM layout; Free / Simple / Complex / Interrupt actions in combat.

**Src PDFs:** `Source/PDF/shadowrunfiftheditioncorerulebook_V2.pdf`
**Printed:** Actions ~p.163-168; Combat Actions Table; Matrix action types pointer ~p.164
**Source Text:** `11 - Combat.md`
**See also:** [Overview](Overview.md) · [Initiative](Initiative.md) · [Ranged Combat](Ranged%20Combat.md) · [Melee Combat](Melee%20Combat.md) · [Called Shots and Special](Called%20Shots%20and%20Special.md) · [Movement](Movement.md) · Matrix / Magic Basics

**Scope:** Combine rules for one Action Phase; Core Free/Simple/Complex lists; Interrupt Init costs; reload action types
**Out of scope:** Full Matrix action procedures; full spellcasting; per-weapon FA bullet counts beyond note (Ranged); Barriers

## Inventory (completeness checklist)

- [x] Full Free / Simple / Complex / Interrupt lists (Core tables)
- [x] What you can combine in one Action Phase
- [x] Interrupt costs (Init Score)

---

## Schema

| Token | Meaning |
| --- | --- |
| Action Phase | Your turn in an Initiative Pass |
| Attack action | Fire / throw / melee / cast attack, etc. |
| Interrupt | Out-of-turn; costs Initiative Score; does not spend your Phase (unless Score drops too low) |

---

## What you can combine (one Action Phase)

| Package | Allowed |
| --- | --- |
| A | **1 Complex Action** + **1 Free Action** |
| B | **2 Simple Actions** + **1 Free Action** |
| Attack limit | With two Simples: only **one** may be an attack action |
| Movement | Declare in Phase; Walk/Run budget is per **Combat Turn** ([Movement](Movement.md)) |
| Order | Usually any order; sequence matters (draw before fire) |
| Delay | Instead of acting: Delayed Action ([Initiative](Initiative.md)) |

| Free Action timing | Rule |
| --- | --- |
| Normal | 1 Free per Initiative Pass: on your Phase **or** later in that Pass |
| Before your first Phase | Only if **not** surprised |
| Extra Frees | GM may allow if trivial (drop + short phrase) |

Score ≤ 0: no Phase; still 1 Free + defend.

---

## Free Actions (Core table + notes)

| Action | Notes |
| --- | --- |
| Call a Shot | Must combine with Fire / Throw / Melee Attack |
| Change Linked Device Mode | DNI/wireless: cyberware, smartgun mode, choke, wireless on/off, etc. |
| Drop Object | One or both hands; fragile may break |
| Drop Prone | Not if surprised |
| Eject Smartgun Clip | Mental; still need Simple to insert new clip |
| Gesture | Intuition (2) for unfamiliar watchers |
| Multiple Attacks | Split pool; combine with Fire / Throw / Melee / Reckless Spellcasting / Cast Spell |
| Run | Required each Pass while exceeding Walk rate this Turn |
| Speak / Text / Transmit Phrase | Short phrase; more = more Frees; DNI text OK |

---

## Simple Actions (Core table + notes)

| Action | Notes |
| --- | --- |
| Activate Focus | |
| Call Spirit | |
| Change Device Mode | Non-linked / slower devices |
| Command Spirit | |
| Dismiss Spirit | |
| Fire Bow | |
| Fire Weapon (SA, SS, BF, FA) | As Simple: SA/SS/BF/FA per firearm rules; **no other attack** same Phase. Simple FA = 6 rounds (typ.). Smartgun mode change often Free |
| Insert Clip | |
| Observe in Detail | Perception |
| Pick Up / Put Down Object | Careful; Drop is Free |
| Quick Draw | |
| Ready / Draw Weapon | |
| Reckless Spellcasting | |
| Reload Weapon | See reload table (some are Complex) |
| Remove Clip | |
| Shift Perception | Astral perceive toggle, etc. |
| Stand Up | From prone/kneeling; if wounded: Body + Willpower (2) |
| Take Aim | Cumulative; +1 DP **or** +1 Accuracy each; lost if any other action (incl. Free) before attack; max bonus = half Wil (round up); may span Phases/Turns |
| Take Cover | |
| Throw Weapon | No other attack same Phase; Multiple Attacks Free for multi at Short/Medium |
| Use Simple Device | |

---

## Complex Actions (Core table + notes)

| Action | Notes |
| --- | --- |
| Astral Projection | |
| Banish Spirit | |
| Cast Spell | |
| Fire Weapon (FA) | Complex FA = 10 rounds (typ.); cumulative recoil |
| Fire Long Burst or Semi-Auto Burst | Per Ranged |
| Fire Mounted or Vehicle Weapon | |
| Melee Attack | |
| Reload Weapon | Per reload table |
| Rigger Jump In | VCR + rigger-adapted vehicle/drone |
| Sprint | Running + Str [Physical]; extends Run rate ([Movement](Movement.md)) |
| Summoning | |
| Use Skill | Appropriate skill as Complex |

---

## Interrupt Actions (Init Score cost)

Take any time in the Turn (even before your Phase) if **not** surprised and Score can pay. Does **not** consume your Action Phase. Cost applies when used.

| Interrupt | Init cost | Effect (summary) |
| --- | --- | --- |
| **Block** | -5 | Melee: + Unarmed Combat to one Defense; empty hand; Limit = Physical |
| **Dodge** | -5 | Melee: + Gymnastics to one Defense; Limit = Physical |
| **Parry** | -5 | Melee: + melee weapon skill to one Defense; that weapon in hand; Limit = Physical |
| **Hit the Dirt** | -5 | Vs suppression when Free already used; skip Reaction+Edge; prone next Phase |
| **Intercept** | -5 | Melee attack out of turn vs someone moving past (within 1 + **your** Reach m) or breaking melee |
| **Full Defense** | -10 | + Willpower to Defense Tests vs **any** attack for **rest of Combat Turn**; stacks with Block/Dodge/Parry |

Full Defense / defense detail: [Called Shots and Special](Called%20Shots%20and%20Special.md).

---

## Reload methods (action type)

| Method | Result | Action |
| --- | --- | --- |
| Removable clip (c) | Remove or insert clip | Simple |
| Speed loader | Fully load gun | Complex |
| Fill clip | Insert (Agility) rounds into clip | Complex |
| Break action (b) | Insert 2 rounds | Complex |
| Belt fed (belt) | Remove or insert belt | Complex |
| Fill belt/drum | Insert (Agility) rounds | Complex |
| Internal magazine (m) | Insert (Agility) rounds | Complex |
| Muzzle-loader (ml) | Load 1 muzzle tube | Complex |
| Cylinder (cy) | Insert (Agility) rounds | Complex |
| Drum (d) | Remove or insert drum | Complex |
| Bow | Nock 1 arrow | Simple |

---

## Matrix actions (type only)

Procedures: Matrix chapter / Matrix Basics. Types on Combat Actions chart include:

| Free (examples) | Simple (examples) | Complex (examples) |
| --- | --- | --- |
| Load/Unload Program; Switch two Matrix Attrs; Swap two Programs; Invite Mark | Call/Dismiss Sprite; Change Icon; Command Sprite; Jack Out; Crash Program; Send Message; Switch Interface Mode; Edit File; Reboot; Set Data Bomb | Brute Force; Hack on the Fly; Data Spike; Matrix Perception; Jump Into Rigged Device; Trace Icon; Thread Complex Form; many others |

Variable: Control Device, Matrix Search, Enter/Exit Host, Erase Mark (GM/action listing).

---

## Coverage notes

- Core Combat Actions Table + Interrupt Init costs: complete for Action Economy.
- Fire mode bullet counts / recoil progression: [Ranged Combat](Ranged%20Combat.md).
- Called shot effects: [Called Shots and Special](Called%20Shots%20and%20Special.md).
