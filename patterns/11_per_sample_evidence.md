# Pattern 11: Per-Sample Evidence (Paired Clouds, Distribution Grids, Exceedance Curves)

## Purpose
Show that an effect exists **in the data, row by row**, not only in a pooled mean. This is the pattern an
author reached for whenever a point-and-interval figure was rejected as "crude": the same numbers, drawn at the
level of the individual sample, with the pooled statistic reduced to a side note.

## Claim types
- "Construction B changes nothing relative to construction A" → paired cloud on the diagonal.
- "Intervention C removes the effect" → paired cloud pinned to the zero line.
- "Estimator P is fragile under condition X, estimator Q is not" → two overlaid per-sample distributions, one wide
  and one narrow, repeated across cohorts and conditions as a grid.
- "P makes fewer large errors than Q" → exceedance curves (fraction of samples whose error exceeds x, log y).
- "The learner beats the baseline on most samples at low budget, not at high budget" → error-vs-error clouds per
  budget with the percentage below the diagonal printed.

## Structure

```
+------------------+------------------+------------------+---------------+
| object / example | paired cloud     | mechanism cloud  | endpoint      |
| (matrix, strip)  | y = x reference  | binned medians   | (smallest,    |
|                  | zero reference   | zero crossing    |  last)        |
+------------------+------------------+------------------+---------------+
```
Reading order: object → mechanism → all samples → endpoint. Any layer can be dropped; the endpoint layer is the
only one that may *not* be the largest panel.

## Required elements (min. 6)
1. Per-sample points or per-sample distributions filling the panel (hundreds to thousands of samples).
2. One reference line that encodes the null: identity `y = x`, zero line, or "unchanged".
3. Structure that is the conclusion (diagonal, band, slant, width difference) and passes the load-bearing test
   in [FORM_LADDER.md](../docs/FORM_LADDER.md) before drawing.
4. Sample count per panel, printed in ink grey.
5. Encoding consistent with the paper's table: condition = color, cohort = marker shape or row, estimator = grey.
6. Pooled quantities as printed numbers (with source) or in a last, small panel — never as the main panel.

## Anti-patterns specific to this pattern
- The same cloud repeated with different variables after a rejection (change the layer, not the axes).
- A grid of bare clouds with nothing else — one form, no composition, is still "crude".
- Decorative contours on clouds that do not overlap.
- Composite x-axes the reader cannot name (‖Δc‖₁, "distance in feature space").
- Degenerate control panels (a perfect diagonal) at full size; compress them.
- Sentences inside the panel.

## Code (see `afp/evidence.py`)

```python
from afp.evidence import paired_cloud, binned_median, peak_normalized_hist, exceedance_curve, ecdf, structure_strength

# 1. check before you draw
print(structure_strength(x_shared, y_disjoint, kind="paired"))     # corr, pass/fail
print(structure_strength(g, effect, kind="mechanism"))             # corr and binned-median rise vs IQR

# 2. paired cloud with identity + zero references
paired_cloud(ax, x_shared, y_disjoint, color=BLUE, identity=True, zero=False)
paired_cloud(ax, x_shared, y_matched,  color=ORANGE, identity=False, zero=True)

# 3. mechanism cloud + binned medians
paired_cloud(ax, g, effect, color=BLUE, identity=False, zero=True)
binned_median(ax, g, effect, nbins=10, color="k")

# 4. two overlaid per-sample distributions, peak-normalized on a common grid
edges = np.arange(-0.24, 0.2401, 0.008)
peak_normalized_hist(ax, shift_std, edges, color=BLUE)
peak_normalized_hist(ax, shift_rc,  edges, color=GREEN)

# 5. exceedance curves (fraction of rows with |r| > x), log y
exceedance_curve(ax, np.abs(res_std), color=BLUE)
exceedance_curve(ax, np.abs(res_rc),  color=GREEN)
ax.set_yscale("log")
```

## Real examples (author-accepted)
- Composition-channel figure: object matrix + paired cloud (r = 0.999 on the diagonal; matched arm on zero) +
  small endpoint groups.
- Boundary figure: risk ratio vs filled cells, three system sizes on one curve, zero crossing at ~12 cells.
- Input-representation figure: 3 × 3 grid of peak-normalized shift distributions (wide vs narrow, both collapse
  under matching) + exceedance column.
- Budget figure: 3 × 4 grid of log–log error-vs-error clouds with the percentage of rows below the diagonal
  falling from ~67 % at K = 8 to ~20–30 % at K = 1024.

Details and verdicts: [CASE_STUDIES_AUTHOR_REVIEW.md](../docs/CASE_STUDIES_AUTHOR_REVIEW.md).
