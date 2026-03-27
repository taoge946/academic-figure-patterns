# Pattern 01: Hero Figure (Figure 1)

## Purpose
The "elevator pitch" of the paper -- enables reviewers to grasp the contribution within 30 seconds.

## Claim Type
"We propose a new method that is better / faster / simpler than existing approaches on problem X"

## Top-Venue Standard Structures

### Structure A: Three-Panel Layout (Most Common)
```
+---------------+----------------+--------------+
|  (a) Problem  | (b) Method     | (c) Result   |
|  Pain point / |  Core pipeline |  One stand-  |
|  failure of   |  of your       |  out result  |
|  prior work   |  approach      |  number      |
+---------------+----------------+--------------+
```
- **(a) Left**: Convey the intuition behind the problem -- why existing methods fail (schematic diagram)
- **(b) Center**: Core pipeline of your method (not the full architecture, but the key insight)
- **(c) Right**: A "killer" result (a small plot + key number) to hook the reader

**Typical example**: ViT Figure 1 = image patches -> transformer -> accuracy beats CNN

### Structure B: Side-by-Side Comparison
```
+------------------------+------------------------+
|  (a) Existing Method   |  (b) Our Method        |
|  X  Slow/poor/complex  |  OK  Fast/good/simple  |
|  [concrete visual]     |  [concrete visual]     |
|  "3.2 hours"           |  "12 minutes"          |
+------------------------+------------------------+
```

### Structure C: Panoramic Result (For Experimentally-Driven Papers)
```
+----------------------------------------------+
|  (a) Method schematic (small, top corner)    |
|  +--------------------------------------+    |
|  |  (b) Main result: scatter/Pareto/bar |    |
|  |  Your method: large marker           |    |
|  |  Baselines: small markers            |    |
|  |  Key gap annotated with arrow + text |    |
|  +--------------------------------------+    |
+----------------------------------------------+
```

## Required Elements

1. **Visual comparison**: Do not show only your method -- a reference point for comparison is mandatory
2. **Key numbers**: At least one impressive quantitative result displayed directly on the figure
3. **Semantic color coding**: Your method uses a prominent color (red/orange); baselines use muted colors (gray/blue) -- maintain consistency throughout the entire paper
4. **Minimal text**: The figure should be understandable without reading the main text
5. **Annotations / arrows**: Highlight where the key differences lie -- do not force reviewers to find them

## Common Pitfalls

- Do not draw a generic block diagram with no results
- Do not include an overly detailed method pipeline (save that for the Method section)
- Do not produce a purely conceptual figure with no numbers or data
- Do not use more than 4 colors without semantic association
- Do not create a figure that requires reading the full text to understand

## Implementation Strategy

Hero Figures are typically **hybrid figures** -- part schematic (hand-drawn / TikZ / AI-generated), part data plot.
Focus on the data portion; for the schematic portion, consider:
- Drawing simple diagrams with matplotlib patches/annotations
- Assembling the final figure with `subplot_mosaic`

```python
fig, axd = plt.subplot_mosaic(
    [["method", "result_main"],
     ["method", "result_sub"]],
    figsize=(TEXTWIDTH, TEXTWIDTH*0.45),
    width_ratios=[1.2, 1],
    gridspec_kw={"hspace": 0.15, "wspace": 0.25})
```
