# Pattern 09: Distribution / Statistical Analysis Figure

## Purpose
Show the distributional characteristics of performance, not just the mean. Demonstrate the stability and robustness of your method.

## Claim Types
- "Our method is more robust across different instances"
- "Performance variance is significantly lower"
- "The improvement is statistically significant"

## Top-Venue Standard: Do Not Just Report mean +/- std

### Structure A: Violin + Strip Plot (Recommended)
```python
import seaborn as sns

fig, ax = plt.subplots(figsize=(COLWIDTH, COLWIDTH*0.6))

# Violin plot to show distribution shape
sns.violinplot(data=df, x='method', y='metric', ax=ax,
               inner=None, alpha=0.3, palette='Set2')

# Strip / swarm plot to show individual data points
sns.stripplot(data=df, x='method', y='metric', ax=ax,
              size=3, alpha=0.6, jitter=True, palette='Set2')

# Annotate means
means = df.groupby('method')['metric'].mean()
for i, (method, mean) in enumerate(means.items()):
    ax.hlines(mean, i-0.2, i+0.2, color='black', lw=2)
    ax.text(i+0.25, mean, f'{mean:.1f}', fontsize=8, va='center')

# Statistical test results
from scipy.stats import mannwhitneyu
_, p = mannwhitneyu(data_ours, data_baseline, alternative='greater')
significance = '***' if p < 0.001 else '**' if p < 0.01 else '*' if p < 0.05 else 'n.s.'
# Draw significance bracket
y_max = df['metric'].max() * 1.05
ax.plot([0, 0, 1, 1], [y_max, y_max*1.02, y_max*1.02, y_max], 'k-', lw=1)
ax.text(0.5, y_max*1.03, significance, fontsize=12, ha='center')
```

### Structure B: Box Plot + Pairwise Comparison
```
Pairwise comparisons between methods:
┌──────────┬──────────┬──────────┐
│ Ours vs A │ Ours vs B │ Ours vs C │
│ Paired     │ Paired     │ Paired     │
│ difference │ difference │ difference │
│ box plot   │ box plot   │ box plot   │
│ >0 = win   │            │            │
└──────────┴──────────┴──────────┘
Reference line at 0; shade the region above 0 in green
```

### Structure C: CDF Comparison (Cumulative Distribution)
```python
# Multiple methods' CDFs on one plot
for method, values in results.items():
    sorted_vals = np.sort(values)
    cdf = np.arange(1, len(sorted_vals)+1) / len(sorted_vals)
    ax.step(sorted_vals, cdf, label=method, lw=1.5)

ax.set_xlabel('Performance')
ax.set_ylabel('Cumulative Fraction of Instances')
# If your CDF is further right -> your method is better overall
# If CDFs do not cross -> your method is better on all instances (stochastic dominance)
```

### Structure D: Heatmap Matrix (Multiple Datasets x Multiple Metrics)
```python
# Rows = methods, Columns = dataset-metric combinations
# Color encoding: gap relative to the best method

relative = (data - data.max(axis=0)) / data.max(axis=0) * 100
sns.heatmap(relative, annot=data, fmt='.1f',
            cmap='RdYlGn', center=0,
            linewidths=0.5, linecolor='white')
# Green = close to best, Red = large gap
# Numbers show raw values; colors show relative gaps
```

### Structure E: Robustness Analysis (Performance vs. Perturbation Strength)
```
┌──────────────────────────────────────────┐
│ x = noise / perturbation level            │
│ y = performance                           │
│ One line per method + confidence band     │
│ Your method degrades more slowly at high  │
│ perturbation levels -> annotate:          │
│ "Ours: -2.3% at noise=0.5"              │
│ "Baseline: -8.7% at noise=0.5"          │
└──────────────────────────────────────────┘
```

## Required Elements

1. **Full distributions**: Violin / box / CDF -- not just mean +/- std
2. **Statistical tests**: p-value and significance markers
3. **Individual data points**: Strip / swarm plot showing raw data
4. **Reference lines**: Mark key thresholds or baseline performance levels
5. **Sample size annotations**: n = ? next to each group or in the caption

## Anti-Patterns

- Do not report only mean +/- std without showing the distribution shape
- Do not claim "significantly better" without a statistical test
- Do not use box plots without specifying what the whiskers represent
- Do not substitute bar charts + error bars for violin plots (this hides the distribution shape)
- Do not draw distribution plots with very small sample sizes (n < 5)
