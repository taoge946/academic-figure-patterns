# Pattern 07: Analysis / Understanding Figure

## Purpose
Help readers understand **why** your method works, not just **that** it works.

## Claim Types
- "Our method learns more discriminative representations"
- "The attention mechanism focuses on relevant regions"
- "There exists a phase transition at threshold X"

## Top-Venue Standard: Analysis Figures Must Include Comparisons

### Structure A: Embedding Visualization (t-SNE / UMAP)
```
┌──────────────┬──────────────┬──────────────┐
│ (a) Baseline  │ (b) Ours      │ (c) Ours +    │
│ t-SNE          │ t-SNE          │ augmentation  │
│ classes mixed  │ clearly        │ tighter       │
│ together       │ separated      │ clusters      │
└──────────────┴──────────────┴──────────────┘
```

**Key rules**:
- Must include baseline comparison (a single t-SNE plot proves nothing)
- Color by ground-truth class labels
- Keep perplexity / n_neighbors consistent across panels
- Add silhouette score or cluster purity as numeric annotations
- Use `ax.annotate` to label key class names

```python
# Don't just plot points -- quantify the clustering quality
from sklearn.metrics import silhouette_score
score = silhouette_score(embeddings, labels)
ax.text(0.05, 0.95, f'Silhouette: {score:.3f}',
        transform=ax.transAxes, fontsize=9,
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
```

### Structure B: Attention / Heatmap Overlay
```
┌───────────────────────────────────────────┐
│ Input          Baseline Attn    Our Attn   │
│ [original]     [heatmap overlay] [heatmap] │
│                attention         attention  │
│                scattered         focused    │
│                                ← annotate  │
└───────────────────────────────────────────┘
```

### Structure C: Hyperparameter / Threshold Sensitivity Analysis
```
┌──────────────┬──────────────┐
│ (a) Single     │ (b) Two       │
│ parameter      │ parameters    │
│ x = param val  │ heatmap       │
│ y = performance│ x,y = params  │
│ annotate       │ color = perf  │
│ optimal range  │ ★ = optimum   │
│ (shaded band)  │               │
└──────────────┴──────────────┘
```

**Key point**: Annotate the recommended value and the stable range -- do not just plot a bare curve.

### Structure D: Behavior / Mechanism Analysis (Understanding-Oriented)
```
Illustrate how the method's behavior changes under different conditions:
- Error rate vs. noise level (phase transition)
- Performance vs. sample difficulty (which samples benefit most)
- Activation distribution evolution (before / during / after training)
```

## Advanced Presentation Techniques

### Grouped Heatmap with Marginal Statistics
```python
fig, axd = plt.subplot_mosaic(
    [["heatmap", "marginal_right"],
     ["marginal_bottom", "."]],
    width_ratios=[4, 1], height_ratios=[4, 1],
    figsize=(7, 6))

im = axd["heatmap"].imshow(confusion_matrix, cmap='Blues')
axd["marginal_right"].barh(range(n), row_sums)
axd["marginal_bottom"].bar(range(n), col_sums)
```

### Phase Transition Annotation
```python
# Locate the transition point
threshold_idx = np.argmax(np.diff(performance) > delta_threshold)
ax.axvline(x=x_values[threshold_idx], ls='--', color='red', alpha=0.7)
ax.fill_between(x_values[:threshold_idx], 0, 1,
                alpha=0.05, color='blue', label='Phase I')
ax.fill_between(x_values[threshold_idx:], 0, 1,
                alpha=0.05, color='red', label='Phase II')
ax.text(x_values[threshold_idx], y_top,
        f'Transition at\n$p_c = {x_values[threshold_idx]:.2f}$',
        fontsize=9, ha='center')
```

## Anti-Patterns

- Do not show a single t-SNE plot without comparison
- Do not show an attention map without overlaying it on the original input
- Do not plot hyperparameter sensitivity with only 3 data points
- Do not present analysis figures without quantitative metrics -- "it looks like" is insufficient
- Do not analyze only success cases while ignoring failure cases
