# Technique 03: Professional Annotations

## When to Use
**Nearly every figure should use annotations.** Annotations are the key to transforming a "data plot" into a "story plot."

## Annotation Types

### Type A: Key Finding Callout
```python
# Annotation with arrow + text box
ax.annotate(
    '3.2x faster',                          # text
    xy=(step_ours, threshold),              # arrow target
    xytext=(step_ours + 200, threshold - 5),# text position
    fontsize=9, fontweight='bold',
    color='tab:red',
    bbox=dict(boxstyle='round,pad=0.3',
              facecolor='lightyellow',
              edgecolor='gray', alpha=0.9),
    arrowprops=dict(
        arrowstyle='-|>',                   # arrow style
        connectionstyle='arc3,rad=-0.2',    # curved connector
        color='gray', lw=1.2))
```

### Type B: Reference Lines + Labels
```python
# Horizontal reference line: random baseline
ax.axhline(y=random_acc, ls=':', color='gray', alpha=0.6, lw=1)
ax.text(ax.get_xlim()[1], random_acc, ' Random\n chance',
        fontsize=7, va='bottom', color='gray')

# Horizontal reference line: human performance
ax.axhline(y=human_acc, ls='--', color='green', alpha=0.4, lw=1)
ax.text(ax.get_xlim()[1], human_acc, ' Human',
        fontsize=7, va='bottom', color='green')

# Vertical reference line: phase boundary
ax.axvline(x=phase_boundary, ls='--', color='gray', alpha=0.5)
ax.text(phase_boundary, ax.get_ylim()[1] * 0.98,
        'Phase transition', fontsize=7, ha='center', rotation=90)
```

### Type C: Shaded Regions
```python
# Highlight winning/losing regions
ax.fill_between(x, y_ours, y_baseline,
                where=(y_ours > y_baseline),
                alpha=0.1, color='green', label='Ours wins')
ax.fill_between(x, y_ours, y_baseline,
                where=(y_ours < y_baseline),
                alpha=0.1, color='red', label='Baseline wins')
```

### Type D: Value Labels on Bars
```python
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 0.5,
            f'{height:.1f}',
            ha='center', va='bottom', fontsize=7,
            fontweight='bold' if is_best else 'normal')
```

### Type E: Delta / Improvement Arrows
```python
# Draw an improvement arrow between two bars
ax.annotate('',
    xy=(x_ours, y_ours),
    xytext=(x_baseline, y_baseline),
    arrowprops=dict(arrowstyle='->', color='green', lw=2))
delta = y_ours - y_baseline
ax.text((x_ours + x_baseline)/2,
        (y_ours + y_baseline)/2 + 1,
        f'+{delta:.1f}%', fontsize=9, ha='center',
        color='green', fontweight='bold')
```

### Type F: Corner Summary Text Box
```python
from matplotlib.offsetbox import AnchoredText

textstr = f'Avg. improvement: +{avg_delta:.1f}%\nWin rate: {win_rate:.0f}%'
at = AnchoredText(textstr, loc='upper left',
                  prop=dict(size=8), frameon=True)
at.patch.set_boxstyle("round,pad=0.3")
at.patch.set_facecolor("white")
at.patch.set_alpha(0.9)
ax.add_artist(at)
```

## arrowstyle Reference
- `'->'` : Simple arrow
- `'-|>'` : Triangular head (most professional)
- `'fancy'` : Decorative arrow
- `'-['` : Square bracket (for annotating intervals)

## connectionstyle Reference
- `'arc3,rad=0.2'` : Curved arc (rad controls curvature)
- `'angle3,angleA=0,angleB=90'` : Angled connector
- `'angle,angleA=0,angleB=90,rad=10'` : Rounded angled connector
