"""
Example 03: Scaling Analysis — Linear vs Log-Log

Demonstrates how axis scale choice is itself an argument.
Log-log reveals power-law relationships invisible on linear axes.

CLAIM: "Our method scales as O(n^1.2) while baselines scale as O(n^2)"
PATTERN: 04_scaling
STORYTELLING: S7 (axis choice as argument) + S2 (dual panel: two sequence lengths)
"""
import matplotlib.pyplot as plt
import numpy as np
import os, sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from afp import setup_style, get_method_colors, save_fig, add_vref_line
from afp.style import COLORS_PRIMARY

# ================================================================
# Synthetic scaling data
# ================================================================
n = np.array([100, 200, 500, 1000, 2000, 5000, 10000])

# Ours: O(n^1.2)
ours_time = 0.001 * n ** 1.2

# Baselines with different scaling
transformer_time = 0.0005 * n ** 2.0
gnn_time = 0.002 * n ** 1.5
mlp_time = 0.0001 * n ** 1.8

methods = ['MLP', 'GNN', 'Transformer', 'Ours']
all_data = {
    'MLP': mlp_time,
    'GNN': gnn_time,
    'Transformer': transformer_time,
    'Ours': ours_time,
}


def plot_before():
    """Linear scale — differences crushed at large n."""
    fig, ax = plt.subplots(figsize=(5, 3))
    for name, data in all_data.items():
        ax.plot(n, data, '-o', label=name, markersize=4)
    ax.set_xlabel('Problem Size (n)')
    ax.set_ylabel('Runtime (s)')
    ax.set_title('Runtime Scaling')
    ax.legend()
    fig.savefig('figures/03_before.pdf', bbox_inches='tight')
    fig.savefig('figures/03_before.png', dpi=150, bbox_inches='tight')
    plt.close(fig)
    print('Saved: figures/03_before.pdf')


def plot_after():
    """Log-log with fit lines, crossover annotation, and dual panel."""
    TEXTWIDTH, COLWIDTH = setup_style(venue='icml')
    colors = get_method_colors(methods)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(TEXTWIDTH, TEXTWIDTH * 0.35))

    # --- Panel (a): Log-log scaling ---
    for name, data in all_data.items():
        marker = 'o' if name != 'Ours' else 's'
        lw = 1.8 if name == 'Ours' else 1.0
        zorder = 10 if name == 'Ours' else 5
        ax1.loglog(n, data, '-' + marker[0], label=name, color=colors[name],
                   markersize=4 if name != 'Ours' else 5,
                   linewidth=lw, zorder=zorder, alpha=0.9)

    # Fit lines with slope annotations
    slopes = {'Ours': 1.2, 'Transformer': 2.0, 'GNN': 1.5, 'MLP': 1.8}
    for name, slope in slopes.items():
        if name in ['Ours', 'Transformer']:
            ax1.text(n[-1] * 1.3, all_data[name][-1],
                     f'$O(n^{{{slope}}})$',
                     fontsize=6, color=colors[name], va='center')

    # Crossover point annotation
    # Find where Ours becomes faster than Transformer
    cross_idx = np.argmin(np.abs(ours_time - transformer_time))
    cross_n = n[cross_idx]
    ax1.axvline(x=cross_n, ls='--', color='gray', alpha=0.4, lw=0.8)
    ax1.text(cross_n * 0.6, ax1.get_ylim()[0] * 3,
             f'Crossover\nn={cross_n}', fontsize=6, color='gray',
             ha='center')

    ax1.set_xlabel('Problem Size $n$')
    ax1.set_ylabel('Runtime (s)')
    ax1.legend(fontsize=6, loc='upper left')
    ax1.text(-0.15, 1.05, '(a)', transform=ax1.transAxes,
             fontweight='bold', fontsize=10)

    # --- Panel (b): Speedup ratio ---
    for name in ['Transformer', 'GNN', 'MLP']:
        speedup = all_data[name] / ours_time
        ax2.semilogx(n, speedup, '-o', label=f'vs {name}',
                     color=colors[name], markersize=3, linewidth=1.0)

    ax2.axhline(y=1.0, ls=':', color='gray', alpha=0.5, lw=0.8)
    ax2.text(n[0] * 0.8, 1.05, 'Equal', fontsize=6, color='gray')

    # Shade the "our method is faster" region
    ax2.axhspan(1.0, ax2.get_ylim()[1] if ax2.get_ylim()[1] > 10 else 60,
                alpha=0.05, color=COLORS_PRIMARY['ours'])
    ax2.text(n[-1] * 0.5, 2, 'Ours faster', fontsize=6,
             color=COLORS_PRIMARY['ours'], alpha=0.7, ha='center')

    ax2.set_xlabel('Problem Size $n$')
    ax2.set_ylabel('Speedup over Ours')
    ax2.legend(fontsize=6, loc='upper left')
    ax2.text(-0.15, 1.05, '(b)', transform=ax2.transAxes,
             fontweight='bold', fontsize=10)

    save_fig(fig, '03_after', formats=['pdf', 'png'])


if __name__ == '__main__':
    os.makedirs('figures', exist_ok=True)
    print("=== BEFORE (linear scale) ===")
    plot_before()
    print("\n=== AFTER (log-log with annotations) ===")
    plot_after()
