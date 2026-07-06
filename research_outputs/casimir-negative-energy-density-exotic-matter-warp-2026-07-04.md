# Casimir negative energy density → exotic matter → warp — supported memo (V1 invocation)
<!-- memo-schema: 0.4 -->

> Captured 2026-07-04. Source: Claude Code (`/research` orchestrator → /research-intake by-hand). Slug: casimir-negative-energy-density-exotic-matter-warp-2026-07-04.
> Audit floor: 5/5 locators per row. Mapping floor: rationale → quantity. Banned-phrase + cite-token + source-identity advisory applied.
> 13 supported (all high — arXiv abstracts + Wikipedia verbatim). 4 unsupported (body-only figures on search-summary provenance / low confidence).

## Research Context

- **Problem:** Anti-gravity deep-dive candidate #2 (Casimir / macroscopic negative-energy sourcing) — the load-bearing node of `research_outputs/antigravity-full-landscape-assessment.md`: Casimir is the ONLY lab-measured negative-energy source, upstream of every warp/wormhole metric. Does it have *even the slightest* path to macroscopic anti-gravity?
- **Captured:** 2026-07-04
- **Schema:** memo-schema 0.4

## Audit table (verbatim, supported rows only)

| Claim / quantity | Value | Units | Source | Year | Locator | URL | Quoted excerpt (≤25 words) | Conf |
|---|---|---|---|---|---|---|---|---|
| Casimir force per area (ideal plates) | −π²/240·ℏc/a⁴ | N/m² | Casimir effect (Wikipedia) | 1948 | Derivation | https://en.wikipedia.org/wiki/Casimir_effect | "F_c/A = −ℏcπ²/240a⁴" | high |
| Casimir energy-density constant | π²/720 | ·ℏc/a⁴ | Casimir effect | 2026 | Physical properties | https://en.wikipedia.org/wiki/Casimir_effect | "Constant in energy formula: π²/720" | high |
| Lamoreaux measured force vs theory | within 5 | % | Casimir effect (PRL 1997) | 1997 | Measurement | https://en.wikipedia.org/wiki/Casimir_effect | "Lamoreaux quantitatively measured the Casimir force to be within 5% of the value predicted by the theory" | high |
| Energy density negative vs ordinary vacuum | qualitative | — | Casimir effect | 2026 | Speculative applications | https://en.wikipedia.org/wiki/Casimir_effect | "energy density in very small regions of space to be negative relative to the ordinary vacuum energy" | high |
| Warp-bubble wall thickness (QI bound) | a few hundred | Planck lengths | Unphysical nature of Warp Drive | 1997 | Abstract | https://arxiv.org/abs/gr-qc/9702026 | "the bubble wall thickness is on the order of only a few hundred Planck lengths" | high |
| Warp bubble @10c wall thickness | ≤10⁻³² | m | Alcubierre drive (Wikipedia) | 2026 | Wall thickness | https://en.wikipedia.org/wiki/Alcubierre_drive | "warp bubble traveling at 10-times the speed of light must have a wall thickness of no more than 10−32 meters" | high |
| Alcubierre requires exotic matter | qualitative | — | Alcubierre drive | 2026 | Introduction | https://en.wikipedia.org/wiki/Alcubierre_drive | "implies a negative energy density and therefore requires exotic matter" | high |
| All warp spacetimes violate energy conditions | qualitative | — | Alcubierre drive | 2026 | Mass–energy requirement | https://en.wikipedia.org/wiki/Alcubierre_drive | "all known warp-drive spacetime theories violate various energy conditions" | high |
| Energy to cross Milky Way (Alcubierre) | −10⁶⁴ | kg-equiv | Alcubierre drive (Alcubierre 1994) | 2026 | Mass–energy requirement | https://en.wikipedia.org/wiki/Alcubierre_drive | "energy equivalent of −10^64 kg might be required to transport a small spaceship across the Milky Way" | high |
| DCE: virtual→real photons | qualitative | — | Observation of the DCE | 2011 | Abstract | https://arxiv.org/abs/1105.4714 | "convert virtual photons into directly observable real photons" | high |
| DCE SQUID modulation | ~11 | GHz | Observation of the DCE | 2011 | Abstract | https://arxiv.org/abs/1105.4714 | "modulating the inductance of a… SQUID… at high frequencies (~11 GHz)" | high |
| DCE effective boundary speed | a few percent | of c | Observation of the DCE | 2011 | Abstract | https://arxiv.org/abs/1105.4714 | "an electrical length that can be changed at a few percent of the speed of light" | high |
| DCE two-mode squeezing = quantum signature | qualitative | — | Observation of the DCE | 2011 | Abstract | https://arxiv.org/abs/1105.4714 | "two-mode squeezing of the emitted radiation, which is a signature of the quantum character" | high |

## Source-Locator Coverage

- Rows submitted: 17 · Survived audit floor: 13 · Survived mapping floor: 13 · Survived banned-phrase: 13 · Final supported: 13
- Survival rate: 13/17 (76%). 4 unsupported → body-only figures on search-summary provenance + 1 low-confidence.

## Caveats per row

- All 13 supported rows are verbatim from arXiv abstracts (gr-qc/9702026, 1105.4714) or Wikipedia (Casimir / Alcubierre). No cite-token noise, no banned phrases.
- Wikipedia rows carry a further-primary chain (Casimir 1948; Lamoreaux PRL 1997; Alcubierre 1994; Pfenning-Ford 1997) — encyclopedia is the fetched surface, primary is named. Confidence stays high (formula/measurement are textbook-settled, not contested).

## Decisions for Human Confirmation (cap 5)

| Claim | Value | Units | Source URL | Candidate use / Verification needed | Conf |
|---|---|---|---|---|---|
| Casimir force ∝ a⁻⁴ (−π²ℏc/240a⁴) | −π²/240 | ·ℏc/a⁴ | https://en.wikipedia.org/wiki/Casimir_effect | **Candidate use:** the scaling that DOOMS Casimir as a macroscopic energy source — density huge only at nm gaps, total energy minuscule. **Verify:** compute total negative energy achievable over realistic area/gap vs warp −10⁶⁴ kg. | high |
| Warp wall ≤ a few hundred Planck lengths | ~10⁻³² | m | https://arxiv.org/abs/gr-qc/9702026 | **Candidate use:** THE QI wall — macroscopic warp forces near-Planck-thin neg-energy shell ⇒ unphysical magnitude. **Verify:** fetch gr-qc/9702026 body for the −400 M_sun figure (currently unsupported). | high |
| Alcubierre needs −10⁶⁴ kg-equiv | −10⁶⁴ | kg | https://en.wikipedia.org/wiki/Alcubierre_drive | **Candidate use:** the magnitude gap Casimir must bridge and cannot (dup-confirms nordic memo). **Verify:** confirm assumptions in Alcubierre 1994. | high |
| Lamoreaux confirmed Casimir to 5% | 5 | % | https://en.wikipedia.org/wiki/Casimir_effect | **Candidate use:** grounds Casimir as REAL (not speculative) — the honest floor under the whole neg-energy corner. **Verify:** none; textbook-settled. | high |
| DCE creates real photons from vacuum (Wilson 2011) | ~11 GHz / few-% c | — | https://arxiv.org/abs/1105.4714 | **Candidate use:** vacuum IS manipulable in the lab — but yields *photons*, not *thrust* or macroscopic neg-energy. **Verify:** any proposal converting DCE output to net force? (none known). | high |

*Additional candidates exist (the 4 unsupported body-figures); see `_unsupported.md`.*

## Verification trace (Mission Control L1)

Invoked as part of run `2026-07-04-1645-research-casimir-negative-energy-warp` (`mission-control-runs/…/intent-contract.md`).
- Audit floor: 13 pass / 4 fail · Mapping floor: 13 pass · Banned-phrase: 0 hard / 0 soft · Cite-token: 0 · Source-identity advisory: 3 provenance-flag (search-summary body figures) / 0 author / 0 quote-shape.
- **Sub-task "Intake validation": PASS** — 13 supported + 4 unsupported written.

## Promotion Gate reminder

INPUT to the 4-step Promotion Gate, not an approval. No number lifts into any artifact without: URL resolves, section exists, quote verbatim, mapping natural.
