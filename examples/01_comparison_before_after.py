"""
Example 01: Method Comparison — Before vs After

Before: Plain bar chart (undergraduate level)
After: Dot plots per dataset (mean ± sd over seeds) + the per-metric gap to the best baseline

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
std_B = {
    'MLP':         [1.4, 1.6, 1.5, 1.5, 1.0],
    'GNN':         [1.0, 1.2, 1.1, 1.2, 0.8],
    'Transformer': [1.1, 1.2, 1.1, 1.3, 0.9],
    'Ours':        [0.6, 0.7, 0.6, 0.5, 0.4],
}
N_SEEDS = 5  # the std values above are over 5 seeds

FIG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'figures')


def plot_before():
    """Undergraduate level: single plain bar chart."""
    fig, ax = plt.subplots(figsize=(5, 3))
    x = np.arange(len(methods))
    ax.bar(x, [data_A[m][0] for m in methods])
    ax.set_xticks(x)
    ax.set_xticklabels(methods)
    ax.set_ylabel('Accuracy (%)')
    ax.set_title('Comparison Results')
    fig.savefig(os.path.join(FIG_DIR, '01_before.png'), dpi=200, bbox_inches='tight')
    plt.close(fig)
    print('Saved: examples/figures/01_before.png')


def plot_after():
    """Two dot-plot panels (one per dataset) + the per-metric gap to the best baseline.

    Dots, not bars: every value lies between 76 and 95, and a bar's length only reads
    correctly when the axis starts at zero.  Position encodings (dots, intervals) may use a
    zoomed axis, so the differences stay visible without exaggerating them.  Panel (c)
    shows the quantity the claim is actually about -- the gap -- against a zero line.
    """
    TEXTWIDTH, _ = setup_style(venue='icml')
    pct = r'\%' if plt.rcParams['text.usetex'] else '%'
    colors = get_method_colors(methods)

    fig = plt.figure(figsize=(TEXTWIDTH, TEXTWIDTH * 0.40))
    gs = gridspec.GridSpec(1, 3, width_ratios=[2.2, 2.2, 1.6], figure=fig)

    x = np.arange(len(metrics))
    offsets = (np.arange(len(methods)) - (len(methods) - 1) / 2) * 0.16
    axes = []
    for k, (name, data, std) in enumerate([('dataset A', data_A, std_A),
                                           ('dataset B', data_B, std_B)]):
        ax = fig.add_subplot(gs[k], sharey=axes[0] if axes else None)
        for i, m in enumerate(methods):
            ours = m == 'Ours'
            ax.errorbar(x + offsets[i], data[m], yerr=std[m], fmt='o',
                        ms=3.2 if ours else 2.4, color=colors[m],
                        elinewidth=0.7, capsize=0, zorder=4 if ours else 3,
                        label=m if k == 0 else None)
        ax.set_xticks(x)
        ax.set_xticklabels(metrics)
        ax.set_xlim(-0.5, len(metrics) - 0.5)
        ax.tick_params(axis='x', which='minor', bottom=False, top=False)
        ax.text(0.03, 0.97, name, transform=ax.transAxes, va='top', fontsize=7, color='#555555')
        if k == 0:
            ax.set_ylabel(f'score ({pct}), mean $\\pm$ sd over {N_SEEDS} seeds'
                          if plt.rcParams['text.usetex'] else
                          f'score ({pct}), mean ± sd over {N_SEEDS} seeds')
        else:
            plt.setp(ax.get_yticklabels(), visible=False)
        axes.append(ax)
    axes[0].set_ylim(74, 96)
    axes[0].yaxis.set_major_locator(plt.MultipleLocator(5))
    axes[0].legend(loc='lower right', ncol=2, fontsize=6, handletextpad=0.2,
                   columnspacing=0.6, borderaxespad=0.2)

    # (c) the claim is about the gap, so draw the gap
    ax3 = fig.add_subplot(gs[2])
    baselines = [m for m in methods if m != 'Ours']
    for k, (data, std, mk, name) in enumerate([(data_A, std_A, 'o', 'A'),
                                               (data_B, std_B, 's', 'B')]):
        best = np.max([data[m] for m in baselines], axis=0)
        best_sd = np.array([std[max(baselines, key=lambda m: data[m][j])][j]
                            for j in range(len(metrics))])
        gap = np.array(data['Ours']) - best
        sd = np.sqrt(np.array(std['Ours']) ** 2 + best_sd ** 2)
        ax3.errorbar(gap, np.arange(len(metrics)) + (k - 0.5) * 0.25, xerr=sd, fmt=mk,
                     ms=2.8, color=COLORS_PRIMARY['ours'], mfc='white' if k else None,
                     elinewidth=0.7, capsize=0, label=f'dataset {name}')
    ax3.axvline(0, color='#333333', lw=0.6)
    ax3.set_yticks(np.arange(len(metrics)))
    ax3.set_yticklabels(metrics)
    ax3.tick_params(axis='y', which='minor', left=False, right=False)
    ax3.invert_yaxis()
    ax3.set_xlim(-3.5, 8.5)
    ax3.xaxis.set_major_locator(plt.MultipleLocator(2))
    ax3.set_xlabel('Ours $-$ best baseline (pp)' if plt.rcParams['text.usetex']
                   else 'Ours − best baseline (pp)')
    ax3.legend(loc='lower left', fontsize=6, handletextpad=0.2, borderaxespad=0.2,
               frameon=True, framealpha=1, edgecolor='none')

    for ax, lab in zip(axes + [ax3], 'abc'):
        ax.text(-0.02, 1.02, f'({lab})', transform=ax.transAxes, ha='right',
                va='bottom', fontweight='bold', fontsize=9)

    save_fig(fig, '01_after', fig_dir=FIG_DIR, formats=['pdf', 'png'])


if __name__ == '__main__':
    os.makedirs(FIG_DIR, exist_ok=True)
    print("=== BEFORE (default single bar chart) ===")
    plot_before()
    print("\n=== AFTER (rules applied) ===")
    plot_after()
