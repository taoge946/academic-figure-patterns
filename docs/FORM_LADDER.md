# The Form Ladder: What "Sophisticated" and "Cheap" Actually Mean

> Calibrated on seven main-text figures and two dozen rejected versions reviewed by a physicist author
> (a physics manuscript, Sep 2026), then validated by three blind runs in which an agent that had read only this document
> and the spec rules produced first drafts the author accepted. See
> [CASE_STUDIES_AUTHOR_REVIEW.md](CASE_STUDIES_AUTHOR_REVIEW.md) for the verbatim verdicts.

## The one-line criterion

A reader's first-glance judgement is about **information density and structure**: is the panel filled with
per-sample data (per-row, per-state, per-session), does that data show a structure one can see (a diagonal, a
horizontal band, a slanted line, a fork, a crossing of zero, a width difference), and does the conclusion *live*
in that structure?

- **Cheap** = the panel holds only statistics: a few points with error bars, a few mean lines. The reader could
  read the table instead; the figure adds nothing.
- **Showy** = there is structure but it does not carry the conclusion: density rivers, decorative contours,
  quantile bands that mean nothing.

Both pits sit on either side of the path below.

## Step 1: find the per-sample layer before choosing a form

Before drawing any result figure, look for **per-sample arrays** (npz / csv of rows, states, sessions), not just
summary json.

- Per-sample data exists → the main panel must use it; summary quantities become side notes or the smallest panel.
- Only summaries exist → ask whether the analysis can export per-sample values (in our projects it always could).
  Only if it truly cannot, draw points with intervals, and make that the smallest panel.
- **A summary-only main panel is rejected with near certainty.**

## Step 2: the ladder (try from the top, use the highest level that holds)

The levels are *information layers*, not chart types. A scatter cloud is only one possible form at levels 2–4;
matrices, sorted strips, ridge distributions, trajectory bundles, slopegraphs and small-multiple grids are all
valid at the same level. "You seem to love scatter clouds — path dependence?" was itself a verdict.

1. **The object itself.** If the figure is about a *thing* (a setting composition, a record, a circuit, a
   sequence), draw the thing first, as a matrix / strip / grid, using one real instance (state the selection rule
   in the data file; do not pick the prettiest).
   *Example:* a settings × qubits measurement-axis matrix, three blocks side by side (reference / arbitrary / matched replacement).
2. **Per-sample paired view.** The same sample under two constructions, x–y. The conclusion is the cloud's shape:
   diagonal = identical, horizontal band = unrelated, slanted line = proportional.
   *Example:* per-row label shifts under two replacement schemes fall on the diagonal; the matched scheme collapses to the zero line.
3. **Per-sample effect vs an explanatory variable.** x = a mechanism variable the reader can name, y = the effect,
   with binned medians; where the structure crosses zero is the boundary.
   *Example:* risk ratio against the number of filled cells; three system sizes fall on one curve that crosses zero at a boundary.
4. **Multi-group per-sample small multiples.** A grid by cohort / pair / arm, shared axes, one cloud or one
   distribution per cell plus one summary line.
   *Example:* five qubit pairs, one lifted clearly above zero, the others pinned at zero; or a 3 × 3 matrix of
   peak-normalized shift distributions (cohort × reuse design) where one input is wide and the other narrow.
5. **Summary panel** (points + intervals, dumbbell, slopegraph): only for endpoint quantities, placed **last and
   smallest**, or grouped so the grouping itself is the structure.

### The load-bearing test (run it before drawing)

Compute, do not eyeball:

| Form | Passes when |
|---|---|
| Binned medians vs x | rise/fall of medians > IQR band width |
| Paired cloud | correlation > 0.9 (or a clearly non-diagonal shape that *is* the claim) |
| Cloud vs explanatory variable | correlation > 0.5 |
| Two overlaid distributions | width ratio visibly ≠ 1 (≥ 2×), or a mean shift > 1 sd |
| Exceedance / ECDF pair | curves separate by a visible factor over a range, not only at one quantile |

A panel that fails is "structure-shaped" and gets deleted, however pretty. We kept a mechanism cloud with
r ≈ 0.25 once; it was the first thing the author cut.

Axes carry only quantities a reader can name (cell count, property value, anchor value), never composite
distances like ‖c_reuse − c_clean‖₁. Derived quantities beyond "archived column differences, binned medians,
counts" must be cleared with the analysis owner first.

## Step 3: forms that were rejected, verbatim reasons

| Rejected form | Verdict |
|---|---|
| Three panels of points + vertical intervals | "a bit crude", "still monotonous, still points and lines" |
| Jittered session / row strips as a main panel | "all dot-plots", "what advantage over error bars?" — a strip is an error bar in disguise unless the claim is about unanimity vs. outliers |
| Three scatter clouds in a row for one figure | "you only know scatter plots?" — after a rejection, change the *chart type*, not the variables inside the cloud |
| Density river / gradient columns | "does it mean anything?" |
| Quantile bands / violins / lines as main panel | "still lines and points, too empty" |
| Toy mini-plots inside a concept figure | replaced by schematic clouds in the same visual language as the data figures |
| Decorative contours | only when one-sample-one-point clouds overlap heavily; never on concept figures |
| Same form twice in one figure (b and c both point plots) | reject |
| Heat-map tiles of binned means as the main figure | "these color blocks look weird and cheap" — a tile grid of summaries is a table |
| Bare 2 × 3 grid of identical clouds, nothing else | "too crude, garbage" — one form repeated with no composition |
| Slope-before vs slope-after with fold bars; risk-vs-damage plane with 9 points | "a pile of messy points" — summary points dressed as data |
| Re-forming an *accepted* figure because a task list asked for "more comparisons" | "why did you change it back?" — task lists are content requests, not form requests |

## Step 4: what accepted figures had in common

- One claim per panel; form follows claim. Form may repeat across figures if each says its own thing.
- Explanatory text in ink greys, never series colors. **No sentences inside the figure**: labels ≤ 6 words, no
  verbs, no colon explanations ("median |shift| 0.059" is fine; "binned medians cross zero at z ≈ 0.45: high
  labels pulled down" goes to the caption).
- Key numbers may be printed if they come from the data file with a source; check sign and interval before
  printing ("−0.10 [−0.03, 0.21]" once slipped through).
- A degenerate control panel (a perfect diagonal, a flat band) says "nothing happened": true, but not worth a
  full cell. Compress it to a narrow strip or merge it into the neighbour.
- Intervals reaching the axis floor get a small arrow at the bar end, not a bar to the frame.
- Panel order = reading order: **object → mechanism → all samples → endpoint**.
- One script + one data file per figure; only subtraction, binning and counting of archived arrays.
- Full width for double-column venues (180 mm), annotation text 5–8 pt depending on venue, panel letters in the
  venue's format.

## Step 5: when the author says "cheap" / "crude" / "monotonous"

1. Diagnose which layer failed (no per-sample data? structure fails the load-bearing test? same form repeated?).
2. State the diagnosis and confirm it before changing anything.
3. Change the *layer*, not the variables; consult the venue corpus if two changes in a row failed.
4. Log the version; keep the rejected file.

## Blind-run record

Three agents that read only this document plus the spec rules were asked to draw new figures from data they had
never seen. Run 1 started at ladder level 2–3 without prompting, but added a structure-weak mechanism cloud and a
redundant ring encoding. Run 2 fixed those, then wrote sentences inside the figure, mis-signed an annotation, and
gave two degenerate control panels a full row. Run 3, after adding those three rules above, produced a draft that
went to the author unchanged. The rules converged in three rounds.
