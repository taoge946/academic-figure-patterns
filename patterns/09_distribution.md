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

# Effect size with its interval, not only a p-value
from scipy.stats import mannwhitneyu
stat, p = mannwhitneyu(data_ours, data_baseline, alternative='two-sided')
effect = stat / (len(data_ours) * len(data_baseline))   # P(ours > baseline), 0.5 = no difference
# report e.g. "P(ours > baseline) = 0.71, Mann-Whitney U two-sided p = 0.003, n = 40 vs 40"
# in the caption; if you print a marker in the figure, the caption must say which test, n, and
# how multiple comparisons were corrected (e.g., Holm across all pairs shown).
```
Notes:
- Use a two-sided test unless the direction was fixed before looking at the data.
- If the same instances are run by both methods, the data are paired: test and plot the per-instance
  difference (Structure B), not two independent groups.
- Stars alone hide the effect size; a tiny, useless difference is "***" with enough samples.

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
            cmap='viridis',            # all values are <= 0: sequential, colorblind-safe
            linewidths=0.5, linecolor='white')
# Bright = close to best, dark = large gap (avoid red-green maps: ~8% of male readers can't separate them)
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
2. **Size of the difference with its uncertainty**: effect size + interval; a test (named, with n and
   multiple-comparison correction) where the claim is "significantly different"
3. **Individual data points**: Strip / swarm plot showing raw data
4. **Reference lines**: Mark key thresholds or baseline performance levels
5. **Sample size annotations**: n = ? next to each group or in the caption

## Anti-Patterns

- Do not report only mean +/- std without showing the distribution shape
- Do not claim "significantly better" without a statistical test, and do not let a star stand in for the
  size of the difference
- Do not use box plots without specifying what the whiskers represent
- Do not substitute bar charts + error bars for violin plots (this hides the distribution shape)
- Do not draw distribution plots with very small sample sizes (n < 5)
