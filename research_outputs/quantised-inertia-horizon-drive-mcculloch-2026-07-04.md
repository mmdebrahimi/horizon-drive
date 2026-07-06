# Quantised Inertia (MiHsC) & the "horizon drive" — McCulloch — supported memo (V1 invocation)
<!-- memo-schema: 0.4 -->

> Captured 2026-07-04. Source: Claude Code (`/research` orchestrator). Slug: quantised-inertia-horizon-drive-mcculloch-2026-07-04.
> Audit floor: 5 of 5 locators per row. Mapping floor: rationale → quantity. Banned-phrase + cite-token scans clean. Source-identity advisory applied (Step 5.5).

## Research Context
- **Problem:** quantised inertia horizon drive McCulloch
- **Captured:** 2026-07-04
- **Schema:** memo-schema 0.4

## Audit table (verbatim, supported rows only)

| Claim / quantity | Numeric value | Units | Source title | Authors / org | Year | Section | Stable URL | Access date | Quoted excerpt (≤25 words) | Extraction rationale | Source type | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| QI-predicted vs observed EmDrive thrust (8 experiments) | pred 3.8,149,7.3,0.23,0.57,0.11,0.64,0.02 / obs 16,147,9,0.09,0.05,0.06,0.03,0.02 | mN | Testing quantised inertia on the emdrive | M.E. McCulloch | 2016 | Abstract | https://arxiv.org/abs/1604.03449 | 2026-07-04 | "The model predicts thrusts of: 3.8, 149, 7.3, 0.23, 0.57, 0.11, 0.64 and 0.02 mN compared with the observed thrusts of: 16, 147, 9..." | Verbatim abstract; paired predicted/observed | preprint (arXiv) | high |
| QI thrust mechanism (asymmetric Unruh radiation, tapered cavity) | qualitative | — | Testing quantised inertia on the emdrive | M.E. McCulloch | 2016 | Abstract | https://arxiv.org/abs/1604.03449 | 2026-07-04 | "more Unruh waves are allowed at the wide end, leading to a greater inertial mass for the photons there... the cavity must move towards its narrow end" | Verbatim mechanism | preprint (arXiv) | high |
| Falsifiable reversal prediction (axial length = small-end diameter → thrust reverses) | qualitative | — | Testing quantised inertia on the emdrive | M.E. McCulloch | 2016 | Abstract | https://arxiv.org/abs/1604.03449 | 2026-07-04 | "if the axial length is equal to the diameter of the small end of the cavity, the thrust should be reversed" | Verbatim; concrete falsifiable test | preprint (arXiv) | high |
| QI predicts dwarf-galaxy dynamics w/o dark matter; beats MoND; no free parameter | 11 | dwarf satellites | Low-acceleration dwarf galaxies as tests of quantised inertia | M.E. McCulloch | 2017 | Abstract | https://arxiv.org/abs/1703.01179 | 2026-07-04 | "Quantised inertia slightly outperforms MoND... has the fundamental advantage over MoND that it does not need an adjustable parameter" | Verbatim abstract | preprint (arXiv) | high |
| QI predicts a minimum galactic mass (inertia loss at low accel) | 1.1×10⁹ | M_solar | Minimum accelerations from quantised inertia | M.E. McCulloch | 2010 | Abstract (EPL 90, 29001) | https://arxiv.org/abs/1004.3303 | 2026-07-04 | "a minimum apparent mass of 1.1x10^9 M_solar, close to the observed minimum mass" | Verbatim; EPL-published | peer-reviewed (EPL) | high |
| QI's minimum acceleration ≈ the observed cosmic acceleration | qualitative | — | Minimum accelerations from quantised inertia | M.E. McCulloch | 2010 | Abstract | https://arxiv.org/abs/1004.3303 | 2026-07-04 | "stabilising the acceleration at a minimum value, which is close to the observed cosmic acceleration" | Verbatim; equivalence stated in abstract | peer-reviewed (EPL) | high |
| Minimum-acceleration numeric a₀ = 2c²/Θ | ~2×10⁻¹⁰ | m/s² | Minimum accelerations from QI (body) / QI summary | M.E. McCulloch | 2010 | Body (eq.), not abstract | https://arxiv.org/abs/1004.3303 | 2026-07-04 | "a minimum acceleration of 2c²/Θ ~ 2×10⁻¹⁰ m/s² (where Θ is the co-moving Hubble diameter)" | Numeric via WebSearch summary — NOT verbatim-fetched from paper body | preprint + secondary | medium |
| Independent critical analysis: two major flaws in the QI derivation | qualitative | — | A sceptical analysis of Quantized Inertia | Michele Renda | 2019 | Abstract | https://arxiv.org/abs/1908.01589 | 2026-07-04 | "Two major flaws were found in the original derivation" | Verbatim; load-bearing skeptical counterweight | preprint (arXiv) | high |

## Source-Locator Coverage
- Total rows submitted: 12
- Survived audit floor: 8
- Survived mapping floor: 8
- Survived banned-phrase scan: 8 (0 hard-reject, 0 soft-warn)
- Final supported: **8** · Survival rate: 8/12 (67%)

## Caveats per row
- **Row 7 (a₀ = 2×10⁻¹⁰ m/s²):** `provenance: websearch-summary` — the exact number came from a search summary, not a verbatim fetch of the 1004.3303 PDF body. The *abstract* confirms the mechanism + cosmic-acceleration equivalence, but the numeric + equation locator need a direct-source check before high-confidence use. Downgraded high→medium.
- **Row 8 (two major flaws):** this is a **critical counterweight** (an independent skeptical rebuttal), not a QI claim — kept supported precisely so the honest picture isn't one-sided. The flaws themselves aren't detailed in the abstract; the full paper (Renda 2019) must be read for specifics.
- **Rows 1–6:** verbatim from arXiv/EPL abstracts; no cite-token noise, no banned phrases.

## Decisions for Human Confirmation (cap 5)

| Claim | Numeric value | Units | Source URL | Candidate use / Verification needed | Confidence |
|---|---:|---|---|---|---|
| QI's falsifiable minimum acceleration a₀ = 2c²/Θ | ~2×10⁻¹⁰ | m/s² | https://arxiv.org/abs/1004.3303 | **Candidate use:** the single most testable QI prediction — a universal floor acceleration = cosmic acceleration, testable in galaxies, wide binaries, JuMBOs. **Verification needed:** fetch the exact value + equation locator from the PDF body; confirm the claimed JuMBO/wide-binary support against primary papers. | medium |
| EmDrive thrust predicted vs observed (order-of-magnitude match) | see table | mN | https://arxiv.org/abs/1604.03449 | **Candidate use:** QI's headline propulsion claim — same mechanism as the galaxy-rotation fit. **Verification needed:** the EmDrive effect itself is refuted by the Dresden/Tajmar null; confirm whether QI's fit survives once the underlying thrust is attributed to thermal/EMI artifact. | high |
| QI thrust-reversal prediction (axial length = small-end diameter) | qualitative | — | https://arxiv.org/abs/1604.03449 | **Candidate use:** a clean, cheap, falsifiable bench test that could kill or support QI. **Verification needed:** has anyone built the reversed-geometry cavity and measured? (Unknown — chase the experimental follow-ups.) | high |
| QI predicts galaxy/dwarf rotation with no dark matter + no free parameter | 11 dwarfs | count | https://arxiv.org/abs/1703.01179 | **Candidate use:** QI's strongest *scientific* (non-propulsion) evidence — a parameter-free fit beating MoND. **Verification needed:** confirm against the larger SPARC-153 claim + independent re-analyses. | high |
| Independent rebuttal: two major flaws in the QI derivation | qualitative | — | https://arxiv.org/abs/1908.01589 | **Candidate use:** the essential skeptical counterweight — read before treating QI as anything but fringe-frontier. **Verification needed:** read Renda 2019 in full for the specific derivation flaws + McCulloch's response, if any. | high |

## Verification trace (Mission Control L1)
Invoked under Mission Control run `2026-07-04-1409-research-quantised-inertia` (intent-contract at `mission-control-runs/2026-07-04-1409-research-quantised-inertia/intent-contract.md`).
- Audit floor: 8 pass / 4 fail · Mapping floor: 8 pass / 0 fail · Banned-phrase: 0 hard / 0 soft · Cite-token: 0 · Source-identity advisory: 1 provenance-flag (row 7), 0 author-uncertain, 0 table-cell-quote.
- **Intake validation sub-task: PASS** — 8 supported (`<slug>.md`) / 4 unsupported (`<slug>_unsupported.md`).

## Promotion Gate reminder
INPUT to the 4-step Promotion Gate, NOT an approval. Before lifting any number: (1) doc resolves at URL, (2) section exists, (3) quote is verbatim in the doc, (4) mapping is natural. **Row 7 (a₀) specifically fails step 3 right now** (search-summary quote) — verify before use.
