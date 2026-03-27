# Technique 05: Waterfall Chart

## When to Use
Visualize the **cumulative contribution** of each component in ablation studies. Significantly more informative than a standard bar chart.

## Core Code
```python
import numpy as np
import matplotlib.pyplot as plt

def waterfall_chart(ax, categories, deltas, base_value,
                    colors_pos='#2ecc71', colors_neg='#e74c3c',
                    color_base='#3498db', color_final='#2c3e50',
                    show_connectors=True, show_values=True):
    """
    Draw a waterfall chart.

    Parameters:
        categories: ['Base', '+Aug', '+LR', '+Drop', '-BN', 'Final']
        deltas: [0, 3.5, 2.1, 1.2, -0.8, 0]  # first and last are 0 placeholders
        base_value: 82.0  # starting value
    """
    n = len(categories)
    values = [base_value]  # running total
    for d in deltas[1:-1]:
        values.append(values[-1] + d)
    final_value = values[-1]
    values.append(final_value)

    bottoms = []
    heights = []
    colors = []

    for i in range(n):
        if i == 0:  # Base bar
            bottoms.append(0)
            heights.append(base_value)
            colors.append(color_base)
        elif i == n - 1:  # Final bar
            bottoms.append(0)
            heights.append(final_value)
            colors.append(color_final)
        else:  # Delta bars
            d = deltas[i]
            if d >= 0:
                bottoms.append(values[i-1])
                heights.append(d)
                colors.append(colors_pos)
            else:
                bottoms.append(values[i])
                heights.append(-d)
                colors.append(colors_neg)

    bars = ax.bar(range(n), heights, bottom=bottoms,
                  color=colors, edgecolor='white', linewidth=1.5, width=0.6)

    # Connector lines
    if show_connectors:
        for i in range(n - 2):
            y = values[i+1] if i > 0 else base_value
            if i == 0:
                y = base_value
            else:
                y = values[i]
            ax.plot([i + 0.3, i + 0.7], [values[i]]*2,
                    'k-', lw=0.8, alpha=0.5)

    # Value labels
    if show_values:
        for i, bar in enumerate(bars):
            if i == 0 or i == n - 1:
                val_text = f'{heights[i]:.1f}'
                y_pos = bar.get_y() + bar.get_height() + 0.3
            else:
                d = deltas[i]
                val_text = f'+{d:.1f}' if d >= 0 else f'{d:.1f}'
                y_pos = bar.get_y() + bar.get_height() + 0.3

            ax.text(bar.get_x() + bar.get_width()/2, y_pos,
                    val_text, ha='center', va='bottom',
                    fontsize=8, fontweight='bold')

    ax.set_xticks(range(n))
    ax.set_xticklabels(categories, fontsize=8, rotation=15, ha='right')
    ax.set_ylabel('Performance')
    ax.spines[['top', 'right']].set_visible(False)

    return bars

# Usage example
fig, ax = plt.subplots(figsize=(COLWIDTH, COLWIDTH*0.6))
waterfall_chart(ax,
    categories=['Base', '+Attention', '+Residual', '+Aug', '-Dropout', 'Full Model'],
    deltas=[0, 3.5, 2.1, 1.2, -0.8, 0],
    base_value=82.0)
```

## Variant: Bidirectional Waterfall (Additive + Subtractive)

```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(TEXTWIDTH, COLWIDTH*0.5))

# Left: progressively add components from the base
waterfall_chart(ax1,
    categories=['Base', '+A', '+B', '+C', 'Full'],
    deltas=[0, 3.5, 2.1, 1.2, 0],
    base_value=82.0)
ax1.set_title('Additive', fontsize=9, pad=8)

# Right: progressively remove components from the full model
waterfall_chart(ax2,
    categories=['Full', '-A', '-B', '-C', 'Base'],
    deltas=[0, -4.1, -1.8, -1.0, 0],
    base_value=88.8)
ax2.set_title('Subtractive', fontsize=9, pad=8)
```
