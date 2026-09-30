# Technique 02: Broken Axis

## When to Use
- One baseline's performance is far above (or below) the others, compressing the meaningful data range
- You need to display two data intervals at different scales simultaneously
- Starting the y-axis at 0 makes the actual differences invisible

## Core API
```python
# Method 1: Manual two-subplot approach (full control)
fig, (ax_top, ax_bot) = plt.subplots(2, 1, sharex=True,
    figsize=(COLWIDTH, COLWIDTH*0.8),
    gridspec_kw={'height_ratios': [1, 3], 'hspace': 0.08})

# Plot the same data in both subplots
for name, vals in data.items():
    ax_top.bar(x, vals, label=name)
    ax_bot.bar(x, vals, label=name)

# Set respective y-ranges
ax_top.set_ylim(95, 100)   # outlier region
ax_bot.set_ylim(50, 75)    # main data region

# Hide spines at the junction
ax_top.spines.bottom.set_visible(False)
ax_bot.spines.top.set_visible(False)
ax_top.tick_params(bottom=False)

# Draw diagonal break marks
d = 0.015
kwargs = dict(transform=ax_top.transAxes, color='k', clip_on=False, lw=1)
ax_top.plot((-d, +d), (-d, +d), **kwargs)
ax_top.plot((1-d, 1+d), (-d, +d), **kwargs)
kwargs.update(transform=ax_bot.transAxes)
ax_bot.plot((-d, +d), (1-d, 1+d), **kwargs)
ax_bot.plot((1-d, 1+d), (1-d, 1+d), **kwargs)
```

```python
# Method 2: brokenaxes library (simpler)
# pip install brokenaxes
from brokenaxes import brokenaxes

fig = plt.figure(figsize=(COLWIDTH, COLWIDTH*0.7))
bax = brokenaxes(ylims=((50, 75), (95, 100)), hspace=0.08, fig=fig)
bax.bar(x, values)
bax.set_xlabel('Methods')
bax.set_ylabel('Accuracy (%)')
bax.legend()
```

## Best Practices
- **Not for bar charts whose values all sit in a narrow band.** A bar's length is its value; breaking the axis
  under every bar is truncation with extra steps. For that case use dots with intervals or a difference plot
  (`patterns/02_main_comparison.md`). Broken axes are for one or two outliers far from the rest.
- Broken axes are legitimate, but the break must be clearly marked with diagonal lines
- Do not use this to exaggerate differences -- if differences are inherently small, use inset zoom instead
- Explain in the caption why a broken axis is used
