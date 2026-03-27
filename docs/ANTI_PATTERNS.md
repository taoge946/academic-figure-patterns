# Figure Anti-Patterns: A Blacklist

When generating figures for academic papers, **never** commit any of the following mistakes. Each one is distilled from real reviewer feedback and is a telltale sign of an inexperienced author.

---

## AP-01: The Bare Minimum

**Symptom**: The figure contains only the most basic elements -- 3 bars, 1 line, a few dots. No error bars, no annotations, no reference lines, no supplementary information.

**Reviewer's reaction**: _"This figure tells me nothing I can't read from a table"_

**Fix**: Every figure should include at least 2 of the following 3 elements:
- Error bars / confidence bands
- Reference lines (baseline / random / human / theoretical bound)
- Annotations (best point, key finding, phase boundary)

---

## AP-02: No Context

**Symptom**: Only your method is shown, with no baseline comparison. Or results are limited to a single metric on a single dataset.

**Reviewer's reaction**: _"So what? Is this good or bad?"_

**Fix**:
- Include at least 2 baselines for comparison
- Show at least 2 datasets or 2 metrics
- Mark random chance / trivial baseline as a lower bound

---

## AP-03: The Three-Trick Pony (plt.plot / plt.bar / plt.scatter and nothing else)

**Symptom**: Every figure uses only the most basic line plots, bar charts, or scatter plots, with no advanced visualization techniques.

**Reviewer's reaction**: _"This looks like a homework assignment"_

**Fix**: Choose figure types that match your data characteristics:
- Ablation --> Waterfall / Dumbbell, not just bars
- Multi-metric --> Radar / faceted subplots, not just grouped bars
- Distribution --> Violin / Ridge / CDF, not just bar + error bar
- Ranking --> Bump chart, not just a table
- Trade-off --> Pareto frontier, not just scatter
- Fine detail --> Inset zoom, don't make the reviewer guess

---

## AP-04: The Silent Figure (No Story)

**Symptom**: The figure is drawn but conveys no clear message. There is no headline annotation, no arrow pointing to the key finding.

**Reviewer's reaction**: _"What am I supposed to see here?"_

**Fix**:
- Each figure should have one clear takeaway (state it in the first sentence of the caption)
- Use `ax.annotate()` to highlight key findings ("3.2x faster", "Phase transition at p=0.11")
- Use shaded regions / vertical lines to mark regime boundaries

---

## AP-05: Misleading Precision

**Symptom**: Reporting 92.34567% without error bars. Or a bar chart with the y-axis starting at 0 while all values lie between 90-95%, flattening the differences.

**Reviewer's reaction**: _"This is either sloppy or deliberately misleading"_

**Fix**:
- Report only as many significant digits as justified by your data
- Set the y-axis range to reveal differences (but don't exaggerate -- use a broken axis instead of truncating)
- Always include error bars, specifying whether they represent std / SEM / 95% CI

---

## AP-06: Color Chaos

**Symptom**:
- Using matplotlib's default `tab10` palette with no semantic mapping
- Inconsistent colors across figures (the same method gets different colors in different figures)
- Using red vs. green to distinguish categories without considering colorblindness

**Fix**:
- Maintain a consistent color scheme across all figures: your method always has the same color
- Use colorblind-friendly palettes (avoid pure red paired with pure green)
- Assign semantic meaning to colors: warm = good, cool = poor; or fixed colors per method

---

## AP-07: The plt.title() Offense

**Symptom**: Using `plt.title()` to add a title inside the figure, wasting precious figure space and duplicating the LaTeX caption.

**Reviewer's reaction**: _"Obviously a screenshot from a Jupyter notebook"_

**Fix**:
- Never use `plt.title()`
- Place the title in the LaTeX `\caption{}`
- Inside the figure, only include panel labels ("(a)", "(b)") and data annotations

---

## AP-08: Missing Axis Labels

**Symptom**: No xlabel / ylabel, or labels that are vague ("value", "score", "performance").

**Fix**:
- Clearly specify the metric name and units: "Accuracy (%)", "Latency (ms)", "CNOT Count"
- If using a log scale, indicate "log scale"

---

## AP-09: The Overpowering Legend

**Symptom**: The legend is so large it obscures the data, or an identical legend is repeated in every panel.

**Fix**:
- Place the legend where it does not overlap with data (or outside the plot area)
- Use a single shared legend for multi-panel figures
- If method names are long, use abbreviations and explain them in the caption

---

## AP-10: Wasted Space

**Symptom**: The effective data area occupies only 30% of the canvas, with large blank regions. Or subplot spacing is excessive.

**Fix**:
- Use `plt.tight_layout()` or `layout='constrained'`
- Adjust `wspace` / `hspace`
- For data-dense content, use small multiples / facets to convey more information

---

## AP-11: Misuse of Log Scale

**Symptom**: Data spanning multiple orders of magnitude is plotted on a linear axis, compressing differences into invisibility. Or information that a log scale would reveal is hidden.

**Reviewer's reaction**: _"Did they even look at their own plot?"_

**Source**: Emergent Abilities used log y to reveal "zero is not zero"; Scaling Laws used log-log to reveal power laws

**Fix**:
- Spanning 2+ orders of magnitude --> log scale
- Power law relationships --> log-log
- Exponential decay/growth --> semi-log
- Performance concentrated at the high end (90-99%) --> consider log(1-acc) or log scale

---

## AP-12: Single-Panel Syndrome

**Symptom**: A figure has only one panel, even when a second panel would clearly strengthen the argument.

**Reviewer's reaction**: _"Why didn't they also show [the other dimension]?"_

**Source**: ResNet (train + test), Mamba (seq 2048 + 8192), DPO (frontier + robustness) all use dual panels

**Fix**:
- Showing train results --> add a test panel
- One dataset --> add at least one more dataset
- One sequence length --> add a different length
- Performance --> add an efficiency/cost panel

---

## AP-13: No Reference Lines / No Baselines

**Symptom**: The figure shows only your method and baselines, with no "ceiling" or "floor" reference.

**Source**: Nearly all top-venue papers include reference lines

**Fix**:
- Random chance / majority class baseline (lower bound)
- Human performance / theoretical bound (upper bound)
- Previous SOTA (horizontal dashed line)
- GPT-4 / classical limit (domain ceiling)

---

## AP-14: Caption Describes Instead of Concluding

**Symptom**: The caption reads "Figure 3 shows the accuracy of different methods on CIFAR-10"

**Reviewer's reaction**: _"I can see that. Tell me what I should conclude."_

**Source**: The first sentence of every NeurIPS Best Paper caption is a conclusion

**Fix**:
- Bad: "This figure shows training curves"
- Good: "Deeper residual networks achieve lower training error"
- Bad: "Results on 4 datasets"
- Good: "Our method achieves SOTA on all 4 datasets with 3x less compute"

---

## Quick Reference Table

| Issue | Poor Figure | Good Figure |
|-------|------------|-------------|
| Information density | 3 bars, done | Grouped bar + error bar + reference line + annotation |
| Comparison | Only shows own method | 6+ baselines with categorical grouping |
| Ablation | A single table | Waterfall chart showing cumulative contributions |
| Distribution | mean +/- std | Violin + strip + statistical test |
| Scaling | Linear axis, 3 points | Log-log + fit line + multiple configurations |
| Qualitative | One output image | Grid comparison + zoom-in + metric overlay |
| Training curves | One loss curve | Multi-panel + CI band + phase annotation |
| Trade-off | One scatter plot | Pareto frontier + configuration labels + dominated region |
