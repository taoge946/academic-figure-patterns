# Before / after gallery on synthetic data

Nine datasets, each drawn twice from the **same `.npz` file** (`examples/data/`, described in `data/DATA_README.md`):

- **before** — the five-minute look at the data: one panel, one basic chart type (bar, line or scatter), matplotlib
  defaults, means where aggregation is needed, no error bars, no reference lines, no annotations
  (`examples/before_<id>.py`, drawn by an agent that was given only the data description and these constraints).
- **after** — drawn with the rules in `docs/SPEC_FIRST.md` and `docs/FORM_LADDER.md` (`examples/11*.py`, `examples/12*.py`).

All numbers are synthetic, so no result values and no experimental settings are printed inside the panels (labels are generic: scheme A/B, cohort, budget, task); the forms are the ones a
corresponding author accepted after rejecting the summary-only versions (`docs/CASE_STUDIES_AUTHOR_REVIEW.md`).
Run any script from the repository root with `PYTHONPATH=. python examples/<script>.py`.

| | before (context-free default) | after (rules applied) |
|---|:---:|:---:|
| **11a** object + paired cloud + endpoint | ![](figures/11a_before.png) | ![](figures/11a_after.png) |
| **11b** distribution grid + exceedance column | ![](figures/11b_before.png) | ![](figures/11b_after.png) |
| **11c** mechanism cloud with compressed control | ![](figures/11c_before.png) | ![](figures/11c_after.png) |
| **11d** error-vs-error grid + ECDF row | ![](figures/11d_before.png) | ![](figures/11d_after.png) |
| **12a** joint cloud, contours, marginals + decomposition | ![](figures/12a_before.png) | ![](figures/12a_after.png) |
| **12b** ML hero: scaling with a baseline-failure region | ![](figures/12b_before.png) | ![](figures/12b_after.png) |
| **12c** systems sweep (MICRO / ASPLOS look) | ![](figures/12c_before.png) | ![](figures/12c_after.png) |
| **12d** ridges + parameter-free prediction + resolution | ![](figures/12d_before.png) | ![](figures/12d_after.png) |
| **12e** measured parameter heat map + prediction contour | ![](figures/12e_before.png) | ![](figures/12e_after.png) |

## What changes between the columns

| Before typically shows | After shows instead |
|---|---|
| means with error bars, one bar or point per condition | every sample, with a reference line that encodes the null (identity, zero, "unchanged") |
| overlaid histograms of counts on one axis | peak-normalized distributions per cohort × condition, so widths compare; controls compressed |
| one panel per quantity, all the same size | reading order object → mechanism → all samples → endpoint; endpoint smallest and last |
| the model plotted as a second heat map | the model as one contour on the measurement, plus line cuts where the crossing can be read |
| default colors, legends over data, titles in the axes | condition = color, cohort = row or marker, estimator = grey; labels ≤ 6 words, no sentences |

Both columns are honest plots of the same arrays. The difference is what a reader can conclude in two seconds.

**What this comparison does and does not show.** The "before" column is deliberately minimal (one panel,
defaults, no intervals), so it is a teaching contrast, not a fair benchmark: it does not show that these forms
beat a *careful* simple figure. A careful dot plot with intervals is often the right answer, and for some
claims (a single pooled statistic, a handful of samples) it is the best one. See
[docs/RULE_STRENGTH.md](../docs/RULE_STRENGTH.md) for which rules are requirements and which are preferences.

## Forms by venue

| Script | Form (ladder level) | Venue look |
|---|---|---|
| `11a_object_paired_cloud.py` | object matrix; per-sample paired cloud on the identity line vs matched arm on zero; dose curve last (1 + 2 + 5) | physics |
| `11b_distribution_grid_exceedance.py` | 3 cohorts × 3 conditions grid of peak-normalized shift distributions; exceedance column (4) | physics |
| `11c_mechanism_cloud.py` | per-sample effect vs nameable mechanism variable, three sizes on one curve; binned medians + IQR; control strip (3 + 5) | physics |
| `11d_error_grid_ecdf.py` | 3 × 4 log–log error-vs-error clouds drifting across the diagonal with budget; ECDF row (4) | physics |
| `12a_joint_cloud_marginals.py` | joint cloud of two defect types with 25 % / 60 % contours and marginals; decomposition bars with bias below; contour small multiples | physics, npj letters |
| `12b_hero_scaling.py` | runtime + memory vs size on twin log axes, baseline-failure band, gap arrows; speedup vs size with 1× line | ICML / NeurIPS |
| `12c_systems_sweep.py` | per-device metric with the gap filled; cost vs input size with a ratio band on a twin axis and a baseline-limit wall | MICRO / ASPLOS |
| `12d_ridge_prediction_resolution.py` | stacked ridges control vs defect; ratio vs noise floor with simulated cohorts, measured cohorts and two prediction lines; resolution panel | physics |
| `12e_parameter_heatmap.py` | heat map of a measured quantity over a 2-D grid with the theory zero-crossing as a contour; two line cuts | PRX Quantum corpus form |

## What to copy from the scripts rather than from the pictures

- `structure_strength(...)` is called **before** a cloud is drawn and its result printed; a failing panel is not drawn.
- Reference lines encode the null; there is no decorative structure.
- Control conditions get a narrow strip (`11c`) or a narrow column (`11b`).
- Labels ≤ 6 words, no verbs; explanations belong in the caption.
- Panel letters use the APS form `(a)`; `letter(..., style="bold")` switches to the Nature-family form.
