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

### Option A: Grouped Bar Chart (3--8 methods x 2--5 datasets)
```
Each group = one dataset
Each bar   = one method
- Display values above bars (bold the best)
- Error bars are mandatory
- Horizontal dashed lines for random baseline / human performance
- Your method uses a solid fill; baselines use light fill / hatching
```

**Required elements**:
- Horizontal reference lines (random chance / human / theoretical upper bound)
- Error bars (specify whether std or 95% CI)
- Best result highlighted (bold number / asterisk / distinct color)
- Methods grouped by category (classical / DL-based / ours)
- Y-axis origin should not start at 0 when all values fall in a narrow range (e.g., if values are 85--95, start the axis at 83)

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
```python
ax2 = ax.twinx()
ax2.plot(x, metric2, '--', color='tab:red')
ax2.set_ylabel('Metric 2', color='tab:red')
ax2.tick_params(axis='y', labelcolor='tab:red')
```

## Common Pitfalls

- Do not plot only 3 bars with no error bars and no reference lines
- Do not use the same color for all methods, making them indistinguishable
- Do not show only one metric on one dataset
- Do not start the y-axis at 0 when all values cluster between 90--95 (differences become invisible)
- Do not omit numerical labels, forcing reviewers to estimate values by eye
- Do not ignore compute cost -- if your method uses 10x the resources, this must be disclosed
