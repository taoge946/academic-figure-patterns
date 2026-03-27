# Technique 04: Complex Multi-Panel Layouts

## When to Use
A single figure needs to present multiple related but distinct panels. In top-venue papers, **most important figures are multi-panel figures**.

## Method 1: subplot_mosaic (Recommended -- Most Intuitive)

```python
# ASCII layout: A spans two rows, B and C each occupy one row
fig, axd = plt.subplot_mosaic(
    """
    AB
    AC
    """,
    figsize=(TEXTWIDTH, TEXTWIDTH * 0.5),
    width_ratios=[2, 1],
    height_ratios=[1, 1],
    gridspec_kw={"hspace": 0.15, "wspace": 0.2},
    layout="constrained")

axd["A"].plot(...)   # Main panel (large)
axd["B"].bar(...)    # Auxiliary panel 1
axd["C"].imshow(...)  # Auxiliary panel 2
```

### Common Layout Patterns

```python
# 1. Main figure + side auxiliaries (Main Result + Detail)
"""
AAB
AAC
"""

# 2. One wide figure on top + three narrow figures below
"""
AAAA
BCDD
"""

# 3. 2x2 with an enlarged upper-left panel
"""
AB
CD
"""

# 4. Triptych (most common for ablation/comparison)
"""
ABC
"""

# 5. Schematic on top + three result plots below
"""
MMMM
ABCD
"""
```

## Method 2: GridSpec Nesting (Most Flexible)

```python
import matplotlib.gridspec as gridspec

fig = plt.figure(figsize=(TEXTWIDTH, TEXTWIDTH * 0.6))
gs_outer = fig.add_gridspec(2, 2, width_ratios=[3, 1],
                            hspace=0.25, wspace=0.2)

# Left column: one large figure
ax_main = fig.add_subplot(gs_outer[:, 0])

# Upper right: nested 2x1
gs_inner = gs_outer[0, 1].subgridspec(2, 1, hspace=0.1)
ax_r1 = fig.add_subplot(gs_inner[0])
ax_r2 = fig.add_subplot(gs_inner[1])

# Lower right: single figure
ax_r3 = fig.add_subplot(gs_outer[1, 1])
```

## Panel Labels

```python
from matplotlib.offsetbox import AnchoredText

for label, ax in axd.items():
    at = AnchoredText(f'({label.lower()})',
                      loc='upper left',
                      prop=dict(size=11, weight='bold'),
                      frameon=False, pad=0.1)
    ax.add_artist(at)
```

Or more simply:
```python
for i, (label, ax) in enumerate(axd.items()):
    ax.text(-0.12, 1.05, f'({chr(97+i)})',
            transform=ax.transAxes, fontsize=12,
            fontweight='bold', va='top')
```

## Shared Legend (Single Legend for Multiple Panels)

```python
# Method 1: fig.legend() placed outside the panels
handles, labels = axd["A"].get_legend_handles_labels()
fig.legend(handles, labels,
           loc='upper center', ncol=4,
           bbox_to_anchor=(0.5, 1.02),
           fontsize=8, frameon=False)

# Remove individual subplot legends
for ax in axd.values():
    if ax.get_legend():
        ax.get_legend().remove()
```

## Size Constants (Per Venue)

```python
# Automatic sizing with tueplots
from tueplots import figsizes
fig_size = figsizes.icml2024(nrows=1, ncols=2)['figure.figsize']

# Or manually set common sizes
VENUE_WIDTHS = {
    'neurips': 5.5,      # inches, single column
    'icml': 6.75,        # inches, full width (two-column)
    'icml_half': 3.25,   # inches, single column
    'iclr': 5.5,         # inches, single column
    'nature': 7.09,      # inches, full width
    'nature_half': 3.54, # inches, single column
    'prl': 3.375,        # inches, single column
    'prl_full': 6.75,    # inches, full width
}
```
