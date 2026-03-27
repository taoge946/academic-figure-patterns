# Technique 06: Radar / Spider Chart

## When to Use
Compare multiple methods across 4--8 metrics simultaneously. Instantly reveals whether one method dominates across the board or each method has its own strengths.

## Core Code

```python
import numpy as np
import matplotlib.pyplot as plt

def radar_chart(ax, categories, data_dict, colors=None, fill_alpha=0.1):
    """
    Draw a radar chart.

    Parameters:
        categories: ['Accuracy', 'Speed', 'Memory', 'Robustness', 'Simplicity']
        data_dict: {'Ours': [95, 88, 72, 91, 85],
                    'Baseline A': [90, 65, 90, 80, 70], ...}
        colors: List of colors; None for automatic assignment
    """
    N = len(categories)
    angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
    angles += angles[:1]  # close the polygon

    ax.set_theta_offset(np.pi / 2)     # start from the top
    ax.set_theta_direction(-1)          # clockwise

    # Set tick marks
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=8)

    # Set y-axis range and grid
    ax.set_ylim(0, 100)
    ax.set_yticks([20, 40, 60, 80, 100])
    ax.set_yticklabels(['20', '40', '60', '80', '100'], fontsize=6, alpha=0.5)
    ax.set_rlabel_position(30)

    if colors is None:
        cmap = plt.cm.Set2
        colors = [cmap(i / len(data_dict)) for i in range(len(data_dict))]

    for (name, values), color in zip(data_dict.items(), colors):
        vals = values + values[:1]  # close the polygon
        ax.plot(angles, vals, 'o-', linewidth=1.5, label=name,
                color=color, markersize=4)
        ax.fill(angles, vals, alpha=fill_alpha, color=color)

    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1),
              fontsize=8, frameon=False)

# Usage
fig, ax = plt.subplots(figsize=(5, 5), subplot_kw=dict(projection='polar'))
radar_chart(ax,
    categories=['Acc', 'F1', 'Speed', 'Memory', 'Robust'],
    data_dict={
        'Ours': [95, 92, 88, 75, 91],
        'GNN': [90, 88, 65, 90, 80],
        'Transformer': [93, 91, 40, 50, 85],
        'MLP': [82, 78, 95, 95, 70],
    })
```

## Best Practices
- **Normalize metrics**: All metrics must be on the same scale (0--100 or 0--1); otherwise the area is meaningless
- **Align metric direction**: All metrics must follow "higher is better." For "lower is better" metrics (e.g., latency), invert them or use 1/x
- **Use 4--8 metrics**: Fewer is better served by a bar chart; more causes visual clutter
- **No more than 4 methods**: Otherwise overlapping lines become illegible
- **Annotate key values**: Label specific numbers on the dimensions where your method wins the most
