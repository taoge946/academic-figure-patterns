# Technique 12: ConnectionPatch (Cross-Subplot Connectors)

## When to Use
- Mark a region in an overview plot and show its details in an adjacent subplot
- Connect a specific bar in a bar chart to a breakdown pie chart
- Any scenario requiring a visual link between two subplots

## Core Code

```python
from matplotlib.patches import ConnectionPatch, FancyBboxPatch
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(TEXTWIDTH, COLWIDTH*0.5))

# ax1: Overview plot (e.g., bar chart)
bars = ax1.bar(methods, values)

# ax2: Detail plot (e.g., breakdown)
ax2.pie(breakdown_values, labels=breakdown_labels, autopct='%1.1f%%')

# Connect a specific bar to the pie chart
con = ConnectionPatch(
    # From a point in ax1
    xyA=(bar_x + bar_width/2, bar_top), coordsA=ax1.transData,
    # To a point in ax2
    xyB=(-0.1, 0), coordsB=ax2.transData,
    # Style
    arrowstyle="->",
    connectionstyle="arc3,rad=0.3",
    color="gray", lw=1.5, ls='--')

fig.add_artist(con)  # must be added to fig, not ax
```

## Common Usage: Main Plot + Zoomed Subplot

```python
fig, (ax_main, ax_detail) = plt.subplots(1, 2,
    figsize=(TEXTWIDTH, COLWIDTH*0.5),
    width_ratios=[2, 1])

# Main plot with all data
ax_main.plot(x, y)

# Draw a highlight box on the main plot
from matplotlib.patches import Rectangle
rect = Rectangle((x1, y1), x2-x1, y2-y1,
                 linewidth=2, edgecolor='red',
                 facecolor='red', alpha=0.1)
ax_main.add_patch(rect)

# Detail plot showing the zoomed region
ax_detail.plot(x, y)
ax_detail.set_xlim(x1, x2)
ax_detail.set_ylim(y1, y2)

# Connector lines (right edge of box -> left edge of detail plot)
for y_frac in [0, 1]:  # top and bottom connector lines
    con = ConnectionPatch(
        xyA=(x2, y1 + y_frac * (y2 - y1)), coordsA=ax_main.transData,
        xyB=(0, y_frac), coordsB=ax_detail.transAxes,
        arrowstyle="-", color="red", lw=1, ls='--', alpha=0.5)
    fig.add_artist(con)
```
