# SPEC — example 11a: does replacing part of a record change the per-sample values?

Figure claim (one sentence): replacing rows of the record changes the per-sample quantity in a way that is
reproduced when the replacement is redrawn with fresh samples (scheme B) and removed when the replacement preserves
the record's composition (scheme C); the pooled statistic grows with the dose.

Role: main-text figure. Reading order: the object (what a record and its replacements look like) → all samples
(paired cloud) → endpoint quantity (dose curve, smallest, last).

Data: `examples/data/11a.npz` only. Operations: subtraction of archived columns, pair counts, plotting. No fit,
no resampling.

Encoding (paper-wide table): blue = scheme A/B (the treatment), orange = scheme C (the control), ink greys for
references and explanatory text. Cloud parameters s = 3.4, alpha = 0.32, rasterized. 180 mm wide, text ≥ 7 pt,
APS panel letters "(a)".

## Panel a — the object (ladder level 1)
1. Conclusion: the three records differ only in the 16 replaced rows; scheme C keeps each row's category counts.
2. Compares: reference matrix vs replacement A vs replacement B, plus their pair-count grids.
3. Encoding: three 64 × 6 category matrices side by side, replaced rows tinted; a 3 × 3 pair-count grid under each.
4. If wrong: the replaced rows would look identical to the reference, or the pair counts of scheme C would differ
   from the reference as much as scheme A's do.

## Panel b — per-sample paired cloud (ladder level 2)
1. Conclusion: scheme B reproduces the per-sample shift of scheme A (diagonal); scheme C removes it (zero line).
2. Compares: for each of the 1,600 samples, x = shift under scheme A; y = shift under scheme B (blue) and under
   scheme C (orange).
3. Encoding: blue cloud on the identity line, orange cloud on the zero line; dashed identity and solid zero
   references; no printed numbers.
4. If wrong: the blue cloud would be a round blob or a horizontal band; the orange cloud would sit on the diagonal.

Load-bearing test before drawing: paired correlation of scheme A vs scheme B > 0.9 (`structure_strength`).

## Panel c — endpoint (ladder level 5, smallest and last)
1. Conclusion: the pooled statistic grows monotonically with the dose and is resolved from zero above the smallest doses.
2. Compares: pooled statistic at five doses, schemes A and B side by side, against the shaded resolution band.
3. Encoding: points with 95 % bars, symlog y so the small doses inside the band stay visible, log x.
4. If wrong: the points would sit inside the band at every dose, or the two schemes would separate.

Not drawn: nothing else; the pooled numbers themselves belong in a table.
