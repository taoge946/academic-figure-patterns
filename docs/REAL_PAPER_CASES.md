# Real Top-Venue Paper Figure Case Studies

**Visual analysis of 50+ result figures from 18 top-tier papers**

This document covers only **result figures** (data-driven), excluding architecture diagrams, flowcharts, and method schematics.
Each case records: the paper, figure number, claim, visualization approach, key design decisions, and an "amateur vs. top-venue" comparison.

---

## I. Comparison Figures (Main Comparison)

### Case C01: GPT-4 Fig 4 -- Exam Percentile Grouped Bar
- **Paper**: GPT-4 Technical Report (arXiv:2303.08774)
- **Claim**: "GPT-4 passes most professional/academic exams at human-level"
- **Visualization**: Grouped horizontal bar chart; each bar = one exam; color distinguishes GPT-4 vs GPT-3.5
- **Key Design Decisions**:
  - Sorted by percentile (not alphabetically by exam name) --> narrative flow: "from strongest to weakest"
  - Horizontal bars (not vertical) --> exam names can be displayed in full
  - Two-color comparison (GPT-4 dark green vs GPT-3.5 light green) --> gap visible at a glance
  - Percentile scale (0%-100%) --> intuitive understanding of "pass rate"
- **Amateur version**: Only 5 exams as vertical bars, no sorting
- **Top-venue version**: All 25+ exams shown, sorted by score, dual-model comparison, numeric labels on every bar

### Case C02: ViT Fig 2 -- VTAB Benchmark Grouped Bar
- **Paper**: An Image is Worth 16x16 Words (arXiv:2010.11929)
- **Claim**: "ViT is competitive across diverse vision task categories"
- **Visualization**: 4 groups x 4 methods grouped bar, numbers labeled above bars
- **Key Design Decisions**:
  - Groups = dataset categories (overall + 3 subcategories), not individual datasets
  - Exact numbers on each bar --> no need to read the y-axis
  - Subcategory names include task counts in parentheses: Natural (7 tasks)
  - y-axis does not start at 0 (starts around 50%), magnifying differences
- **Amateur version**: 4 bars, one overall score, no subcategory breakdown
- **Top-venue version**: Overall + subcategory breakdown, numeric bar labels, optimized y-axis

### Case C03: Mamba Fig 6 -- Scaling Law Comparison
- **Paper**: Mamba (arXiv:2312.00752)
- **Claim**: "Mamba scales better than all attention-free models, matches Transformer++"
- **Visualization**: Two panels (seq 2048 vs 8192), log-log perplexity vs FLOPs
- **Key Design Decisions**:
  - Log-log axes --> standard Chinchilla format, familiar to readers
  - 7 models with distinct colors + markers --> clear differentiation
  - Two panels show "advantage amplifies at longer sequences" --> progressive narrative
  - Mamba line consistently below Transformer++ --> geometric relationship is the argument
- **Amateur version**: One panel, 3 lines, linear axes
- **Top-venue version**: Dual-panel comparison across regimes, 7 lines, log-log, Chinchilla style

### Case C04: DPO Fig 2 -- Reward-KL Frontier
- **Paper**: Direct Preference Optimization (arXiv:2305.18290)
- **Claim**: "DPO achieves highest reward at every KL level (Pareto optimal)"
- **Visualization**: Left = scatter (reward vs KL), right = line (win rate vs temperature)
- **Key Design Decisions**:
  - Left panel: each point = one training run (different hyperparameters), 6 methods in different colors
  - DPO points form the **upper envelope** (Pareto frontier) --> geometric dominance is more intuitive than numbers
  - Right panel: reference line (GPT-4 dashed) --> provides a "ceiling" reference
  - Error bars honestly displayed --> what reviewers value most
- **Amateur version**: A bar chart comparing 5 methods' rewards
- **Top-venue version**: Frontier scatter showing dominance across the full parameter space + robustness line plot

### Case C05: ResNet Fig 1 -- Degradation Problem
- **Paper**: Deep Residual Learning (arXiv:1512.03385)
- **Claim**: "Deeper networks have HIGHER training error (not just test error)"
- **Visualization**: Dual panel (left = train error, right = test error), each with two curves (20-layer vs 56-layer)
- **Key Design Decisions**:
  - The gap between curves exists on the **training set** too --> rules out overfitting as an explanation
  - 56-layer (deeper) consistently above --> counterintuitive, grabs attention
  - Side-by-side dual panel --> reader immediately sees "same pattern on both sides"
  - This is a **problem-definition figure**, not a solution figure --> establishes motivation
- **Amateur version**: Only test error in one panel
- **Top-venue version**: Train + test dual panel, making the "counterintuitive finding" irrefutable

---

## II. Ablation and Component Analysis

### Case A01: Emergent Abilities Fig 3 -- Same Data, Different Metric
- **Paper**: Are Emergent Abilities a Mirage? (NeurIPS 2023 Best Paper)
- **Claim**: "Changing the metric removes the appearance of emergence"
- **Visualization**: 2-row x 3-column grid; top row = Accuracy (nonlinear), bottom row = Token Edit Distance (linear)
- **Key Design Decisions**:
  - **Same data** plotted twice, only the metric changes --> the strongest ablation: "the only variable is the metric"
  - Top row shows "sharp transition," bottom row shows "smooth improvement" --> visual contrast is the argument
  - The grid structure itself is the proof --> no text annotations needed
  - Color encodes Target Str Len --> shows parameter sweep
- **Amateur version**: Describing in text that "things look different with a different metric"
- **Top-venue version**: Grid lets readers see the contrast themselves, zero text annotations

### Case A02: Emergent Abilities Fig 4 -- Log-Scale Reveals Hidden Information
- **Paper**: Same as above
- **Claim**: "Better statistics (more test data, log scale) removes emergence"
- **Visualization**: 3 columns, y-axis changed to log scale
- **Key Design Decisions**:
  - **Log y-axis reveals the truth**: regions that appear "zero" on a linear scale actually show above-random performance
  - Confidence intervals vary with sample size --> demonstrates the effect of measurement resolution
  - Uses the same 3 tasks as Fig 1 --> enables direct comparison
- **Amateur version**: Simply stating "emergence disappears on a log scale"
- **Top-venue version**: Lets readers see the linear vs log-scale difference on **the same data**

---

## III. Scaling Figures

### Case S01: Scaling Laws (Kaplan) -- Classic Three-Panel Power Law
- **Paper**: Scaling Laws for Neural LMs (arXiv:2001.08361)
- **Claim**: "Performance follows power laws in compute, data, and parameters"
- **Visualization**: Three log-log panels (compute, dataset, params vs loss)
- **Key Design Decisions**:
  - **Each panel addresses a single relationship** --> clear, no confusion
  - Power law fit lines + equation annotations --> quantitative
  - Multiple model sizes in rainbow colors (blue to red) --> intuitive: "redder = larger"
  - Log-log turns power laws into straight lines --> visually self-evident
- **Amateur version**: One panel with 3 lines, linear axes, no fits
- **Top-venue version**: Three panels isolating three factors, log-log + fit lines + equations

### Case S02: Chinchilla Fig 3-4 -- IsoFLOP Curves + Contour
- **Paper**: Training Compute-Optimal LLMs (arXiv:2203.15556)
- **Claim**: "For each compute budget, there is an optimal model size"
- **Visualization**: Fig 3 = IsoFLOP U-shaped curves, Fig 4 = 2D contour plot
- **Key Design Decisions**:
  - **IsoFLOP curves**: each line = fixed compute, x = model size, y = loss --> U-shaped valley shifts
  - Contour plot = maximum information density: x = params, y = tokens, color = loss
  - Optimal line overlaid on contour --> "this line is the Chinchilla Scaling Law"
  - Color encodes compute budget --> rainbow from low (blue) to high (red)
- **Amateur version**: A table listing loss values for different configurations
- **Top-venue version**: IsoFLOP curves showing structure + contour plot showing the full landscape + optimal line

### Case S03: ViT Fig 3 -- Dataset Size Crossover
- **Paper**: ViT (arXiv:2010.11929)
- **Claim**: "ViT needs large pretraining to beat CNNs, but once you have it, dominates"
- **Visualization**: Scatter with shaded BiT band
- **Key Design Decisions**:
  - **Gray shaded band = BiT's performance range** --> instead of individual points, draw a "band"
  - 3 columns = 3 dataset scales (small -> medium -> large) --> left-to-right narrative
  - ViT's points move from "below the band" to "above the band" --> crossover story
  - 5 ViT variants with different colors + sizes --> variant differentiation
- **Amateur version**: All points in the same color, no reference band
- **Top-venue version**: BiT shaded band as visual baseline, crossover clearly visible

### Case S04: Mamba Fig 5 -- Sequence Extrapolation
- **Paper**: Mamba (arXiv:2312.00752)
- **Claim**: "Mamba extrapolates perfectly to 4000x longer sequences"
- **Visualization**: Accuracy vs sequence length (log x)
- **Key Design Decisions**:
  - Log x-axis --> shows 4 orders of magnitude of extrapolation range
  - Mamba's line stays at 1.0 while all others collapse to ~0 --> **visual impact**
  - The gap between training length and test length is the key --> mark with a vertical dashed line
  - 7 models compared --> thorough baselines
- **Amateur version**: 3 models at 2 lengths in a bar chart
- **Top-venue version**: 7 models across continuous length range, log scale showing orders-of-magnitude differences

---

## IV. Training Curves

### Case T01: ResNet Fig 4 -- ImageNet Training Curves
- **Paper**: Deep Residual Learning (arXiv:1512.03385)
- **Claim**: "ResNet solves the degradation problem -- deeper is now better"
- **Visualization**: Dual panel (training error vs validation error), multiple curves
- **Key Design Decisions**:
  - Forms a contrast with Fig 1 (problem demonstration) --> "before: deeper was worse; now: deeper is better"
  - Dual panel maintains consistency --> not overfitting, genuinely learning
  - Curve colors correspond to different depths --> consistency
- **Amateur version**: A single loss curve
- **Top-venue version**: A solution figure symmetric to the problem figure, dual panel

### Case T02: LLaMA Fig 1 -- Multi-Scale Training Loss
- **Paper**: LLaMA (arXiv:2302.13971)
- **Claim**: "LLaMA follows predictable scaling during training"
- **Visualization**: Single panel, 4 lines (4 model sizes)
- **Key Design Decisions**:
  - x-axis = tokens processed --> shows training progress
  - 4 lines naturally stratify --> larger models achieve lower loss
  - Minimal but information-complete --> 4 lines suffice to make the point
  - Key: this is **one of the rare cases where simplicity is enough**
- **Why simplicity works here**: Because the claim itself is "loss decreases smoothly" -- no complex visualization is needed

---

## V. Distribution and Statistics

### Case D01: Google QEC Fig 3 -- Logical Error Rate
- **Paper**: Suppressing quantum errors by scaling surface code (Nature 2023)
- **Claim**: "d=5 code has lower logical error rate than d=3 (error suppression working)"
- **Visualization**: Scatter + fit lines, d=3 vs d=5 across different physical error rates
- **Key Design Decisions**:
  - **Log axes**: logical error rate spans multiple orders of magnitude
  - Theoretical predictions overlaid on experimental data (not fitted -- independent predictions)
  - d=3 and d=5 in different colors --> immediately visible that "d=5 is better"
  - Error bars from bootstrap --> statistical method clearly stated
- **Amateur version**: A bar chart: d=3=X%, d=5=Y%
- **Top-venue version**: Trends + error bars + theoretical predictions across continuous physical error rates

### Case D02: Google Sycamore Fig 2 -- ECDF + Topology Heatmap
- **Paper**: Quantum supremacy (Nature 2019)
- **Claim**: "XEB fidelity is consistent across the processor"
- **Visualization**: ECDF (empirical cumulative distribution function) + chip topology error heatmap
- **Key Design Decisions**:
  - **ECDF replaces histogram** --> lossless information, more compact
  - **Heatmap drawn on actual chip topology** --> not an abstract grid, but the physical layout
  - Dual-layer information: statistical distribution (ECDF) + spatial distribution (topology heatmap)
- **Amateur version**: A histogram
- **Top-venue version**: ECDF + topology heatmap combination

---

## VI. Quantum Computing-Specific Figure Types

### Case Q01: Google Sycamore Fig 4 -- XEB Fidelity Scaling (The Money Shot)
- **Paper**: Quantum supremacy (Nature 2019)
- **Claim**: "Quantum computer performs a task exponentially faster than classical"
- **Visualization**: XEB fidelity vs number of qubits/cycles
- **Key Design Decisions**:
  - Experimental data points + theoretical prediction lines
  - Key annotation: classical simulation boundary ("above this line, classical simulation is infeasible")
  - Inset: time estimate text ("10,000 years vs 200 seconds")
  - **Purple shaded region = classically intractable zone** --> visual representation of "quantum supremacy"
- **Amateur version**: A bar chart: quantum=200s, classical=10000yr
- **Top-venue version**: Continuous scaling showing where the boundary lies and why it cannot be crossed

### Case Q02: IBM Utility Fig 4 -- Expectation Values Beyond Classical
- **Paper**: Evidence for quantum utility (Nature 2023)
- **Claim**: "Quantum results match exact values where classically verifiable, extend beyond"
- **Visualization**: Expectation value curves + light cone inset
- **Key Design Decisions**:
  - **"Verify then extrapolate" narrative**: left half has classical exact solutions for comparison; right half has quantum results only
  - Light cone inset --> explains why the right half is classically intractable
  - Multiple error mitigation methods shown with different line styles
  - Error bars clearly labeled with confidence level
- **Amateur version**: A bar chart: quantum vs classical
- **Top-venue version**: Continuous data showing the natural transition from verification to extrapolation regions

### Case Q03: Google QEC Fig 4 -- Error Budget + Phase Diagram
- **Paper**: Suppressing quantum errors (Nature 2023)
- **Claim**: "We are below the threshold, error suppression improves with code distance"
- **Visualization**: Multi-panel: error budget pie/bar + scaling + phase diagram
- **Key Design Decisions**:
  - Error budget = "how much each error source contributes" --> guides improvement priorities
  - Scaling plot = "how logical error rate changes with increasing code distance"
  - Phase diagram = "which side of the threshold are we on"
  - **3 panels tell 3 layers of story**: composition --> trend --> position
- **Amateur version**: Simply stating "our logical error rate is X"
- **Top-venue version**: Decompose error components + show scaling trend + locate on the phase diagram

### Case Q04: Google QEC Fig 2 -- 3D Space-Time Visualization
- **Paper**: Same as above
- **Claim**: "Surface code decoding works across space and time"
- **Visualization**: 3D perspective view (x = space, y = space, z = time)
- **Key Design Decisions**:
  - **3D perspective shows syndrome evolution in space-time**
  - 8 sub-panels showing different detection events
  - Time axis pointing upward --> readers can "see" errors propagating over time
- **Amateur version**: 2D slice screenshots
- **Top-venue version**: Full 3D space + time perspective

---

## VII. Analysis / Understanding Figures

### Case AN01: ViT Fig 7 -- Triple Analysis (Extreme Information Density)
- **Paper**: ViT (arXiv:2010.11929)
- **Claim**: "ViT learns meaningful representations at every level"
- **Visualization**: Three vertically stacked, completely different visualizations
- **Key Design Decisions**:
  - **Top**: 4x7 RGB embedding filter patches (learned basis functions)
  - **Middle**: 7x7 position similarity heatmap grid ("heatmap of heatmaps")
  - **Bottom**: Attention distance vs depth scatter (one point per head)
  - Three visualizations tell three layers of story: filter quality --> positional encoding structure --> attention behavior
- **Amateur version**: A single attention heatmap
- **Top-venue version**: Three entirely different analyses combined in one figure

### Case AN02: Emergent Abilities Fig 2 -- One Figure Equals a Complete Proof
- **Paper**: Are Emergent Abilities a Mirage? (NeurIPS 2023 Best Paper)
- **Claim**: "Emergence is an artifact of metric choice, not a fundamental property"
- **Visualization**: 6 panels, A->B->(C,D) vs A->B->(E,F) fork structure
- **Key Design Decisions**:
  - **Panels A-B**: Common starting point (loss + per-token probability)
  - **Panels C-D** (left branch): Nonlinear metric --> emergence appears
  - **Panels E-F** (right branch): Linear metric --> emergence disappears
  - **Bold arrow labels: "Nonlinearly score" vs "Linearly score"** --> causal chain visualized
  - Mathematical formulas placed between panels --> derivation embedded in the figure
  - **This single figure is the entire paper's proof**
- **Amateur version**: 4 independent subplots, reader must connect the causal chain themselves
- **Top-venue version**: Causal fork structure visible at a glance, arrows + labels make the mechanism clear

---

## VIII. Cross-Paper Design Principles

### Principle 1: Sorting is Narrative
- GPT-4 Fig 4: Exams sorted by score --> "from strongest to weakest"
- All comparisons: Baselines grouped by category, not alphabetically
- ResNet: 7 figures arranged along a "problem --> solution --> validation --> analysis" narrative arc

### Principle 2: Reference Lines / Regions are Essential
- ViT: Gray BiT shaded band
- DPO: GPT-4 dashed reference line
- Sycamore: Classical simulation boundary
- All comparison figures: Random chance baseline

### Principle 3: Log Scale is an Argumentative Weapon
- Emergent Abilities: Log y-axis reveals "zero is not zero"
- Scaling Laws: Log-log turns power laws into straight lines
- Mamba: Log x-axis shows 4 orders of magnitude of extrapolation
- QEC: Log y-axis shows exponential error suppression

### Principle 4: Dual Panel > Single Panel
- ResNet: Train + test side by side --> rules out overfitting
- Mamba Scaling: Seq 2048 + seq 8192 --> shows amplified advantage
- DPO: Frontier + robustness --> two dimensions

### Principle 5: Grid Structure = Zero-Annotation Proof
- Emergent Abilities Fig 3: Rows = metric, columns = task --> the grid itself is the argument
- DDPM Fig 7: Columns = noise level --> visual gradient is the argument

### Principle 6: Consistent Color Semantics
- Every paper: "Our method" = one fixed prominent color (green/blue/red), unchanged throughout
- Baselines = gray or muted tones
- Good = warm colors, poor = cool colors (or the reverse, but be consistent)

### Principle 7: Caption as Argument
- The first sentence of every figure caption is a conclusion, not a description
- "DPO provides the highest reward" not "This figure shows reward vs KL"
- Bold text in captions highlights key conclusions

### Principle 8: The Right Level of Information Density
- Each figure has at least 3 information layers: data + context (reference lines/bands) + interpretation (annotations/highlights)
- But no more than 5-7 data lines/groups per panel
- Multi-panel (3-5 panels) is the sweet spot
