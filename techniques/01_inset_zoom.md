# Technique 01: Inset Zoom

## When to Use
- The main plot covers a wide data range, but key differences are concentrated in a small region
- Training curves need a close-up of the convergence region to reveal final gaps
- Dense point clusters in scatter plots need magnification
- Subtle differences in qualitative figures need emphasis

## Core API
```python
# Method 1: ax.inset_axes() -- Recommended, automatically draws indicator box
axins = ax.inset_axes(
    [0.55, 0.05, 0.42, 0.42],  # [left, bottom, width, height] in axes fraction
    xlim=(x1, x2), ylim=(y1, y2))  # data range of the zoom region

# Re-plot the same data in the inset
for method, data in all_data.items():
    axins.plot(data['x'], data['y'])

# Automatically draw the connector box and indicator lines
ax.indicate_inset_zoom(axins, edgecolor="black", linewidth=1)

# Optional: adjust inset tick marks
axins.tick_params(labelsize=7)
axins.set_xticklabels([])  # if too crowded
```

```python
# Method 2: Manual creation (more control)
from mpl_toolkits.axes_grid1.inset_locator import inset_axes, mark_inset

axins = inset_axes(ax, width="40%", height="40%", loc='lower right',
                   borderpad=2)
axins.set_xlim(x1, x2)
axins.set_ylim(y1, y2)
mark_inset(ax, axins, loc1=2, loc2=4, fc="none", ec="0.5", ls='--')
```

## Complete Example: Training Curve + Convergence Region Zoom
```python
fig, ax = plt.subplots(figsize=(COLWIDTH, COLWIDTH*0.7))

# Main plot
for name, (steps, vals, ci_lo, ci_hi) in curves.items():
    line, = ax.plot(steps, vals, label=name, lw=1.5)
    ax.fill_between(steps, ci_lo, ci_hi, alpha=0.15, color=line.get_color())

# Inset: zoom into the last 20% of training
x_start = int(len(steps) * 0.8)
axins = ax.inset_axes([0.45, 0.1, 0.5, 0.45],
                       xlim=(steps[x_start], steps[-1]),
                       ylim=(min_final - margin, max_final + margin))

for name, (steps, vals, ci_lo, ci_hi) in curves.items():
    axins.plot(steps, vals, lw=1.5)
    axins.fill_between(steps, ci_lo, ci_hi, alpha=0.15)

ax.indicate_inset_zoom(axins, edgecolor="gray", linewidth=0.8)
axins.tick_params(labelsize=7)
axins.set_title('Convergence detail', fontsize=7, pad=2)
```

## Best Practices
- Do not let the inset occlude key data in the main plot
- Lines/markers in the inset must match the main plot (colors, styles)
- If the inset is too small to be legible, consider using a separate subplot instead
