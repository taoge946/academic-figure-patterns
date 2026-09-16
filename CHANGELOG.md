# Changelog

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
