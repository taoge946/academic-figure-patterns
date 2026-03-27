# Technique 13: Advanced Chart Types (Beyond the Basic Toolkit)

This file covers advanced chart types used in top-venue papers that are often overlooked.
**Each offers higher information density and stronger visual impact than its basic counterpart.**

---

## 1. Raincloud Plot = Violin + Strip + Box Combined

**Replaces**: Standard bar chart + error bar
**Advantage**: Shows distribution shape, individual data points, and statistical summary in a single plot

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch

def raincloud(ax, data_dict, colors=None, width=0.6, jitter=0.04):
    """Raincloud plot: half-violin + strip + box

    data_dict: {'Method A': array, 'Method B': array, ...}
    """
    positions = range(len(data_dict))
    names = list(data_dict.keys())

    for i, (name, vals) in enumerate(data_dict.items()):
        color = colors[i] if colors else f'C{i}'

        # Half violin (right side only)
        parts = ax.violinplot([vals], positions=[i], showmeans=False,
                               showextrema=False, widths=width)
        for pc in parts['bodies']:
            # Keep only the right half
            m = np.mean(pc.get_paths()[0].vertices[:, 0])
            pc.get_paths()[0].vertices[:, 0] = np.clip(
                pc.get_paths()[0].vertices[:, 0], m, np.inf)
            pc.set_facecolor(color)
            pc.set_alpha(0.3)

        # Strip plot (left side, jittered)
        jittered_x = i - width/4 + np.random.uniform(-jitter, jitter, len(vals))
        ax.scatter(jittered_x, vals, s=8, color=color, alpha=0.5, zorder=3)

        # Box plot (center, narrow)
        bp = ax.boxplot([vals], positions=[i], widths=0.08,
                         patch_artist=True, zorder=4,
                         medianprops=dict(color='white', lw=1.5),
                         boxprops=dict(facecolor=color, alpha=0.8),
                         whiskerprops=dict(color=color),
                         capprops=dict(color=color),
                         flierprops=dict(marker='none'))

    ax.set_xticks(positions)
    ax.set_xticklabels(names)
```

---

## 2. Beeswarm Plot

**Replaces**: Strip plot (where points overlap and become illegible)
**Advantage**: Points do not overlap, simultaneously showing distribution shape and individual values

```python
# Requires pip install swarmplot, or use seaborn
import seaborn as sns

sns.swarmplot(data=df, x='method', y='accuracy', ax=ax,
              size=3, palette=method_colors, alpha=0.7)
# Overlay boxplot for statistical summary
sns.boxplot(data=df, x='method', y='accuracy', ax=ax,
            width=0.3, showcaps=False, boxprops=dict(alpha=0.3),
            whiskerprops=dict(alpha=0), flierprops=dict(marker='none'),
            medianprops=dict(color='black', lw=2))
```

---

## 3. Waterfall Chart for Ablation Studies

**Replaces**: Grouped bar chart
**Advantage**: Intuitively shows "each component's incremental contribution"

```python
def waterfall_ablation(ax, base_value, components, deltas, colors=None):
    """Waterfall chart for ablation experiments

    base_value: base model performance
    components: ['+ Attention', '+ Residual', '+ Norm', '+ Data Aug']
    deltas: [+2.3, +1.5, +0.8, +3.1]  (increment per component)
    """
    all_labels = ['Base'] + components + ['Full']
    cumulative = [base_value]
    for d in deltas:
        cumulative.append(cumulative[-1] + d)

    n = len(all_labels)
    for i in range(n):
        if i == 0:  # Base
            ax.bar(i, cumulative[0], color='#95a5a6', width=0.6)
            ax.text(i, cumulative[0] + 0.3, f'{cumulative[0]:.1f}',
                    ha='center', va='bottom', fontsize=8, fontweight='bold')
        elif i == n - 1:  # Full
            ax.bar(i, cumulative[-1], color='#e74c3c', width=0.6)
            ax.text(i, cumulative[-1] + 0.3, f'{cumulative[-1]:.1f}',
                    ha='center', va='bottom', fontsize=8, fontweight='bold')
        else:  # Components
            delta = deltas[i-1]
            bottom = cumulative[i-1]
            color = colors[i-1] if colors else ('#27ae60' if delta > 0 else '#e74c3c')
            ax.bar(i, delta, bottom=bottom, color=color, width=0.6, alpha=0.8)
            # Label the delta value
            ax.text(i, bottom + delta/2, f'+{delta:.1f}' if delta > 0 else f'{delta:.1f}',
                    ha='center', va='center', fontsize=7, color='white', fontweight='bold')
            # Connector line
            ax.plot([i-0.3, i-0.3, i+0.3], [bottom, bottom, bottom],
                    color='gray', lw=0.5, ls='--')

    ax.set_xticks(range(n))
    ax.set_xticklabels(all_labels, rotation=30, ha='right')
```

---

## 4. Dumbbell Chart for With/Without Comparisons

**Replaces**: Grouped bar chart (two bars)
**Advantage**: Directly shows "the gap between before and after" -- the line length encodes effect size

```python
def dumbbell_chart(ax, categories, values_before, values_after,
                    color_before='#3498db', color_after='#e74c3c'):
    """Dumbbell chart for with/without comparisons"""
    y_pos = range(len(categories))

    for i, (cat, v0, v1) in enumerate(zip(categories, values_before, values_after)):
        # Connecting line
        ax.plot([v0, v1], [i, i], color='gray', lw=1.5, zorder=1)
        # Before point
        ax.scatter(v0, i, color=color_before, s=60, zorder=2, edgecolors='white', lw=0.5)
        # After point
        ax.scatter(v1, i, color=color_after, s=60, zorder=2, edgecolors='white', lw=0.5)
        # Delta label
        delta = v1 - v0
        mid = (v0 + v1) / 2
        ax.text(mid, i + 0.15, f'+{delta:.1f}' if delta > 0 else f'{delta:.1f}',
                ha='center', va='bottom', fontsize=7, color='#2c3e50')

    ax.set_yticks(y_pos)
    ax.set_yticklabels(categories)
    ax.invert_yaxis()
```

---

## 5. Bump Chart (Ranking Change Plot)

**Replaces**: Ranking columns in tables
**Advantage**: Intuitively shows "how rankings change across conditions"

```python
def bump_chart(ax, methods, datasets, ranks):
    """Bump chart: visualize ranking changes

    methods: ['Ours', 'GNN', 'MLP', ...]
    datasets: ['CIFAR', 'ImageNet', 'COCO']
    ranks: {method: [rank_on_ds1, rank_on_ds2, ...]}
    """
    x = range(len(datasets))

    for method in methods:
        r = ranks[method]
        color = '#e74c3c' if method == 'Ours' else '#95a5a6'
        lw = 2.5 if method == 'Ours' else 1.0
        alpha = 1.0 if method == 'Ours' else 0.5

        ax.plot(x, r, 'o-', color=color, lw=lw, alpha=alpha, ms=8, zorder=3)

        # Label method name at the rightmost point
        ax.text(x[-1] + 0.1, r[-1], method, va='center', fontsize=8,
                fontweight='bold' if method == 'Ours' else 'normal',
                color=color)

    ax.set_xticks(x)
    ax.set_xticklabels(datasets)
    ax.invert_yaxis()  # Rank 1 at the top
    ax.set_ylabel('Rank')
    ax.set_xlim(-0.3, len(datasets) - 0.5)
```

---

## 6. Pareto Frontier

**Replaces**: Plain scatter plot
**Advantage**: Shows "efficiency-accuracy trade-off" with dominated region annotation

```python
def pareto_frontier(ax, methods_data, our_method='Ours'):
    """Pareto frontier scatter

    methods_data: {method: {'x': cost, 'y': perf, 'size': optional}}
    """
    # Plot all methods
    for method, d in methods_data.items():
        is_ours = method == our_method
        ax.scatter(d['x'], d['y'],
                   s=120 if is_ours else 60,
                   marker='*' if is_ours else 'o',
                   color='#e74c3c' if is_ours else '#3498db',
                   edgecolors='black' if is_ours else 'none',
                   linewidths=1 if is_ours else 0,
                   zorder=3 if is_ours else 2,
                   label=method)

    # Compute and draw the Pareto frontier
    points = [(d['x'], d['y'], m) for m, d in methods_data.items()]
    points.sort(key=lambda p: p[0])

    frontier_x, frontier_y = [], []
    best_y = -np.inf
    for x, y, m in points:
        if y > best_y:
            frontier_x.append(x)
            frontier_y.append(y)
            best_y = y

    ax.plot(frontier_x, frontier_y, '--', color='gray', alpha=0.5, lw=1)

    # Dominated region shading
    ax.fill_between(frontier_x, frontier_y, ax.get_ylim()[0],
                     alpha=0.05, color='gray')

    ax.set_xlabel('Cost (FLOPs / Time / Memory)')
    ax.set_ylabel('Performance')
```

---

## 7. ECDF (Empirical Cumulative Distribution Function)

**Replaces**: Histogram
**Advantage**: Lossless information, multiple groups can overlay without occlusion; standard in Nature/Science

```python
def ecdf_comparison(ax, data_dict, colors=None):
    """Multi-group ECDF comparison

    data_dict: {'d=3': array, 'd=5': array, ...}
    """
    for i, (name, vals) in enumerate(data_dict.items()):
        sorted_vals = np.sort(vals)
        ecdf = np.arange(1, len(sorted_vals) + 1) / len(sorted_vals)
        color = colors[i] if colors else f'C{i}'
        ax.step(sorted_vals, ecdf, where='post', lw=1.5,
                color=color, label=name)

    ax.set_ylabel('Cumulative Probability')
    ax.set_ylim(-0.02, 1.05)
    ax.legend()

    # Optional: mark the median
    for i, (name, vals) in enumerate(data_dict.items()):
        median = np.median(vals)
        color = colors[i] if colors else f'C{i}'
        ax.axvline(median, color=color, ls=':', lw=0.8, alpha=0.5)
```

---

## 8. Ridge Plot = Stacked Density Curves

**Replaces**: Multiple separate histograms
**Advantage**: Compactly shows distribution evolution across conditions

```python
from matplotlib.patches import PathPatch
from scipy.stats import gaussian_kde

def ridge_plot(ax, data_dict, colors=None, overlap=0.6):
    """Ridge plot: stacked density curves

    data_dict: OrderedDict {'epoch 0': array, 'epoch 10': array, ...}
    """
    names = list(data_dict.keys())
    n = len(names)

    for i, (name, vals) in enumerate(data_dict.items()):
        color = colors[i] if colors else plt.cm.viridis(i / n)
        kde = gaussian_kde(vals)
        x = np.linspace(vals.min(), vals.max(), 200)
        density = kde(x)

        # Offset: shift each group upward by (1 - overlap)
        offset = i * (1 - overlap)
        ax.fill_between(x, offset, density + offset,
                         alpha=0.6, color=color, zorder=n-i)
        ax.plot(x, density + offset, color='black', lw=0.5, zorder=n-i+1)

    ax.set_yticks([i * (1 - overlap) for i in range(n)])
    ax.set_yticklabels(names)
    ax.set_ylim(-0.1, n * (1 - overlap) + 0.5)
```

---

## 9. Significance Brackets (Statistical Significance Annotations)

**Replaces**: Writing "p < 0.05" in the caption
**Advantage**: Directly shows on the figure which pairs of groups differ significantly

```python
def add_significance_bracket(ax, x1, x2, y, h, text='***'):
    """Draw a statistical significance bracket between two bars

    x1, x2: x-positions of the two groups
    y: starting y-position of the bracket
    h: bracket height
    text: significance marker ('*', '**', '***', 'n.s.')
    """
    ax.plot([x1, x1, x2, x2], [y, y+h, y+h, y], lw=1, color='black')
    ax.text((x1+x2)/2, y+h, text, ha='center', va='bottom',
            fontsize=8, color='black')


# Usage example
# bars = ax.bar(...)
# add_significance_bracket(ax, 0, 1, 92, 0.5, '***')
# add_significance_bracket(ax, 0, 2, 94, 0.5, 'n.s.')
```

---

## 10. Heatmap with Topology

**Replaces**: Standard grid heatmap
**Advantage**: Displays data on the actual physical topology (chip layout, network structure, graph)

See `patterns/10_quantum_hardware.md`, Sub-pattern A.

---

## Decision Tree for Choosing a Chart Type

```
What do you want to show?
|
+-- Distributions of multiple methods    --> Raincloud / Beeswarm / Ridge
+-- Incremental component contributions  --> Waterfall
+-- With/without comparisons             --> Dumbbell
+-- Ranking changes across datasets      --> Bump Chart
+-- Accuracy-efficiency trade-off        --> Pareto Frontier
+-- Distribution of a single metric      --> ECDF (not histogram)
+-- Multiple distributions across conditions --> Ridge Plot
+-- Statistical significance between groups  --> Significance Brackets
+-- Values on spatial/topological layout     --> Topology Heatmap
```
