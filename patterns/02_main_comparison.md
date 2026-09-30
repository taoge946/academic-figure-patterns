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
- **Profile** of each method across metrics -> Radar Chart
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
+------------------------+---------------+
| (a) Main bar chart     | (b) Radar     |
| 4 datasets x 6 methods | 5 metrics     |
| with error bars + refs | profile comp. |
+------------------------+---------------+
| (c) Performance vs. efficiency scatter + Pareto  |
| x=FLOPs, y=Acc, size=memory                     |
+--------------------------------------------------+
```

## Key Techniques

### Data Organization
```python
# Group methods by category, not alphabetically
method_groups = {
    "Classical": ["LP", "SDP", "Greedy"],
    "DL-based": ["GNN", "Transformer", "LSTM"],
    "Ours": ["Ours (small)", "Ours (large)"]
}
# Your method always comes last (the last item seen = strongest impression)
```

### Statistical Annotations
```python
# Mark a star where your method is significantly better than the second-best
if p_value < 0.05:
    ax.text(x, y + offset, '*', fontsize=14, ha='center', fontweight='bold')
if p_value < 0.01:
    ax.text(x, y + offset, '**', fontsize=14, ha='center', fontweight='bold')
```

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
