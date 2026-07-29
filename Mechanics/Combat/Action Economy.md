# Combat - Action Economy

Agent reference (SR5). LLM layout; Free / Simple / Complex / Interrupt actions in combat.

**Src PDFs:** `Source/PDF/shadowrunfiftheditioncorerulebook_V2.pdf` · `Source/PDF/runandgun.pdf`
**Printed:** Core Actions ~p.163-168; RnG Killshots/Tactics new actions ~p.119-125
**Source Text:** `11 - Combat.md` · `08 - Killshots and More.md` · `Run and Gun Condensed.md`
**See also:** [Overview](Overview.md) · [Initiative](Initiative.md) · [Ranged Combat](Ranged%20Combat.md) · [Melee Combat](Melee%20Combat.md) · [Martial Arts](Martial%20Arts.md) · [Called Shots and Special](Called%20Shots%20and%20Special.md) · [Small Unit Tactics](Small%20Unit%20Tactics.md) · [Movement](Movement.md)

**Scope:** Core Free/Simple/Complex/Interrupt + RnG combat actions (Killshots/Tactics)
**Out of scope:** Full Matrix procedures; full spellcasting; Barriers

## Inventory (completeness checklist)

- [x] Full Free / Simple / Complex / Interrupt lists (Core tables)
- [x] RnG Simple/Complex/Interrupt additions (Killshots/Tactics)
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

## Run & Gun actions (Killshots / Tactics)

Many require **Martial Art training** unless using Edge **Lucky Move** (`../Edge.md`). MA technique cross-refs: [Martial Arts](Martial%20Arts.md).

### Simple Actions (RnG additions)

| Action | Notes |
| --- | --- |
| **Clinch** | Opposed Gymnastics + Agility [Physical] vs Reaction + Intuition. Negates Reach; initiator gets Superior Position; both may move up to 2 m together; firearm penalty = clinch net hits. Inferior may Escape; superior may release (Free); inferior may Interrupt -5 to re-clinch (+1 dice, no superior bonus to defender). Leads to Subduing, Knock Down, Throw |
| **Iaijutsu** | Quick Draw (properly sheathed/holstered) then attack as **Simple** this Phase |
| **Kip-up** | From prone: Agility + Gymnastics (3); success = close combat attack as Simple (must be in Reach) |
| **Playing Possum** | Complex Con + Charisma vs Con+Charisma or Performance vs Charisma+Willpower. Net hits = Perception threshold for attackers; +1 die per 3 damage boxes (ignore wound mod). Unaware targets get no Defense |
| **Push** | Unarmed vs opponent in Reach; no damage; push min 1 m outside Reach; pusher may Walk. May Intercept -5 if foe enters Reach |
| **Shove** | While running: unarmed attack, no damage. Str + net hits > Physical Limit: push net hits m in movement direction; else stop at obstacle. Fail: fall Prone |
| **Throw Person** | After successful Clinch/Subduing: opposed throw; damage = net hits; max distance = thrower Str - target Body (min 0). May Interrupt -10 after successful Block |

### Complex Actions (RnG additions)

| Action | Notes |
| --- | --- |
| **Aimed Burst** | BF-capable (not SA Burst): +1 DV, 3 rounds, **no** -2 to defender; track recoil |
| **Double-Tap** | SA-capable: +1 DV, 2 rounds, no defense penalty |
| **Brain Blaster** | FA: +2 DV, 6 rounds |
| **Ballestra** | Clubs/blades: +1 Reach; -1 Defense; no active defense until after next Action Phase |
| **Enhanced Suppression** | Suppressive fire: 5 m end width; Drop Prone cannot avoid test |
| **Flechette Suppressive Fire** | See [Called Shots and Special](Called%20Shots%20and%20Special.md) choke tables |
| **Finishing Move** | -10 Init, 1 Edge: if first melee hit damages, extra strike +2 dice; optional taunt Free; once/turn |
| **Flying Kick** | 1+ m approach: +1 Reach and +1 attack; fail = -1 Defense until next Phase |
| **Full Offense** | +2 close combat attack; no defense Interrupts; -5 Init |
| **Half-Sword** | Blade Reach ≥1: +2 AP on hit; fail -2 next non-Defense action, no Parry/Block; must Ready to attack again; both hands |
| **Haymaker** | Opponent +2 Defense; success +1 DV |
| **Herding** | No damage; move foe 1 m/net hit (Walk cap); may split pool |
| **Pouncing Dragon** | Superior position: +2 DV; lose Superior Position after |
| **Reading the Defense** | Melee + Intuition (3) while engaged: +3 next melee vs that foe or -1 on fail; glitch worse; crit glitch -3+ Defense vs any next attack |
| **Sacrifice Move** | Like Shove but Str + **Body** + net hits; both Prone on success |
| **Evade** | With movement: Agility + Gymnastics (1); each hit over threshold bypasses one Interceptor (Shadow Block counters) |

Core reprints in chapter (reference only): Charge Attack, Escape, Subduing, Touch-Only Attack.

### Free Actions (RnG additions)

| Action | Init cost | Effect |
| --- | --- | --- |
| **Pre-emptive Block** | -5 | Block defense option all Combat Turn (only during your Action Phase) |
| **Pre-emptive Dodge** | -5 | Dodge defense option all Combat Turn |
| **Pre-emptive Parry** | -5 | Parry defense option all Combat Turn |

### Interrupt Actions (RnG additions)

| Interrupt | Init | Effect |
| --- | --- | --- |
| **Counterstrike** | -7 | Unarmed + Reaction vs attack; more hits = counter DV + net hits |
| **Riposte** | -7 | Armed: weapon + Reaction vs attack; fail take +2 DV |
| **Reversal** | -7 | Unarmed in clinch: reverse roles; threshold = opponent clinch/subdue hits |
| **Sacrifice Throw** | -10 | Str + Body + net hits vs Physical Limit; both Prone; throw 1 + net hits m |
| **Shadow Block** | -5 | vs Dodge or Evade: Gymnastics + Agility vs target net hits; reduce their hits |
| **Dive for Cover** | -5 | Drop Prone behind cover within 4 m (vs suppression) |
| **Run For Your Life / Dive on Grenade** | -5 | Flee blast with remaining Move; or move toward grenade, Drop Prone, take full blast (gas: half radius) |
| **Right Back At Ya!** | -10 | Agility (2) then Throwing Weapons -2 to return grenade (trigger dependent) |
| **Protecting the Principle** | -5 + 1 Edge | Move 2 m; intercept for ally; no Defense, Body + Armor only; once/turn |

Core Interrupts (Block -5, Dodge -5, Parry -5, Full Defense -10, Hit the Dirt -5, Intercept -5): listed above in Core section.

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
- RnG Killshots/Tactics actions: complete summary.
- Fire mode bullet counts / recoil: [Ranged Combat](Ranged%20Combat.md).
- Called shot effects: [Called Shots and Special](Called%20Shots%20and%20Special.md).
