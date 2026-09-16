# Spec First: Write the Figure Before You Plot It

> Field-tested on a physics manuscript over 20+ author-review rounds (Sep 2026). Every figure that skipped
> this step was rejected at least twice; every figure that went through it was accepted within two rounds.

The root cause of "homework-looking" figures is **plotting before deciding what the panel compares**.
Fonts and colors come last. What decides quality is whether every panel is held up by one explicit
comparison. So the workflow has two stages, and the first one produces no plot.

## Stage 1: the spec (no plotting code yet)

One paragraph per panel. **Four questions, all mandatory:**

1. **Claim** — the one sentence a reader should get with the caption covered.
2. **Comparison** — what is compared against what. A panel with no comparison object is deleted.
3. **Encoding** — which visual encoding makes that comparison legible without reading the caption.
4. **Counterfactual** — *what would this panel look like if the claim were false?*
   If you cannot answer, the panel does not carry weight. Delete it or find data that does.

Attach one **encoding table for the whole paper**, not one per figure:

| Role | Encoding | Rule |
|---|---|---|
| Experimental condition / defect type | Color (3–4 fixed, colorblind-safe, validated) | Same order in every figure |
| Platform / chip / dataset | Marker shape | |
| Sample size / cohort size | Marker area | |
| Decomposition (e.g., intercept vs state-dependent) | Fill (solid vs hatched) | |
| Theory prediction | Dashed line without fit, labelled "prediction, no fit" | |
| Uncertainty | One convention (e.g., session bootstrap 95%), 1 px caps | Resolution limit as shaded band |
| Pre-registered / sealed cohort | Outline ring | Only when it distinguishes something |
| Estimators / methods | Grey gradient | **Never borrow condition colors** |
| Explanatory text | Ink grey, not series colors | Labels ≤ 6 words, no sentences |

Concept figures (Fig. 1) get a content spec only (which elements), and are drawn last.

### Hard bans

- A panel with no comparison object.
- A figure that could be a table (delete it; keep the table).
- matplotlib defaults: style, palette, legend placement.
- More than one claim per panel.
- Panels added to fill the page.
- Twin y-axes.

**Stop here and get the spec reviewed.** Do not start plotting until the comparison objects are approved.
"Just draw it" from a reviewer does not waive the spec; a five-line spec still goes first.

## Stage 2: draw, in order of load-bearing weight

- Draw the most load-bearing quantitative figure first, the central-claim figure second, the concept figure last.
- **One data file + one script per figure.** Every number in the data file carries its source (ledger row, hashed
  archive). Nothing is refit or resampled inside the plotting script; the script does subtraction, binning,
  counting, and asserts that its whole-panel means equal the archived values.
- Re-verify the numbers the figure depends on before drawing. If the check fails, do not draw.
- Self-check before showing anyone: render at the target column width (e.g., 180 mm double column), minimum
  text ≥ 6–7.5 pt, panel letters in the venue's format, vector PDF, and **cover the caption and write down each
  panel's conclusion**, then compare with the spec.
- Log every version (script hash, data hash, PDF hash, the reviewer's verdict in their own words). Superseded
  versions are archived, never deleted.

## When the reviewer says "this looks cheap"

Do not change the form blindly. First state your diagnosis of *which layer* failed (see
[FORM_LADDER.md](FORM_LADDER.md)) and confirm it with them. Three blind form-swaps in a row
(cloud → points → histogram) is the documented failure mode; each swap without a diagnosis was rejected.

## Using top-venue figures as reference

Look at them for **form**, not style, and only **after** the spec passed and the first draft exists.
Looking first drags the design toward whatever you saw. Take 3–5 recent figures of the same type from the
target venue (render their main figures into a contact sheet) and adjust the form once.

## Spec template

```
# SPEC — <figure id>: <one-line claim>

Figure claim (one sentence): ...
Role: main / supplementary; reading order: object → mechanism → all samples → endpoint.
Data: archived per-row arrays only (list files). Operations: subtraction, binning, counts. No re-analysis.
Encoding (inherited from the paper's table): ...

## Panel a — <form> (ladder level N)
1. Conclusion: ...
2. Compares: ...
3. Encoding: ...
4. If wrong: ...

## Panel b — ...
```

A worked, accepted example of this template: `examples/specs/SPEC_replication_example.md`.
