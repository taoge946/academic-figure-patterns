"""
Helper functions for publication-quality figure annotations and visual storytelling.

These helpers implement common visual patterns found in top-venue papers:
- Reference lines and shaded regions for context
- Annotation helpers for highlighting key findings
- Inset zoom for detail inspection
- Data sorting utilities for narrative ordering
"""
import matplotlib.pyplot as plt
import numpy as np
import os


def save_fig(fig, name, fig_dir='figures/', formats=None):
    """Save figure in publication formats.

    Args:
        fig: matplotlib Figure object
        name: Filename without extension
        fig_dir: Output directory
        formats: List of formats (default: ['pdf'])
    """
    if formats is None:
        formats = ['pdf']
    os.makedirs(fig_dir, exist_ok=True)
    for fmt in formats:
        path = os.path.join(fig_dir, f'{name}.{fmt}')
        fig.savefig(path)
        print(f'Saved: {path}')
    plt.close(fig)


def add_panel_labels(axes, fontsize=12, offset=(-0.12, 1.05)):
    """Add (a), (b), (c) labels to multi-panel figures.

    Args:
        axes: dict, list, ndarray, or single Axes
        fontsize: Label font size
        offset: (x, y) position in axes coordinates
    """
    if isinstance(axes, dict):
        ax_list = list(axes.values())
    elif isinstance(axes, (list, np.ndarray)):
        ax_list = list(np.array(axes).flat)
    else:
        ax_list = [axes]
    for i, ax in enumerate(ax_list):
        label = f'({chr(97 + i)})'
        ax.text(offset[0], offset[1], label,
                transform=ax.transAxes, fontsize=fontsize,
                fontweight='bold', va='top')


def add_reference_line(ax, y, label, color='gray', ls=':', alpha=0.6):
    """Add a horizontal reference line (e.g., random chance, human baseline).

    Args:
        ax: matplotlib Axes
        y: Y-coordinate for the line
        label: Text label (e.g., 'Random', 'Human', 'SOTA')
        color, ls, alpha: Line styling
    """
    ax.axhline(y=y, ls=ls, color=color, alpha=alpha, lw=0.8)
    ax.text(ax.get_xlim()[1], y, f' {label}',
            fontsize=7, va='bottom', color=color, alpha=0.8)


def add_vref_line(ax, x, label, color='gray', ls='--', alpha=0.6):
    """Add a vertical reference line (e.g., crossover point, threshold).

    Args:
        ax: matplotlib Axes
        x: X-coordinate for the line
        label: Text label
        color, ls, alpha: Line styling
    """
    ax.axvline(x=x, ls=ls, color=color, alpha=alpha, lw=0.8)
    ax.text(x, ax.get_ylim()[1], f' {label}',
            fontsize=7, va='top', ha='left', color=color, alpha=0.8,
            rotation=90)


def annotate_best(ax, x, y, text, color='tab:red'):
    """Annotate the best result with an arrow.

    Args:
        ax: matplotlib Axes
        x, y: Coordinates of the best point
        text: Annotation text (e.g., '91.3%', 'Best')
        color: Arrow and text color
    """
    ax.annotate(text, xy=(x, y),
                xytext=(x, y + (ax.get_ylim()[1] - ax.get_ylim()[0]) * 0.08),
                fontsize=8, fontweight='bold', color=color, ha='center',
                arrowprops=dict(arrowstyle='->', color=color, lw=1.2))


def annotate_gap(ax, x1, y1, x2, y2, text, color=None):
    """Annotate the performance gap between two points.

    Draws a double-headed arrow between the points with a label.

    Args:
        ax: matplotlib Axes
        x1, y1: First point coordinates
        x2, y2: Second point coordinates
        text: Gap label (e.g., '+4.2%', '3.2x faster')
        color: Arrow color (default: ours color)
    """
    if color is None:
        from afp.style import COLOR_OURS
        color = COLOR_OURS
    mid_y = (y1 + y2) / 2
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='<->', color=color, lw=1.2))
    ax.text((x1 + x2) / 2 + 0.1, mid_y, text,
            fontsize=7, fontweight='bold', color=color, va='center')


def significance_bracket(ax, x1, x2, y, text='*', h=0.02):
    """Draw a statistical significance bracket between two bars.

    A marker alone hides the size of the difference; prefer plotting the difference with its interval
    (patterns/02_main_comparison.md). If you use this, the caption must name the test, n, and the
    multiple-comparison correction.

    Args:
        ax: matplotlib Axes
        x1, x2: X-coordinates of the two bars
        y: Y-coordinate for the bracket
        text: Significance marker ('*', '**', '***', 'n.s.')
        h: Bracket height as fraction of y-range
    """
    y_range = ax.get_ylim()[1] - ax.get_ylim()[0]
    bar_h = y_range * h
    ax.plot([x1, x1, x2, x2], [y, y + bar_h, y + bar_h, y], 'k-', lw=1)
    ax.text((x1 + x2) / 2, y + bar_h, text,
            ha='center', va='bottom', fontsize=10)


def add_shaded_region(ax, ymin, ymax, label=None, color=None, alpha=0.08):
    """Add a shaded horizontal band (e.g., baseline performance range).

    Inspired by ViT Fig. 3's BiT performance band.

    Args:
        ax: matplotlib Axes
        ymin, ymax: Band boundaries
        label: Optional text label
        color: Fill color (default: highlight color)
        alpha: Fill transparency
    """
    if color is None:
        from afp.style import COLOR_HIGHLIGHT
        color = COLOR_HIGHLIGHT
    ax.axhspan(ymin, ymax, alpha=alpha, color=color, zorder=0)
    if label:
        ax.text(ax.get_xlim()[1], (ymin + ymax) / 2, f' {label}',
                fontsize=6, va='center', color=color, alpha=0.8)


def add_inset_zoom(ax, xlim, ylim, loc='upper left', width="40%",
                   height="35%", borderpad=1.5):
    """Add an inset zoom panel to magnify a region of interest.

    Args:
        ax: Parent matplotlib Axes
        xlim: (xmin, xmax) for the zoomed region
        ylim: (ymin, ymax) for the zoomed region
        loc: Inset location ('upper left', 'lower right', etc.)
        width, height: Inset size as percentage strings
        borderpad: Padding between inset and parent axes

    Returns:
        Inset Axes object (plot your data on this too)
    """
    from mpl_toolkits.axes_grid1.inset_locator import inset_axes, mark_inset
    axins = inset_axes(ax, width=width, height=height, loc=loc,
                       borderpad=borderpad)
    axins.set_xlim(*xlim)
    axins.set_ylim(*ylim)
    axins.tick_params(labelsize=5)
    mark_inset(ax, axins, loc1=2, loc2=4, fc="none", ec="0.5", lw=0.5)
    return axins


def sorted_bar_data(methods, values, stds=None, ascending=True):
    """Sort bar chart data by values (sorting = narrative).

    Top-venue papers always sort bars by performance, not alphabetically.
    This creates a natural visual arc from worst to best.

    Args:
        methods: List of method names
        values: List/array of values
        stds: Optional list/array of standard deviations
        ascending: If True, sort from lowest to highest (recommended:
                   your method appears last/rightmost as the best)

    Returns:
        (sorted_methods, sorted_values, sorted_stds) tuple
    """
    idx = np.argsort(values) if ascending else np.argsort(values)[::-1]
    sorted_methods = [methods[i] for i in idx]
    sorted_values = np.array(values)[idx]
    sorted_stds = np.array(stds)[idx] if stds is not None else None
    return sorted_methods, sorted_values, sorted_stds
