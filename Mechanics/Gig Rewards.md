# Gig Rewards

Agent reference (SR5). LLM layout; run pay, Karma awards, Street Cred / Notoriety / Public Awareness; Karma spend pointer.

**Src PDFs:** `Source/PDF/shadowrunfiftheditioncorerulebook_V2.pdf`
**Printed:** Reputation ~p.372-373; Run Rewards ~p.375-376; Character Advancement ~p.103-107
**Source Text:** `19 - Gamemaster Advice.md` · Advancement costs in `08 - Creating A Shadowrunner.md` / [Finishing Touches](Character%20Creation/Finishing%20Touches.md)
**See also:** [Actions Outside Combat](Actions%20Outside%20Combat.md) (Street Cred on Social) · [Advancement](Advancement.md) (Karma spend costs) · [Housing and Lifestyle](Housing%20and%20Lifestyle.md) · Character Creation Qualities

**Scope:** Optional Cash Rewards formula; Karma Rewards table; Street Cred / Notoriety / Public Awareness; BTB alternate Cred/Karma spends; Notoriety quality list; Public Awareness bands; Karma spend pointer (to Advancement)
**Out of scope:** Full Positive/Negative quality writeups; Karma spend costs (see [Advancement](Advancement.md), not duplicated here); Negotiation scene scripting; campaign-specific bonus gear

## Inventory (completeness checklist)

- [x] Run pay guidelines; Karma awards
- [x] Street Cred / Notoriety / Public Awareness formulas
- [x] Better Than Bad alternate Karma / Street Cred spends

---

## Schema

| Token | Meaning |
| --- | --- |
| Base pay | 3,000¥ per runner + 100¥ per Negotiation net hit |
| Multiplier | (Highest opposing Active dice pool / 4, down) + danger adds |
| Street Cred | Floor(total Karma earned / 10); Social Limit mod when known |
| Notoriety | Bad-rep score; min 0 |
| Public Awareness | How famous outside the shadows |

---

## Cash (optional guidelines)

Per player who participated. Negotiate at Mr. Johnson meet; Karma after the run.

### Formula

1. **Base** = 3,000¥ + **100¥ × Negotiation net hits** (start of run).
2. **Multiplier** = (highest meaningful opposing **Active** Skill+Attr pool / 4, round down) + table adds. Count permanent ware/magic; not gear/situational mods. Only pools that actually opposed the runners.
3. Pay = Base × Multiplier, then apply cost type %.

### Cash Rewards modifiers (add to multiplier)

| Situation | Modifier |
| --- | --- |
| Highest opposing Dice Pool | +(Dice Pool / 4) |
| Outnumbered 3:1 in combat | +1 |
| Outnumbered 2:1 by Professional Rating 4+ (not cumulative with 3:1) | +1 |
| Faced pack of ≥6 critters | +1 |
| Encountered ≥3 different spirits (not watchers) in one encounter | +1 |
| Impressive speed and/or subtlety | +1 |
| Risked public exposure / raised profile as natural part of run | +1 |
| Direct contact with notably dangerous Sixth World element (Red Samurai, MCT Zero Zone, etc.) | +1 |

### Cost type %

| Type | Modifier |
| --- | --- |
| Standard run | 0% |
| Cold-hearted bastard (wetwork, corp oppression, drugs, trafficking, etc.) | +10-20% |
| Good feelings (hooding, help little guy) | -10-20% |

GM may add bonus equipment. Team share / fixer cut: negotiate before the run.

---

## Karma awards

Add situations, then apply **same** good/evil modifier family as cash (if used).

### Karma Rewards

| Situation | Karma |
| --- | --- |
| Character survived | 2 |
| Group completed all objectives | 2 |
| Group completed some objectives | 1 |
| Overall adventure challenge | Highest opposed Dice Pool / 6 (round down) |

### Karma Modifiers

| Type | Modifier |
| --- | --- |
| Standard run | 0 |
| Cold-hearted bastard run | -2 |
| Good feelings run | +2 |

---

## Reputation

Three separate scores.

### Street Cred

| Rule | Detail |
| --- | --- |
| Formula | Floor(**total Karma earned** / 10); GM may add for noteworthy feats |
| Use | Positive **Limit** modifier on Social Tests when reputation is known |
| Trade | Sacrifice **2** Street Cred to remove **1** Notoriety |

### Better Than Bad: alternate Karma / Street Cred spends

**Verified from:** `Better Than Bad Condensed.md`. Karma and Street Cred are interchangeable for these (GM discretion where noted).

| Spend | Cost |
| --- | --- |
| Raise contact **Loyalty** by 1 | Karma/Cred equal to new Loyalty (max Loyalty 4); that many months; one such change at a time |
| Raise contact **Connection** by 1 | 10 Karma/Cred total; need Loyalty ≥ 3; once per contact |
| Influence skill group test bonus | 1 Karma or Cred per +1 die, max 3/test |
| Faction Reputation +1 | Equal to new score (max 3 this way); months = new score; one change at a time |
| Lifestyle payment -1 level | 1 Karma or Cred per 1,000¥ saved; ends if lifestyle changes |
| Call favor (GM OK) | 2 x Favor Rating; capped by contact Loyalty; owe equal/lesser favor back or lose Street Cred equal to spend |

Also: **Consummate Professional** quality halves Street Cred gain (total Karma / 20 instead of / 10). See [Qualities Supplemental](Character%20Creation/Qualities%20Supplemental.md).

### Notoriety

Starts at 0. Adjust for qualities (min 0): **+1** per listed Negative, **-1** per listed Positive.

**Positive (reduce):** Blandness, First Impression, Lucky

**Negative (increase):** Addiction, Bad Luck, Combat Paralysis, Elf Poser, Gremlins, Incompetent (any), Ork Poser, Scorched, SINner (criminal SIN only), Spirit Bane, Uncouth, Uneducated, Weak Immune System

GM may award +1 Notoriety in play for stains (refuse to finish run, piss off Johnson, betray teammates, kill innocents, work for a dragon, etc.). No double-dip for the same act. High Notoriety makes contacts colder.

### Public Awareness

How well media / public / authorities know you. Award for loud fails (fight HTR, extract celebrities, explode in crowds, leave evidence, broadcast crimes, etc.).

#### Public Awareness Table

| Rating | Awareness |
| --- | --- |
| 0-3 | Unheard of outside the shadow community |
| 4-6 | Known to shadow-watchers (conspiracy types, specialty LE) |
| 7-9 | Known by those in the know (investigative press, LE, some officials) |
| 10+ | Household name; sim/trid portrayals |

---

## Spending Karma (advancement)

Full Karma costs (attributes, skills, specializations, qualities, initiate/submersion grades), training rates, and downtime limits live in [Advancement](Advancement.md) - not duplicated here to avoid drift. Key point since it's easy to get wrong: buying a **Positive quality** or buying off a **Negative quality** in play costs the listed Karma value **x2**, not the flat listed value (see Advancement's Qualities in play table).

Post-chargen Active skill max normally **12** (13 with Aptitude). Instruction can cut training time ([Actions Outside Combat](Actions%20Outside%20Combat.md)).
