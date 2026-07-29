# Character Creation - Resources and Gear

Agent reference (SR5). LLM layout; Priority nuyen spend, chargen gear caps, lifestyle, starting cash.

**Src PDFs:** `Source/PDF/shadowrunfiftheditioncorerulebook_V2.pdf`
**Printed:** Chargen Step Six ~p.94-95; Street Gear Avail/grades ~p.416, 451; Lifestyle ~p.373
**Source Text:** `08 - Creating A Shadowrunner.md` · `21 - Street Gear.md`
**See also:** [Overview](Overview.md) · [Priority System](Priority%20System.md) · [Metatype](Metatype.md) · [Attributes](Attributes.md) · [Magic and Resonance](Magic%20and%20Resonance.md) · `../Housing and Lifestyle.md` · Encyclopedia gear files

**Scope:** Resources Priority yen; Street/Prime overrides; Avail/Device Rating caps; Karma-to-yen; carryover; lifestyle buy-in + starting nuyen; ware grades at chargen; Essence/+4; racial lifestyle cost; gear checklist
**Out of scope:** Full gear catalogs (Encyclopedia); play Availability Test / fencing → [Buying and Fencing Gear](../Buying%20and%20Fencing%20Gear.md); full lifestyle options (Housing)

## Inventory (completeness checklist)

- [x] Priority yen amounts (all play levels)
- [x] Avail <=12 / Device Rating <=6 (and Street/Prime)
- [x] Karma to yen 2,000/Karma caps; <=5,000 yen carryover; starting nuyen lifestyle dice
- [x] Lifestyle buy-in months; dwarf +20% / troll +100% lifestyle
- [x] Fake SIN / licenses; ammo; must-buy reminders
- [x] Augment Essence / +4 Attr reminder
- [x] Implant grade multipliers (standard / alpha / used at chargen)

---

## Schema

| Token | Meaning |
| --- | --- |
| Resources pool | Priority yen (+ optional Karma convert) |
| Carryover | Unspent Resources <=5,000 yen into play |
| Starting nuyen | Lifestyle dice result + carryover |
| Avail | Number (+ optional R/F); chargen max by play level |

---

## Resources Priority (yen)

| Pri | Experienced | Street-Level | Prime Runner |
| --- | --- | --- | --- |
| A | 450,000 | 75,000 | 500,000 |
| B | 275,000 | 50,000 | 325,000 |
| C | 140,000 | 25,000 | 210,000 |
| D | 50,000 | 15,000 | 150,000 |
| E | 6,000 | 6,000 | 100,000 |

Assign last Priority letter to Resources (Overview / Priority System).

---

## Chargen purchase caps

| Play level | Max Availability | Max Device Rating |
| --- | --- | --- |
| Street-Level | 10 | 4 |
| Experienced (default) | **12** | **6** |
| Prime Runner | 15 | 6 |

| Rule | Detail |
| --- | --- |
| R / F | Restricted / Forbidden letter still OK if numeric Avail within cap |
| GM veto | Always applies, even if Avail/Device Rating legal |
| After play starts | Higher Avail/Device Rating via Availability Tests / runs (Street Gear) |

### Augmentation caps (chargen)

| Rule | Detail |
| --- | --- |
| Attr bonus | All sources combined: Mental/Physical attr bonus <= **+4** |
| Grades available | **Standard**, **alphaware**, **used** only (no beta/delta at creation) |
| Essence | Starts 6; ware reduces Essence (apply grade multiplier) |
| Mag/Res | Essence loss reduces Magic/Resonance (see Magic and Resonance) |
| Racial replace | Cybereyes replace natural low-light (must buy mod back); orthoskin replaces troll +1 dermal armor |
| Sheet notation | Natural (augmented), e.g. Strength 4 (6) |
| Free pools | Ware does **not** raise Knowledge free points or contact Karma (use unaugmented Int/Log/Cha) |
| Limits / Init | Ware **does** count for Final Calculations |
| Same grade | Accessories/add-ons must match the implant's grade |

### Implant grades (chargen-legal)

Prices in gear lists are **standard**. Apply multipliers:

| Grade | Essence cost | Availability | Cost | At chargen? |
| --- | --- | --- | --- | --- |
| Standard | ×1.0 | - | ×1 | Yes |
| Alphaware | ×0.8 | +2 | ×1.2 | Yes |
| Used | ×1.25 | −4 | ×0.75 | Yes |
| Betaware | ×0.7 | +4 | ×1.5 | **No** |
| Deltaware | ×0.5 | +8 | ×2.5 | **No** |

Used is its own grade (no "used alphaware").

---

## Karma to yen (gear only)

| Play level | Max Karma convert | Rate | Max extra yen |
| --- | --- | --- | --- |
| Street-Level | 5 | 2,000 yen / Karma | 10,000 |
| Experienced | **10** | 2,000 yen / Karma | **20,000** |
| Prime Runner | 25 | 2,000 yen / Karma | 50,000 |

| Rule | Detail |
| --- | --- |
| Direction | Karma -> yen only (cannot convert Resources yen to Karma) |
| Timing | During Step Six (and still subject to gear caps) |

---

## Spend / carryover

| Rule | Detail |
| --- | --- |
| Intent | Spend vast majority of Resources pool on gear + lifestyle |
| Carryover max | Keep **<= 5,000 yen** unspent; add to starting nuyen |
| Excess | Any unspent Resources **over 5,000 is lost** |
| Form in play | Carryover + starting nuyen as cash/credsticks/accounts (GM) |

---

## Lifestyle (chargen)

Buy one or more months of a lifestyle with Resources. Monthly costs:

| Lifestyle | Cost / month |
| --- | --- |
| Street | Free |
| Squatter | 500 yen |
| Low | 2,000 yen |
| Middle | 5,000 yen |
| High | 10,000 yen |
| Luxury | 100,000 yen |

| Metatype | Lifestyle cost modifier |
| --- | --- |
| Dwarf | **+20%** |
| Troll | **+100%** (double) |
| Others | x1 |

Examples: Low x 3 months = 6,000 yen; troll Low x 3 months = 12,000 yen.

Full lifestyle options / permanent buy: `../Housing and Lifestyle.md`.

---

## Starting nuyen (into play)

```
Starting nuyen = (Lifestyle Starting Nuyen roll) + (Resources carryover <= 5,000)
```

| Lifestyle | Starting Nuyen roll |
| --- | --- |
| Street | 1D6 x 20 yen |
| Squatter | 2D6 x 40 yen |
| Low | 3D6 x 60 yen |
| Middle | 4D6 x 100 yen |
| High | 5D6 x 500 yen |
| Luxury | 6D6 x 1,000 yen |

If multiple lifestyles prepaid, use the lifestyle that defines how the character lives day-to-day (primary); GM call if split (e.g. Middle home + Low safehouse).

---

## Gear checklist (Core essentials)

Buy from Encyclopedia / Street Gear as needed:

| Category | Notes |
| --- | --- |
| Weapons (melee / ranged) | + holsters, accessories |
| Ammunition | Easy to forget; expensive specialty ammo |
| Clothing / armor | Mods (fire resist, nonconductivity, etc.) |
| Cyberware / bioware | Grades + Essence |
| Commlink | Nearly mandatory |
| Fake SIN(s) + fake licenses | Guns, magic, driving, etc. |
| Cyberdeck + programs | Deckers |
| Tools / B&E / surveillance / sensors | |
| Lifestyle (months) | Above |
| Vehicle(s) / drones | Riggers especially |
| Biotech / DocWagon | Medkit, contract |
| Magical goods | Foci, lodge materials, reagents |
| Certified credstick(s) | Hold carryover / starting cash |
| Disguises | |

---

## Procedure (Step Six)

1. Take Priority Resources yen for play level.
2. Optional: convert Karma to yen (cap above).
3. Buy gear within Avail / Device Rating / GM approval.
4. Buy lifestyle months (apply dwarf/troll %).
5. Leave <=5,000 yen unspent; lose the rest of the pool.
6. Roll Starting Nuyen for primary lifestyle; add carryover.
7. Note Essence, Mag/Res loss, augmented attrs for Final Calculations.

---

## Coverage notes

- Chargen Resource rules matched to Core Step Six + Alternate Gameplay.
- Item prices/Avail: Encyclopedia catalogs; play Acquisition Tests not expanded here.
- Checklist Core example once said troll "+50% gear"; Metatype Attribute Table only doubles **Lifestyle**. Use lifestyle modifiers only unless a specific gear line says otherwise.
