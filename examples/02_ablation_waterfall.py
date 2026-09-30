"""
Example 02: Ablation Study — Plain Bars vs Waterfall Chart

Demonstrates how a waterfall chart tells the ablation story better
than a plain bar chart.

CLAIM: "Each component contributes positively, with attention being most critical (+5.2%)"
PATTERN: 03_ablation
STORYTELLING: S4 (causal branching) — show cumulative contribution
"""
import matplotlib.pyplot as plt
import numpy as np
import os, sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from afp import setup_style, save_fig
from afp.style import COLORS_PRIMARY, COLOR_POSITIVE, COLOR_NEGATIVE


FIG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'figures')

# ================================================================
# Data: ablation components and their contributions
# ================================================================
components = ['Base', '+ Aug.', '+ Attn.', '+ Reg.', '+ Ens.', 'Full']
values =     [78.3,    2.1,      5.2,       1.8,      1.5,       88.9]
# Base=78.3, then deltas, Full=sum


def plot_before():
    """Plain bars — hard to see cumulative effect."""
    fig, ax = plt.subplots(figsize=(5, 3))
    all_values = [78.3, 80.4, 85.6, 87.4, 88.9]
    labels = ['Base', '+Aug', '+Attn', '+Reg', 'Full']
    ax.bar(labels, all_values)
    ax.set_ylabel('Accuracy (%)')
    ax.set_title('Ablation Study')
    fig.savefig(os.path.join(FIG_DIR, '02_waterfall_before.pdf'), bbox_inches='tight')
    fig.savefig(os.path.join(FIG_DIR, '02_waterfall_before.png'), dpi=150, bbox_inches='tight')
    plt.close(fig)
    print('Saved: examples/figures/02_waterfall_before.pdf')


def plot_after():
    """Waterfall chart — shows each component's contribution clearly."""
    TEXTWIDTH, COLWIDTH = setup_style(venue='icml')

    fig, ax = plt.subplots(figsize=(COLWIDTH * 1.3, COLWIDTH * 0.9))

    # Build waterfall
    base = values[0]
    deltas = values[1:-1]
    total = values[-1]
    labels = components

    # Calculate running totals for bar positioning
    cumulative = [base]
    for d in deltas:
        cumulative.append(cumulative[-1] + d)

    # Colors: base=gray, positive delta=green, total=ours
    bar_colors = [COLOR_NEGATIVE if v < 0 else COLOR_POSITIVE for v in deltas]

    x = np.arange(len(labels))

    # Base level: a mark, not a bar -- the axis does not start at zero, so a bar
    # from the frame would misstate its value.  Only the floating steps are lengths.
    ax.plot([x[0] - 0.4, x[0] + 0.4], [base, base], color='#555555', lw=2.2,
            solid_capstyle='butt')
    ax.text(x[0], base + 0.3, f'{base:.1f}', ha='center', fontsize=7,
            fontweight='bold')

    # Delta bars (floating)
    for i, (d, c) in enumerate(zip(deltas, bar_colors)):
        bottom = cumulative[i]
        ax.bar(x[i + 1], d, bottom=bottom, color=c,
               edgecolor='white', linewidth=0.5, alpha=0.85)
        # Delta label
        ax.text(x[i + 1], bottom + d + 0.3, f'+{d:.1f}',
                ha='center', fontsize=7, fontweight='bold',
                color='#2d2d2d')
        # Connector line
        if i < len(deltas) - 1:
            ax.plot([x[i + 1] - 0.4, x[i + 2] + 0.4],
                    [cumulative[i + 1], cumulative[i + 1]],
                    color='gray', ls=':', lw=0.5, alpha=0.5)

    # Final level (same reasoning as the base)
    ax.plot([x[-1] - 0.4, x[-1] + 0.4], [total, total], color=COLORS_PRIMARY['ours'],
            lw=2.2, solid_capstyle='butt')
    ax.text(x[-1], total + 0.3, f'{total:.1f}', ha='center', fontsize=7,
            fontweight='bold', color=COLORS_PRIMARY['ours'])

    # Connector from last delta to total
    ax.plot([x[-2] - 0.4, x[-1] + 0.4],
            [cumulative[-1], cumulative[-1]],
            color='gray', ls=':', lw=0.5, alpha=0.5)

    # Reference line: base performance
    ax.axhline(y=base, ls='--', color='gray', alpha=0.3, lw=0.8)
    ax.text(-0.45, base - 0.8, 'Base', fontsize=6, color='gray')

    # Highlight largest contributor
    max_idx = np.argmax(deltas)
    ax.annotate('largest step',
                xy=(x[max_idx + 1] + 0.4, cumulative[max_idx] + deltas[max_idx] / 2),
                xytext=(x[max_idx + 1] + 0.9, cumulative[max_idx] + deltas[max_idx] / 2 - 1.5),
                fontsize=6, color=COLORS_PRIMARY['ours'], va='center',
                arrowprops=dict(arrowstyle='->', color=COLORS_PRIMARY['ours'],
                                lw=0.8))

    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=7, rotation=15, ha='right')
    ax.set_ylabel(r'Accuracy (\%)' if plt.rcParams['text.usetex'] else 'Accuracy (%)')
    ax.set_ylim(76, 92)

    save_fig(fig, '02_waterfall_after', fig_dir=FIG_DIR, formats=['pdf', 'png'])


if __name__ == '__main__':
    os.makedirs(FIG_DIR, exist_ok=True)
    print("=== BEFORE (plain bars) ===")
    plot_before()
    print("\n=== AFTER (waterfall chart) ===")
    plot_after()
