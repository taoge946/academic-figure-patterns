# Claim-to-Pattern Quick Index

Before creating a figure, identify your claim, then look up the corresponding pattern here.

## Performance / Effectiveness

| What You Want to Say | Pattern | Recommended Visualization |
|---------------------|---------|--------------------------|
| "Our method is the best overall" | `02_main_comparison` | Grouped bar + radar + scatter |
| "We outperform the baseline by X%" | `02_main_comparison` | Grouped bar (annotate delta) |
| "Best on all datasets" | `02_main_comparison` | Heatmap matrix / bump chart |
| "Our method is more robust" | `09_distribution` | Violin + robustness curve |
| "Lower variance, more stable" | `09_distribution` | Box/violin + CDF |

## Efficiency

| What You Want to Say | Pattern | Recommended Visualization |
|---------------------|---------|--------------------------|
| "Faster at equal accuracy" | `08_pareto_tradeoff` | Pareto scatter + arrow annotation |
| "Better accuracy-efficiency trade-off" | `08_pareto_tradeoff` | Pareto frontier |
| "Remains efficient as scale grows" | `04_scaling` | Log-log scaling + fit |
| "Converges faster" | `05_training_dynamics` | Comparative training curves + speedup annotation |

## Method Explanation

| What You Want to Say | Pattern | Recommended Visualization |
|---------------------|---------|--------------------------|
| "Every component contributes" | `03_ablation` | Waterfall / dumbbell |
| "Our core idea is..." | `01_hero_figure` | Three-panel layout |
| "Learns better representations" | `07_analysis` | t-SNE comparison + silhouette |
| "Attention focuses on the right regions" | `07_analysis` | Attention heatmap overlay |
| "There is a phase transition / threshold effect" | `07_analysis` | Phase transition + shaded regions |

## Qualitative Results

| What You Want to Say | Pattern | Recommended Visualization |
|---------------------|---------|--------------------------|
| "Higher output quality" | `06_qualitative` | Grid comparison + zoom-in |
| "More diverse / more accurate generation" | `06_qualitative` | Grid + quantitative overlay |
| "Works even on hard samples" | `06_qualitative` | Easy-to-Hard gradient + failure cases |

## Hyperparameter / Design Choice

| What You Want to Say | Pattern | Recommended Visualization |
|---------------------|---------|--------------------------|
| "Insensitive to hyperparameters" | `07_analysis` (Structure C) | Sensitivity curve + stable-region shading |
| "Optimal configuration is X" | `07_analysis` (Structure C) | 2D heatmap + star at optimum |

## Quantum Hardware / Experiment

| What You Want to Say | Pattern | Recommended Visualization |
|---------------------|---------|--------------------------|
| "Qubit performance is uniformly distributed" | `10_quantum_hardware` (A) | Chip topology heatmap + ECDF |
| "Experiment matches theory" | `10_quantum_hardware` (B) | Theory overlay + residual |
| "Error component breakdown" | `10_quantum_hardware` (C) | Stacked bar error budget |
| "Where the quantum advantage lies" | `10_quantum_hardware` (D) | Verification-to-extrapolation narrative |
| "Syndrome evolution in space-time" | `10_quantum_hardware` (E) | 3D space-time scatter |
| "Error decreases with increasing code distance" | `10_quantum_hardware` (B+C) | Log-scale scaling + error budget |

## Argumentation Techniques (Distilled from NeurIPS Best Papers)

| What You Want to Say | Pattern | Recommended Visualization | Example |
|---------------------|---------|--------------------------|---------|
| "The prior conclusion is an artifact" | `07_analysis` | Same data, different metric grid | Emergent Abilities Fig 3 |
| "A different lens on the data changes the conclusion" | `07_analysis` | Log-scale or alternative metric | Emergent Abilities Fig 4 |
| "The causal chain is A -> B -> C" | `01_hero` | Fork structure + arrows | Emergent Abilities Fig 2 |
| "Our method is Pareto-optimal" | `08_pareto_tradeoff` | Scatter frontier | DPO Fig 2 |
| "Better across all regimes" | `04_scaling` | Dual panel (short/long, small/large) | Mamba Fig 6 |

## Common Combinations (for composite figures)

**Main Results Figure** (most common combination):
```
Pattern 02 (bar chart) + Pattern 08 (Pareto scatter)
= Top: absolute performance comparison; Bottom: efficiency trade-off
```

**Deep Analysis Figure**:
```
Pattern 07 (t-SNE) + Pattern 09 (distribution) + Pattern 03 (ablation)
= Representation quality + statistical significance + component contributions
```

**Full Story Figure 1**:
```
Pattern 01 (hero) = Method overview + a condensed Pattern 02 results preview
```
