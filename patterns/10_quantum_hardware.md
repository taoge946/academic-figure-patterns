# Pattern 10: Quantum Hardware / Experimental Results Figure

## Purpose
Present quantum hardware experimental data: fidelity, error rates, qubit performance, and circuit execution results.
Applicable to Nature / Science / PRL / PRX Quantum / QST-level publications.

## Reference Papers
- Google Sycamore (Nature 2019) -- XEB fidelity, processor heatmap
- Google QEC (Nature 2023) -- error budget, scaling, 3D syndrome
- IBM Utility (Nature 2023) -- mitigation comparison, beyond-classical

---

## Sub-pattern A: Chip Topology Heatmap

**Purpose**: Display qubit- or coupler-level performance metrics on the physical chip layout.

**Structure**:
```
┌─────────────────────────┐
│  Chip Topology Heatmap  │  <- actual topology, not a grid
│  (error rates / T1 /    │
│   fidelity per qubit)   │
│  + colorbar             │
├─────────────────────────┤
│  ECDF of same metric    │  <- distributional summary
└─────────────────────────┘
```

**Key requirements**:
- Use the **actual chip topology** for the heatmap (not a square grid)
- Use ECDF instead of histogram -- lossless and more compact
- Colorbar must include tick marks and units
- Annotate the best and worst qubits
- Do not use abstract qubit-index ordering

**Code pattern**:
```python
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
from matplotlib.patches import Circle
import numpy as np

def plot_chip_topology_heatmap(qubit_positions, qubit_values,
                                edges, ax, cmap='RdYlGn_r',
                                vmin=None, vmax=None):
    """Plot a performance heatmap on the actual chip topology.

    qubit_positions: dict {qubit_id: (x, y)}
    qubit_values: dict {qubit_id: metric_value}
    edges: list of (q1, q2) coupler connections
    """
    # Draw coupler connections
    for q1, q2 in edges:
        x = [qubit_positions[q1][0], qubit_positions[q2][0]]
        y = [qubit_positions[q1][1], qubit_positions[q2][1]]
        ax.plot(x, y, 'k-', lw=0.5, alpha=0.3, zorder=1)

    # Draw qubit nodes
    xs = [qubit_positions[q][0] for q in qubit_values]
    ys = [qubit_positions[q][1] for q in qubit_values]
    vals = [qubit_values[q] for q in qubit_values]

    sc = ax.scatter(xs, ys, c=vals, cmap=cmap, s=80,
                    edgecolors='k', linewidths=0.5,
                    vmin=vmin, vmax=vmax, zorder=2)

    ax.set_aspect('equal')
    ax.axis('off')
    return sc


def plot_ecdf(values, ax, label=None, color='C0'):
    """ECDF: a better distributional display than histograms."""
    sorted_vals = np.sort(values)
    ecdf = np.arange(1, len(sorted_vals) + 1) / len(sorted_vals)
    ax.step(sorted_vals, ecdf, where='post', lw=1.5,
            color=color, label=label)
    ax.set_ylabel('Cumulative probability')
    ax.set_ylim(0, 1.05)
```

---

## Sub-pattern B: Theory vs. Experiment Overlay

**Purpose**: Show the agreement between experimental data and independent theoretical predictions.

**Key distinction**:
- "Theoretical prediction" is NOT "curve fitting" -- the theory comes from independent measurements, not from fitting the experimental data
- This is a **core argumentation technique** in Nature-level papers

**Structure**:
```
Single panel:
- Experimental data points (scatter with error bars)
- Theoretical prediction curve (smooth line, distinct line style)
- Annotation: "Theory from independent calibration"
- Optional: residual subplot below
```

**Code pattern**:
```python
fig, (ax_main, ax_res) = plt.subplots(2, 1, figsize=(COLWIDTH, COLWIDTH*0.8),
                                       height_ratios=[3, 1], sharex=True)

# Main: experiment + theory
ax_main.errorbar(x_exp, y_exp, yerr=y_err, fmt='o', ms=4,
                  color='C0', capsize=2, label='Experiment')
ax_main.plot(x_theory, y_theory, '-', color='C1', lw=1.5,
              label='Theory (independent)')
ax_main.fill_between(x_theory, y_theory_lo, y_theory_hi,
                      alpha=0.2, color='C1')

# Residual
residuals = y_exp - np.interp(x_exp, x_theory, y_theory)
ax_res.errorbar(x_exp, residuals, yerr=y_err, fmt='o', ms=3,
                 color='C0', capsize=2)
ax_res.axhline(0, color='gray', ls='--', lw=0.5)
ax_res.set_ylabel('Residual')
```

---

## Sub-pattern C: Error Budget

**Purpose**: Decompose total error into individual sources to guide improvement priorities.

**Structure**:
```
┌──────────────┬──────────────┐
│ Stacked bar  │ Scaling plot │
│ (error       │ (total error │
│  components) │  vs code     │
│              │  distance)   │
└──────────────┴──────────────┘
```

**Code pattern**:
```python
# Stacked bar for error budget
components = ['Measurement', 'Leakage', 'Crosstalk', 'T1 decay', 'Other']
values = [0.003, 0.001, 0.002, 0.004, 0.001]
colors = ['#e74c3c', '#e67e22', '#f1c40f', '#3498db', '#95a5a6']

bottom = 0
for comp, val, col in zip(components, values, colors):
    ax.bar(0, val, bottom=bottom, color=col, label=comp, width=0.5)
    if val > 0.001:  # Only label large components
        ax.text(0.3, bottom + val/2, f'{comp}\n{val:.1%}',
                va='center', fontsize=7)
    bottom += val
```

---

## Sub-pattern D: "Validate then Extrapolate" Narrative Figure

**Purpose**: First demonstrate correctness in a classically verifiable regime, then present results in the unverifiable regime.

**This is the hallmark technique of Nature-level quantum computing papers** (IBM Utility, Google Supremacy).

**Structure**:
```
┌──────────────────────────────────────┐
│   ←  Classically verifiable  →│← Beyond →│
│                                │           │
│   Exp ● ● ● ● ● ● ● ● ● ●  │  ● ● ●   │
│   Theory ─────────────────    │           │
│                                │           │
│   ┌─────┐ Shaded region:     │  ???      │
│   │Inset│ "classical limit"  │           │
│   └─────┘                    │           │
└──────────────────────────────────────┘
```

**Key design elements**:
- Vertical dashed line separating the "verifiable" and "unverifiable" regions
- Left side: experiment matches theory (building trust)
- Right side: only experimental data (demonstrating beyond-classical capability)
- Inset explaining why the right side is classically intractable (light cone / exponential blowup)

---

## Sub-pattern E: 3D Space-Time Syndrome Figure

**Purpose**: Visualize QEC syndrome evolution across spatial and temporal dimensions.

**Note**: This is rarely needed, but is highly effective in Nature-level QEC papers.

```python
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(COLWIDTH, COLWIDTH))
ax = fig.add_subplot(111, projection='3d')

# Syndrome events as scatter
ax.scatter(x_space, y_space, z_time, c=syndrome_type,
           cmap='coolwarm', s=20, alpha=0.7)

# Matching edges
for (x1,y1,t1), (x2,y2,t2) in matched_pairs:
    ax.plot([x1,x2], [y1,y2], [t1,t2], 'b-', lw=0.5, alpha=0.5)

ax.set_xlabel('X (space)')
ax.set_ylabel('Y (space)')
ax.set_zlabel('Round (time)')
ax.view_init(elev=20, azim=45)
```

---

## Checklist: Quantum Hardware Figures

- [ ] Error bars specify the statistical method (bootstrap / shot noise / repeated calibration)
- [ ] Theoretical predictions come from independent measurements, not fitting (if fitted, state so clearly)
- [ ] Chip topology figures use the actual physical layout, not abstract qubit indices
- [ ] Log scale for metrics spanning orders of magnitude (error rate, fidelity loss)
- [ ] ECDF preferred over histogram
- [ ] Colormap is perceptually uniform (viridis / inferno, not jet)
- [ ] Qubit count, circuit depth, and number of shots are annotated
