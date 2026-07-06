# Space horizon-drive enablers — unsupported claims (V1 invocation)

> Slug: space-horizon-drive-hts-fission-cooling-2026-07-05. Captured 2026-07-05.
> 7 rows on search-summary provenance (primaries exist but not fetched this pass). Rejected = "verify against primary," not "wrong."

## Rejected rows

| Row content | Rejection reason | Suggested follow-up |
|---|---|---|
| Nb SRF cavity Q 10¹⁰–10¹¹ at 2 K | search-summary provenance (CERN p183 not fetched) | Fetch CERN p183 or the LCLS-II design report for the verbatim Q + section. |
| LCLS-II Nb intrinsic Q 2.7×10¹⁰ at 2 K, 16 MV/m | search-summary provenance | Fetch the LCLS-II TDR for the verbatim figure. |
| KRUSTY 5.5 kW-thermal, 28 kg U-235 core, 850 °C | search-summary provenance (NTRS 20180005435 not fetched) | Fetch the NTRS KRUSTY results paper for verbatim. |
| 10 kWe Kilopower Mars 1500 kg (~6.7 W/kg) | search-summary provenance; specific power is inferred, not stated | Fetch the Kilopower design paper for the verbatim mass; note W/kg is derived. |
| Fission Surface Power 40 kWe, <6000 kg, 10 yr | search-summary provenance (NTRS 20220004670 not fetched) | Fetch the NTRS 40 kWe FSP concept paper for verbatim requirements. |
| MIRI needs a 7 K active cryocooler | search-summary provenance | Fetch a NASA MIRI cryocooler page for verbatim. |
| Effective deep-space sky temperature ~7 K | low confidence; secondary summary, no primary locator | Fetch a passive-radiative-cooling review for the verbatim value. |

## Corrected premise (integrity note)
The user's "aneutronic fusion like Zap Energy" is a **misattribution**: Zap Energy's sheared-flow Z-pinch is **D-T/D-D → neutronic**, not aneutronic. Aneutronic (p-B¹¹) efforts are TAE/HB11, need ~600 keV, and have **no net-power device**. No fusion source is citable for space power — the honest comparison is **fission microreactor (real) vs fusion (nonexistent)**. Documented as an honest gap in the raw memo, not carried as a supported row.

## Summary
- Total rejected: 7 · search-summary provenance: 6 · low confidence: 1 · hard-reject: 0
- Plus 1 corrected misattribution (Zap ≠ aneutronic) retired from the premise.
- **Meta-note:** the 8 supported rows already settle the three probe questions; these 7 are numeric detail whose primaries (NTRS, CERN) are one fetch-pass from supported.
