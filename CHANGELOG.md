# Changelog

## 0.2.1 — 2026-09-30

A rule review. Some advice was stronger than its evidence, and one piece broke an integrity rule.

### Fixed
- **Pattern 02 no longer recommends truncating a bar chart's y-axis** ("values 85–95 → start at 83"). Bars
  start at zero; narrow ranges use a dot plot or a difference plot (new Options A and E). AP-05, CHECKLIST E1
  and the broken-axis technique now say the same thing.
- `setup_style()` crashed on machines without LaTeX (tueplots bundles default to `usetex=True`). It now
  enables LaTeX only when it is installed; `usetex=` overrides.
- Examples 01–03 wrote to `./figures/` and needed LaTeX; they now write to `examples/figures/` from any
  working directory. Their "after" figures were redrawn: 01 uses dot plots per dataset plus the gap to the
  best baseline (was: bars truncated at 45, a radar chart with its radius starting at 70, a `%` swallowed by
  LaTeX); 02 draws base/final as level marks instead of bars from a truncated frame; 03 drops a "crossover"
  line where nothing crosses and puts the speedup on a log axis. The waterfall script no longer overwrites
  `02_*.png`.

### Changed
- New `docs/RULE_STRENGTH.md`: integrity requirements vs design defaults vs one reviewer's preferences.
  FORM_LADDER, SPEC_FIRST and CHECKLIST point to it and state their scope.
- The load-bearing test is a diagnostic for a *form*, not a gate on reporting a *result*; weak or null
  results are reported in a simpler form or a table (FORM_LADDER, CHECKLIST S3, `structure_strength` docstring).
- README: minimum-element counts removed from the pattern table and AP-01; the 2-second test asks what the
  comparison shows rather than "who wins"; claims come with their counterfactual; "before" figures are
  labelled a teaching contrast, not a benchmark; related projects listed with a license note.
- Pattern 02, 11: "when not to use" sections. Pattern 03: order dependence and spread of waterfall steps.
  Checklist C2 is now "simplest sufficient form"; E5 "annotations true of the data" added.

### Added
- `tests/`: numeric tests for `afp.evidence`, style setup without LaTeX, every example script run headless,
  and the synthetic data behind the example figures compared with the committed `.npz` files.
- GitHub Actions workflow running the tests.
- `README_zh.md`: Chinese overview (method, gallery, install, rule tiers, pattern index); linked from the
  English README.
- README: install from GitHub (the package is not on PyPI yet), the four spec questions near the top, LaTeX
  noted as optional, the per-sample evidence helpers listed in the Python API.

## 0.2.0 — 2026-09-16

The March release was distilled from published top-venue papers. This release adds what six months of
**real author review** taught (two manuscripts, ~30 rejected figure versions, three blind validation runs),
and it changes some advice.

### Added
- `docs/SPEC_FIRST.md` — the two-stage workflow: a four-question spec per panel and a paper-wide encoding
  table *before* any plotting; hard bans; self-check; spec template.
- `docs/FORM_LADDER.md` — what "sophisticated" vs "cheap" means to a reviewer, the five-level form ladder,
  the numeric load-bearing test, the verbatim list of rejected forms, and the blind-run record.
- `docs/CASE_STUDIES_AUTHOR_REVIEW.md` — nine figures, rejected versions → accepted versions, with the
  author's own verdicts (images to follow once the manuscript is public).
- `docs/VENUE_RULES.md` — APS / Nature-family / ML / systems rules that change the figure, including the two
  that flip between venues (caption content, twin axes).
- `patterns/11_per_sample_evidence.md` — paired clouds, distribution grids, exceedance curves.
- `afp/evidence.py` — `structure_strength`, `paired_cloud`, `binned_median`, `peak_normalized_hist`, `ecdf`,
  `exceedance_curve`, `fraction_below_diagonal`.
- `examples/gallery/` — an accepted ICML 2026 hero figure (LoRe) with notes; `examples/specs/` — a worked
  spec written with the template.
- `examples/11*.py` + `examples/README_pattern11.md` — four runnable synthetic-data examples reproducing the
  accepted forms (object + paired cloud + endpoint; distribution grid + exceedance column; mechanism cloud with
  compressed control; error-vs-error grid + ECDF row) and the summary-only "before" they replace.
- `examples/data/*.npz` + `DATA_README.md` — every example exports the arrays it plots; `examples/before_<id>.py` — the
  same nine datasets drawn by a context-free agent with default matplotlib, giving a before/after pair per form
  (`examples/README_pattern11.md`). The synthetic figures print no computed results and carry no experimental settings: labels are generic (scheme A/B/C, cohort, budget level, task A/B, parameter 1/2).
- `examples/12a–12e*.py` — five more forms on synthetic data: joint cloud with density contours and marginals plus
  decomposition bars; ML hero scaling figure with OOM band; systems-venue sweep (heavy lines, twin axis, timeout
  wall); ridge distributions + parameter-free prediction curve + resolution panel; measured-quantity parameter
  heat map with a prediction contour and line cuts.
- Anti-patterns AP-15 to AP-21 (summary-only main panel, jitter strips as main panel, chart-type cycling,
  sentences inside the figure, degenerate control at full size, decorative contours, redundant encoding).

### Changed
- README: new "Field-tested rules" section; the storytelling link now points at `docs/STORYTELLING.md`
  (it pointed at a non-existent file).
- AP-14 ("caption describes instead of concluding") is now marked venue-dependent: APS journals want the
  caption to describe and the text to conclude.

### Lessons that override earlier advice
- "Add elements until the panel has ≥ 6" is not the fix for a cheap figure. The fix is per-sample data with a
  structure that *is* the conclusion. Six annotations on three bars is still three bars.
- Do not swap chart types after a rejection without stating a diagnosis; three blind swaps in a row were each
  rejected.

## 0.1.0 — 2026-03-27
Initial release: 10 patterns, 13 techniques, 14 anti-patterns, 25+ real-paper cases, `afp` helpers.
