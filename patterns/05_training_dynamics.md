# Pattern 05: Training Dynamics Figure

## Purpose
Visualize behavior during training to demonstrate convergence, stability, or training efficiency of the method.

## Claim Type
- "Our method converges faster / more stably"
- "Training exhibits distinct phases"
- "Our regularization prevents overfitting"

## Top-Venue Standard: Never Just a Single Loss Curve

### Structure A: Multi-Panel Training Overview
```
+------------------------+--------------------+
| (a) Train/Val Loss     | (b) Val Metric     |
| Two lines + gap annot. | Key metric over    |
| Phase transitions      | time + baseline    |
| marked                 | comparison         |
+------------------------+--------------------+
| (c) Learning rate / Gradient norm / Effective rank    |
| Internal training state -- proves training is healthy |
+-------------------------------------------------------+
```

### Structure B: Comparative Training Curves (Most Common)
```
- Multiple methods on the same plot
- x = training steps / epochs / wall time
- y = validation metric
- One line per method + shaded confidence interval
- Inset zoom on the critical region (e.g., near convergence)
- Annotate: steps your method needs to reach a threshold vs. baseline
```

### Structure C: Train-Generalization Gap Analysis
```
On the same plot:
1. Train loss (solid line)
2. Val loss (dashed line)
3. Gap = Train - Val (filled region, color indicating overfitting severity)

Annotate "overfitting begins" where the gap starts increasing
Annotate "regularization effect" where your method keeps the gap small
```

## Required Elements

1. **Multiple curves for comparison**: At least your method + 1 strong baseline
2. **Shaded confidence band**: Standard deviation across multiple runs
3. **Phase annotations**: Vertical dashed lines + text labels marking training phases
   ```python
   ax.axvline(x=phase_boundary, ls='--', color='gray', alpha=0.5)
   ax.text(phase_boundary, y_top, 'Phase 2:\nFine-tuning',
           fontsize=8, ha='center')
   ```
4. **Reference lines**: Convergence target / final performance / baseline final value
5. **Inset zoom**: Magnify the convergence region to reveal the final gap
6. **Meaningful x-axis**: If methods have different per-step costs, use wall time instead of epochs

## Advanced Techniques

### Annotating Convergence Speed
```python
# Find the first step that reaches the threshold
threshold = 0.90
step_ours = np.argmax(acc_ours >= threshold)
step_base = np.argmax(acc_base >= threshold)

ax.axhline(y=threshold, ls=':', color='gray', alpha=0.5)
ax.annotate(f'Ours: {step_ours} steps',
            xy=(step_ours, threshold), xytext=(step_ours+100, threshold-0.05),
            arrowprops=dict(arrowstyle='->', color='tab:red'),
            fontsize=8, color='tab:red')
ax.annotate(f'Baseline: {step_base} steps',
            xy=(step_base, threshold), xytext=(step_base+100, threshold+0.03),
            arrowprops=dict(arrowstyle='->', color='tab:blue'),
            fontsize=8, color='tab:blue')

speedup = step_base / step_ours
ax.text(0.95, 0.05, f'{speedup:.1f}x faster',
        transform=ax.transAxes, fontsize=11, fontweight='bold',
        ha='right', va='bottom',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))
```

### Train/Val Gap Visualization
```python
ax.plot(steps, train_loss, '-', label='Train', alpha=0.8)
ax.plot(steps, val_loss, '--', label='Val', alpha=0.8)
ax.fill_between(steps, train_loss, val_loss,
                alpha=0.15, color='red', label='Generalization gap')
```

## Common Pitfalls

- Do not plot a single bare loss curve with no comparison
- Do not omit confidence bands / multiple runs
- Do not use epochs on the x-axis when methods have vastly different per-epoch costs (misleading)
- Do not leave the plot without any annotations, forcing reviewers to interpret on their own
- Do not show only training loss without validation loss (generalization cannot be assessed)
