# Pattern 08: Pareto / Trade-off Figure

## Purpose
Show how your method balances multiple competing objectives.

## Claim Types
- "Our method achieves a better accuracy-efficiency trade-off"
- "We push the Pareto frontier in quality vs. speed"

## Top-Venue Standard Structures

### Core Structure
```
y = performance metric (accuracy / F1 / fidelity)
x = cost metric (FLOPs / latency / #params / depth)  [typically log scale]

- Each point = one configuration of one method
- Your method: ★ large marker + vivid color
- Baselines: ● small markers + gray / muted colors
- Pareto frontier: dashed line connecting optimal points
- "Dominated region": shaded area below the frontier
- Label each point with its configuration name ("Small", "Base", "Large")
```

### Full Code Pattern
```python
fig, ax = plt.subplots(figsize=(COLWIDTH, COLWIDTH*0.75))

# Baselines
for method, configs in baselines.items():
    costs, perfs = zip(*configs)
    ax.scatter(costs, perfs, s=40, alpha=0.6, label=method,
               marker='o', edgecolors='white', linewidth=0.5)

# Ours - larger markers
our_costs, our_perfs = zip(*our_configs)
ax.scatter(our_costs, our_perfs, s=120, marker='★',
           color='tab:red', zorder=5, label='Ours',
           edgecolors='darkred', linewidth=0.5)

# Pareto frontier (ours)
pidx = pareto_frontier(np.array(our_costs), np.array(our_perfs))
sorted_pareto = sorted(zip(np.array(our_costs)[pidx],
                           np.array(our_perfs)[pidx]))
px, py = zip(*sorted_pareto)
ax.plot(px, py, '--', color='tab:red', alpha=0.5, zorder=4)
ax.fill_between(px, py, ax.get_ylim()[0],
                alpha=0.03, color='tab:red')

# Label configurations
for name, cost, perf in zip(config_names, our_costs, our_perfs):
    ax.annotate(name, (cost, perf),
                textcoords="offset points", xytext=(8, 4),
                fontsize=7, color='tab:red')

# "Improvement arrow" (optional but powerful)
ax.annotate('', xy=(our_best_cost, our_best_perf),
            xytext=(baseline_best_cost, baseline_best_perf),
            arrowprops=dict(arrowstyle='->', color='green', lw=2))
ax.text((our_best_cost + baseline_best_cost)/2,
        (our_best_perf + baseline_best_perf)/2 + offset,
        f'{improvement:.1f}% better\n{speedup:.1f}× faster',
        fontsize=8, ha='center', color='green',
        bbox=dict(boxstyle='round', fc='lightyellow', alpha=0.8))

ax.set_xscale('log')
ax.set_xlabel('Computational Cost (FLOPs)')
ax.set_ylabel('Accuracy (%)')
ax.legend(loc='lower right', fontsize=8)
```

### Multi-Objective Variants

**Three-objective Pareto** (using bubble chart):
```python
# x = cost, y = accuracy, size = memory
ax.scatter(costs, accs, s=memory_normalized * 300,
           alpha=0.6, edgecolors='black', linewidth=0.5)
# Add size legend
for s, label in [(50, '100MB'), (150, '500MB'), (300, '1GB')]:
    ax.scatter([], [], s=s, c='gray', alpha=0.6, edgecolors='black',
               linewidth=0.5, label=label)
ax.legend(title='Memory', loc='upper left')
```

**Dual-panel layout**:
```
┌──────────────────┬──────────────────┐
│ (a) Acc vs FLOPs  │ (b) Acc vs Latency│
│ Theoretical cost   │ Wall-clock time   │
│ comparison         │ comparison        │
└──────────────────┴──────────────────┘
If the two panels tell different stories (theoretically efficient but
not faster in practice), explain the discrepancy in the text.
```

## Required Elements

1. **Pareto frontier line**: Not just a scatter plot -- connect the frontier points
2. **Configuration labels**: Annotate what each point represents
3. **Dominated region shading**: Make the Pareto concept immediately clear
4. **Multiple baseline series**: Each baseline should also have multiple configuration points
5. **Log scale**: Use when costs span orders of magnitude
6. **Improvement annotations**: Quantify gains with arrows or text labels

## Anti-Patterns

- Do not plot only a few isolated points without a frontier line
- Do not show your method with only a single configuration point (cannot demonstrate trade-off)
- Do not omit labels for what each configuration represents
- Do not conflate theoretical FLOPs with actual latency
- Do not use linear axes for data spanning orders of magnitude
