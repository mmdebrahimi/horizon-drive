# Subsystem Scoping Memo — Cryogenic / SRF Upgrade Path

**Project:** horizon-drive Phase-1 → high-Q decisive experiment
**Subsystem:** cavity material/temperature ladder (the Q-axis)
**Date:** 2026-07-20
**Status:** research/scoping — this is the expensive, specialist end. Read the cost-honesty caveats.

---

## Overview

Phase-1 uses a room-temperature **copper** cavity, Q₀ ≈ 2.7×10⁴. The claimed propulsion-grade effect scales as **F ∝ Q** and needs Q ≈ 10¹⁰, i.e. a **superconducting cavity at cryogenic temperature**. Because the discriminator is literally proportional to Q, the material/temperature ladder IS the independent variable of the decisive experiment: each rung is a data point on the F-vs-Q line, and a straight line through several decades of Q is what a real F∝Q effect looks like (vs. a flat null).

The ladder:

| Rung | Material / temp | Q₀ (this experiment's regime) | Cryo needed |
|---|---|---|---|
| 0 (have) | Copper, 293 K | ~2.7×10⁴ | none |
| 1 (intermediate) | High-RRR Cu, ~4 K | ~10⁵ (see honesty note) | 4 K only |
| 2a | Niobium, ~2 K | ~10¹⁰–10¹¹ | **superfluid He (2 K)** |
| 2b (**preferred Q-target**) | Nb₃Sn on Nb, 4.2 K | ~1–2×10¹⁰ | ordinary LHe (4.2 K) |

Bottom line up front: **Nb₃Sn @ 4.2 K is the right superconducting target** (same Q as Nb @ 2 K, ~10× less cryo complexity, and this is a *low-field Q-only* test so Nb₃Sn's one real weakness — field-dependent quench — does not bite). The **high-RRR cryo-copper 4 K rung is worth doing first** as a cheap middle Q-point, but be honest: it buys ~1 order of magnitude of Q (anomalous skin effect caps it near ~10⁵), not the ~10⁶ the shared context optimistically assumed.

---

## The Q-ladder as the discriminator axis

- F ∝ Q means the experiment's sensitivity and its *falsifiability* both live on the Q-axis. A single high-Q point is weak evidence; a **line across decades of Q** is the strong test.
- Copper RT (2.7×10⁴) and Nb₃Sn 4.2 K (~10¹⁰) already span ~6 decades — a big lever arm.
- Adding cryo-copper (~10⁵ at 4 K) inserts a **third point** between them, obtained *before* you commit to superconductivity, and it exercises the whole cryostat/RF-at-cold chain on a cheap cavity. Even a ~10× Q step is a real, independent point on the F∝Q line.
- Practical caution: at fixed geometry, changing Q by cooling/material also changes surface fields, thermal environment, and coupling. Keep geometry and mode fixed across rungs; measure Q₀ by the standard loaded-Q + coupling method at each temperature so the F∝Q fit isn't confounded.

---

## Cryostat options (cost tiers, operating complexity)

Two families reach 4.2 K; going to 2 K adds a pumped/JT stage.

### A. LHe bath / flow cryostat
- **Physics:** static LHe bath at 4.2 K (often with a 77 K LN₂ shield to cut boil-off). To reach ~1.8–2 K you **pump on the bath below the λ-point** (sub-atmospheric superfluid), i.e. add a large roughing/Roots pump train.
- **Pros:** simplest hardware; **lowest vibration** (no moving cold parts except pumps); this is what SRF vertical-test stands (HZB SVTS, Fermilab VTS) use, and they routinely hit 1.4–2 K.
- **Cons:** consumes LHe (~1 L/hr per watt at 4 K); **refills interrupt duty cycle**; helium price volatility; needs a reliable LHe supply and ideally recovery.
- **Cost tier:** cryostat hardware low; **operating cost high and unpredictable**. Small vertical dewar/insert: low-to-mid five figures + ongoing LHe. 2 K adds a pump set (mid five figures).

### B. Closed-cycle cryocooler (Gifford-McMahon or pulse-tube)
- **Physics:** mechanical refrigerator (compressor + cold head) reaching ~2.8–4 K, ~1.5 W @ 4.2 K (e.g. Cryomech PT415). No cryogen inventory. **2 K continuously** is achievable by liquefying He gas at the cold head and running a **Joule-Thomson valve + dry pump** (closed-cycle superfluid; demonstrated 1.7 K, 100+ hr runs) — but this is a specialist add-on.
- **GM vs pulse-tube:**
  - **GM:** cheaper for equal cooling power; works in **any orientation**; more vibration; needs displacer maintenance. With a vibration-isolation exchange-gas mount, GM can match PT vibration at lower cost.
  - **Pulse-tube (PT415/PT420):** no moving cold part → **low vibration + long maintenance interval** (~20,000 hr / >2 yr); **must run vertical, 2nd stage down**; more expensive. Needs a water-cooled 3-phase compressor (~10 kW).
- **Pros:** turnkey, push-button, no cryogen logistics, continuous 100%-duty operation → "no trained operator needed." This is what makes **conduction-cooled SRF** possible (see Nb₃Sn section) and is explicitly pitched as the way "university groups and industries can do in-house SRF R&D without full-stack helium systems."
- **Cons:** vibration (couples to RF/mechanical Q measurements — mitigate with soft thermal links / exchange gas); capital cost higher than a bare dewar; wall power + cooling water.
- **Cost tier:** a complete 4 K PT system (cold head + compressor) is **~tens of thousands USD** (quote-only; refurbished PT410/PT415 units exist on the secondary market with short warranties). GM comparable-power systems cheaper.

**Recommendation:** for a small researcher, a **cryocooler (PT for low-vibration Q work, GM+exchange-gas if budget-driven)** avoids the LHe-supply headache and gives continuous duty. Stay at **4.2 K** — going to 2 K (superfluid, JT or pumped bath) roughly doubles cryo complexity for no benefit if you adopt Nb₃Sn.

---

## Nb vs Nb₃Sn (for a Q-only, low-field test)

| | Niobium | Nb₃Sn (on Nb) |
|---|---|---|
| Tc | 9.25 K | 18.3 K |
| Q~10¹⁰ operating temp | **~2 K (superfluid He)** | **4.2–4.4 K (ordinary LHe / cryocooler)** |
| Low-field Q₀ | ~10¹⁰–10¹¹ @ 2 K | ~1–2×10¹⁰ @ 4.2 K; up to 5×10¹⁰ @ 2 K, ~10¹¹ low-field @ 2 K (JLab) |
| Surface resistance @ 4.2 K | ~10× higher than Nb₃Sn | few nΩ (best-in-class at 60–70 mT) |
| Weakness | needs 2 K | **field-dependent Q-slope, thermal quench ~70 mT** (far below 400 mT theoretical Hsh) |
| Fab | bulk Nb, EB-welded | **coat existing Nb cavity** via tin vapor-diffusion (500 °C nucleation → 1100–1200 °C coating) |

**Key point for this experiment:** Nb₃Sn's headline limitation is quench at high accelerating gradient (~14–17 MV/m, ~70 mT). **A propulsion-effect Q-test is a low-field measurement** — you operate near the low-field plateau where Nb₃Sn @ 4.2 K already delivers 1–2×10¹⁰. The quench ceiling is irrelevant to a Q-only test. So Nb₃Sn gives you **the same Q as niobium but with ordinary 4.2 K liquid helium / a single cryocooler**, cutting cryogenic operating cost/infrastructure by roughly an order of magnitude. Nb₃Sn is the correct Q-only target; Nb @ 2 K only wins if you later need very high field *and* the last factor of a few in Q.

---

## SRF vendors / facilities + access models

Fully-assembled, ready-to-test SRF cavities come from a **very short list**. Realistic access for a small researcher is *not* "buy one off the shelf" — it's collaboration or coating-service.

**Industrial cavity fabricators (build-to-print, big-project scale):**
- **RI Research Instruments GmbH** (Germany, DESY-linked) — one of two worldwide full-service suppliers; built 429 of the European XFEL cavities.
- **Ettore Zanon S.p.A. / Zanon Research & Innovation** (Italy, INFN-linked) — the other; shared XFEL + LCLS-II production.
- These two are the only firms that deliver fully assembled, tested cavities. Pricing is **quote/contract-only, never listed**; they're geared to multi-hundred-cavity orders (US SRF procurement ran ~$149M, ~70% foreign-supplied).

**National labs (R&D, coating, testing — the realistic route for a small program):**
- **Jefferson Lab (JLab)** — Nb₃Sn multicell coating system; large-grain single-cell fabrication; vertical test.
- **Fermilab (FNAL)** — Nb₃Sn vapor-diffusion, **conduction-cooled cryocooler SRF**, VTS with 1.4 K dewars; the compact-accelerator program most aligned with a small turnkey system.
- **Cornell** — Nb₃Sn pioneer (~10¹⁰ @ 4.2 K single-cell); strong university SRF group.
- **DESY** (XFEL surface-treatment transfer), **INFN-LASA** (single-cell cost-reduction studies, orders placed with RI), **KEK** (seamless hydroforming), **IMP/IHEP (China)** (conduction-cooled Nb₃Sn e-linac with beam).

**Access models for a small researcher (in order of realism):**
1. **Coating service / collaboration:** supply (or buy) a bare single-cell 1.3 GHz Nb cavity, have JLab/Fermilab/Cornell Nb₃Sn-coat + vertical-test it under a user agreement or collaboration. Lowest capital, but gated on lab willingness and queue.
2. **Buy a processed single-cell Nb cavity** from RI/Zanon (or via a lab), coat elsewhere.
3. **Turnkey conduction-cooled route:** pair a coated single-cell cavity with a commercial cryocooler in a simple vacuum vessel — the Fermilab model explicitly aimed at putting SRF in reach of university/industry groups without a helium plant.

---

## The cryo-copper intermediate rung (RRR>100 Cu at ~4 K)

**Idea:** before committing to superconductivity, cool a **high-purity (RRR>100) copper** cavity to ~4 K to get a genuine middle Q-point and de-risk the whole cold-RF chain.

**What you actually get — honesty note:**
- Measured reality (haloscope + SRF-adjacent literature): cryogenic copper reaches **~10⁵ at sub-GHz** (e.g. ~4.5×10⁵ Q₀ at 57 MHz OFE copper @ 4 K), **~10⁵ at hundreds of MHz**, and only **~10⁴ at multi-GHz**. The 340 MHz bulk-copper study (arXiv:2211.00135) reached RRR≈120 after 400 °C anneal + Cu-plate and is the best direct experimental analogue.
- **The ~10⁶ figure in the shared context is optimistic.** The **anomalous skin effect** is the reason: below ~4 K the electron mean free path exceeds the RF skin depth, so RF surface resistance stops tracking DC resistivity. DC RRR can hit 400+, but **Q gains lag far behind** — real-world cooling gives ~10–60% Q improvement over naive expectation, capped near ~10⁵ at your likely frequency. Oxide layers and joints erode it further.
- So this rung realistically moves Q from 2.7×10⁴ → **~1–4×10⁵** (≈4–15×), *not* to 10⁶. It is a **real extra decade** on the F∝Q line — still valuable — but don't oversell it.

**Why still worth it:**
- **Cheap:** reuses a copper cavity (machinable, no coating, no superconductivity); only cost is the 4 K cryostat you need anyway for the SRF rung.
- **De-risks:** validates the cryostat, cold RF feedthroughs, coupling, vibration handling, and the F-measurement at cold — on a disposable cavity — before a five-figure Nb₃Sn cavity goes in.
- **Adds a genuine mid-ladder point** between RT copper and Nb₃Sn, strengthening the F∝Q discriminator with an independent measurement in a regime with *no superconducting physics* (rules out "effect only appears with superconductors" confounders).
- Keep it **sub-GHz** to maximize the achievable Q (the anomalous-skin penalty worsens with frequency).

---

## Realistic cost tiers per rung

Order-of-magnitude, USD, small single-researcher program. Cavity prices anchored to Fermilab's public "car analogy" (2021): processed **1-cell ≈ $40k**, bare 9-cell ≈ $85k, dressed 9-cell ≈ $250k. Cryostat/cryocooler quote-only.

| Rung | Cavity | Cryogenics | Other | Rough total |
|---|---|---|---|---|
| **0 — Cu, RT (have)** | ~$1–5k (machined Cu) | none | RF/VNA existing | in hand |
| **1 — cryo-Cu, 4 K** | reuse Cu (RRR>100 stock, anneal) | 4 K **cryocooler** ~$30–80k (PT) *or* small LHe dewar+insert (lower capital, ongoing LHe) | cold feedthroughs, thermometry ~$5–15k | **~$40–100k** (dominated by the cryostat you need anyway) |
| **2b — Nb₃Sn @ 4.2 K (preferred)** | single-cell Nb ~$40k + Nb₃Sn coating (lab collab / service, often in-kind) | **same 4 K cryocooler as rung 1** (reused) | vacuum vessel, conduction links, RF ~$10–30k | **~$70–150k** *if* coating via collaboration; **higher** if buying full-service from RI/Zanon |
| **2a — Nb @ 2 K (only if needed)** | single-cell Nb ~$40k | 2 K = pumped superfluid bath **or** JT-stage cryocooler: **+$30–80k** over 4 K | Roots/roughing pump train, controls | **~$120–250k+**, higher operating complexity |

**Notes:**
- Rungs 1 and 2b **share the same 4 K cryostat** — buy the cryocooler once, run cryo-copper first, then swap in the Nb₃Sn cavity. This is the efficient path and the main argument for the intermediate rung.
- Numbers exclude labor, RF amplifier/VNA (assume you have Phase-1 gear), magnet (if the effect needs one), and lab overhead/user-agreement fees.
- 2 K (rung 2a) is a genuine step-up in cost *and* operating burden (superfluid handling, big pumps) — avoid unless a Q-only-at-2K margin is scientifically required.

---

## Open risks

1. **Cryo-copper Q ceiling.** Anomalous skin effect likely caps rung-1 Q near ~10⁵, below the shared-context ~10⁶. Frequency choice matters (go sub-GHz). Risk: the middle point is smaller a lever than hoped.
2. **Vibration ↔ Q measurement.** Cryocooler vibration can modulate cavity frequency/coupling and corrupt a precise Q (and F) measurement. Mitigate: pulse-tube + soft thermal links/exchange-gas mount, or accept LHe-bath low-vibration for the precision runs.
3. **Nb₃Sn coating access.** No small researcher coats Nb₃Sn in-house (1100–1200 °C tin vapor-diffusion furnace). Whole rung-2b hinges on a lab collaboration/service slot — schedule and willingness are the real gating items, not cash.
4. **Field-regime consistency.** Nb₃Sn's high-Q is a *low-field* property; ensure the F-effect test genuinely operates low-field, else quench/Q-slope confounds the F∝Q fit.
5. **Confounders across rungs.** Changing material/temperature changes more than Q (surface fields, thermal contraction, coupling, mode purity). Hold geometry/mode fixed; calibrate Q₀ identically at each rung so the F∝Q line isn't an artifact.
6. **Helium supply / cost volatility** (if LHe-bath chosen) vs. **wall-power + cooling-water + capital** (if cryocooler). Pick per local infrastructure.
7. **This is the specialist/expensive end.** Even the "cheap" superconducting rung is ~$70–150k *with* an in-kind coating collaboration, and assumes access to national-lab SRF expertise. Budget and partnerships, not physics, are the near-term bottleneck.

---

## Sources (URLs)

Cryostats / cryocoolers:
- Closed-cycle vs bath trade-off (attocube): https://www.attocube.com/en/products/cryostats/why-choosing-a-closed-cycle-cryostat
- Closed-cycle superfluid (He II) production with GM cryocooler: https://www.sciencedirect.com/science/article/abs/pii/S0011227514001672
- High-capacity closed-cycle 1.4 K cryostat: https://www.sciencedirect.com/science/article/abs/pii/S0011227526001529
- CUORE tonne-scale cryogenics (PT replacing LHe bath in DRs): https://arxiv.org/pdf/2108.07883
- Cryomech PT415 (Bluefors): https://bluefors.com/products/pulse-tube-cryocoolers/pt415-1k/
- PT vs GM (Lake Shore/Janis, price + orientation + vibration): https://www.lakeshore.com/products/product-detail/janis/pulse-tube-cryocoolers-vs.-gifford-mcmahon-cryocoolers
- Cryogenic Ltd GM/PT spec sheet: https://www.cryogenic.co.uk/sites/default/files/product_files/cryo_cooler_spec_0.pdf

Nb₃Sn vs Nb / SRF materials:
- Snowmass 2021 Nb₃Sn SRF white paper: https://arxiv.org/pdf/2203.06752
- Fermilab: Nb₃Sn a maturing technology: https://lss.fnal.gov/archive/2022/conf/fermilab-conf-22-321-td.pdf
- JLab Nb₃Sn single-cell results (Q₀ >5×10¹⁰ @2K, 2×10¹⁰ @4K): https://www.osti.gov/biblio/1975499
- Nb₃Sn multicell coating system at JLab (RSI): https://pubs.aip.org/aip/rsi/article/91/7/073911/966914
- Tin vapor-diffusion coating optimization: https://www.sciencedirect.com/science/article/abs/pii/S0169433223023887
- IHEP niobium cavity Nb₃Sn coating (Rs at 4.2 K ~ Nb at 2 K): https://www.sciencedirect.com/science/article/abs/pii/S0921453422000922

SRF vendors / facilities / cost:
- Zanon Research RF cavities: https://www.zanonresearch.com/rf-cavities/
- JLab business plan for domestic SRF supply (JLAB-TN-24-043, $149M/$100M figures): https://www.osti.gov/servlets/purl/2497788
- XFEL industrial cavity production (RI + Zanon build-to-print): https://journals.aps.org/prab/abstract/10.1103/PhysRevAccelBeams.19.092001
- Fermilab SRF capabilities: https://technology.fnal.gov/capabilities/srf-technology-and-materials/
- Fermilab USPAS cavity cost figures ($40k/$85k/$250k): https://uspas.fnal.gov/materials/21onlineSBU/Cryo/12%20-%20SRF%20Cavities.pdf
- HZB Small Vertical Test Stand / single-cell testing context: https://journals.aps.org/prab/abstract/10.1103/1jh5-65xh

Conduction-cooled Nb₃Sn (turnkey/compact, cryocooler):
- Fermilab first cryocooler conduction-cooled SRF demo: https://arxiv.org/abs/2001.07821
- Fermilab compact-accelerator conduction-cooling slides: https://lss.fnal.gov/archive/2024/slides/fermilab-slides-24-0218-etd-td.pdf
- IMP/CAS LHe-free Nb₃Sn e-linac with beam: https://arxiv.org/abs/2404.09187

Cryo-copper / anomalous skin effect:
- Anomalous skin effect + copper cavity at cryogenic conditions (340 MHz, RRR≈120): https://arxiv.org/abs/2211.00135
- Cryogenic surface resistance of copper (PRAB, RRR≈100 OFE): https://link.aps.org/pdf/10.1103/PhysRevAccelBeams.22.063101
- Anomalous skin effect study of normal metals (OSTI): https://www.osti.gov/servlets/purl/1827721
- Haloscope cryo-copper Q limits (~10⁵ sub-GHz, ~10⁴ multi-GHz): https://arxiv.org/pdf/2404.15926
- KLASH proposal (OFE Cu Q₀=4.5×10⁵ @4K, 57 MHz): https://arxiv.org/pdf/1707.06010
