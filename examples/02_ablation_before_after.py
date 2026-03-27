"""
Example 02: Ablation Study — Before vs After

Before: Plain bar chart of final values
After: Waterfall + contribution heatmap showing component interactions

CLAIM: "Attention contributes +5.2% (largest); all components are complementary"
PATTERN: 03_ablation
STORYTELLING: S4 (causal branching) + progressive build-up
"""
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
import os, sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from afp import setup_style, save_fig
from afp.style import COLORS_PRIMARY, COLOR_POSITIVE, COLOR_NEGATIVE

# ================================================================
# Data
# ================================================================
components = ['Base', '+ Augment.', '+ Attention', '+ Regulariz.', '+ Ensemble', 'Full Model']
deltas =     [78.3,    2.1,          5.2,           1.8,            1.5,          0]  # last = total placeholder
cumulative = [78.3, 80.4, 85.6, 87.4, 88.9, 88.9]

# Interaction matrix: does combining X+Y give more/less than X+Y individually?
comp_short = ['Aug', 'Attn', 'Reg', 'Ens']
interaction = np.array([
    [ 2.1,  1.3,  0.5,  0.2],  # Aug
    [ 1.3,  5.2,  0.8,  0.4],  # Attn
    [ 0.5,  0.8,  1.8,  0.3],  # Reg
    [ 0.2,  0.4,  0.3,  1.5],  # Ens
])


def plot_before():
    """Plain bars — can't see contributions."""
    fig, ax = plt.subplots(figsize=(5, 3))
    configs = ['Base', 'Base+Aug', '+Attn', '+Reg', 'Full']
    vals = [78.3, 80.4, 85.6, 87.4, 88.9]
    ax.bar(configs, vals)
    ax.set_ylabel('Accuracy (%)')
    ax.set_title('Ablation Study')
    fig.savefig('figures/02_before.png', dpi=200, bbox_inches='tight')
    plt.close(fig)
    print('Saved: figures/02_before.png')


def plot_after():
    """Waterfall + interaction heatmap."""
    TEXTWIDTH, _ = setup_style(venue='icml')

    fig = plt.figure(figsize=(TEXTWIDTH, TEXTWIDTH * 0.35))
    gs = gridspec.GridSpec(1, 2, width_ratios=[3, 2], wspace=0.3)

    # ──────── Panel (a): Waterfall ────────
    ax1 = fig.add_subplot(gs[0])
    x = np.arange(len(components))

    for i in range(len(components)):
        if i == 0:
            # Base bar
            ax1.bar(x[i], cumulative[i], color='#777777',
                    edgecolor='white', linewidth=0.5)
            ax1.text(x[i], cumulative[i] + 0.4, f'{cumulative[i]:.1f}',
                     ha='center', fontsize=6.5, fontweight='bold')
        elif i == len(components) - 1:
            # Full model bar (from 0)
            ax1.bar(x[i], cumulative[i], color=COLORS_PRIMARY['ours'],
                    edgecolor='white', linewidth=0.5)
            ax1.text(x[i], cumulative[i] + 0.4, f'{cumulative[i]:.1f}',
                     ha='center', fontsize=6.5, fontweight='bold',
                     color=COLORS_PRIMARY['ours'])
        else:
            # Delta bar (floating)
            d = deltas[i]
            bottom = cumulative[i - 1]
            color = COLOR_POSITIVE if d > 0 else COLOR_NEGATIVE
            # Color intensity by contribution size
            alpha = 0.5 + 0.5 * (abs(d) / max(deltas[1:-1]))
            ax1.bar(x[i], d, bottom=bottom, color=color,
                    edgecolor='white', linewidth=0.5, alpha=alpha)
            ax1.text(x[i], bottom + d + 0.4, f'+{d:.1f}',
                     ha='center', fontsize=6.5, fontweight='bold',
                     color='#2d2d2d')

            # Connector line
            if i < len(components) - 2:
                ax1.plot([x[i] - 0.35, x[i + 1] + 0.35],
                         [cumulative[i], cumulative[i]],
                         color='gray', ls=':', lw=0.4, alpha=0.4)

    # Connector: last delta to total
    ax1.plot([x[-2] - 0.35, x[-1] + 0.35],
             [cumulative[-2], cumulative[-2]],
             color='gray', ls=':', lw=0.4, alpha=0.4)

    # Reference: base performance
    ax1.axhline(y=cumulative[0], ls='--', color='gray', alpha=0.25, lw=0.6)

    # Highlight largest contributor
    max_d_idx = np.argmax(deltas[1:-1]) + 1
    ax1.annotate('Largest\ncontributor',
                 xy=(x[max_d_idx], cumulative[max_d_idx]),
                 xytext=(x[max_d_idx] + 1, cumulative[max_d_idx] + 3),
                 fontsize=5.5, color=COLORS_PRIMARY['ours'],
                 arrowprops=dict(arrowstyle='->', color=COLORS_PRIMARY['ours'],
                                 lw=0.7, connectionstyle='arc3,rad=0.15'))

    # Total improvement bracket
    ax1.annotate('', xy=(x[-1] + 0.45, cumulative[-1]),
                 xytext=(x[-1] + 0.45, cumulative[0]),
                 arrowprops=dict(arrowstyle='<->', color='#333', lw=0.8))
    ax1.text(x[-1] + 0.55, (cumulative[0] + cumulative[-1]) / 2,
             f'+{cumulative[-1] - cumulative[0]:.1f}%',
             fontsize=6, fontweight='bold', va='center', color='#333')

    ax1.set_xticks(x)
    ax1.set_xticklabels(components, fontsize=5.5, rotation=20, ha='right')
    ax1.set_ylabel('Accuracy (%)', fontsize=7)
    ax1.set_ylim(72, 95)
    ax1.text(-0.1, 1.05, '(a)', transform=ax1.transAxes,
             fontweight='bold', fontsize=9)

    # ──────── Panel (b): Interaction heatmap ────────
    ax2 = fig.add_subplot(gs[1])

    im = ax2.imshow(interaction, cmap='YlOrRd', aspect='auto', vmin=0, vmax=6)

    # Annotate cells
    for i in range(len(comp_short)):
        for j in range(len(comp_short)):
            val = interaction[i, j]
            color = 'white' if val > 3.5 else 'black'
            weight = 'bold' if i == j else 'normal'
            ax2.text(j, i, f'{val:.1f}', ha='center', va='center',
                     fontsize=7, color=color, fontweight=weight)

    ax2.set_xticks(range(len(comp_short)))
    ax2.set_yticks(range(len(comp_short)))
    ax2.set_xticklabels(comp_short, fontsize=6.5)
    ax2.set_yticklabels(comp_short, fontsize=6.5)

    cbar = fig.colorbar(im, ax=ax2, shrink=0.8, pad=0.02)
    cbar.ax.tick_params(labelsize=5.5)
    cbar.set_label('Contribution (%)', fontsize=6)

    ax2.set_title('Component Interactions', fontsize=7.5, pad=5)
    ax2.text(-0.15, 1.05, '(b)', transform=ax2.transAxes,
             fontweight='bold', fontsize=9)

    save_fig(fig, '02_after', formats=['pdf', 'png'])


if __name__ == '__main__':
    os.makedirs('figures', exist_ok=True)
    print("=== BEFORE ===")
    plot_before()
    print("\n=== AFTER ===")
    plot_after()
