# Advanced Presentation Techniques Overview

These techniques elevate figures beyond the basic `plt.plot/bar/scatter` toolkit.

## Information Enhancement (Making Figures More Informative)

| # | Technique | One-Line Description | Best Use Case |
|---|-----------|---------------------|---------------|
| 01 | Inset Zoom | Embed a magnifying lens within the main plot | Convergence regions, dense point clusters |
| 02 | Broken Axis | Truncate unimportant data ranges | Outlier baselines |
| 03 | Annotations | Arrow + text callouts for key findings | Any figure |
| 04 | Dual Y-axis | Two metrics sharing the x-axis | Simultaneous loss + accuracy display |
| 05 | Reference Lines | Horizontal/vertical reference lines | Random chance, human performance, bounds |

## Layout (Making Figures Richer)

| # | Technique | One-Line Description | Best Use Case |
|---|-----------|---------------------|---------------|
| 06 | subplot_mosaic | ASCII-defined multi-panel layouts | Asymmetric panel combinations |
| 07 | GridSpec Nesting | Nested subplot grids | Highly complex layouts |
| 08 | ConnectionPatch | Cross-subplot connectors | Overview-to-detail, zoom indicators |
| 09 | Marginal Plots | Marginal distributions | Scatter + per-axis histograms |

## Advanced Chart Types (Replacing Basic Charts)

| # | Technique | Replaces | Advantage |
|---|-----------|----------|-----------|
| 10 | Waterfall Chart | Ablation bar chart | Shows cumulative contributions |
| 11 | Dumbbell Chart | Ablation bar chart | Shows before/after comparisons |
| 12 | Radar/Spider | Multi-metric table | Profile visible at a glance |
| 13 | Bump Chart | Ranking table | Ranking changes visible at a glance |
| 14 | Ridge/Joy Plot | Multiple histograms | Distribution shift trends |
| 15 | Sankey Diagram | Textual flow descriptions | Data flow visualization |
| 16 | CDF Curves | Box plot | Complete distribution comparison |
| 17 | Bubble Chart | 3D scatter | Encodes a third dimension |

## Narrative Techniques (Telling a Story, Not Just Showing Data)

| # | Technique | One-Line Description | Top-Venue Example |
|---|-----------|---------------------|-------------------|
| S1 | Setup then reveal | First reproduce prior conclusions, then reveal them as artifacts | Emergent Abilities Fig 1->3 |
| S2 | Dual panel to rule out alternatives | Train + test side-by-side to rule out overfitting | ResNet Fig 1, Fig 4 |
| S3 | Validate then extrapolate | Left = verifiable region builds trust, right = beyond | IBM Utility Fig 4 |
| S4 | Causal fork diagram | Panel layout expresses causal relationships | Emergent Abilities Fig 2 |
| S5 | Progressive information density | Simple -> mechanism -> data -> analysis | ViT Fig 7, Learning Dynamics Fig 1 |
| S6 | Reference region/band | Shaded band replaces individual baseline points | ViT Fig 3 (BiT band) |
| S7 | Axis choice as argument | Log scale reveals hidden information | Emergent Abilities Fig 4 |
| S8 | Ordering as narrative | Sort by score rather than alphabetically | GPT-4 Fig 4 |
| S9 | Caption first sentence = conclusion | Write "X achieves" not "This shows" | DPO, Mamba |
| S10 | One figure, one claim | Each figure answers exactly one question | Common across all top venues |

See: `techniques/14_storytelling.md`

## Advanced Chart Types (With Complete Code)

See: `techniques/13_advanced_chart_types.md`

Includes: Raincloud, Beeswarm, Waterfall, Dumbbell, Bump Chart, Pareto Frontier,
ECDF, Ridge Plot, Significance Brackets, Topology Heatmap -- all with ready-to-use functions.

## Quantum Hardware-Specific Chart Types

See: `patterns/10_quantum_hardware.md`

Includes: Chip Topology Heatmap, Theory vs. Experiment Overlay, Error Budget,
Validate-then-Extrapolate Narrative Figures, 3D Space-Time Syndrome -- all with code patterns.

---

## Usage Principles

1. **Don't use techniques for their own sake** -- every technique should serve a specific claim
2. **Use at least one** -- bare-bones basic plots are an anti-pattern
3. **Combine freely** -- Inset zoom + Annotations on the same figure is common
4. **Check pattern recommendations** -- each pattern file suggests suitable techniques
5. **Narrative techniques matter most** -- advanced chart types are supplementary; narrative structure is the core
6. **Consult the case library** -- when unsure how to plot something, check `REAL_PAPER_CASES.md` for similar examples
