# Matrix Basics

Agent reference (SR5). LLM layout; persona ASDF, Noise, marks, hosts/IC, Overwatch/convergence, cybercombat, dumpshock, technomancer overview.

**Src PDFs:** `Source/PDF/shadowrunfiftheditioncorerulebook_V2.pdf`
**Printed:** Matrix chapter ~p.214-257 (attrs, damage, modes, Noise, OS, PAN, marks, hosts/IC, technomancers)
**Source Text:** `13 - The Matrix.md`
**See also:** [Dice and Tests](Dice%20and%20Tests.md) · [Rigging Basics](Rigging%20Basics.md) · [Combat/Initiative](Combat/Initiative.md) · Encyclopedia Cyberdecks · *Data Trails* / *Kill Code* for Foundations and advanced hosts

**Scope:** ASDF attrs; deck config; Noise tables; illegal Attack/Sleaze fail results; Overwatch Score + convergence (grid + host); marks; PAN/WAN; hosts/IC overview; Matrix damage / bricking / biofeedback; dumpshock; user modes; Living Persona / threading / Fading overview
**Out of scope:** Full Matrix action list reprint; every IC writeup; full complex-form library; Foundation architecture (Data Trails)

## Inventory (completeness checklist)

- [x] Persona / device attrs; Noise; Overwatch Score
- [x] Marks; Hosts; Foundation pointer
- [x] Cybercombat; Convergence; dumpshock
- [x] Technomancer Living Persona / sprites / complex forms overview

---

## Schema

| Token | Meaning |
| --- | --- |
| ASDF | Attack, Sleaze, Data Processing, Firewall |
| Mark | Access token on an icon (max 3 unless owner) |
| OS | Overwatch Score; illegal trail for GOD |
| Convergence | OS 40: 12 DV Matrix, reboot, location reported |
| Dumpshock | Forced VR disconnect: 6S cold-sim / 6P hot-sim biofeedback |

---

## Matrix attributes (ASDF)

| Attr | Role |
| --- | --- |
| Attack | Illegal offense / brute; Limit for Attack actions |
| Sleaze | Stealth / probe; Limit for Sleaze actions |
| Data Processing | Legal computing; Limit for many DP actions; VR Init key |
| Firewall | Defense / virtual armor |

Commlinks: usually **Data Processing + Firewall** only. Cyberdecks and hosts: all four. Files defend with **owner** ratings.

**Deck config:** At boot, assign the deck's Attribute Array to ASDF. Free Action on your Phase: swap two Matrix attrs **or** swap a running program with a stored one.

---

## User modes

| Mode | Init | Notes |
| --- | --- | --- |
| AR | Meat Initiative | No biofeedback from Black IC-style attacks; may take -2 Perception if glued to AR |
| Cold-sim VR | +2D6 Init dice (3D6 total typical) | Biofeedback → Stun |
| Hot-sim VR | +3D6 Init dice (4D6 total); +1 DP Matrix tests | Biofeedback → Physical; illegal |

---

## Noise

Noise = distance band + situations - Noise Reduction. Leftover positive Noise = **penalty to your Matrix actions** (never to defense/resistance). Direct cable: ignore Noise and cross-grid penalties.

### Distance

| Physical distance to target | Noise |
| --- | --- |
| Directly connected (any distance) | 0 |
| Up to 100 m | 0 |
| 101-1,000 m | 1 |
| 1,001-10,000 m | 3 |
| 10,001-100,000 m | 5 |
| Greater than 100 km | 8 |

### Situations (add)

| Situation | Noise |
| --- | --- |
| Dense foliage | 1 per 5 m |
| Faraday cage | No signal |
| Fresh water | 1 per 10 cm |
| Jamming | 1 per hit on Jam Signals |
| Metal-laced earth/wall | 1 per 5 m |
| Salt water | 1 per cm |
| Spam / static zone | Zone Rating |
| Wireless negation (paint, etc.) | Rating |

Cross-grid: usually **-2** to actions vs other grids. Public grid: **-2** (even in hosts). Hop grids legally or via Brute Force / Hack on the Fly.

---

## Marks

Get marks by invite, **Brute Force** (Attack), or **Hack on the Fly** (Sleaze). Max **3** marks on a target (owners excepted). Marks last until reboot / convergence wipe. Different actions need different mark counts.

**PAN:** Slave up to (Device Rating × 3) devices to a link/deck. Slaves may use master's ratings on defense; mark on slave → mark on master. Direct-wired attack: slave cannot borrow master ratings.

---

## Illegal actions and Overwatch

All **Attack** and **Sleaze** actions are illegal.

| Fail | Result |
| --- | --- |
| Attack | Take 1 unresisted Matrix damage per net hit on defense |
| Sleaze | Target places a mark on you; device alerts owner / host launches IC |

**Overwatch Score:** Starts when you first Attack/Sleaze after a fresh boot. +defense hits on each illegal action; +**2D6** every **15 minutes** (GM secret). Check OS action / Baby Monitor to peek.

### Convergence (OS = 40, on a grid)

1. 12 DV Matrix damage (resist normally).
2. Forced reboot (lose marks); dumpshock if in VR.
3. Physical location reported to grid owner and host (if any).

**Inside a host:** OS still ticks, but at 40 the host gets **3 marks** on you and starts IC instead of grid dump. Leave after host-convergence → demiGOD hits you immediately. Jack out from inside if you can.

Sanctioned spiders/IC do not accrue OS.

---

## Matrix damage

| Rule | Detail |
| --- | --- |
| Monitor | 8 + (Device Rating / 2) boxes |
| Resist | Device Rating + Firewall |
| Full | Device **bricked** until repaired |
| Persona hit | Damage goes to the device running the persona |
| Technomancer | Matrix damage → Stun to meat; resist Device Rating + Firewall |
| Biofeedback | VR only; resist Willpower + Firewall; Stun cold / Physical hot unless stated |

**Dumpshock:** Forced VR drop without graceful AR switch. DV **6S** cold / **6P** hot; resist Willpower + Firewall; **-2** all actions for (10 - Willpower) minutes. Bricked deck → no Firewall on resist.

**Link-lock:** Cannot Switch Interface / Enter-Exit Host / Reboot until Jack Out (usually dumpshock).

---

## Cybercombat (quick)

| Piece | Pointer |
| --- | --- |
| Basic attack | Data Spike (Attack action) |
| Full Defense | Full Matrix Defense |
| Loud mark | Brute Force |
| Quiet mark | Hack on the Fly |

Fighting IC/spiders: hosts share marks and spotting among IC. Host launches **≤1 IC type per Combat Turn**, up to Host Rating programs at once.

### Hosts

Rating 1-12. ASDF usually Rating, Rating+1, Rating+2, Rating+3 in some order. IC uses host attrs. Sample ratings: public/personal 1-2 through megacorp HQ / military 11-12.

**Foundation:** deeper host architecture (Data Trails). Core hosts are enough for most runs.

---

## Technomancers (overview)

No deck required. **Living Persona:**

| Matrix attr | From |
| --- | --- |
| Device Rating | Resonance |
| Attack | Charisma |
| Sleaze | Intuition |
| Data Processing | Logic |
| Firewall | Willpower |

Cannot reconfigure ASDF or run deck programs on living persona; not a slave/master. Natural **hot-sim** only (cold-sim needs gear persona). +2 Matrix Perception. Resonance actions (threading, etc.) do **not** raise OS.

**Threading:** Complex forms; Level up to Resonance × 3; Noise/grid mods apply; sustain **-2** each. **Fading** like Drain: resist Resonance + Willpower; Physical if threading hits > Resonance.

**Sprites:** Compile/register (Resonance skills); analogous to spirits. Full lists in Core Resonance Library / Data Trails.
