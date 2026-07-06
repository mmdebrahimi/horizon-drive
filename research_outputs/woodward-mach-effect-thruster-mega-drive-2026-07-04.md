# Woodward Mach-effect thruster (MEGA drive) & the Tajmar 2021 null — supported memo (V1 invocation)
<!-- memo-schema: 0.4 -->

> Captured 2026-07-04. Source: Claude Code (`/research`). Slug: woodward-mach-effect-thruster-mega-drive-2026-07-04.
> Audit floor: 5/5 locators. Mapping floor: rationale→quantity. Source-identity advisory applied. **Caveat: primary papers were paywalled (403 to WebFetch); several rows rest on search-summary provenance and are flagged medium — verify against ResearchGate PDFs before high-confidence use.**

## Research Context
- **Problem:** Woodward Mach-effect thruster MEGA drive transient mass fluctuation Tajmar 2021 null
- **Captured:** 2026-07-04 · **Schema:** memo-schema 0.4

## Audit table (verbatim, supported rows only)

| Claim | Numeric value | Units | Source title | Authors / org | Year | Section | Stable URL | Access date | Quoted excerpt (≤25 words) | Extraction rationale | Source type | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Woodward/Mach-effect definition | qualitative | — | Woodward effect (encyclopedic) | Woodward (1990) | 1990 | Definition | https://en.wikipedia.org/wiki/Woodward_effect | 2026-07-04 | "transient mass fluctuations arise in any object that absorbs internal energy while undergoing a proper acceleration" | Core mechanism; provenance: search-summary | secondary | medium |
| Tajmar SpaceDrive conclusion: artifacts, not thrust | qualitative | — | Experimental investigation of Mach-Effect thrusters on torsion balances | Tajmar et al. (TU Dresden) | 2021 | Acta Astronautica 182 | https://www.sciencedirect.com/science/article/abs/pii/S0094576521001119 | 2026-07-04 | "the results show the presence of thermal and vibrational artifacts rather than the predicted thrust forces" | The peer-reviewed null; provenance: search-summary (primary 403) | peer-reviewed (paywalled) | medium |
| Tajmar verbatim verdict | qualitative | — | Tajmar tests refute EmDrive + Mach-Effect claims | M. Tajmar / NextBigFuture | 2021 | (news; direct-fetch verified) | https://www.nextbigfuture.com/2021/04/tajmar-tests-refutes-emdrive-reactionless-drive-and-mach-effect-thruster-claims.html | 2026-07-04 | "the Mach-Effect-Thruster (an idea by J. Woodward) is unfortunately a vibration artifact and also not a real thrust" | Directly fetched verbatim quote | secondary (news, direct) | medium |
| Orientation-independence diagnostic (the smoking gun) | qualitative | — | Experimental investigation of Mach-Effect thrusters on torsion balances | Tajmar et al. | 2021 | Acta Astronautica 182 | https://www.sciencedirect.com/science/article/abs/pii/S0094576521001119 | 2026-07-04 | "force traces with the same magnitude were observed in all orientations, notably in the no-thrust producing axis" | A real thrust reverses with orientation; artifact doesn't. provenance: search-summary | peer-reviewed (paywalled) | medium |
| Measurement noise floor + drive band | <5 (noise); 20–50 | nN; kHz | Tajmar tests refute… (NBF) | Tajmar / NBF | 2021 | (news; direct-fetch verified) | https://www.nextbigfuture.com/2021/04/tajmar-tests-refutes-emdrive-reactionless-drive-and-mach-effect-thruster-claims.html | 2026-07-04 | background noise "lower than 5 nN after averaging"; testing "between 20 and 50 kHz" | Directly fetched; sensitivity context | secondary (news, direct) | medium |

## Source-Locator Coverage
- Total rows submitted: 12 · Survived audit floor: 5 · Survived mapping floor: 5 · Banned-phrase: 5 (0 hard/0 soft) · Final supported: **5** · Survival rate: 5/12 (42%)
- **Low survival is expected + honest here:** the two primary papers returned HTTP 403 to WebFetch, so 7 rows lack an in-source section locator and/or rest on search-summary provenance → routed to unsupported *pending primary-source verification*, not rejected as wrong.

## Caveats per row
- All 5 supported rows are **medium** (none high): 3 carry `provenance: websearch-summary` (verify vs the paywalled Acta Astronautica paper / ResearchGate PDF 349845653); 2 are directly-fetched from a news source (verbatim-verified but secondary).
- No cite-token noise, no banned phrases.

## Decisions for Human Confirmation (cap 5)

| Claim | Numeric value | Units | Source URL | Candidate use / Verification needed | Confidence |
|---|---:|---|---|---|---|
| Best independent test attributes MET "thrust" to thermal+vibration artifacts | qualitative | — | https://www.sciencedirect.com/science/article/abs/pii/S0094576521001119 | **Candidate use:** the decisive evidence for the dossier — verdict on Woodward = *not supported* by controlled replication. **Verification needed:** read the Acta Astronautica 182 (2021) paper / ResearchGate PDF; confirm the artifact conclusion + methods. | medium |
| Orientation-independence: force same in the no-thrust axis | qualitative | — | https://www.sciencedirect.com/science/article/abs/pii/S0094576521001119 | **Candidate use:** the single cleanest physics argument (a real thrust must reverse; an artifact doesn't). **Verification needed:** confirm the orientation-test data in the primary. | medium |
| Tajmar's own verdict: "vibration artifact… not a real thrust" | qualitative | — | https://www.nextbigfuture.com/2021/04/tajmar-tests-refutes-emdrive-reactionless-drive-and-mach-effect-thruster-claims.html | **Candidate use:** quotable summary of the null. **Verification needed:** trace the quote to Tajmar's own paper/talk (news source is verbatim but secondary). | medium |
| Claimed MET effect size (Fearn) is tiny: ~2 µN / 40 nN/W | 2 / 40 | µN / nN/W | https://www.researchgate.net/publication/335217801 | **Candidate use:** quantifies how marginal the *positive* claim is — near any lab's artifact floor. **Verification needed:** confirm value in the Fearn/Woodward RG PDF (currently unsupported — no in-source locator). | medium |
| Measurement noise floor <5 nN (drive 20–50 kHz) | <5 | nN | https://www.nextbigfuture.com/2021/04/tajmar-tests-refutes-emdrive-reactionless-drive-and-mach-effect-thruster-claims.html | **Candidate use:** shows the Dresden rig resolves well below the 2 µN claim — the null is not a sensitivity failure. **Verification needed:** confirm noise floor in the primary. | medium |

## Verification trace (Mission Control L1)
Run `2026-07-04-1550-research-woodward-mach-effect`.
- Audit floor: 5 pass / 7 fail · Mapping: 5 pass · Banned-phrase: 0/0 · Cite-token: 0 · Source-identity: 3 provenance-flag, 0 author-uncertain, 0 table-cell.
- **Intake validation: PASS** — 5 supported / 7 unsupported (0 hard-reject; low survival is the paywall gap, honestly surfaced).

## Promotion Gate reminder
INPUT to the 4-step Promotion Gate, not an approval. **Every supported row here is medium** — none should be lifted without fetching the paywalled Acta Astronautica primary and confirming the quote is verbatim + the value is in-source.
