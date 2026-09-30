---
name: academic-figure-patterns
description: Design and review result figures for academic papers (ML, physics, systems venues). Use before writing plotting code for a paper figure, when redesigning a figure a reviewer called cheap or confusing, or when checking a figure for misleading encodings. Decides what evidence goes in each panel, picks a form from a pattern library, and ends with a self-check.
---

# Academic Figure Patterns — entry point for AI assistants

This file is the workflow. The rest of the repository is reference material: read a document only when a step
below points to it. Paths are relative to the repository root.

## Rule strength (read once)

Rules here come in three tiers ([docs/RULE_STRENGTH.md](docs/RULE_STRENGTH.md)); when they conflict, the
higher tier wins:

1. **Integrity**: never violate, whatever the user, venue or aesthetics ask.
2. **Design defaults**: follow unless you can state why this data or claim is different.
3. **Calibrated preferences** (FORM_LADDER thresholds, "endpoint last and smallest", "≤ 6-word labels",
   the per-sample preference): one author's review record. Use as a prior for similar work, and say so when
   you rely on one; do not present them as standards.

## Tier 1: integrity rules (hard constraints)

- Bars start at zero. For values in a narrow range, use dots with intervals or a difference plot; never a
  truncated or broken bar axis.
- Radar charts start at radius 0, and are not the main evidence for a claim.
- Every interval is labelled: what it is (sd, SEM, 95 % CI, bootstrap CI) and over what (seeds, samples).
- Every annotation is computed from the plotted data: gaps, speedups, "crossover" lines, stars. Nothing
  typed in by hand, nothing that is not true of the data.
- Do not drop, hide or shrink data because it weakens the claim: failure cases, weak effects, null results,
  and settings where the method loses stay in the figure, the supplement or a table.
- Do not change the claim to fit the figure, or the figure to fit a claim the data do not support. If the
  data do not support the user's claim, tell them.
- Compare like with like: same splits, same seeds where possible, compute differences disclosed.
- Venue hard requirements (sizes, fonts, file format, AI-image policy): [docs/VENUE_RULES.md](docs/VENUE_RULES.md).

## Workflow

### 1. Look at the data first
List what exists: per-sample arrays (rows, instances, states, seeds) or only summaries? How many samples
per condition? Are conditions paired (same instances / seeds)? This decides the form more than the claim does.

### 2. Write the spec before any code
Per panel, four answers ([docs/SPEC_FIRST.md](docs/SPEC_FIRST.md)):
1. **Claim**: what the reader should conclude with the caption covered.
2. **Comparison**: what against what. No comparison object → no panel.
3. **Encoding**: which form makes that comparison readable.
4. **Counterfactual**: what the panel would look like if the claim were false. The chosen form must be able
   to show that outcome.

Show the spec to the user and get agreement before plotting when you can. Template:
[examples/specs/SPEC_example_11a.md](examples/specs/SPEC_example_11a.md).

### 3. Pick the form
- Look up the claim in [docs/CLAIM_TO_PATTERN.md](docs/CLAIM_TO_PATTERN.md), then read only that pattern
  file in `patterns/`, including its "when not to use" section.
- Per-sample data and a claim about samples → [patterns/11_per_sample_evidence.md](patterns/11_per_sample_evidence.md)
  and [docs/FORM_LADDER.md](docs/FORM_LADDER.md).
- A handful of numbers per method → dot plot with intervals, or a difference plot
  ([patterns/02_main_comparison.md](patterns/02_main_comparison.md)). A table if the figure adds nothing.
- Choose the simplest form that answers the question. An elaborate chart type is not a goal.

### 4. Check the form numerically before drawing
For structure-based forms (paired cloud, mechanism cloud, overlaid distributions), compute the structure
first: `afp.evidence.structure_strength(x, y, kind=...)`, width ratios, share below the diagonal. If the
structure is not there, change the **form** (simpler plot, distribution of the difference, table row), not
the result, and tell the user the effect is weak.

### 5. Draw
- One script and one data file per figure; the script only loads, subtracts, bins and counts. No refitting
  or resampling inside the plotting script unless that is the analysis and it is stated.
- Style: `afp.setup_style(venue=...)` (LaTeX optional) or `afp.evidence.evidence_style()` for per-sample
  figures. Size the figure at its final width (`afp.VENUE_WIDTHS`); do not scale later.
- Working examples to copy from: `examples/01_comparison_before_after.py` (dot + difference plot),
  `examples/11a–11d_*.py`, `examples/12a–12e_*.py` (per-sample and venue-specific forms).
- Techniques only when needed: [techniques/OVERVIEW.md](techniques/OVERVIEW.md).

### 6. Self-check, then report
Render the figure, look at it, and check:

| Check | How |
|---|---|
| Tier 1 rules above | read the code: axis limits, interval definitions, where each annotation's number comes from |
| Text size at final width ≥ 6 pt (APS ≥ 7.5 pt) | figure size × font size in the script |
| No overlapping text, nothing clipped | look at the rendered image |
| Each panel's conclusion, caption covered | write it down; compare with the spec's claim |
| Counterfactual | could this figure have shown the claim to be false? |
| Venue rules | [docs/VENUE_RULES.md](docs/VENUE_RULES.md): panel letters, caption style, twin axes |

Full list: [docs/CHECKLIST.md](docs/CHECKLIST.md). Programmatic checks cover sizes, limits and numbers;
whether the evidence supports the claim and whether the figure misleads is a judgement: state yours and
leave it to the user to confirm.

Deliver: the spec, the script, the rendered figure, and a short report of the self-check, including anything
you could not verify and any Tier 3 preference you relied on.

## When the user says the figure looks "cheap" or "wrong"

Do not swap chart types blindly. Diagnose which layer failed (no comparison? summary only while
per-sample data exist? structure not visible? same form repeated? text inside the figure?), state the
diagnosis, and change that layer ([docs/FORM_LADDER.md](docs/FORM_LADDER.md), "Step 5";
[docs/ANTI_PATTERNS.md](docs/ANTI_PATTERNS.md)).
