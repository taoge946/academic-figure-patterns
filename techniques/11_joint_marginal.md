# Technique 11: Joint Plot with Marginal Distributions

## When to Use
Visualize the relationship between two variables while simultaneously showing each variable's distribution. Commonly used for efficiency-performance analysis.

## Core Code

```python
from mpl_toolkits.axes_grid1 import make_axes_locatable

fig, ax_main = plt.subplots(figsize=(5, 5))

# Main scatter plot
for name, (x, y) in methods.items():
    is_ours = 'ours' in name.lower()
    ax_main.scatter(x, y,
                    s=150 if is_ours else 60,
                    marker='*' if is_ours else 'o',
                    zorder=5 if is_ours else 3,
                    label=name, alpha=0.8)

# Add marginal distributions
divider = make_axes_locatable(ax_main)
ax_top = divider.append_axes("top", 0.8, pad=0.1, sharex=ax_main)
ax_right = divider.append_axes("right", 0.8, pad=0.1, sharey=ax_main)

# Marginal histograms
for name, (x, y) in methods.items():
    ax_top.hist(x, bins=15, alpha=0.5, label=name)
    ax_right.hist(y, bins=15, orientation='horizontal', alpha=0.5)

ax_top.xaxis.set_tick_params(labelbottom=False)
ax_right.yaxis.set_tick_params(labelleft=False)

ax_main.set_xlabel('Computational Cost (FLOPs)')
ax_main.set_ylabel('Accuracy (%)')
ax_main.legend(fontsize=8)
```

## Seaborn Shortcut (Less Control but More Convenient)

```python
import seaborn as sns

g = sns.JointGrid(data=df, x='flops', y='accuracy', hue='method')
g.plot_joint(sns.scatterplot, s=60, alpha=0.8)
g.plot_marginals(sns.kdeplot, fill=True, alpha=0.3)
g.set_axis_labels('FLOPs', 'Accuracy (%)')
g.figure.set_size_inches(5, 5)
```
