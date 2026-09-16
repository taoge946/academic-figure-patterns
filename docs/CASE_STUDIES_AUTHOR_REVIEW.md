# Case Studies: Rejected → Accepted, With the Author's Own Words

Nine main-text and supplementary figures of one physics manuscript (quantum hardware, measurement-derived
labels; PRX Quantum format), reviewed by the corresponding author over Sep 2026. Unlike the top-venue
analyses in [REAL_PAPER_CASES.md](REAL_PAPER_CASES.md), these are **versions a real author rejected and the
versions they accepted**, so they calibrate taste better than any published example.

Images will be added after the manuscript is public. Until then each entry names the forms precisely enough to
reproduce them. Ladder levels refer to [FORM_LADDER.md](FORM_LADDER.md).

## Round 1 (first manuscript version, seven figures)

| Figure | Rejected versions (author's words) | Accepted version | Ladder |
|---|---|---|---|
| Boundary figure | v4 four panels of mean lines + points ("too crude, a few lines and dots"); v5 quantile bands ("still lines and points, too empty"); v7 density river ("does it mean anything?") | v8: (a) mean curve with per-state fractions printed in a top row; (b) **per-state cloud** of risk ratio vs number of filled Pauli cells, three system sizes falling on one curve that crosses zero at a boundary, binned medians + IQR band; (c) the hardware states as paired differences | 3 |
| Damage figure | (b) six points ("reviewers will be baffled"); (c) empty | (b) simulated cohorts as light points + mean line, the hardware cohorts on top, prediction lines 1−2x (black dashed) / 1−x (grey dotted); (c) resolution panel: grey control band vs blue reuse interval per cohort | 3 + 5 |
| Intercept figure | many contours, rings, connecting lines, global-learner points ("too busy, can't see the point"); a task-list-driven rewrite to two point-interval panels ("why did you change it back? ugly"); then three clouds + dumbbell + slopegraph ("ugly again — what was wrong with the original?") | v14/15: (a) three **per-row clouds** of defect vs reference property (purity: horizontal band; correlator: one-sided slant through the origin; ⟨Z⟩: two-sided slant through zero), points + decile median line only; (b) a dumbbell per cohort (hollow = no learner share, filled = learner share with interval) | 2 + 5 |
| Concept figure | v1–v2 toy mini-plots ("garbage", "cheap"); a version with contours ("you love contours and scatter, path dependence?") | v4: (a) one full-width pipeline row (chip → interleaved record strips → three streams → learner/audit boxes); (b–d) **schematic clouds** (a few hundred points, no contours) in the same coordinates as the data figure | object + schematic |
| Composition-channel figure | v1/v2 three point-interval panels ("a bit crude", "still monotonous") | v4, two rows: (a) **object matrix** — one real state, settings × qubit measurement axes, clean / arbitrary / matched blocks + axis-pair count grid + that row's label shift; (b) dose curve, log–log; (c) **per-row paired cloud** (shared vs fresh shots on the diagonal; matching pinned to zero); (d) endpoint statistic as a few grouped items | 1 + 2 + 5 |
| Hardware figure | (accepted before the review round) | per-state cloud + density contours + marginals; the author's reference point for "sophisticated" | 2 |
| Anchor check (SI) | — | small-multiple grid over five qubit pairs: per-row corrected vs raw damage against the anchor value, per-pair mean line; (b) three treatments | 4 + 5 |

## Round 2 (rewritten manuscript, three result figures)

| Figure | Rejected versions | Accepted version |
|---|---|---|
| Interventions figure | v2 jittered session strips in all panels ("all dot-plots", "what advantage over error bars?"); v3 with in-figure explanatory lines | v4: (a) five peak-normalized log histograms of the per-row label change by dose, median ticks; (b) per-row label change after intervention vs shared shots (fresh shots on the diagonal, matching on the zero line); (c) ECDF of the per-row witness increment for four constructions; (d) small dose curve, last |
| Budget figure | v2 strips; v3/v4 text-heavy (a) ("too small, too many words"); (b) too small | v6, full page height: (a) simulation ridges on two scales; (b) pooled gain curve + a small-budget baseline side panel; (c) grid of log–log **error-vs-error clouds** with the share of rows below the diagonal; (d) two rows of ECDFs with an inset |
| Input-representation figure | 17 versions: point-interval triplet; input paired cloud; shift band; label-change vs input cloud ("you only know scatter plots?"); per-edge fit lines ("appendix material"); heat-map tiles ("weird color blocks"); 2 × 3 bare clouds ("garbage"); slopegraph + endpoint bars ("still crude, can't see the point"); slope-vs-slope points + risk/damage plane ("a pile of messy points") | v18: cohorts × reuse designs, each cell two **peak-normalized distributions** of the per-row learner shift (one input wide, the other narrow; both collapse under matching), mean squared shift printed; plus a column of **exceedance curves** (log y) of the clean residual, where the better input has fewer large errors. The one claim with no per-row structure (a pooled paired difference) stayed in the table |

### What the 17-version figure taught

- The per-row signal for the claim was weak (correlation well below the load-bearing threshold). No clever
  form fixes weak data; the honest options were "find a quantity with per-row structure" (the shift
  distribution, with a clearly visible width ratio) or "leave the claim to the table". Cycling chart types without a diagnosis
  cost eleven versions.
- Every rejected form was a *summary dressed as data*: a few dozen slope points with fold bars, a handful of predictor
  points in a plane, tiles of binned means. The accepted form put every row on the page.
- The author accepted one panel of the summary kind (the small dose curve) when it was last and smallest.

## Cross-venue note

The same author accepted a different look for a systems paper (MICRO/ASPLOS): heavy lines (lw 5), large
markers, filled bands, twin y-axes, Times New Roman 22–29 pt, and rejected simple bars / radar / heat maps /
box plots there too. Venue changes the *style*; the content rules above (comparison object, per-sample
evidence, no summary-only main panels) held in both. See [VENUE_RULES.md](VENUE_RULES.md).

## Reusable assets from these figures

- Cloud parameters: `scatter(s=3.0–3.6, alpha=0.30–0.45, linewidths=0, rasterized=True)`; binned median line
  `lw=1.0` with white-cored markers; zero/identity lines `lw=0.6–0.9`, ink grey, dashed identity.
- Matrices: `imshow(..., interpolation="nearest", aspect="auto")` and `ax.grid(False)`.
- Intervals that reach the axis floor: `marker=7` (down arrow) at the bar end instead of a bar to the frame.
- Peak-normalized overlaid distributions: `np.histogram(..., density=True)` then divide by the max; common bin
  grid for every cell; `fill_between(step="mid", alpha≈0.3)` + `step(where="mid")` outline.
- Exceedance curve: fraction of rows with |residual| > x, log y, one vertical guide at the reported threshold.
- Code for all of these: `afp/evidence.py`.
