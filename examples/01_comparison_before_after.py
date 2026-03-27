"""
Example 01: Method Comparison — Before vs After

Before: Plain bar chart (undergraduate level)
After: Multi-panel composition with grouped bars, radar overlay, and ranking strip

CLAIM: "Our method outperforms all baselines across 5 metrics on 2 datasets"
PATTERN: 02_main_comparison
STORYTELLING: S8 (sorting), S2 (dual dataset), S5 (progressive density)
"""
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
import os, sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from afp import setup_style, get_method_colors, save_fig
from afp.style import COLORS_PRIMARY, COLOR_HIGHLIGHT

# ================================================================
# Data: 4 methods × 5 metrics × 2 datasets
# ================================================================
methods = ['MLP', 'GNN', 'Transformer', 'Ours']
metrics = ['Acc', 'F1', 'Prec', 'Rec', 'AUC']

# Dataset A
data_A = {
    'MLP':         [83.4, 81.1, 80.5, 81.8, 87.2],
    'GNN':         [85.2, 83.7, 84.1, 83.2, 89.1],
    'Transformer': [87.1, 85.9, 86.3, 85.5, 90.8],
    'Ours':        [91.3, 90.8, 90.1, 91.5, 94.2],
}
std_A = {
    'MLP':         [1.2, 1.5, 1.3, 1.4, 0.9],
    'GNN':         [0.8, 1.0, 0.9, 1.1, 0.7],
    'Transformer': [0.9, 1.1, 1.0, 1.2, 0.8],
    'Ours':        [0.5, 0.6, 0.5, 0.4, 0.3],
}

# Dataset B (different relative performance)
data_B = {
    'MLP':         [79.1, 77.3, 76.8, 78.0, 83.5],
    'GNN':         [82.8, 81.2, 80.5, 82.1, 86.4],
    'Transformer': [84.5, 83.1, 82.9, 83.6, 88.0],
    'Ours':        [89.7, 88.4, 87.9, 89.2, 92.8],
}


def plot_before():
    """Undergraduate level: single plain bar chart."""
    fig, ax = plt.subplots(figsize=(5, 3))
    x = np.arange(len(methods))
    ax.bar(x, [data_A[m][0] for m in methods])
    ax.set_xticks(x)
    ax.set_xticklabels(methods)
    ax.set_ylabel('Accuracy (%)')
    ax.set_title('Comparison Results')
    fig.savefig('figures/01_before.png', dpi=200, bbox_inches='tight')
    plt.close(fig)
    print('Saved: figures/01_before.png')


def plot_after():
    """Publication ready: 3-panel composition telling a complete story."""
    TEXTWIDTH, _ = setup_style(venue='icml')
    colors = get_method_colors(methods)

    fig = plt.figure(figsize=(TEXTWIDTH, TEXTWIDTH * 0.42))
    gs = gridspec.GridSpec(1, 3, width_ratios=[2.5, 2.5, 2], wspace=0.35)

    # ──────── Panel (a): Dataset A — Grouped bar with annotations ────────
    ax1 = fig.add_subplot(gs[0])
    x = np.arange(len(metrics))
    width = 0.18
    offsets = np.arange(len(methods)) - (len(methods) - 1) / 2

    for i, m in enumerate(methods):
        bars = ax1.bar(x + offsets[i] * width, data_A[m], width * 0.9,
                       yerr=std_A[m], capsize=1.5,
                       color=colors[m], edgecolor='white', linewidth=0.3,
                       error_kw={'lw': 0.5, 'capthick': 0.5},
                       label=m, alpha=0.9, zorder=3)

    # Reference: random chance
    ax1.axhline(y=50, ls=':', color='gray', alpha=0.4, lw=0.6)
    ax1.text(4.5, 50.5, 'Random', fontsize=5, color='gray')

    # Shade Ours' performance zone
    ours_min = min(data_A['Ours']) - max(std_A['Ours'])
    ours_max = max(data_A['Ours']) + max(std_A['Ours'])
    ax1.axhspan(ours_min, ours_max, alpha=0.04, color=COLORS_PRIMARY['ours'], zorder=0)

    ax1.set_xticks(x)
    ax1.set_xticklabels(metrics, fontsize=6.5)
    ax1.set_ylabel('Score (%)', fontsize=7)
    ax1.set_ylim(45, 100)
    ax1.legend(fontsize=5.5, ncol=2, loc='lower right',
               handlelength=1, columnspacing=0.5)
    ax1.set_title('Dataset A', fontsize=7.5, pad=3)
    ax1.text(-0.12, 1.05, '(a)', transform=ax1.transAxes,
             fontweight='bold', fontsize=9)

    # ──────── Panel (b): Dataset B — same layout for cross-validation ────────
    ax2 = fig.add_subplot(gs[1])

    for i, m in enumerate(methods):
        ax2.bar(x + offsets[i] * width, data_B[m], width * 0.9,
                color=colors[m], edgecolor='white', linewidth=0.3,
                alpha=0.9, zorder=3)

    ax2.axhline(y=50, ls=':', color='gray', alpha=0.4, lw=0.6)

    # Average gap annotation
    avg_gap = np.mean(data_B['Ours']) - np.mean(data_B['Transformer'])
    ax2.annotate(f'Avg. gap\n+{avg_gap:.1f}%',
                 xy=(2, data_B['Ours'][2]),
                 xytext=(3.2, 76),
                 fontsize=6, fontweight='bold',
                 color=COLORS_PRIMARY['ours'],
                 arrowprops=dict(arrowstyle='->', color=COLORS_PRIMARY['ours'],
                                 lw=0.8, connectionstyle='arc3,rad=0.2'))

    ax2.set_xticks(x)
    ax2.set_xticklabels(metrics, fontsize=6.5)
    ax2.set_ylim(45, 100)
    ax2.set_title('Dataset B', fontsize=7.5, pad=3)
    ax2.text(-0.12, 1.05, '(b)', transform=ax2.transAxes,
             fontweight='bold', fontsize=9)

    # ──────── Panel (c): Radar — multi-metric profile at a glance ────────
    ax3 = fig.add_subplot(gs[2], polar=True)

    angles = np.linspace(0, 2 * np.pi, len(metrics), endpoint=False).tolist()
    angles += angles[:1]  # close the polygon

    for m in methods:
        vals = data_A[m] + [data_A[m][0]]
        lw = 1.8 if m == 'Ours' else 0.8
        alpha = 0.95 if m == 'Ours' else 0.6
        ax3.plot(angles, vals, '-o', color=colors[m], linewidth=lw,
                 markersize=2.5 if m == 'Ours' else 1.5, alpha=alpha,
                 label=m, zorder=10 if m == 'Ours' else 5)
        if m == 'Ours':
            ax3.fill(angles, vals, color=colors[m], alpha=0.06)

    ax3.set_xticks(angles[:-1])
    ax3.set_xticklabels(metrics, fontsize=6)
    ax3.set_ylim(70, 100)
    ax3.set_yticks([75, 85, 95])
    ax3.set_yticklabels(['75', '85', '95'], fontsize=5, color='gray')
    ax3.set_title('Multi-metric Profile', fontsize=7.5, pad=12)
    ax3.text(-0.05, 1.12, '(c)', transform=ax3.transAxes,
             fontweight='bold', fontsize=9)

    # Grid styling
    ax3.spines['polar'].set_visible(False)
    ax3.grid(color='gray', alpha=0.2, lw=0.3)

    save_fig(fig, '01_after', formats=['pdf', 'png'])


if __name__ == '__main__':
    os.makedirs('figures', exist_ok=True)
    print("=== BEFORE (undergraduate level) ===")
    plot_before()
    print("\n=== AFTER (publication ready) ===")
    plot_after()
    print("\nCompare figures/01_before.png vs figures/01_after.png")
