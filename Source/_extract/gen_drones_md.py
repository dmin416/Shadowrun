# -*- coding: utf-8 -*-
"""Generate Encyclopedia/Drones.md from verified Core + Rigger 5 data."""
from pathlib import Path

OUT = Path(r"c:\Users\admin\Desktop\Shadowrun\Encyclopedia\Drones.md")

# Each entry: dict with fixed keys for LLM parsing.
# size: Micro|Mini|Small|Medium|Large|Huge|Anthro|Missile|Chassis|Pointer
# src: Core|R5|Core+R5
# skill: Pilot skill
# handl,speed,accel,body,armor,pilot,sensor,seats,avail,cost
# upgrades, similar, rules (mechanical only), notes

def E(**kw):
    return kw

DRONES = []

# ---- MICRO ----
DRONES += [
E(name="Shiawase Kanmushi", size="Micro", src="Core p.465; R5 table p.190",
  skill="Pilot Walker",
  handl="4", speed="2", accel="1", body="0", armor="0", pilot="3", sensor="3",
  seats="—", avail="8", cost="1,000¥",
  upgrades="Gecko tips (walls/ceilings)",
  similar="",
  rules="Four-legged bug crawler; hard to tell from insect at a glance. Fragile: easily destroyed by being stepped on or a tag eraser. Confined-space infiltration."),
E(name="Sikorsky-Bell Microskimmer", size="Micro", src="Core p.465; R5 table p.190",
  skill="Pilot Ground Craft (Hovercraft specialization applies)",
  handl="3", speed="3", accel="1", body="0", armor="0", pilot="3", sensor="3",
  seats="—", avail="6", cost="1,000¥",
  upgrades="",
  similar="",
  rules="Disc-shaped skimmer smaller than a frisbee; can skim over water via weak hoverjets. Easier to spot than Kanmushi but still very small."),
E(name='Horizon "NoizQuito"', size="Micro", src="R5 p.128",
  skill="Pilot Aircraft",
  handl="4", speed="3R", accel="2", body="1", armor="0", pilot="3", sensor="3",
  seats="—", avail="10R", cost="2,000¥",
  upgrades="Flying; speakers; strobes",
  similar="",
  rules="Mosquito-like. Speakers blast up to 160 dB. Wings/body LEDs produce blinding strobes. GAME: Strobes impose -2 to all actions by those looking at the drone (-1 with flare compensation). Speakers impose -2 to all actions by those in earshot (-1 with sound damper). Multiple drones in a group: penalties stack per drone (up to -12 from three drones with both effects). Earshot = GM call."),
E(name="Sony Goldfish", size="Micro", src="R5 p.128–129",
  skill="Pilot Watercraft",
  handl="2/4", speed="1W", accel="1", body="0", armor="0", pilot="2", sensor="2",
  seats="—", avail="6", cost="500¥",
  upgrades="Submersible (dives up to 4 m)",
  similar="Mitsuhama Minnow; NeoNET Pinkeens",
  rules="Realistic fish proportions. Entry-level water microdrone. Water heavily degrades wireless signal."),
]

# ---- MINI ----
DRONES += [
E(name="Horizon Flying Eye", size="Mini", src="Core p.465–466; R5 table p.190",
  skill="Pilot Aircraft",
  handl="4", speed="3", accel="2", body="1", armor="0", pilot="3", sensor="3",
  seats="—", avail="8", cost="2,000¥ (flash-pak/smoke variant +500¥)",
  upgrades="",
  similar="",
  rules="Eyeball-sized spherical VTOL with omnidirectional thrust. Can roll on ground; must fly to clear stairs/curbs. Optional built-in flash-pak + smoke grenade (+500¥); detonating either destroys the drone. Cybereye ocular drone (Core) functions as this model when removed."),
E(name="MCT Fly-Spy", size="Mini", src="Core p.466; R5 table p.190",
  skill="Pilot Aircraft",
  handl="4", speed="3", accel="2", body="1", armor="0", pilot="3", sensor="3",
  seats="—", avail="8", cost="2,000¥",
  upgrades="",
  similar="",
  rules="Large-insect sized/shaped flyer; better altitude than micro bugs. Eye-in-sky / shadowing; relatively hard to spot."),
E(name="Aerodesign Systems Condor LDSD-23", size="Mini", src="R5 p.129",
  skill="Pilot Aircraft",
  handl="2", speed="0R", accel="0", body="1(1)", armor="0", pilot="2", sensor="4",
  seats="—", avail="6R", cost="4,000¥",
  upgrades="",
  similar="Ares Cloudship; Renraku Buzzard",
  rules="Solar-powered hydrogen balloon long-duration observation drone. Transparent / radar-invisible materials. Can hover for days–weeks. Deflated: smaller than bowling pin; inflated balloon ~kitchen table. Completely vulnerable if detected; cannot flee."),
E(name="Aztechnology Hedgehog", size="Mini", src="R5 p.129",
  skill="Pilot Ground Craft",
  handl="3", speed="1G", accel="1", body="1(0)", armor="0", pilot="4", sensor="3",
  seats="—", avail="8F", cost="8,000¥",
  upgrades="Electronic Warfare (2) autosoft",
  similar="Ares NS-Aardvark; Lone Star Mockingbird",
  rules="Crawler sub-design of Aztechnology Crawler. Security-sniffing: find C3 broadcasts; passive listen + decrypt. Hidden: up to 48 hours on one charge."),
E(name="Cyberspace Designs Dragonfly", size="Mini", src="R5 p.129",
  skill="Pilot Aircraft",
  handl="4", speed="2P", accel="1", body="1(0)", armor="3", pilot="3", sensor="2",
  seats="—", avail="12R", cost="4,000¥",
  upgrades="Melee Bite Acc 3, Reach —, DV 3P, AP -2; Targeting (Melee) autosoft",
  similar="Ares Sparrowhawk (mounts modified Ares Light Fire 70); Renraku Yokujin",
  rules="Quad-copter anti-drone hunter. Protected in-body rotors. Beak shears mini/micro drones. Can swarm larger drones but not designed vs appreciable armor."),
E(name="Festo Pigeon 2.0", size="Mini", src="R5 p.129",
  skill="Pilot Exotic Vehicle",
  handl="4", speed="2P", accel="1", body="1(1)", armor="0", pilot="2", sensor="2",
  seats="—", avail="8", cost="3,000¥",
  upgrades="Realistic Features (1)",
  similar="Sony Nightingale; Renraku Bluebird",
  rules="Lifelike flying bird drone (baseline chrome; lifelike model common for surveillance)."),
E(name="Horizon CU^3", size="Mini", src="R5 p.130",
  skill="Pilot Aircraft",
  handl="4", speed="1P", accel="1", body="1(1)", armor="0", pilot="2", sensor="3",
  seats="—", avail="4", cost="3,000¥",
  upgrades="Clearsight (2) autosoft",
  similar="MCT Redlight; Evo CultureCapture",
  rules="Single-fan vectored-thrust camera drone; stable, quiet. Optional Professional Upgrade: Pilot 4 + Clearsight 4 for +3,000¥. Pros often run three for multi-angle."),
E(name="Renraku Gerbil", size="Mini", src="R5 p.130",
  skill="Pilot Ground Craft",
  handl="4/2", speed="2G", accel="1", body="1(1)", armor="0", pilot="2", sensor="2",
  seats="—", avail="4", cost="2,000¥",
  upgrades="",
  similar="GM-Nissan Mouse; MCT Zipper",
  rules="Tiny wheeled; fits ventilation shafts and most pipes. Quick/nimble vs metahuman pursuit."),
E(name="Renraku Scuttler Remote Cyberhand", size="Mini", src="R5 p.130",
  skill="Pilot Walker",
  handl="n/a", speed="n/a", accel="n/a", body="n/a", armor="n/a", pilot="n/a", sensor="—",
  seats="—", avail="8", cost="8,000¥",
  upgrades="",
  similar="Evo Hi-Five; Ares Thing",
  rules="Detachable cyberhand with remote rigger controls + computer. Middle digit: poor sensor suite; other four digits for locomotion. Better manipulation than similar-size drones; less quick/nimble due to hand shape. No Capacity for further upgrades. CYBERWARE TABLE: Essence 0.25, Capacity (5), Avail 8, Cost 8,000¥."),
]

# ---- SMALL ----
DRONES += [
E(name="Aztechnology Crawler", size="Small", src="Core p.466; R5 table p.189",
  skill="Pilot Walker",
  handl="4", speed="3", accel="1", body="3", armor="3", pilot="4", sensor="3",
  seats="—", avail="4", cost="4,000¥",
  upgrades="",
  similar="",
  rules="Handles stairs/obstacles. Remote snooper for rough rural/urban terrain. Pilot a step above most of its class."),
E(name="Lockheed Optic-X2", size="Small", src="Core p.466; R5 table p.191",
  skill="Pilot Aircraft",
  handl="4", speed="4", accel="3", body="2", armor="2", pilot="3", sensor="3",
  seats="—", avail="10", cost="21,000¥",
  upgrades="Signature-limiting stealth",
  similar="",
  rules="VSTOL stealth. Wings folded: cyberdeck-sized; deployed: large hawk / bird of prey. Radar systems and visual/audio Perception Tests: -3 dice pool to spot."),
E(name="Ares Arms Sentry V", size="Small", src="R5 p.130–131",
  skill="Pilot Ground Craft",
  handl="4/—", speed="1G", accel="1", body="2(0)", armor="6", pilot="3", sensor="2",
  seats="—", avail="4R", cost="4,000¥",
  upgrades="Standard weapon mount; Colt Cobra TZ-120; 30 standard ammo; Targeting (3); SmartSoft",
  similar="Shpagina Evo-2; Shiawase Minebea GridSys",
  rules="Rail-drone: hangs from facility rails; draws power + accepts commands via rail (impervious to wireless hijack; works on dedicated secondary power in blackouts). Mercury variant: unarmed courier on same rail system (messages/packages); in active hostiles Mercuries store out of way for Sentry deployment."),
E(name="Citron-Brouillard Smoke Generator", size="Small", src="R5 p.130–132",
  skill="Pilot Ground Craft",
  handl="3", speed="1G", accel="1", body="2(0)", armor="0", pilot="2", sensor="2",
  seats="—", avail="8", cost="4,000¥",
  upgrades="Smoke generator: 12 one-minute doses normal smoke + 3 one-minute doses thermal (IR-blocking) smoke",
  similar="",
  rules="Tracked. Stationary: billowing screen ~150 m diameter. Rolling: trail ~100 m wide × 250 m long. Cloud ~10 m high. Begins dissipating 1 minute after shutoff (becomes light cloud); fully gone 1 minute later. Other gases fit tank but not at proprietary smoke volume."),
E(name="Cyberspace Designs Wolfhound", size="Small", src="R5 p.131–132",
  skill="Pilot Aircraft",
  handl="3", speed="2J", accel="1", body="2(1)", armor="0", pilot="2", sensor="4",
  seats="—", avail="12", cost="30,000¥",
  upgrades="",
  similar="Ares Sergeant; S-K Dawnrider",
  rules="Recon: high sensors + speed over durability/arms. Only drone of its size to break sound barrier; usually stays subsonic to conceal location."),
E(name="Evo Proletarian", size="Small", src="R5 p.131–132",
  skill="Pilot Ground Craft",
  handl="4/2", speed="2G", accel="1", body="2(1)", armor="0", pilot="2", sensor="2",
  seats="—", avail="6", cost="4,000¥",
  upgrades="Drone arm (STR 4, AGI 2); Automotive Mechanic Toolkit; Automotive Mechanic (2) autosoft",
  similar="",
  rules="Three-wheeled mechanic assistant (dents, tires, oil, tools, schematics display, undercarriage watch, speakers). Many repair/construction/butler autosofts available."),
E(name="Ferret RPD-5X Wheeled Perimeter Drone", size="Small", src="R5 p.132 (text also RPD-1X); table RPD-5X",
  skill="Pilot Ground Craft",
  handl="4/2", speed="1G", accel="1", body="2(1)", armor="3", pilot="3", sensor="3",
  seats="—", avail="8R", cost="4,000¥",
  upgrades="Mini weapon mount; Defiance Shocker; 4 taser darts; flashlight",
  similar="Aztechnology IDS; NeoNET Janus",
  rules="Cheap light security patrol. Awful off-road; stay on established paths."),
E(name="Festo Sewer Snake", size="Small", src="R5 p.132",
  skill="Pilot Ground Craft / water as applicable",
  handl="3", speed="1G/1W", accel="1/1", body="2(1)", armor="0", pilot="2", sensor="2",
  seats="—", avail="10", cost="6,000¥",
  upgrades="Submersible; gecko grips",
  similar="",
  rules="Slither + swim; long narrow body. Gecko grips for vertical climb. Handles 10 m dive pressure. Little room for further mods."),
E(name="Horizon Mini-Zep", size="Small", src="R5 p.132",
  skill="Pilot Aircraft",
  handl="2", speed="0P", accel="0", body="2(4)", armor="0", pilot="2", sensor="2",
  seats="4", avail="4", cost="2,000¥",
  upgrades="Electrochromatic coating on airbag",
  similar="",
  rules="LtA ad drone. Electrochromic ads; small radio transmitter for AR spam to nearby commlinks. Loiter ~8 hours via fans. Can rebroadcast weather/APB/etc. Seats 4 in compiled table (passenger/rack capacity as printed)."),
E(name="Knight Errant P5 Pursuit Drone", size="Small", src="R5 p.133–134",
  skill="Pilot Ground Craft",
  handl="4/2", speed="6G", accel="2", body="2(1)", armor="0", pilot="3", sensor="2",
  seats="—", avail="10R", cost="8,000¥",
  upgrades="",
  similar="",
  rules="Limpet pursuit drone from KE cruisers. Top speed: batteries last 10 minutes. Magnetically attaches to pursued vehicle undercarriage; KE tracks wireless signal. Broadcast uses second battery (~24 hour life)."),
E(name="Lone Star Castle Guard", size="Small", src="R5 p.133–134",
  skill="Pilot Ground Craft",
  handl="4/2", speed="1G", accel="1", body="2(0)", armor="6", pilot="3", sensor="2",
  seats="—", avail="8R", cost="10,000¥",
  upgrades="Light weapon mount; Targeting (3); Smartsoft; four SmartSafety bracelets",
  similar="",
  rules="Home-security pistol-armed drone (CAS common). Extra SmartSafety bracelets/pet collars: 50¥ each. CAS tooling differs from metric (repair kit note)."),
E(name="Mitsuhama Gun Turret", size="Small", src="R5 p.133–134",
  skill="No Pilot skill required (immobile)",
  handl="—", speed="—", accel="—", body="2(0)", armor="6", pilot="3", sensor="2",
  seats="—", avail="4R", cost="4,000¥",
  upgrades="Standard weapon mount. Standard Downgrade: Immobile",
  similar="",
  rules="Rotates only; cheap Zero-Zone staple. Common variants: Retractable or Up-Armored; some take larger mount."),
E(name="Mitsuhama Seven (core / Wheelie)", size="Small", src="R5 p.133–135",
  skill="Pilot Ground Craft (chassis-dependent)",
  handl="4/2", speed="2G", accel="1", body="1(3)", armor="0", pilot="1", sensor="1",
  seats="—", avail="—", cost="2,000¥",
  upgrades="Fragile (1)",
  similar="",
  rules="Bare-bones hobbyist chassis (launched 2077). Official IDs 77-MPD-01+. Standard Upgrades Fragile (1) on line. See chassis SKUs below for other locomotion packs."),
E(name="Mitsuhama Seven Treads", size="Chassis", src="R5 p.135; table p.191",
  skill="Pilot Ground Craft",
  handl="3", speed="2G", accel="1", body="1(3)", armor="0", pilot="1", sensor="1",
  seats="—", avail="2", cost="2,000¥",
  upgrades="Fragile (1)", similar="", rules="Tracked Seven chassis."),
E(name="Mitsuhama Seven Dirty", size="Chassis", src="R5 p.135; table p.191",
  skill="Pilot Ground Craft",
  handl="2/4", speed="2G", accel="1", body="1(3)", armor="0", pilot="1", sensor="1",
  seats="—", avail="2", cost="2,000¥",
  upgrades="Fragile (1)", similar="", rules="Off-road suspension Seven chassis."),
E(name="Mitsuhama Seven Quad", size="Chassis", src="R5 p.135; table p.191",
  skill="Pilot Walker",
  handl="4", speed="1G", accel="1", body="1(3)", armor="0", pilot="1", sensor="1",
  seats="—", avail="4", cost="2,000¥",
  upgrades="Fragile (1)", similar="", rules="Four-legged Seven chassis."),
E(name="Mitsuhama Seven Swims", size="Chassis", src="R5 p.135; table p.191",
  skill="Pilot Watercraft",
  handl="3", speed="2W", accel="1", body="1(3)", armor="0", pilot="1", sensor="1",
  seats="—", avail="4", cost="1,000¥",
  upgrades="Fragile (1)", similar="", rules="Surface-aquatic Seven chassis."),
E(name="Mitsuhama Seven Hovers", size="Chassis", src="R5 p.135; table p.191",
  skill="Pilot Aircraft",
  handl="4", speed="1P", accel="1", body="1(3)", armor="0", pilot="1", sensor="1",
  seats="—", avail="6", cost="4,000¥",
  upgrades="Fragile (1)", similar="", rules="Quad-copter Seven chassis."),
E(name="Mitsuhama Seven Soars", size="Chassis", src="R5 p.135; table p.191",
  skill="Pilot Aircraft",
  handl="3", speed="2J", accel="1", body="1(3)", armor="0", pilot="1", sensor="1",
  seats="—", avail="8", cost="4,000¥",
  upgrades="Fragile (1)", similar="", rules="Traditional flyer Seven chassis."),
E(name="NeoNET Prairie Dog", size="Small", src="R5 p.134–135",
  skill="Pilot Ground Craft",
  handl="2/4", speed="2G", accel="1", body="2(0)", armor="3", pilot="3", sensor="4",
  seats="—", avail="12F", cost="8,000¥",
  upgrades="Electronic Warfare (3) autosoft; directional jammer (4); area jammer (6)",
  similar="",
  rules="Decommissioned PCC military ECM/jamming infantry drone. Large off-road wheels; keeps pace with dismounted infantry. Demilitarized civilian version still antenna-heavy."),
E(name="Pratt & Whitney Sundowner", size="Small", src="R5 p.134–135",
  skill="Pilot Aircraft",
  handl="3", speed="4P", accel="1", body="2(0)", armor="0", pilot="2", sensor="2",
  seats="—", avail="8", cost="10,000¥",
  upgrades="Aerial chemical sprayer: 10 doses; each covers line 125 m long × 25 m wide × 10 m high; large spray doses cost 10× normal dose cost",
  similar="Shiawase Hyakusho; Aztechnology Roundup",
  rules="Low-speed agricultural spray / skywriting aircraft."),
E(name='Proteus A.G. "Krake"', size="Small", src="R5 p.134–137",
  skill="Pilot Watercraft",
  handl="5", speed="3W", accel="4", body="2(0)", armor="2", pilot="4", sensor="3",
  seats="—", avail="18F", cost="10,000¥",
  upgrades="Plasma torch; specialized weapon (ink pouch); Nautical Mechanic toolkit; weapon mount",
  similar="",
  rules="Squid-form; six tentacles for propulsion/agility. One tentacle: plasma torch + multitool (touch range only; useless in combat). Optional security retrofit: micro-torpedo cluster + ink pouch. INK: cloud of ink + metal-flake chafe; obscures vision (even electronic) in 5 m radius; Heavy Smoke penalty for attacks through cloud. MICRO-TORPEDOES (bought separate): Chemical warhead DV 6P AP -4 Blast 1 m radius Avail 18F Cost 3,000¥ (acidic adhesive: continuous damage each Combat Turn until glue solvent, Core p.448). Explosive warhead DV 18P AP -4/-10 Blast -6/m Avail 18F Cost 2,500¥ (as anti-vehicle rockets: -4 AP vs non-vehicles, -10 AP vs vehicles)."),
E(name="SAAB-Thyssen Bloodhound", size="Small", src="R5 p.136–137",
  skill="Pilot Ground Craft",
  handl="3", speed="1G", accel="1", body="2(0)", armor="0", pilot="2", sensor="4",
  seats="—", avail="8", cost="10,000¥",
  upgrades="Geiger counter (6); olfactory scanner (8)",
  similar="",
  rules="Hazmat exploration. Identifies bio/chem/rad; marks with color-coded RFID flags; scoop + storage for soil samples."),
E(name="Renraku Dove", size="Small", src="R5 p.136–137",
  skill="Pilot Aircraft",
  handl="4", speed="2P", accel="1", body="2(1)", armor="0", pilot="2", sensor="2",
  seats="—", avail="4", cost="5,000¥",
  upgrades="Radio signal scanner (6)",
  similar="",
  rules="Licensed exclusively to GOD. Quiet sprawl patrol for illegal wireless; alerts GOD for heavier response. Table name Dove-4 in writeup header."),
E(name="Renraku Jardinero", size="Small", src="R5 p.136–137",
  skill="Pilot Ground Craft",
  handl="2/4", speed="1G", accel="1", body="2(1)", armor="0", pilot="2", sensor="2",
  seats="—", avail="4", cost="2,000¥",
  upgrades="",
  similar="Dozens of Renraku chassis variants (vacuum, floor polish, parking-lot paint, etc.)",
  rules="Automated lawn mower (silent electric). Shared Renraku chassis family."),
E(name="Renraku Job-a-Mat", size="Small", src="R5 p.137–138",
  skill="No Pilot skill required (immobile)",
  handl="—", speed="—", accel="—", body="2(2)", armor="0", pilot="2", sensor="2",
  seats="—", avail="4", cost="3,000¥",
  upgrades="Profession or Knowledge (2) autosoft. Downgrade: Immobile",
  similar="",
  rules="Immobile service kiosk chassis (BarristaBot, Intern paperwork, etc.). ~two dozen marketed models. Odd requests escalate to rigger backup. Renraku branding often omitted."),
E(name="Renraku Pelican", size="Small", src="R5 p.137–138",
  skill="Pilot Aircraft",
  handl="4", speed="2P", accel="1", body="2(1)", armor="0", pilot="2", sensor="2",
  seats="—", avail="2", cost="4,000¥",
  upgrades="Storage compartment (heated/cooled modular underhung)",
  similar="MCT Transporter-3; Evo Kourier",
  rules="Quad-copter delivery drone (food wholesale)."),
E(name="Telestrian Industries Shamus", size="Small", src="R5 p.137–139",
  skill="Pilot Ground Craft",
  handl="3", speed="3G", accel="1", body="4(0)", armor="4", pilot="3", sensor="8",
  seats="—", avail="10", cost="30,000¥",
  upgrades="Quicksilver camera; Sensor array Rating 8 with: atmosphere sensor; camera (low-light, normal, thermographic); Geiger; MAD; olfactory; radio signal scanner; ultrasound; X-ray",
  similar="",
  rules="Forensic walker (canine/arachnid). Projects trideo crime-scene reconstruction to investigator PAN. Quicksilver camera: needs mana-sensitive film plate (Street Grimoire p.214) per use. Vs standard quicksilver: development 5 minutes (not 2); thresholds for tests with developed images +1."),
]

# ---- MEDIUM ----
DRONES += [
E(name="Ares Duelist", size="Medium", src="Core p.466; R5 table p.190",
  skill="Pilot Walker",
  handl="3", speed="3", accel="1", body="4", armor="4", pilot="3", sensor="3",
  seats="—", avail="5R", cost="4,500¥",
  upgrades="Unique Targeting (Swords) Rating 3 autosoft; pair of standard swords in special mounts (cannot swap those swords; additional mounts use normal rules)",
  similar="",
  rules="Anthropomorphic patrol walker styled after Renraku Red Samurai oyoroi. Blade arms primary."),
E(name="GM-Nissan Doberman", size="Medium", src="Core p.466; R5 table p.190",
  skill="Pilot Ground Craft",
  handl="5", speed="3", accel="1", body="4", armor="4", pilot="3", sensor="3",
  seats="—", avail="4R", cost="5,000¥",
  upgrades="Standard weapon mount",
  similar="",
  rules="Tracked perimeter-patrol drone; day/night."),
E(name="MCT-Nissan Roto-Drone", size="Medium", src="Core p.466; R5 table p.191",
  skill="Pilot Aircraft",
  handl="4", speed="4", accel="2", body="4", armor="4", pilot="3", sensor="3",
  seats="—", avail="6", cost="5,000¥",
  upgrades="",
  similar="",
  rules="Modular rotor-wing. Treat Body as 3 higher than actual for how many weapon mounts or customizations it can integrate."),
E(name="Ares Cheetah", size="Medium", src="R5 p.138–140",
  skill="Pilot Walker",
  handl="4", speed="6G", accel="2", body="2(0)", armor="6", pilot="3", sensor="2",
  seats="—", avail="12R", cost="14,000¥",
  upgrades="Fragile (1); Jaws Acc 3, Reach —, DV 5P, AP -3",
  similar="",
  rules="Fastest quad mech; claws for traction. Rare taser-head swap replaces jaws."),
E(name="Evo Krokodil", size="Medium", src="R5 p.139–141",
  skill="Pilot Ground Craft / Pilot Watercraft",
  handl="3", speed="2G/3W", accel="1", body="3(1)", armor="6", pilot="2", sensor="2",
  seats="—", avail="8R", cost="12,000¥",
  upgrades="Amphibious",
  similar="",
  rules="Tracked amphibious; can roll into river and out without slowing. Not submersible: dies if dunked >1 m. Must reseal after mods or sinks. Can float nearly submerged for loiter/record."),
E(name="Federated-Boeing Kull", size="Medium", src="R5 p.140–141",
  skill="Pilot Aircraft",
  handl="3", speed="4P", accel="2", body="3(3)", armor="0", pilot="3", sensor="2",
  seats="—", avail="4", cost="10,000¥",
  upgrades="Two single-use underwing bomb racks (parachute supply crates)",
  similar="Esprit Industries Recon-TF1; Saeder-Krupp Bussard",
  rules="Mid aerial with small internal cargo. Short landing strip vs full plane."),
E(name="MCT Tunneler", size="Medium", src="R5 p.140–141",
  skill="Pilot Ground Craft",
  handl="3", speed="0P", accel="0", body="3(2)", armor="6", pilot="2", sensor="2",
  seats="—", avail="8R", cost="10,000¥",
  upgrades="Drill: dig through barrier Armor 12 or less at 1 meter per hour",
  similar="",
  rules="Mine rescue crawler; tunnel large enough for humans/dwarfs/elves to shimmy (orks/trolls need larger gear). Loud and slow. Tunnels often unstable."),
E(name="Renraku LEBD-2 Law Enforcement Backup Drone", size="Medium", src="R5 p.140–141",
  skill="Pilot Aircraft",
  handl="4", speed="2P", accel="1", body="3(0)", armor="9", pilot="4", sensor="4",
  seats="—", avail="12R", cost="20,000¥",
  upgrades="Mini weapon mount; Yamaha Pulsar; 4 taser darts; Smartsoft; Targeting (4); Clearsight (4); Knowledge: Legal Codes (4)",
  similar="",
  rules="Roto-drone for Neo-PD one-officer/one-drone teams; charges on patrol-car back mount. Assaulting often treated as assaulting an officer. Strong facial-recognition / warrant pipeline via Renraku DBs."),
E(name="Transys Steed", size="Medium", src="R5 p.140–142",
  skill="Pilot Ground Craft",
  handl="4/2", speed="1G", accel="1", body="3(1)", armor="0", pilot="2", sensor="2",
  seats="—", avail="2", cost="4,000¥",
  upgrades="",
  similar="Evo Freedom; DocWagon Chariot",
  rules="Motorized wheelchair; trode-based DNI control. Street-legal; indoor-capable."),
]

# ---- LARGE ----
DRONES += [
E(name="Cyberspace Designs Dalmatian", size="Large", src="Core p.466; R5 table p.189",
  skill="Pilot Aircraft",
  handl="5", speed="5", accel="3", body="5", armor="5", pilot="3", sensor="3",
  seats="—", avail="6R", cost="10,000¥",
  upgrades="",
  similar="",
  rules="Large VTOL recon; can hover. Stored ~lawn-mower size; deployed ~large hang glider. Licensed by Lone Star / Knight Errant for urban patrol."),
E(name="Steel Lynx Combat Drone", size="Large", src="Core p.466; R5 table p.190",
  skill="Pilot Ground Craft",
  handl="5", speed="4", accel="2", body="6", armor="12", pilot="3", sensor="3",
  seats="—", avail="10R", cost="25,000¥",
  upgrades="Heavy weapon mount",
  similar="",
  rules="Hardened ground combat; four wheeled legs."),
E(name="Aeroquip Dustoff", size="Pointer", src="R5 p.141 (points to Bullets & Bandages)",
  skill="TBD (no local Bullets & Bandages PDF)",
  handl="TBD", speed="TBD", accel="TBD", body="TBD", armor="TBD", pilot="TBD", sensor="TBD",
  seats="TBD", avail="TBD", cost="TBD",
  upgrades="TBD",
  similar="",
  rules="Full stats in Bullets & Bandages (not in local Source/PDF). R5 note only: runners mod as cramped personal helicopter (~motorcycle cost); prices rose after hack popularized. STATS UNVERIFIED HERE."),
E(name="Ares Matilda", size="Large", src="R5 p.141–142",
  skill="Pilot Ground Craft",
  handl="1", speed="2G", accel="1", body="8", armor="8", pilot="2", sensor="1",
  seats="—", avail="12R", cost="18,000¥",
  upgrades="Two riot shields; standard weapon mount; underbarrel grenade launcher; Targeting (3)",
  similar="",
  rules="Tracked refrigerator-shaped mobile cover. Side blast doors (riot shields) fold out for advancing officers. Minigrenade launcher for gas ahead. If shot hits from rear flank while shields deployed: Armor halved."),
E(name="Ares Mule", size="Large", src="R5 p.141–143",
  skill="Pilot Walker",
  handl="4", speed="1G", accel="1", body="4(3)", armor="6", pilot="2", sensor="2",
  seats="—", avail="4", cost="8,000¥",
  upgrades="Drone arm (STR 6, AGI 2)",
  similar="",
  rules="Four-legged cargo hauler (~marching soldier speed); carries squad supplies. Head/neck grip like primitive cyberarm."),
E(name="Ares Paladin", size="Large", src="R5 p.142–143",
  skill="Pilot Ground Craft",
  handl="5", speed="4G", accel="1", body="5(0)", armor="18", pilot="3", sensor="2",
  seats="—", avail="8R", cost="5,000¥",
  upgrades="Tracked platform",
  similar="",
  rules="Hydraulic arms lift plasteel/Kevlar plate to intercept rounds when networked sensors detect shot. GAME: In network, on shot within detection range of any networked device: Perception test; hits = extra Armor for protected VIP that Initiative Pass; then plate = Good Cover (Core p.190) while VIP uses Take Cover. Solo: no Armor bonus on shot; only Good Cover."),
E(name='CrashCart "MediCart"', size="Large", src="R5 p.142–144",
  skill="Pilot Ground Craft",
  handl="5", speed="5G", accel="1", body="6(2)", armor="5", pilot="4", sensor="4",
  seats="—", avail="6", cost="10,000¥",
  upgrades="Tracked; hydraulic rescue tools; medkit",
  similar="",
  rules="Disaster-recovery. Arms lift up to 200 kg. GAME: Acts needing STR+Body use 3× Body (carry 270 kg without test). Deploys medkit within 2 m; Pilot replaces medkit Rating; 20 uses; cannot use medkit without drone; refill with normal replacement components."),
E(name="GTS Tower", size="Large", src="R5 p.143–144",
  skill="Pilot Aircraft",
  handl="2", speed="1P", accel="1", body="4(0)", armor="6", pilot="2", sensor="2",
  seats="—", avail="8", cost="10,000¥",
  upgrades="Drone rack (4)",
  similar="Cyberspace Designs Nexus; GN-Nissan Beehive",
  rules="LtA retrans + airbase for up to 4 minidrones or 8 microdrones."),
E(name="Saeder-Krupp Mk-17D Neptune", size="Large", src="R5 p.143–144",
  skill="Pilot Watercraft",
  handl="2", speed="3W", accel="1", body="5(0)", armor="3", pilot="4", sensor="3",
  seats="—", avail="10R", cost="17,500¥",
  upgrades="Submersible; Searchlight",
  similar="Proteus Tiefaucher; Shiawase Suredo",
  rules="Fits standard torpedo tube. Fully submersible to 1 km. Advanced Pilot for autonomous deep ops (radio hard underwater); surfaces at designated times/places for data transfer."),
E(name="Mitsuhama Malakim", size="Large", src="R5 p.143–144",
  skill="Pilot Aircraft",
  handl="3", speed="6P", accel="2", body="4(0)", armor="9", pilot="4", sensor="4",
  seats="—", avail="20F", cost="40,000¥",
  upgrades="Standard weapon mount; area jammer (6); directional jammer (6); Targeting (4)",
  similar="",
  rules="GOD response quad-copter; non-lethal focus + jamming; works with Dove spotters."),
]

# ---- HUGE ----
DRONES += [
E(name="Ares KN-Y0 Phobos (Y1)", size="Huge", src="R5 p.143–145; table p.189",
  skill="Pilot Ground Craft",
  handl="3", speed="2G", accel="1", body="6(0)", armor="18", pilot="5", sensor="3",
  seats="—", avail="16F", cost="250,000¥",
  upgrades="Targeting (5); Smartsoft; heavy weapon mount; RPK HMG + 200 rounds",
  similar="",
  rules="Unmanned micro-tank anti-infantry turret variant. Intended to deploy with Deimos/Eris."),
E(name="Ares KN-Y0 Deimos (Y2)", size="Huge", src="R5 p.143–145; table p.189",
  skill="Pilot Ground Craft",
  handl="3", speed="2G", accel="1", body="6(0)", armor="18", pilot="5", sensor="3",
  seats="—", avail="20F", cost="220,000¥",
  upgrades="Targeting (5); Smartsoft; heavy weapon mount; Panther XXL assault cannon + 15 rounds",
  similar="",
  rules="Anti-armor KN-Y0 variant."),
E(name="Ares KN-Y0 Eris (Y4)", size="Huge", src="R5 p.143–145; table p.189",
  skill="Pilot Ground Craft",
  handl="3", speed="2G", accel="1", body="6(0)", armor="18", pilot="5", sensor="3",
  seats="—", avail="24F", cost="270,000¥",
  upgrades="Targeting (5); Smartsoft; large weapon mount; Antioch MGL-12 with clip-switch among up to 24 grenades; area jammer (6); directional jammer (6); Electronic Warfare (5)",
  similar="",
  rules="Grenade/C3-inhibition KN-Y0 variant. No Y3 listed."),
E(name="Mesametric Kodiak", size="Huge", src="R5 p.145–146",
  skill="Pilot Ground Craft",
  handl="2/4", speed="2G", accel="1", body="6(2)", armor="12", pilot="2", sensor="2",
  seats="—", avail="12R", cost="40,000¥",
  upgrades="Drone arm (STR 12, AGI 2); bulldozer blade; Road Engineering (2) autosoft",
  similar="",
  rules="Road work / clear / construct / destroy. Industrial variants exist (timber, powerline, etc.)."),
E(name="NeoNET Avenging Angel", size="Huge", src="R5 p.145–146",
  skill="Pilot Aircraft",
  handl="3", speed="6J", accel="2", body="6(0)", armor="12", pilot="6", sensor="6",
  seats="—", avail="40F", cost="1,000,000¥",
  upgrades="Heavy weapon mount (single fuel-air bomb payload)",
  similar="",
  rules="Multi-MACH milspec GOD strike drone; city-block fuel-air bomb. Officially never used."),
]

# ---- ANTHRO ----
DRONES += [
E(name="Aztechnology Criado Juan", size="Anthro", src="R5 p.145–147",
  skill="Pilot Walker (anthro)",
  handl="2", speed="2G", accel="1", body="2", armor="0", pilot="2", sensor="2",
  seats="—", avail="2", cost="8,000¥",
  upgrades="Full anthro limb set (see Anthro rules)",
  similar="Renraku Manservant; Telestrian Industries Jeeves",
  rules="Budget house-bot. Domestic cleaning baseline; specialty autosofts expensive."),
E(name="Horizon Little Buddy", size="Anthro", src="R5 p.146–147",
  skill="Pilot Walker (anthro)",
  handl="2", speed="1G", accel="1", body="1", armor="0", pilot="2", sensor="2",
  seats="—", avail="4", cost="2,000¥",
  upgrades="Instruction (2) autosoft",
  similar="Hasbro Playsalot; Sony Headstart",
  rules="Child-sized nanny/teacher/playmate. Contacts parents on unprogrammed situations / wounded or missing child. Optional First Aid autosofts marketed."),
E(name="MCT Kenchiku-Kikai", size="Anthro", src="R5 p.146–148",
  skill="Pilot Walker (anthro)",
  handl="2", speed="2G", accel="1", body="5", armor="3", pilot="2", sensor="2",
  seats="—", avail="8R", cost="20,000¥",
  upgrades="Industrial Mechanic (2) autosoft; limbs enhanced to Strength 8",
  similar="S-K Colossus; Ares JHI-65",
  rules="Ork-sized construction anthro; uses metahuman tools. Many pre-wireless units still in field."),
E(name="NeoNET Juggernaught", size="Anthro", src="R5 p.147–148",
  skill="Pilot Walker (anthro)",
  handl="3", speed="4G", accel="1", body="6", armor="12", pilot="3", sensor="3",
  seats="—", avail="14R", cost="100,000¥",
  upgrades="One standard weapon mount per arm; two one-use grenade drops; anti-riot / point-blank gas dispensers (as marketed)",
  similar="",
  rules="Largest two-legged mecha on market (~head taller than average troll). Articulated hands for tools/restraint. Heavy, clumsy; floors/stairs risk."),
E(name="Saeder-Krupp Direktionssekretar", size="Anthro", src="R5 p.148–149",
  skill="Pilot Walker (anthro)",
  handl="4", speed="4G", accel="2", body="4", armor="3", pilot="4", sensor="4",
  seats="—", avail="12R", cost="40,000¥",
  upgrades="Advanced knowbot Pilot; subtle armored core; fully articulated hands",
  similar="Sony Orderly-4; Ares Pygmalion",
  rules="Executive secretary anthro: datapush, finances, books, clean, file, notes; capable security/unarmed lethality. Highly customizable appearance."),
E(name="Shiawase i-Doll", size="Anthro", src="R5 p.148–149",
  skill="Pilot Walker (anthro)",
  handl="3", speed="3G", accel="1", body="3", armor="0", pilot="3", sensor="3",
  seats="—", avail="4", cost="20,000¥",
  upgrades="Realistic Features (1); Cooking (3) autosoft",
  similar="Renraku Nadeshiko; Spinrad OoLaLa",
  rules="Customizable domestic servant. Higher realism classes (2–4) cost more (Class 4 most lifelike). Only expensive models approach human pass."),
]

# ---- MISSILE ----
DRONES += [
E(name='Ares "Garuda"', size="Missile", src="R5 p.149–150",
  skill="Pilot Aircraft",
  handl="6", speed="3J/6J", accel="2/4", body="2", armor="2", pilot="4", sensor="3",
  seats="—", avail="20F", cost="8,500¥",
  upgrades="Launched; cluster munitions; laser guidance",
  similar="",
  rules="Rigged cluster-munition missile drone. Dual mode: cruise like drone then booster (Speed/Accel second values). Cluster munitions = multiple small explosives; warhead stats from Core Grenades/Rockets/Missiles p.435 (anti-vehicle, fragmentation, or HE). Explosive costs NOT included. Shoulder-launchable or from mounted launcher. No underwater (needs oxygen). Cluster design lets rigger fire submunitions and keep moving to avoid dumpshock vs older single-warhead rigged missiles."),
]

SIZE_ORDER = ["Micro", "Mini", "Small", "Medium", "Large", "Huge", "Anthro", "Missile", "Chassis", "Pointer"]
SIZE_HEADERS = {
    "Micro": "MICRODRONES",
    "Mini": "MINIDRONES",
    "Small": "SMALL DRONES",
    "Medium": "MEDIUM DRONES",
    "Large": "LARGE DRONES",
    "Huge": "HUGE DRONES",
    "Anthro": "ANTHROPOMORPHIC DRONES",
    "Missile": "DRONE MISSILES",
    "Chassis": "CHASSIS PACKS (Mitsuhama Seven)",
    "Pointer": "CROSS-BOOK POINTERS (no local PDF stats)",
}

def render_entry(d):
    lines = [
        f"### {d['name']}",
        f"- Size: {d['size']}",
        f"- Src: {d['src']}",
        f"- Skill: {d['skill']}",
        f"- Handl: {d['handl']} | Speed: {d['speed']} | Accel: {d['accel']}",
        f"- Body: {d['body']} | Armor: {d['armor']} | Pilot: {d['pilot']} | Sensor: {d['sensor']} | Seats: {d['seats']}",
        f"- Avail: {d['avail']} | Cost: {d['cost']}",
    ]
    if d.get("upgrades"):
        lines.append(f"- Std upgrades/downgrades: {d['upgrades']}")
    if d.get("similar"):
        lines.append(f"- Similar models: {d['similar']}")
    lines.append(f"- Rules: {d['rules']}")
    lines.append("")
    return "\n".join(lines)

header = """# Drones

Agent reference (SR5). Structured field blocks for LLM parsing. Mechanical detail only.

**Src PDFs:** `Source/PDF/shadowrunfiftheditioncorerulebook_V2.pdf` · `Source/PDF/rigger5.pdf`
**Books:** Core (Street Gear Vehicles and Drones) · Rigger 5.0 (The Automated Army / Drone Catalog + compiled tables).
**See also:** `Encyclopedia/Vehicles.md` · `Encyclopedia/Vehicle and Drone Modifications.md` · `Encyclopedia/Rigger Gear.md` · `Mechanics/Rigging.md` · `Mechanics/Vehicles.md`
**Out of scope here:** RCC models (Rigger Gear); full vehicle-mod slot system for cars (Vehicle and Drone Modifications / R5 Building the Perfect Beast); Bullets & Bandages Dustoff full writeup (no local PDF).

## Schema

| Field | Meaning |
| --- | --- |
| Size | Micro / Mini / Small / Medium / Large / Huge / Anthro / Missile / Chassis / Pointer |
| Src | Book + page (Core print ~465–466; R5 catalog ~128–149; R5 compiled tables ~189–191) |
| Skill | Pilot skill to operate that drone |
| Handl | Handling; `A/B` = on-road/off-road or mode pair as printed; `—` = immobile/n/a |
| Speed | Speed rating; optional letter = movement mode for R5 chase mixing (see Common rules). `A/B` = dual-mode |
| Accel | Acceleration; dual-mode when paired with dual Speed |
| Body | Body, or `X(Y)` where X = Body and Y = free Mod Points (R5). If no `(Y)`, treat available mod points = Body unless Body 0 |
| Armor | Armor |
| Pilot | Pilot program Rating (= Device Rating / Matrix attributes) |
| Sensor | Sensor array Rating |
| Seats | Passenger seats if any; usually `—` |
| Avail / Cost | Street Availability / nuyen |
| Std upgrades | Factory gear already consuming Mod Points / included kit |
| Rules | All per-SKU mechanical notes |

## Common rules

### Core (all drones)

- Drones ship with built-in rigger interface (jump-in ready). Device Rating = Pilot Rating; Matrix attributes = Pilot.
- Pilot programs are device-specific dog-brains; cannot freely copy between units (Core Riggers).
- Autosoft Rating cannot exceed the drone's Pilot unless shared from an RCC (Core / R5).
- Autosofts are model-specific (Clearsoft for Crawler does nothing in Proletarian).
- Weapon mounts: unaugmented Body ÷ 3 (round down) mounts; standard mount = assault rifle or smaller + 250 rounds; heavy = 2 mounts, any weapon + 500 belt or Body rockets/missiles; remote only on drones (no manual op) — Core Street Gear.
- Sensor housings by size (Core): small-or-smaller drone max Sensor Rating 3; medium 4; large 5 (arrays often factory-fit at listed Sensor).
- Concealability (Core table): microdrone -6; minidrone -2; small +2; medium +8 (vs Perception to notice carried/stowed as gear).
- Condition / damage: treat as vehicles unless anthro special rule.

### Rigger 5.0 size / chase helpers

- Target size modifiers (R5 Maximum Pursuit): Micro -3; Mini -2; Small -1; Average (vehicles/drones Body ≤8) 0; then Body 9–14 +1; 15–20 +2; >20 +3 (+2 Body per 10 seats when sizing).
- Speed mode letters on R5 Speed column (chase Speed multiplier vs pedestrians/mixed): W Water ×0.8; G Ground ×1; R Rotor ×3; J Jet ×4. Letter **P** appears on many R5 prop/VTOL/LtA aircraft Speeds (not in that multiplier list; GM picks Rotor or Jet as fits the airframe).
- Operational time (R5): normal run ~6 hours before refuel/recharge; idle longer; top-speed continuous shorter. Track narratively, not minute-by-minute.
- Swarms (R5): slave drones to RCC running Swarm program; up to Device Rating × 3 slaves. Swarm Pilot = highest member Pilot or RCC Device Rating (higher); uses highest autosofts/Sensor; lowest Handling/Speed/Accel; action bonus = (drones in swarm - 1) to dice and limit. Combat: one weapon profile represents the volley. Target drones individually.

### R5 Body X(Y) and light mods

- Mod Points = Body. `Body X(Y)`: X = Body, Y = free Mod Points left after factory gear. Attribute +1 (or Armor +3) once with no Mod Point cost; further raises cost Mod Points = increase - 1. Body itself cannot be raised. Cap: attributes ≤ 2× starting (use 0.5 if starting 0). See R5 Drone Modification for costs; deeper vehicle-slot system is separate chapter.

### Anthropomorphic drones (R5)

- Come with two drone arms + two drone legs (Obvious; may be Synthetic).
- Physical Condition Monitor = 8 + (Body / 2) (more durable than typical drones).
- Can use many metahuman items (clothing, weapons, tools).

### Pilots / autosofts (R5 price reminder)

- Pilot Rating 1 Avail 4 Cost 100¥; 2 — / 400¥; 3 8R / 1,800¥; 4 12R / 3,200¥; 5 16F / 10,000¥; 6 24F / 20,000¥.
- Autosoft Rating 1–6: Avail Rating×2, Cost Rating×500¥.
- Smartsoft (Restricted): treated as Rating 3 autosoft; full smartgun use via sensors.
- Group autosoft: Rating 2; shared-signal group commands.
- Personality tweak Avail 4 / 100¥; Linguistics Avail 4 / 50¥ (verbal command vocab limited; Language Skillset autosoft is real translation).

### Core vs R5 Core reprints

- R5 compiled tables reprint Core drones and state R5 Mod Point / adjusted lines replace originals when using R5. This file lists Core page for Core SKUs and uses R5 compiled stats where both appear.

## Catalog

"""

parts = [header]
for size in SIZE_ORDER:
    group = [d for d in DRONES if d["size"] == size]
    if not group:
        continue
    parts.append(f"## {SIZE_HEADERS[size]}\n")
    for d in group:
        parts.append(render_entry(d))

# quick inventory footer
parts.append("## Inventory checklist\n")
parts.append(f"Total SKUs in this file: {len(DRONES)} (includes Seven chassis packs, KN-Y0 variants, Dustoff pointer).\n")
parts.append("""
Core Street Gear drones (11): Kanmushi, Microskimmer, Flying Eye, Fly-Spy, Crawler, Optic-X2, Duelist, Doberman, Roto-Drone, Dalmatian, Steel Lynx.

R5 catalog unique lines covered: NoizQuito, Goldfish, Condor, Hedgehog, Dragonfly, Pigeon 2.0, CU^3, Gerbil, Scuttler, Sentry V (+Mercury note), Smoke Generator, Wolfhound, Proletarian, Ferret, Sewer Snake, Mini-Zep, KE P5, Castle Guard, Gun Turret, Seven (+7 chassis), Prairie Dog, Sundowner, Krake (+micro-torpedo ammo), Bloodhound, Dove, Jardinero, Job-a-Mat, Pelican, Shamus, Cheetah, Krokodil, Kull, Tunneler, LEBD-2, Steed, Dustoff pointer, Matilda, Mule, Paladin, MediCart, Tower, Neptune, Malakim, KN-Y0 Phobos/Deimos/Eris, Kodiak, Avenging Angel, Criado Juan, Little Buddy, Kenchiku-Kikai, Juggernaught, Direktionssekretar, i-Doll, Garuda.
""")

OUT.write_text("".join(parts), encoding="utf-8")
print("Wrote", OUT, "entries", len(DRONES), "chars", OUT.stat().st_size)
