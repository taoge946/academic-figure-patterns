# Pattern 03: Ablation Study Figure

## Purpose
Demonstrate that every component of your method is necessary -- not just a pile of tricks.

## Claim Type
"Each proposed component contributes positively to the final performance"

## Top-Venue Standard

When reviewing ablation experiments, reviewers want to know:
1. How much does each component contribute independently?
2. Are there interaction effects between components?
3. Which component is most critical when removed?
4. How does the base model (without any of your additions) perform?

## Presentation Choices

### Option A: Waterfall Chart (Best Choice -- Shows Cumulative Contributions)
```
Base --> +Component A (+2.3%) --> +Component B (+1.5%) --> +Component C (+0.8%) --> Final

Visual:
|============|                              Base: 82.0
|============|===|                          +Aug: +3.5
|============|===|==|                       +LR:  +2.1
|============|===|==|=|                     +Drop: +1.2
             |===|==|=|  <-- red downward   -BN:  -0.8
|========================|                  Final: 88.0

- Positive contributions: green, upward
- Negative contributions: red, downward
- Connector lines between adjacent bars
- Delta values labeled on each bar
```

**Why this is better than a plain bar chart**:
- A plain bar chart shows only final values, hiding the order of contributions
- A waterfall chart reveals the cumulative process, making each component's contribution immediately visible

**Caveats (0.2.1)**:
- Step sizes depend on the order components were added. With interactions, "+5.2 from attention" is only
  true for that order. If you claim a component's contribution, also show leave-one-out (full model minus
  that component, Option B/C) or state the order is fixed by design.
- Only the floating steps are lengths. If the axis does not start at zero, draw the base and final values
  as level marks, not bars from the frame (`examples/02_ablation_waterfall.py`).
- Each step should carry its run-to-run spread; a +0.3 step inside a ±0.5 spread is not a contribution.

### Option B: Grouped Bar + Arrow (Showing With/Without Differences)
```
Each group has two bars: with component / without component
Connected by an arrow, labeled with delta

  |==|     |====|
  |==| --> |====|  +2.3%
 w/o A     w/ A
```

### Option C: Dumbbell Chart (Most Intuitive for Before/After Comparison)
```
One row per component:
Component A:  o--------------------o  82.0 -> 84.3 (+2.3)
Component B:  o--------------o        82.0 -> 83.5 (+1.5)
Component C:  o--------o             82.0 -> 82.8 (+0.8)

Left dot = w/o, Right dot = w/
Line length = magnitude of contribution
```

### Option D: Multi-Panel Ablation (Multiple Datasets / Metrics)
```
+--------------+--------------+--------------+
| Dataset A    | Dataset B    | Dataset C    |
| waterfall    | waterfall    | waterfall    |
| (same order) | (order changed!) | (same order) |
+--------------+--------------+--------------+
Key insight: If the ranking of contributions differs across datasets, discuss why
```

## Required Elements

1. **Base performance**: Performance without any of your components (clean baseline)
2. **Delta for each component**: Not just final values, but explicit +/- differences
3. **Full model performance**: Final performance with all components included
4. **Error bars**: Ablation experiments should also be run multiple times
5. **Component interactions**: If the effect of A+B together differs from A alone + B alone, this must be annotated

## Advanced Technique: Interaction Effect Heatmap

When there are more than 4 components, create an interaction effect matrix:
```python
# interaction_matrix[i][j] = performance(with_i_and_j) - performance(with_i) - performance(with_j) + baseline
sns.heatmap(interaction_matrix, annot=True, fmt=".1f",
            cmap="RdYlGn", center=0,
            xticklabels=components, yticklabels=components)
# Positive values = synergy
# Negative values = redundancy
```

## Common Pitfalls

- Do not present only a table with no visualization
- Do not perform only subtractive ablation (removing components) without additive ablation (adding components)
- Do not omit the base model performance as a reference
- Do not run each variant only once with no error bars
- Do not simply duplicate the main table results -- the ablation figure should provide additional insight
