# Pattern 06: Qualitative Comparison Figure

## Purpose
Visually demonstrate the output quality of your method -- images, structures, circuits, solutions, etc.

## Claim Types
- "Our method produces visually better / more accurate / cleaner results"
- "Our generated structures have better properties"

## Top-Venue Standard Structures

### Structure A: Grid Comparison (Most Common)
```
              Input    Method A   Method B   Ours     GT/Ref
Example 1     ■         ■          ■         ■★        ■
Example 2     ■         ■          ■         ■★        ■
Example 3     ■         ■          ■         ■★        ■
(easy)       (hard)   (failure)
```

**Key rules**:
- Rows = samples (arranged from easy to hard)
- Columns = methods (your method in the second-to-last column, GT last)
- Must include easy cases (all methods succeed) + hard cases (you win) + failure cases (you also fail)
- Label each cell with a quantitative metric below (PSNR / SSIM / distance, etc.)

### Structure B: Zoom-in Comparison (Required When Differences Are Subtle)
```
┌────────────────────────────────┐
│  Overview image                 │
│    ┌──┐  ┌──┐                  │
│    │R1│  │R2│  ← red/blue box  │
│    └──┘  └──┘                  │
├────────┬────────┬──────────────┤
│ R1 zoom │ R1 zoom │ R1 zoom     │
│ Method A│ Ours   │ GT           │
├────────┼────────┼──────────────┤
│ R2 zoom │ R2 zoom │ R2 zoom     │
│ Method A│ Ours   │ GT           │
└────────┴────────┴──────────────┘
```

**Code pattern**:
```python
from matplotlib.patches import Rectangle, ConnectionPatch

# Draw bounding box on the main image
rect = Rectangle((x, y), w, h, linewidth=2, edgecolor='red', facecolor='none')
ax_main.add_patch(rect)

# Display the cropped region in a zoom subplot
ax_zoom.imshow(img[y:y+h, x:x+w])
ax_zoom.set_title('Method A', fontsize=8)

# Connect the main-image box to the zoom subplot
con = ConnectionPatch(xyA=(x+w, y+h/2), coordsA=ax_main.transData,
                      xyB=(0, 0.5), coordsB=ax_zoom.transAxes,
                      arrowstyle='-', color='red', lw=1)
fig.add_artist(con)
```

### Structure C: Difference Highlighting (Image Restoration / Generation)
```
Overlay semi-transparent red on error regions in baseline outputs
Overlay semi-transparent green on correct regions in your outputs
Or use arrows + text to point out specific differences
```

### Structure D: Qualitative with Statistics (Most Persuasive)
```
┌────────────────────────────────────────────┐
│ (a) Qualitative comparison grid             │
│     (3 examples x 4 methods)               │
├────────────────────┬───────────────────────┤
│ (b) Per-sample      │ (c) Distribution      │
│ quantitative        │ comparison            │
│ bar chart           │ violin / box plot     │
│ (one per example)   │ (full test set)       │
└────────────────────┴───────────────────────┘
Bridge qualitative and quantitative: the top panel lets readers
"see" the difference; the bottom statistics prove it generalizes.
```

## Required Elements

1. **Ground truth / reference**: Without a reference, quality cannot be judged
2. **At least 3 samples**: Including easy + hard + failure cases
3. **Quantitative annotations**: Numbers below each cell (reviewers do not trust "looks better")
4. **Difference guidance**: Arrows / boxes / highlights that tell readers where to look
5. **Zoom-in**: Required whenever differences are small

## For Non-Image Domains (Quantum Circuits / Graphs / Molecules / Scheduling, etc.)

The same principles apply:
```
- Quantum circuits: Compare circuit depth and CNOT count; highlight optimized sections in different colors
- Graph structures: Show side by side; annotate key differing nodes/edges
- Scheduling plans: Gantt charts side by side; annotate makespan differences
- Molecular structures: 3D renderings side by side; annotate bond length/angle differences
```

## Anti-Patterns

- Do not show only your method's output without baseline comparison
- Do not select only the best samples for your method (cherry-picking)
- Do not omit zoom-in views when differences are small
- Do not omit GT / reference
- Do not show qualitative results without accompanying quantitative numbers
- Do not use examples of uniform difficulty (all easy cases)
