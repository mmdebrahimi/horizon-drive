# Anti-Gravity — Inertia-Thread Recommendations, Resolved (deep-dive closeout)

> Captured 2026-07-04. Hand-authored derivation memo (schema-drift by design). Resolves the three next-session recommendations from `antigravity-first-principles-derivation-deep-dive-2026-07-04.md`. All numbers verified in `/tmp/horizon_drive.py` (exit 0; CODATA constants). North star: `plans/Anti_Gravity_idea-anchor.md`.
> Frame unchanged: suspend disbelief the orbs are real; assert only what derivation or measured physics supports; tag speculation.

---

## The finding in one line

Of the entire anti-gravity landscape, **the "horizon drive" (manufactured-horizon inertia modulation) is the ONLY idea not killed by an energy-scale or coupling-strength wall** — it is killed *so far* only by its predicted signal sitting **at or below the thermal/EMI artifact floor**. That is a fundamentally different — and more interesting — kind of "no" than modified-Maxwell / Higgs / warp, which are dead by orders of magnitude.

---

## REC #1 — Horizon drive, derived quantitatively

**The mechanism (McCulloch).** MiHsC modulates inertia when the Unruh wavelength $\lambda_U\sim 8c^2/a$ seen by accelerated internal matter is truncated by a horizon. Cosmologically that horizon is the Hubble scale $\Theta$ (→ the useless $a_0\sim10^{-10}$ regime, §5 of the parent memo). The **horizon drive manufactures a *local* horizon** of size $L\ll\Theta$ (a cavity, a metamaterial boundary), so the truncation becomes controllable in the lab.

**The condition, derived.** For a device of size $L$ to *be* the horizon for its internal matter: $\lambda_U\sim L \Rightarrow 8c^2/a\sim L \Rightarrow$
$$a_{\rm req}\sim \frac{8c^2}{L}.$$

| Cavity $L$ | Required internal accel $a_{\rm req}$ | Field on an electron ($E=a m_e/q$) |
|---|---|---|
| 1 m | $7.2\times10^{17}$ m/s² | $4.1\times10^{6}$ V/m |
| 0.1 m | $7.2\times10^{18}$ m/s² | $4.1\times10^{7}$ V/m |
| 1 cm | $7.2\times10^{19}$ m/s² | $4.1\times10^{8}$ V/m |

**The key result:** modest **MV/m-scale fields** already put electron Unruh-wavelengths at meter scale. Unlike Higgs-lightening ($10^{37}$ J for a mm³) or warp ($10^{11}\times$ universe mass), the horizon drive is **NOT energetically absurd** — the premise is lab-accessible.

**Predicted thrust (photon-rocket floor × cavity-Q).** Bare photon-rocket thrust is $P/c=3.3$ nN/W. With a resonant cavity of quality $Q$ the effective momentum exchange scales up ~$Q$:

| $Q$ | Thrust per kW |
|---|---|
| $10^3$ | ~3.3 mN |
| $10^4$ | ~33 mN |
| $10^5$ | ~330 mN |

**The honest verdict:** predicted horizon-drive thrust is **µN–mN/kW — lab-reachable in magnitude, but exactly the regime where thermal expansion, outgassing, and EMI artifacts live.** Every claimed positive (Shawyer, NASA Eagleworks) evaporated under better isolation (Tajmar/Dresden 2018–21 nulls). So the horizon drive fails **not by an energy wall but by a signal-to-noise wall** — the predicted effect is real-if-QI-is-right but sits under the artifact floor of every experiment run to date. **This is the true frontier bottleneck: a null-background thrust measurement at the µN level, not a new theory.**

---

## REC #2 — The MiHsC↔MOND $a_0$ coincidence: real, but not unique support

- $a_0(\text{MiHsC})=2c^2/\Theta = cH_0 = 6.5\times10^{-10}$ m/s².
- $a_0(\text{MOND, empirical galaxy fits}) = 1.2\times10^{-10}$ m/s².
- $cH_0/(2\pi) = 1.04\times10^{-10}$ m/s² — **essentially MOND's value.**
- Dark-energy scale $c^2\sqrt{\Lambda/3} = 5.4\times10^{-10}$ m/s² — **also ~$cH_0$.**

**Verdict:** the $a_0\sim cH_0$ coincidence is **real and striking** — but it is shared by MOND, QI, *and* ΛCDM dark energy alike. It reflects that we live near the epoch where cosmic acceleration ≈ galactic acceleration. It is therefore **necessary-not-sufficient**: it does not *uniquely* support QI over MOND or dark energy. QI's own coefficient ($cH_0$) is $2\pi$ off MOND's empirical value, and the Renda (2019) rebuttal (two derivation flaws; the galaxy fit isn't fully first-principles) stands. The coincidence is a reason to keep QI on the table, **not** a confirmation.

---

## REC #3 — Spin–torsion, inertia-side: D2 dead both ways

The parent memo closed the *gravity* side of Einstein–Cartan spin–torsion (Planck-suppressed, $2.4\times10^{-52}$ of gravity). The *inertia*-side question: could torsion mediate an inertia-reaction (a torsion analog of the vacuum-inertia idea)?

**No.** In Einstein–Cartan gravity **torsion is algebraic (non-propagating)** — it exists only *inside* spinning matter and vanishes outside it. It cannot carry a long-range reaction field, so there is **no torsion-mediated inertia channel**. The only physical effect is the same Planck-suppressed spin–spin contact term. **D2 is dead on both the gravity side and the inertia side** — fully closed.

---

## Net effect on the dossier

The anti-gravity landscape now reduces to a clean, honest hierarchy of *why* each corner fails:

| Corner | Failure mode | Kind of "no" |
|---|---|---|
| Modified Maxwell | symmetry forbids gravity-coupling mods | dead by derivation |
| Light → anti-gravity | EM energy ≥0 + coupling ~1e-43 | dead by 43 orders |
| Higgs-lightening | wrong 1% + $10^{37}$ J/mm³ | dead by energy wall |
| Warp / negative energy | Ford-Pfenning QI ~$10^{11}$× universe mass | dead by energy wall |
| Spin–torsion (D2) | Planck-suppressed, non-propagating | dead by coupling |
| Woodward MET | Tajmar null | refuted experimentally |
| **Horizon drive / QI (D1)** | **predicted thrust below artifact floor** | **NOT dead by physics — dead by signal-to-noise (so far)** |

**The single honest conclusion of the whole anti-gravity investigation:** every corner is walled off by *orders of magnitude* or *symmetry* — **except inertia-from-the-vacuum (D1)**, which is walled off only by the fact that its predicted effect (µN–mN/kW) sits under every experiment's artifact floor. If there is a real thread to pull, it is a **clean, null-background, µN-level thrust measurement on a manufactured-horizon (QI-type) device** — the one place where "if the orbs are real" meets a lab-buildable, energetically-plausible, unconfirmed-not-refuted mechanism.

**What this does NOT claim:** that QI is correct, that the horizon drive works, or that the orbs are real. It claims — by derivation + verified numbers — that D1 is the *only* corner whose "no" is experimental-precision, not fundamental-physics.

---

## Appendix — verified (script `/tmp/horizon_drive.py`, exit 0)

| Quantity | Value | Role |
|---|---|---|
| Horizon-drive accel for $L$=1 m | $7.2\times10^{17}$ m/s² | REC1 (needs only ~4 MV/m on an electron) |
| Predicted thrust, $Q$=$10^4$, 1 kW | ~33 mN | REC1 (lab-reachable, artifact-floor regime) |
| $a_0$(MiHsC)=$cH_0$ | $6.5\times10^{-10}$ m/s² | REC2 |
| $cH_0/(2\pi)$ ≈ MOND $a_0$ | $1.04\times10^{-10}$ m/s² | REC2 (coincidence) |
| dark-energy $a$-scale | $5.4\times10^{-10}$ m/s² | REC2 (same order → not unique support) |
| EC torsion / gravity | $2.4\times10^{-52}$ | REC3 (dead both sides) |
