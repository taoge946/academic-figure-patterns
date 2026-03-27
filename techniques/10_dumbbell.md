# Technique 10: Dumbbell Chart (Connected Dot Plot)

## When to Use
Visualize before/after or with/without comparisons. Clearer than grouped bar charts, especially when there are many categories.

## Core Code

```python
def dumbbell_chart(ax, categories, values_before, values_after,
                   label_before='Without', label_after='With',
                   color_before='#95a5a6', color_after='#e74c3c'):
    """
    Parameters:
        categories: ['Component A', 'Component B', 'Component C', ...]
        values_before: [82.0, 82.0, 82.0, ...]  (without values)
        values_after: [84.3, 83.5, 82.8, ...]   (with values)
    """
    y = range(len(categories))

    # Connecting lines
    for yi, (vb, va) in enumerate(zip(values_before, values_after)):
        color = '#2ecc71' if va > vb else '#e74c3c'
        ax.hlines(y=yi, xmin=min(vb, va), xmax=max(vb, va),
                  color=color, alpha=0.4, linewidth=6)

    # Points
    ax.scatter(values_before, y, color=color_before, s=80, zorder=5,
               label=label_before, edgecolors='white', linewidth=1)
    ax.scatter(values_after, y, color=color_after, s=80, zorder=5,
               label=label_after, edgecolors='white', linewidth=1)

    # Delta labels
    for yi, (vb, va) in enumerate(zip(values_before, values_after)):
        delta = va - vb
        sign = '+' if delta > 0 else ''
        ax.text(max(vb, va) + 0.3, yi,
                f'{sign}{delta:.1f}', fontsize=8, va='center',
                fontweight='bold',
                color='#2ecc71' if delta > 0 else '#e74c3c')

    ax.set_yticks(y)
    ax.set_yticklabels(categories, fontsize=9)
    ax.set_xlabel('Performance')
    ax.legend(loc='lower right', fontsize=8)
    ax.spines[['top', 'right']].set_visible(False)
    ax.grid(axis='x', alpha=0.2)

# Usage
fig, ax = plt.subplots(figsize=(COLWIDTH, COLWIDTH * 0.5))
dumbbell_chart(ax,
    categories=['+ Attention', '+ Residual', '+ Augmentation', '- Dropout'],
    values_before=[82.0, 82.0, 82.0, 88.8],
    values_after=[85.5, 84.1, 83.2, 88.0])
```

## Use Cases
- Ablation studies (with/without each component)
- Before/after method improvement comparisons
- Paired comparisons across different datasets
