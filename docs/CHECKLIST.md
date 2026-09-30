# Figure Pre-Submission Checklist

After generating each figure, **verify every item below**. Any FAIL must be addressed before the figure is finalized.
Items differ in strength: Section E and D are integrity and format requirements; the rest are design
defaults (see [RULE_STRENGTH.md](RULE_STRENGTH.md)).

---

## 0. Spec -- Before Any Plotting Code (added 0.2, see SPEC_FIRST.md)

- [ ] **S1: Four questions answered per panel** -- claim, comparison, encoding, *what the panel looks like if the claim is false*
- [ ] **S2: Per-sample data located** -- the per-row / per-state / per-session arrays exist and the main panel uses them; pooled statistics are side notes or the smallest, last panel
- [ ] **S3: Form checked numerically** -- if a structure-based form (paired cloud, mechanism cloud, overlaid distributions) is meant to carry the claim, its structure is actually there (FORM_LADDER.md). If it is not, pick a simpler form or a table; the result itself is still reported
- [ ] **S4: One encoding table for the whole paper** -- condition = color, platform = shape, size = area, estimator = grey; no borrowed colors
- [ ] **S5: Spec reviewed and approved** before the first line of plotting code
- [ ] **S6: One script + one data file per figure**; every number carries its source; no refit or resampling in the script

## A. Content -- Most Important

- [ ] **A1: Clear claim** -- Can you state in one sentence what this figure is meant to prove?
- [ ] **A2: Comparative context** -- At least 1 baseline / reference / ground truth is present
- [ ] **A3: Statistical information** -- Error bars / CI / statistical test results are included
- [ ] **A4: Sufficient information density** -- Not "a few bars and done"; per-sample data with visible structure, not merely more annotations (AP-15)
- [ ] **A5: No cherry-picking** -- Includes easy + hard + failure cases (where applicable)
- [ ] **A6: Numeric labels** -- Key values are annotated directly on the figure (best value, gap, speedup); sign and interval checked against the data file
- [ ] **A7: No sentences inside the figure** -- labels ≤ 6 words, no verbs, no colon explanations (AP-18)
- [ ] **A8: Degenerate control panels compressed** -- a perfect diagonal or flat band gets a strip, not a full cell (AP-19)

## B. Narrative

- [ ] **B1: Self-explanatory** -- The figure is roughly understandable without reading the main text
- [ ] **B2: Guided reading** -- Arrows / boxes / text annotations direct the reader to key findings
- [ ] **B3: Panel order** -- object → mechanism → all samples → endpoint; endpoint panel last and smallest
- [ ] **B4: Caption lead sentence** -- ML venues: the first sentence is a takeaway. APS journals: the caption describes what is drawn; the finding goes in the text (VENUE_RULES.md)

## C. Presentation

- [ ] **C1: Appropriate figure type** -- The figure type matches the data characteristics (refer to the patterns/ directory)
- [ ] **C2: Simplest sufficient form** -- No simpler chart would answer the question equally well; any advanced technique (inset, broken axis, ridge, radar) earns its place
- [ ] **C3: Consistent colors** -- The same method has the same color across all figures
- [ ] **C4: Meaningful colors** -- Color encoding carries semantic meaning, not random assignment
- [ ] **C5: Colorblind-friendly** -- Does not rely on red-green distinction; uses shape/pattern as auxiliary cues

## D. Formatting

- [ ] **D1: No plt.title()** -- The title belongs in the LaTeX caption
- [ ] **D2: Complete axis labels** -- xlabel/ylabel include specific metric names and units
- [ ] **D3: Readable font size** -- Smallest text is at least 6pt when printed
- [ ] **D4: Vector output** -- Saved as PDF
- [ ] **D5: Correct dimensions** -- Figure size is set to the actual paper dimensions (not the default (6.4, 4.8))
- [ ] **D6: Compact layout** -- No large areas of wasted whitespace

## E. Integrity

- [ ] **E1: Honest axes** -- Bars start at 0; zoomed axes only for position encodings (dots, lines); every broken or log axis is marked
- [ ] **E2: Fair comparison** -- Baseline hyperparameters are properly tuned, not deliberately handicapped
- [ ] **E3: Transparent compute cost** -- If you used more resources, the figure reflects this
- [ ] **E4: Negative results shown** -- Cases where your method underperforms are also displayed
- [ ] **E5: Annotations true of the data** -- every arrow, "crossover", star and printed gap is computed from the plotted data

---

## Usage

After generating figure code, include a checklist summary in the code comments:

```python
# FIGURE CHECKLIST:
# Claim: "Our method converges 3x faster than baselines on all 4 datasets"
# Pattern: 05_training_dynamics (Structure B: comparative training curves)
# Techniques: inset_zoom (convergence region), annotations (speedup label)
# A1:Y A2:Y(3 baselines) A3:Y(5-run CI) A4:Y A5:N/A A6:Y(speedup labeled)
# B1:Y B2:Y(arrow annotations) B3:Y B4:Y
# C1:Y C2:Y(inset zoom + annotations) C3:Y C4:Y C5:Y
# D1:Y D2:Y D3:Y D4:Y(PDF) D5:Y(tueplots) D6:Y
# E1:N/A E2:Y E3:Y E4:Y
```
