"""
Example 01: Method Comparison — Before vs After

Demonstrates the difference between an undergraduate-level bar chart
and a publication-ready comparison figure.

CLAIM: "Our method significantly outperforms all baselines across two metrics"
PATTERN: 02_main_comparison
STORYTELLING: S8 (sorting as narrative) + S6 (shaded reference region)
"""
import matplotlib.pyplot as plt
import numpy as np
import os, sys

# Add parent directory to path for local development
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from afp import setup_style, get_method_colors, save_fig, add_reference_line
from afp.style import COLORS_PRIMARY

# ================================================================
# Data (sorted by performance — sorting IS narrative)
# ================================================================
methods = ['MLP', 'GNN', 'Transformer', 'Ours']
acc = np.array([83.4, 85.2, 87.1, 91.3])
acc_std = np.array([1.2, 0.8, 0.9, 0.5])
f1 = np.array([81.1, 83.7, 85.9, 90.8])
f1_std = np.array([1.5, 1.0, 1.1, 0.6])


def plot_before():
    """Undergraduate-level: bare minimum, no story."""
    fig, ax = plt.subplots(figsize=(5, 3))
    ax.bar(methods, acc)
    ax.set_ylabel('Accuracy (%)')
    ax.set_title('Comparison Results')
    fig.savefig('figures/01_before.pdf', bbox_inches='tight')
    fig.savefig('figures/01_before.png', dpi=150, bbox_inches='tight')
    plt.close(fig)
    print('Saved: figures/01_before.pdf')


def plot_after():
    """Publication-ready: rich, self-explanatory, visually compelling."""
    TEXTWIDTH, COLWIDTH = setup_style(venue='icml')
    colors = get_method_colors(methods)
    c = [colors[m] for m in methods]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(TEXTWIDTH, TEXTWIDTH * 0.35))
    x = np.arange(len(methods))

    # --- Panel (a): Accuracy ---
    bars1 = ax1.bar(x, acc, yerr=acc_std, capsize=3, color=c,
                    edgecolor='white', linewidth=0.5,
                    error_kw={'lw': 0.8, 'capthick': 0.8})

    # Reference line: random chance
    ax1.axhline(y=50, ls=':', color='gray', alpha=0.5, lw=0.8)
    ax1.text(len(methods) - 0.5, 50.8, 'Random', fontsize=6, color='gray')

    # Value labels on bars
    for i, (v, s) in enumerate(zip(acc, acc_std)):
        is_best = (i == len(methods) - 1)
        ax1.text(i, v + s + 0.8, f'{v:.1f}', ha='center', fontsize=7,
                 fontweight='bold' if is_best else 'normal',
                 color=COLORS_PRIMARY['ours'] if is_best else '#333333')

    # Highlight the gap
    ax1.annotate(f'+{acc[-1] - acc[-2]:.1f}%',
                 xy=(3, acc[-1]), xytext=(2.2, acc[-1] + 3.5),
                 fontsize=7, fontweight='bold', color=COLORS_PRIMARY['ours'],
                 arrowprops=dict(arrowstyle='->', color=COLORS_PRIMARY['ours'],
                                 lw=1))

    # Shaded band for our method's confidence region
    ax1.axhspan(acc[-1] - acc_std[-1], acc[-1] + acc_std[-1],
                alpha=0.06, color=COLORS_PRIMARY['ours'])

    ax1.set_xticks(x)
    ax1.set_xticklabels(methods, fontsize=7)
    ax1.set_ylabel('Accuracy (%)')
    ax1.set_ylim(45, 100)
    ax1.text(-0.15, 1.05, '(a)', transform=ax1.transAxes,
             fontweight='bold', fontsize=10)

    # --- Panel (b): F1 Score ---
    bars2 = ax2.bar(x, f1, yerr=f1_std, capsize=3, color=c,
                    edgecolor='white', linewidth=0.5,
                    error_kw={'lw': 0.8, 'capthick': 0.8})
    ax2.axhline(y=50, ls=':', color='gray', alpha=0.5, lw=0.8)

    for i, (v, s) in enumerate(zip(f1, f1_std)):
        is_best = (i == len(methods) - 1)
        ax2.text(i, v + s + 0.8, f'{v:.1f}', ha='center', fontsize=7,
                 fontweight='bold' if is_best else 'normal',
                 color=COLORS_PRIMARY['ours'] if is_best else '#333333')

    ax2.set_xticks(x)
    ax2.set_xticklabels(methods, fontsize=7)
    ax2.set_ylabel('F1 Score (%)')
    ax2.set_ylim(45, 100)
    ax2.text(-0.15, 1.05, '(b)', transform=ax2.transAxes,
             fontweight='bold', fontsize=10)

    save_fig(fig, '01_after', formats=['pdf', 'png'])


if __name__ == '__main__':
    os.makedirs('figures', exist_ok=True)
    print("=== BEFORE (undergraduate level) ===")
    plot_before()
    print("\n=== AFTER (publication ready) ===")
    plot_after()
    print("\nCompare figures/01_before.png vs figures/01_after.png")
