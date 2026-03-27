# Technique 07: Bump Chart (Ranking Change Plot)

## When to Use
Visualize how method **rankings change** across different datasets or conditions. More intuitive than tables.

## Core Code
```python
def bump_chart(ax, categories, rankings, colors=None, lw=2.5, ms=10):
    """
    Parameters:
        categories: ['CIFAR-10', 'CIFAR-100', 'ImageNet', 'OOD-Bench']
        rankings: {'Ours': [1, 1, 2, 1],
                   'GNN': [3, 2, 1, 3],
                   'Transformer': [2, 3, 3, 2], ...}
    """
    n_cat = len(categories)
    x = range(n_cat)

    if colors is None:
        colors = plt.cm.Set2(np.linspace(0, 1, len(rankings)))

    for (name, ranks), color in zip(rankings.items(), colors):
        is_ours = 'ours' in name.lower()
        ax.plot(x, ranks, 'o-',
                lw=lw * (1.5 if is_ours else 1),
                markersize=ms * (1.3 if is_ours else 1),
                color=color, zorder=5 if is_ours else 3,
                alpha=1.0 if is_ours else 0.7)

        # Label method name at the right end
        ax.text(n_cat - 1 + 0.15, ranks[-1], name,
                va='center', fontsize=8,
                fontweight='bold' if is_ours else 'normal',
                color=color)

        # Label rank number at each point
        for xi, rank in zip(x, ranks):
            ax.text(xi, rank - 0.15, str(rank),
                    ha='center', va='top', fontsize=7, color=color)

    ax.set_xticks(x)
    ax.set_xticklabels(categories, fontsize=9)
    ax.invert_yaxis()  # Rank 1 at the top
    ax.set_ylabel('Rank', fontsize=9)
    ax.set_yticks(range(1, max(max(r) for r in rankings.values()) + 1))
    ax.grid(axis='y', alpha=0.2)
    ax.spines[['top', 'right']].set_visible(False)

    # Leave space on the right for labels
    ax.set_xlim(-0.3, n_cat - 1 + 1.5)
```

## Use Cases
- Compare 5+ methods' rankings across 4+ datasets
- Show a method's consistent strengths or weaknesses across different domains
- Reveal the insight that "no single method ranks first on all datasets"
