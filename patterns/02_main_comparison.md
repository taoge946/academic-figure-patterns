# Pattern 02: Main Comparison Figure

## Purpose
Present your method vs. all baselines on the primary experiment. This is the figure reviewers scrutinize most.

## Claim Type
"Our method achieves state-of-the-art performance across X benchmarks"

## Top-Venue Standard: Information Density Requirements

A strong comparison figure is never just "a few bars." It should simultaneously convey:
1. **Absolute performance**: The numerical value for each method
2. **Relative gap**: How much better you are than the baselines
3. **Statistical significance**: Error bars / confidence intervals
4. **Resource cost**: Compute differences must not be hidden
5. **Multiple dimensions**: At least 2 metrics or 2 datasets

## Presentation Choices

### Option A: Dot Plot (3--8 methods x 2--5 datasets or metrics)
```
Each group = one dataset / metric
Each dot   = one method, with its interval
- The axis may be zoomed (dots encode position, not length)
- Intervals are mandatory; say what they are (sd over 5 seeds, 95% CI, ...)
- Horizontal dashed lines for random baseline / human performance, if they fit the range
- Your method in the prominent color; baselines muted
```
Runnable example: `examples/01_comparison_before_after.py`.

### Option A': Grouped Bar Chart (only when the axis can start at 0)
A bar encodes its value by its **length**, so its axis must start at zero. If all values sit in a narrow
range (e.g., 85--95), zero-based bars make the differences invisible and a truncated axis (e.g., starting at
83) makes a 2-point gap look like a 3x gap. Neither is acceptable: use Option A, or Option E.

**Required elements** (A and A'):
- Intervals (specify std / SEM / 95% CI, and over what)
- Reference lines (random chance / human / theoretical upper bound) where meaningful
- Best result identifiable (bold number / distinct color)
- Methods grouped by category (classical / DL-based / ours)

### Option E: Difference Plot (the claim is "we beat the best baseline")
```
y = metric (or dataset), x = ours - best baseline, with an interval for the difference
Zero line = "no improvement"
```
This draws the quantity the claim is about. If an interval crosses zero, the reader sees it at once.
Panel (c) of `examples/01_comparison_before_after.py` is this form.

### Option B: Table + Supplementary Plot (Most Common Combination)
The main table appears in the text; the supplementary plot shows:
- **Rank changes** across datasets -> Bump Chart
- **Profile** of each method across metrics -> Dot plot per metric (small multiples); a radar chart only
  with the caveats in `techniques/06_radar.md` (its area depends on axis order)
- **Performance vs. efficiency trade-off** -> Scatter + Pareto

### Option C: Scatter Plot (Many Methods / Configurations)
```
x = compute cost (FLOPs / params / time)
y = performance metric
Point size = additional dimension (e.g., memory)
Your method = large star marker; baselines = small circles
Pareto frontier line
```

### Option D: Heatmap (Full Matrix of Datasets x Methods)
```
Rows = methods, Columns = datasets
Color = performance value
Best values outlined / bolded
Rows sorted by average rank
```

## Multi-Panel Composition (Common at Top Venues)

```
+------------------------+------------------------+
| (a) Dot plot           | (b) Difference plot    |
| datasets x methods     | ours - best baseline   |
| mean + interval        | per dataset, with CI,  |
| (zoomed axis is fine)  | zero line = no gain    |
+------------------------+------------------------+
| (c) Performance vs. efficiency scatter + Pareto  |
| x=FLOPs, y=Acc, size=memory                     |
+--------------------------------------------------+
```
(a) shows where every method sits, (b) shows the quantity the claim is about, (c) shows what it costs.
`examples/01_comparison_before_after.py` implements (a) + (b).

## Key Techniques

### Data Organization
```python
# Group methods by category, not alphabetically
method_groups = {
    "Classical": ["LP", "SDP", "Greedy"],
    "DL-based": ["GNN", "Transformer", "LSTM"],
    "Ours": ["Ours (small)", "Ours (large)"]
}
# Keep one fixed order in every figure of the paper (e.g., by category, ours last), stated once.
# The order is for finding things, not for steering the impression: do not re-sort per panel
# to put ours in the most flattering position.
```

### Uncertainty of the Difference (instead of significance stars)
With 3--5 seeds per method and many method x dataset comparisons, a star from `p < 0.05` says little:
the test has almost no power, the multiple comparisons are uncorrected, and the star hides how large the
gain is. Draw the difference and its interval instead (estimation plot, cf. DABEST):
```python
# per-seed scores, same seeds / splits for both methods where possible
diff = ours_scores - best_baseline_scores            # paired if seeds are matched
rng = np.random.default_rng(0)
boot = [rng.choice(diff, len(diff)).mean() for _ in range(5000)]
lo, hi = np.percentile(boot, [2.5, 97.5])
ax.errorbar(diff.mean(), row, xerr=[[diff.mean() - lo], [hi - diff.mean()]], fmt='o')
ax.axvline(0, color='0.3', lw=0.6)                   # zero = no improvement
```
With only 3--5 seeds a bootstrap interval is itself rough; say so, and show the per-seed differences as
points. If a reviewer or venue asks for a test, report the test name, n, the correction for multiple
comparisons, and the effect size, in the caption or a table, not as stars alone.

### Dual Y-Axis (Displaying Two Metrics Simultaneously)
Venue-dependent: tolerated in ML/systems hero figures, banned in the APS workflow (see
`docs/VENUE_RULES.md`). Two side-by-side panels with a shared x-axis are usually clearer.
```python
ax2 = ax.twinx()
ax2.plot(x, metric2, '--', color='tab:red')
ax2.set_ylabel('Metric 2', color='tab:red')
ax2.tick_params(axis='y', labelcolor='tab:red')
```

## When Not to Use This Pattern

- **Two methods, many samples or seeds**: the claim is about per-sample behaviour. Use a paired view
  (ours vs baseline per sample, identity line) from Pattern 11, or an estimation plot (raw data + the
  difference with its CI).
- **Many methods x many datasets**: a table is often the honest choice; a figure only adds value if it shows
  a structure the table hides (ranks changing, a trade-off).
- **Differences inside the noise**: do not design the figure to make them look large. Show the intervals
  and say the methods are comparable.
- **What if the claim were false?** Ours would sit inside the baselines' intervals, and the difference
  plot's intervals would cross zero. If the figure could not show that outcome, it is not testing the claim.

## Common Pitfalls

- Do not plot only 3 bars with no error bars and no reference lines
- Do not use the same color for all methods, making them indistinguishable
- Do not show only one metric on one dataset
- Do not truncate a bar chart's axis to make differences visible; switch to dots or a difference plot
- Do not zero-base dots when values cluster between 90--95 (differences become invisible for no reason)
- Do not omit numerical labels, forcing reviewers to estimate values by eye
- Do not ignore compute cost -- if your method uses 10x the resources, this must be disclosed
