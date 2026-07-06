# Space horizon-drive enablers: HTS, passive cooling, fission power — supported memo (V1 invocation)
<!-- memo-schema: 0.4 -->

> Captured 2026-07-05. Source: Claude Code (`/research` → /research-intake by-hand). Slug: space-horizon-drive-hts-fission-cooling-2026-07-05.
> Audit floor 5/5; mapping/banned/cite/identity scans applied. 8 supported (all high — NASA/Wikipedia/arXiv verbatim). 7 unsupported (search-summary provenance).

## Research Context

- **Problem:** Ground the /probe space-variant of the horizon-drive device — three claims: (1) space's cold sink eases the 4 K cryo problem; (2) fission microreactor (not fusion, not batteries) is the realistic power source; (3) HTS at ~50 K could cut cryogenics. Which hold, quantitatively?
- **Captured:** 2026-07-05
- **Schema:** memo-schema 0.4

## Audit table (verbatim, supported rows only)

| Claim | Value | Units | Source | Year | Locator | URL | Quoted excerpt (≤25 words) | Conf |
|---|---|---|---|---|---|---|---|---|
| KRUSTY full-power mission-sim test | 28 | hours | NASA (RELEASE18-031) | 2018 | Body | https://www.nasa.gov/news-release/demonstration-proves-nuclear-fission-system-can-provide-space-exploration-power/ | "a 28-hour, full-power test that simulated a mission, including reactor startup, ramp to full power, steady operation and shutdown" | high |
| Kilopower electrical output + lifetime | 10 / 10 | kWe / yr | NASA | 2018 | Body | https://www.nasa.gov/news-release/demonstration-proves-nuclear-fission-system-can-provide-space-exploration-power/ | "capable of providing up to 10 kilowatts of electrical power… continuously for at least 10 years" | high |
| JWST passive design temperature | 40 | K | JWST sunshield (Wikipedia) | 2026 | Overview | https://en.wikipedia.org/wiki/James_Webb_Space_Telescope_sunshield | "cool to their design temperature of 40 kelvins" | high |
| JWST V-groove temperature drop | 318 | K | JWST sunshield | 2026 | Overview | https://en.wikipedia.org/wiki/James_Webb_Space_Telescope_sunshield | "acts as a V-groove radiator and causes a temperature drop of 318 K… from front to back" | high |
| JWST solar attenuation | 200 kW→23 mW | W | JWST sunshield | 2026 | Overview | https://en.wikipedia.org/wiki/James_Webb_Space_Telescope_sunshield | "receive about 200 kilowatts of solar radiation, but only pass 23 milliwatts to the other side" | high |
| REBCO critical temperature | ~90 | K | ReBCO HTS RF (arXiv 2509.13668) | 2025 | I Introduction | https://arxiv.org/html/2509.13668v1 | "REBCO… their critical temperature of approximately ∼90 K" | high |
| HTS cavity cooling method | qualitative | — | ReBCO HTS RF | 2025 | I Introduction | https://arxiv.org/html/2509.13668v1 | "HTS cavities could be cooled by liquid nitrogen, cryocoolers or other simplified cryogenic systems instead of liquid helium" | high |
| REBCO RF conductivity vs Cu and Nb (the caveat) | qualitative | — | ReBCO HTS RF | 2025 | IV Steady State | https://arxiv.org/html/2509.13668v1 | "REBCO samples were at least an order of magnitude greater than that of copper, but still lower than niobium at these frequencies" | high |

## Source-Locator Coverage

- Rows submitted: 15 · Survived audit floor: 8 · Mapping floor: 8 · Banned-phrase: 8 · Final supported: 8
- Survival rate: 8/15 (53%). 7 unsupported → Nb-Q benchmark, KRUSTY thermal detail, Kilopower/FSP mass, MIRI 7 K, sky temp — all search-summary provenance (primaries exist at NTRS/CERN, not fetched this pass).

## Caveats per row

- All 8 supported rows verbatim from NASA.gov, Wikipedia (JWST), or arXiv 2509.13668. No cite-token/banned-phrase hits.
- Row 8 (REBCO "still lower than niobium") is the load-bearing finding for the space design: HTS eases cooling but costs Q, and F=ηPQ/c means lower Q → more RF power. The tradeoff is real, not hand-waved.

## Decisions for Human Confirmation (cap 5)

| Claim | Value | Units | Source URL | Candidate use / Verification needed | Conf |
|---|---|---|---|---|---|
| HTS/REBCO "still lower than niobium" at RF | qualitative | — | https://arxiv.org/html/2509.13668v1 | **Candidate use:** the space-design crux — HTS at ~50 K cuts cooling but not-yet-Nb Q means more RF power (F=ηPQ/c). **Verify:** a full-cavity HTS Q at 50 K (sample-level here). | high |
| Passive radiative cooling reaches ~40 K | 40 | K | https://en.wikipedia.org/wiki/James_Webb_Space_Telescope_sunshield | **Candidate use:** in space, cooling to the HTS window (~40 K) is essentially FREE (passive) — the strongest space advantage. **Verify:** none; JWST-demonstrated. | high |
| Fission microreactor = realistic space power (10 kWe/10 yr, tested) | 10 / 10 | kWe / yr | https://www.nasa.gov/news-release/demonstration-proves-nuclear-fission-system-can-provide-space-exploration-power/ | **Candidate use:** the power source for a space drive — NOT fusion (nonexistent) or batteries. **Verify:** scale to ~40-126 kW (FSP 40 kWe class, search-summary). | high |
| JWST attenuates 200 kW solar → 23 mW | 200 kW→23 mW | W | https://en.wikipedia.org/wiki/James_Webb_Space_Telescope_sunshield | **Candidate use:** proves deep-space passive thermal management at scale. **Verify:** none; verbatim. | high |
| Passive floors at ~40 K; 7 K (MIRI) still needs a cryocooler | 7 | K | https://en.wikipedia.org/wiki/James_Webb_Space_Telescope_sunshield | **Candidate use:** a 4 K Nb cavity would STILL need active cooling even in space → favors HTS-at-40K over Nb-at-4K. **Verify:** lift 40 K→4 K COP for the residual stage. | medium |

## Verification trace (Mission Control L1)

Run `2026-07-05-0317-research-space-horizon-drive-hts-fission`. Audit floor: 8 pass / 7 fail · Mapping: 8 · Banned: 0 · Cite-token: 0 · Source-identity: 6 provenance-flag (search-summary). **Sub-task "Intake validation": PASS** — 8 supported + 7 unsupported.

## Promotion Gate reminder

INPUT to the 4-step Promotion Gate. The QI drive itself remains unconfirmed — this memo grounds the ENABLING subsystems (power/cooling/HTS), not the propulsion physics.
