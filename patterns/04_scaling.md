# Pattern 04: Scaling / Efficiency Figure

## Purpose
Demonstrate how the method performs at different scales, proving scalability or efficiency advantages.

## Claim Type
- "Our method scales better with problem size"
- "We achieve the same accuracy with 10x less compute"
- "Performance follows a power-law scaling with model size"

## Top-Venue Standard Structures

### Structure A: Log-Log Scaling Plot (Chinchilla-Style)
```
y = performance (loss / error / accuracy)
x = scale variable (params / FLOPs / data size / problem size)
- Log-log axes: power-law relationships appear as straight lines in log-log space
- One line per method; your line should be lowest (loss) or highest (accuracy)
- Label key configuration points ("ResNet-50", "ViT-B/16")
- Fit and display a power-law equation: y = ax^b
```

**Required elements**:
- Log-log axes (when data spans multiple orders of magnitude)
- Fitted line + equation (not just data points)
- Multiple methods for comparison (do not plot only yours)
- Confidence intervals (shaded bands)

### Structure B: Efficiency Frontier Plot (Accuracy vs. Cost)
```
x = compute cost (FLOPs / wall time / GPU hours) [log scale]
y = performance (accuracy / F1 / BLEU)

- Your method: large star marker; baselines: small circle markers
- Draw the Pareto frontier (your method should lie on or beyond the frontier)
- Label representative configuration names
- Optional: iso-cost / iso-performance lines shown as dashed lines
```

### Structure C: Multi-Panel Scaling (Different Scaling Dimensions)
```
+--------------+--------------+--------------+
|(a) vs #params|(b) vs #data  |(c) vs #time  |
| Model size   | Data size    | Wall-clock   |
| scaling      | scaling      | time         |
+--------------+--------------+--------------+
Three panels telling one story: our method scales better across all dimensions
```

### Structure D: Iso-Cost Curves (Optimal Choice Under Fixed Budget)
```
Multiple curves, each representing a fixed budget level
x = tunable parameter (e.g., model size)
y = performance
- Mark the optimal point on each curve with a star
- Connect all optimal points = optimal scaling trajectory
```

## Key Code Techniques

### Log-Log with Power Law Fit
```python
import numpy as np
from scipy.optimize import curve_fit

def power_law(x, a, b):
    return a * x ** b

popt, pcov = curve_fit(power_law, x_data, y_data)

ax.loglog(x_data, y_data, 'o', label='Data')
x_fit = np.logspace(np.log10(x_data.min()), np.log10(x_data.max()), 100)
ax.loglog(x_fit, power_law(x_fit, *popt), '--',
          label=f'$y = {popt[0]:.2f} \\cdot x^{{{popt[1]:.2f}}}$')
```

### Pareto Frontier
```python
def pareto_frontier(costs, perfs):
    """Return indices of Pareto-optimal points."""
    sorted_idx = np.argsort(costs)
    pareto_idx = [sorted_idx[0]]
    best_perf = perfs[sorted_idx[0]]
    for i in sorted_idx[1:]:
        if perfs[i] > best_perf:
            pareto_idx.append(i)
            best_perf = perfs[i]
    return pareto_idx

# Draw the Pareto frontier
pidx = pareto_frontier(costs, perfs)
ax.plot(costs[pidx], perfs[pidx], 'k--', alpha=0.5, zorder=0)
ax.fill_between(costs[pidx], perfs[pidx], alpha=0.05, color='green',
                label='Pareto-optimal region')
```

### Annotating Configuration Names
```python
for name, x, y in zip(config_names, costs, perfs):
    ax.annotate(name, (x, y), textcoords="offset points",
                xytext=(5, 5), fontsize=7, alpha=0.8)
```

## Common Pitfalls

- Do not use linear axes for data spanning multiple orders of magnitude (all points collapse together)
- Do not plot only your method with no baseline comparison
- Do not leave configuration points unlabeled
- Do not claim "scales well" with only 3 data points
- Do not omit error bands / confidence intervals
- Do not leave the x-axis ambiguous about which resource is being measured (FLOPs? params? GPU hours?)
