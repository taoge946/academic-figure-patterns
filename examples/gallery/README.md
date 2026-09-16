# Gallery: figures that passed author review

Only figures from public work are stored here. Figures from manuscripts under review are described in
[docs/CASE_STUDIES_AUTHOR_REVIEW.md](../../docs/CASE_STUDIES_AUTHOR_REVIEW.md) and will be added when public.

## lore_scaling_hero.png — ICML 2026, "LoRe" (arXiv 2605.29005), Figure 1

Three panels, one claim each:

- **(a), (b)** Runtime (solid) and memory (dashed) against graph size for the baseline and the method, log y,
  twin axes. The baseline's out-of-memory region is a shaded band labelled "baseline OOM"; two annotations
  carry the numbers a reader wants ("8.2× faster", "−79 GB"). The comparison object is the baseline curve,
  and the shaded band is the counterfactual: without the method, the right half of the plot is empty.
- **(c)** Speedup against graph size, log–log, for every framework × task, with a 1× reference line.
  Sorting is by task inside the legend; the method's family shares one hue.

Why it worked: each panel has one comparison and one printed number; the OOM band turns a missing data point
into a visible argument; the reference line gives (c) a null. What would not pass an APS reviewer: twin axes
and the conclusion-first annotations (see [docs/VENUE_RULES.md](../../docs/VENUE_RULES.md)).
