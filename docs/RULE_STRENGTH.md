# How Strong Is Each Rule?

The rules in this repository come from three kinds of source, and they are not equally binding. Read every
rule with its tier in mind. When two rules conflict, the higher tier wins.

| Tier | What it is | Source | How to treat it |
|---|---|---|---|
| **1. Integrity** | The figure must not misstate the data | Standard visualization practice (e.g., Wilke, *Fundamentals of Data Visualization*; Tufte); venue author guidelines | Required. No venue, reviewer or aesthetic preference overrides it |
| **2. Design principles** | Choices that usually make the comparison easier to read | Analysis of published top-venue figures (`REAL_PAPER_CASES.md`, `STORYTELLING.md`) | Default. Follow unless you can say why your data or claim is different |
| **3. Calibrated preferences** | What one set of reviewers accepted and rejected | Author review of two manuscripts (`CASE_STUDIES_AUTHOR_REVIEW.md`, `FORM_LADDER.md`, AP-15 to AP-21) | Useful evidence about taste, not a standard. Check whether your venue and readers are similar |

## Tier 1: integrity (required)

- **Bars start at zero.** A bar encodes a value by its length, so a truncated axis misstates ratios. When the
  values sit in a narrow range (say 85–95), switch to a position encoding (dots, dot + interval) or plot the
  *difference* from a baseline against a zero line. Dots and lines may use a zoomed axis.
- **Say what every interval is** (sd, SEM, 95 % CI, bootstrap CI) and over what (seeds, samples, sessions).
- **Do not hide data that contradicts the claim.** Failure cases, weak effects and null results stay in the
  figure, the supplement or a table.
- **Annotations must be true of the data.** A "crossover" line where nothing crosses, a "significant" star
  without a test, or a gap computed on different runs than the ones drawn are integrity failures.
- **Compare like with like**: same data splits, same compute accounting, baselines tuned in good faith.
- **Venue hard requirements**: sizes, minimum font size, file format, AI-image policies (`VENUE_RULES.md`).

## Tier 2: design principles (defaults with reasons)

- Write the spec first, including what the panel would look like if the claim were false (`SPEC_FIRST.md`).
- Show per-sample data when it exists and the claim is about samples (`FORM_LADDER.md`, Pattern 11).
- One claim per panel; a reference line that encodes the null; consistent encodings across the paper.
- Log axes for quantities spanning orders of magnitude.
- Prefer the simplest form that answers the question. A plain dot plot, line plot or scatter is often the
  right answer; a more elaborate chart type is not a goal in itself.

## Tier 3: calibrated preferences (evidence, not law)

Examples: the load-bearing thresholds (`|r| > 0.9` for paired clouds), "the endpoint panel goes last and
smallest", "no point-and-interval main panels", "labels ≤ 6 words", the systems-venue look (heavy lines,
22–29 pt source fonts). These were stable across one author's reviews and three blind runs, which is
useful. They were not tested across fields, reviewers or venues, so treat them as a strong prior for
similar work, not as requirements.

## Two corrections this tiering forced (0.2.1)

1. The old advice "start the y-axis of a bar chart at 83 when values are 85–95" broke a Tier 1 rule. The
   pattern now recommends dot plots or difference plots instead (`patterns/02_main_comparison.md`).
2. The load-bearing test was worded as a gate on whether a result may be shown. It is a diagnostic for
   whether a *particular form* carries the claim. A weak or null result is still a result: report it in a
   simpler form or a table, never drop it because its structure is not visible.
