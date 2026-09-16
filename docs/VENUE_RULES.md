# Venue Rules That Change the Figure (Not Just the Style)

Content rules ([SPEC_FIRST.md](SPEC_FIRST.md), [FORM_LADDER.md](FORM_LADDER.md)) hold everywhere. The items
below are venue-specific and several of them contradict each other, so check them before drawing.

## APS journals (PRX Quantum, PRL, PRX, PRA…)

Checked against the APS author guidelines and a local corpus of ~380 PRX Quantum papers (Sep 2026).

- **No AI-generated images** anywhere in the figure.
- Double-column width 180 mm; single column ~86 mm. Draw at final size; do not scale down later.
- Panel letters in parentheses, **(a) (b) (c)**, bold, upper-left.
- Smallest letter height ≥ ~2 mm at final size (≥ 7.5 pt in practice); line width ≥ 0.5 pt.
- Vector PDF for line art; rasterize only dense point clouds (`rasterized=True`), keep axes and text vector.
- **Caption describes what is drawn and defines the quantities; findings go to the main text.** This is the
  opposite of the ML convention below. Author's rule for this venue: "the caption says what the figure is;
  what it shows belongs in the text." Keep captions short (Fig. 2 above: eight lines for four panels).
- Common PRX Quantum forms seen in the corpus: overlaid histograms of one quantity under two conditions with a
  prediction dashed line; 2-D parameter-grid heat maps of a *measured* quantity (not of binned summaries);
  model-vs-measurement points with a small embedded table; sequence plots with a train/test divider; box plots
  grouped by size with an upper-bound line.
- A tall composite (180 × 205 mm) overflows the text height once the caption is added; use `0.93\textwidth`
  or trim the figure. `Float too large for page by 38 pt` is the symptom.

## Nature-family and npj journals

- Panel letters lowercase bold **a b c**, no parentheses.
- Single column 88 mm, double 180 mm; text 5–7 pt is common in the corpus.
- Caption first sentence may state the finding.

## ML venues (NeurIPS, ICML, ICLR)

- Caption's first sentence = the takeaway (see AP-14). "Ours" in the prominent color, baselines muted.
- Figure 1 is an elevator pitch; annotations like "8.2× faster" and "baseline OOM" bands are expected.
- Twin y-axes are tolerated in hero figures (runtime + memory); they are banned in the physics workflow above.
- Example accepted at ICML 2026 (LoRe): `examples/gallery/lore_scaling_hero.png` — two log-scale runtime/memory
  panels with the OOM region shaded and gap arrows, plus a speedup-vs-size panel with a 1× reference line.

## Systems venues (ASPLOS, MICRO, HPCA)

Calibrated on one MICRO 2026 paper reviewed by the same author as the physics cases.

- Heavy lines (`lw≈5`), large markers, filled bands between curves, Times New Roman at 22–29 pt in the source
  figure (the figure is shrunk to column width, so the effective size is normal).
- Twin y-axes accepted. A "scalability wall" shaded region is a common device.
- Rejected there as well: plain bars, radar charts, heat maps, box plots as main panels.

## Two rules that flip between venues

| Rule | APS physics | ML / systems |
|---|---|---|
| Caption content | what is drawn + definitions | conclusion first |
| Twin y-axis | banned | accepted in hero figures |

Everything else in this repository applies unchanged.
