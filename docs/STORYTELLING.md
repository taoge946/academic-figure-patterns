# Storytelling in Figures

**Core idea**: A good figure does not merely "display data" -- it "tells a story with data."
This document summarizes narrative techniques distilled from 18 top-venue papers.

---

## Technique 1: Setup then Debunk

**Source**: Emergent Abilities (NeurIPS 2023 Best Paper)

**Approach**:
1. Figure N: Faithfully reproduce the prior conclusion (convince the reader the phenomenon is real)
2. Figure N+1: Reveal that the conclusion is an artifact (a different lens on the same data tells a different story)

**Effect**: The reader experiences "believe --> surprise --> understand," leaving a lasting impression

**When to use**: Your paper's core claim is "a prior finding/method is flawed"

**Code structure**:
```python
# Figure 1: "Reproduce" prior results (setup)
fig, axes = plt.subplots(2, 4, figsize=(TEXTWIDTH, TEXTWIDTH*0.4))
for ax, task in zip(axes.flat, tasks):
    plot_prior_result(ax, task)  # Appears to show emergence

# Figure 3: Same data, different metric (debunk)
fig, axes = plt.subplots(2, 3, figsize=(TEXTWIDTH, TEXTWIDTH*0.35))
for col, task in enumerate(tasks[:3]):
    axes[0, col].set_title(task)
    plot_nonlinear_metric(axes[0, col], task)   # Top row: emergence
    plot_linear_metric(axes[1, col], task)       # Bottom row: smooth
# Row labels
axes[0, 0].set_ylabel('Accuracy\n(nonlinear)', fontweight='bold')
axes[1, 0].set_ylabel('Token Edit Dist.\n(linear)', fontweight='bold')
```

---

## Technique 2: Dual Panel to Rule Out Alternative Explanations

**Source**: ResNet Fig 1 (train + test), Fig 4 (same structure for solution)

**Approach**: Show two panels side by side -- one that admits an alternative explanation, and another that eliminates it

**Classic combinations**:
- Train error + Test error --> "Not overfitting"
- Small data + Large data --> "Not a data scarcity issue"
- Short sequence + Long sequence --> "Advantage amplifies at longer sequences"
- Dataset A + Dataset B --> "Not limited to a single dataset"

**Code pattern**:
```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(TEXTWIDTH, TEXTWIDTH*0.35),
                                 sharey=True)

for method, data in results.items():
    ax1.plot(data['train_x'], data['train_y'], label=method)
    ax2.plot(data['test_x'], data['test_y'], label=method)

ax1.set_title('Training Error', fontsize=9, fontweight='bold')
ax2.set_title('Test Error', fontsize=9, fontweight='bold')
ax1.set_ylabel('Error (%)')
ax2.legend(loc='best', fontsize=7)
```

---

## Technique 3: Verify then Extrapolate

**Source**: IBM Utility (Nature 2023), Google Sycamore (Nature 2019)

**Approach**:
1. Left half of the figure: Show "experiment = theory" in the verifiable region (build trust)
2. Right half of the figure: Show only experimental results in the unverifiable region (demonstrate capability)
3. A vertical dashed line separates the two regions

**Effect**: The reader is first convinced the method is reliable, then accepts the new results

**Code pattern**:
```python
fig, ax = plt.subplots(figsize=(COLWIDTH, COLWIDTH*0.65))

# Verifiable region
mask_verify = x <= x_boundary
ax.plot(x[mask_verify], theory[mask_verify], '-', color='C1', label='Theory')
ax.errorbar(x[mask_verify], exp[mask_verify], yerr=err[mask_verify],
             fmt='o', color='C0', ms=3, capsize=2, label='Experiment')

# Beyond-verification region
mask_beyond = x > x_boundary
ax.errorbar(x[mask_beyond], exp[mask_beyond], yerr=err[mask_beyond],
             fmt='o', color='C0', ms=3, capsize=2)

# Separator + region labels
ax.axvline(x_boundary, color='gray', ls='--', lw=0.8)
ax.text(x_boundary * 0.7, ax.get_ylim()[1] * 0.95,
        'Classically\nverifiable', ha='center', fontsize=7, color='gray')
ax.text(x_boundary * 1.3, ax.get_ylim()[1] * 0.95,
        'Beyond\nclassical', ha='center', fontsize=7, color='#e74c3c',
        fontweight='bold')

# Shaded region
ax.axvspan(x_boundary, ax.get_xlim()[1], alpha=0.05, color='red')
```

---

## Technique 4: Causal Fork Diagram

**Source**: Emergent Abilities Fig 2

**Approach**: Use the spatial layout of panels to express causal relationships
- Common starting point (A, B) --> fork into two branches (C, D vs E, F)
- Arrows + labels indicate "what operation caused the fork"

**Effect**: One figure = a complete causal argument

```python
fig = plt.figure(figsize=(TEXTWIDTH, TEXTWIDTH*0.7))
gs = fig.add_gridspec(3, 4, hspace=0.4, wspace=0.3)

# Common starting point
ax_a = fig.add_subplot(gs[0, 1])   # Panel A (center-left)
ax_b = fig.add_subplot(gs[0, 2])   # Panel B (center-right)

# Left branch (nonlinear --> emergence)
ax_c = fig.add_subplot(gs[1, 0])
ax_d = fig.add_subplot(gs[2, 0])

# Right branch (linear --> no emergence)
ax_e = fig.add_subplot(gs[1, 3])
ax_f = fig.add_subplot(gs[2, 3])

# Arrow annotations
fig.text(0.25, 0.55, '-> Nonlinear\n   metric',
         fontsize=9, fontweight='bold', color='#e74c3c')
fig.text(0.7, 0.55, '-> Linear\n   metric',
         fontsize=9, fontweight='bold', color='#27ae60')
```

---

## Technique 5: Progressive Complexity

**Source**: ViT Fig 7, Learning Dynamics Fig 1

**Approach**: Multiple panels in a figure progress from simple to complex
- Panel A: Concept diagram / toy example (accessible to everyone)
- Panel B: Mechanism diagram (accessible to those who understand the method)
- Panel C: Quantitative data (evaluation results)
- Panel D: Deep analysis (expert-level insight)

**Effect**: Readers at different levels can all extract information from the figure

---

## Technique 6: Reference Band

**Source**: ViT Fig 3 (BiT shaded band), most comparison figures

**Approach**: Instead of plotting individual baseline data points, draw a shaded band representing the "baseline's performance range"

**Advantages**:
- Visually becomes "your method vs. a region" rather than "your method vs. a tangle of lines"
- Easy to spot the crossover point (when your method surpasses the baseline)

```python
# Baseline band
baseline_mean = np.mean(baseline_results, axis=0)
baseline_std = np.std(baseline_results, axis=0)
ax.fill_between(x, baseline_mean - baseline_std, baseline_mean + baseline_std,
                 alpha=0.2, color='gray', label='Baseline range')

# Your method
ax.plot(x, your_results, 'o-', color='#e74c3c', lw=2, label='Ours')
```

---

## Technique 7: Axis Choice as Argument

**Source**: Emergent Abilities, Scaling Laws, Mamba

**Core idea**: The choice of axes is not neutral -- it is part of the argument.

| What You Want to Prove | Which Axes to Use |
|------------------------|-------------------|
| Power law | Log-log (a straight line means power law) |
| Exponential growth/decay | Semi-log (a straight line means exponential) |
| "Zero is not really zero" | Log y-axis (reveals hidden performance) |
| Extrapolation capability | Log x-axis (shows orders-of-magnitude gap) |
| Scaling efficiency | FLOPs on x-axis (not parameter count) |
| Fair comparison | Normalized y-axis (not raw numbers) |

---

## Technique 8: Sorting as Narrative

**Source**: GPT-4 (exams sorted by score), all comparisons (grouped by category)

**Rule**: The ordering of data is not arbitrary -- it tells a story.

| Sorting Method | Narrative Effect |
|---------------|-----------------|
| Descending by score | "From strongest to weakest," best at the top |
| Grouped by category | "Classical vs DL vs Ours," highlights category differences |
| Ascending by difficulty | "Easy to hard," shows how the method scales |
| By time / scale | "Small to large," shows a trend |

---

## Technique 9: Caption Lead Sentence is a Conclusion

**Source**: Nearly all NeurIPS Best Papers

**Approach**: The first sentence of the caption states **the conclusion you want the reader to draw**, not "This figure shows..."

| Poor | Good |
|------|------|
| "This figure shows the accuracy of different methods." | "DPO achieves the highest reward at every KL level." |
| "Training curves of ResNet-20 and ResNet-56." | "Deeper residual networks achieve lower training error, resolving the degradation problem." |
| "Results on VTAB benchmark." | "ViT is competitive across all task categories when pretrained at scale." |

---

## Technique 10: One Figure, One Claim

**Source**: A common trait across all analyzed papers

**Rule**: Each figure answers one and only one question. If a figure tries to prove two unrelated claims simultaneously, split it into two figures.

**Exception**: The hero figure (Fig 1) may preview multiple claims, since its purpose is to hook the reader.

**Litmus test**: If you cannot state this figure's claim in a single sentence, the figure needs to be redesigned.
