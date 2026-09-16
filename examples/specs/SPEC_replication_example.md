# SPEC — fig_replication (Supplementary): the setting-composition channel replicates on two sealed cohorts

Figure claim (one sentence): on both sealed cohorts (Dongling 107 sessions, Baihua 68 sessions) the label shift
produced by 25 % record reuse is carried by the setting composition — fresh shots reproduce it row by row,
composition matching removes it — and the witness increment ΔW follows the same pattern.

Role: robustness / replication figure (SI). Reading order: per-row evidence (a–d, two cohorts as two rows of
identical panels; identical shapes twice = replication) → endpoint quantity (e, smallest, last).

Data: only archived per-row columns (npz) and archived deltas (json). Operations used: subtraction of archived
columns, absolute value, L1 sum over the 15 archived composition features, quantile bins + binned median/IQR,
counts. No re-analysis.

Encoding (inherited from the paper): blue = record reuse (shared shots; disjoint shots drawn with light fill),
orange = intervention (composition-matched), INK greys = references and explanatory text. Marker shape by chip
(Dongling circle, Baihua square), ring = sealed cohort, marker area ∝ sqrt(sessions). Cloud parameters
s=3.2, alpha=0.30, rasterized. 180 mm wide, annotation text 5.2–6 pt, npjQI lowercase bold letters.

## Panel a (Dongling) / c (Baihua): paired cloud — ladder level 2 (per-row paired cloud)
1. Conclusion: re-drawing the 16 borrowed settings with entirely new shots gives the same per-row label shift
   (diagonal); matching their composition gives none (flat band at zero).
2. Compares: for each of the 1,595 (1,020) pair-rows, x = Δz under shared-shot reuse; y = Δz under
   disjoint-shot reuse (blue) and y = Δz under composition-matched reuse (orange).
3. Encoding: blue cloud on the identity line, orange cloud on the zero line; dotted identity and solid zero
   references; medians of |Δz_shared − Δz_disjoint| and |Δz_matched| printed (INK).
4. If wrong: blue cloud would be a round blob or a horizontal band (shots carry the shift, not settings);
   orange cloud would lie on the diagonal (matching does nothing).

## Panel b (Dongling) / d (Baihua): mechanism cloud — ladder level 3 (per-row effect vs explanatory variable)
1. Conclusion: the size of the label shift grows with how much the borrowed settings change the composition;
   at zero composition change (matched) the shift collapses.
2. Compares: x = ‖comp_shared − comp_clean‖₁ (15 archived features), y = |Δz_shared| per row (blue), with
   sextile-binned median + IQR band; orange rows at x = 0 (comp_matched − comp_clean is exactly 0 by
   construction), y = |Δz_matched|.
3. Encoding: rising binned-median line through the blue cloud; orange strip pinned at x = 0 near y = 0.
4. If wrong: flat binned median (shift independent of composition change); orange strip as tall as the blue
   cloud (matching leaves the shift).

## Panel e: endpoint ΔW — ladder level 5 (summary quantities, last and smallest)
1. Conclusion: both cohorts show ΔW rising with reuse fraction, unchanged by disjoint shots, and zero after
   matching; Baihua's shift is resolved from zero, Dongling's 0.25 interval touches zero.
2. Compares: ΔW (vs clean, ×10⁻³) with 95 % session-bootstrap intervals for shared f = 0.05/0.10/0.25,
   disjoint f = 0.25, matched f = 0.25 — two cohort groups.
3. Encoding: horizontal dot-and-interval rows, zero line, blue (shared), light-blue fill (disjoint), orange
   (matched); marker shape by chip, ring for sealed cohort.
4. If wrong: disjoint point far from shared point; matched interval overlapping the shared point instead of zero.

Ladder note: the object level (the 64-setting matrix itself) is not repeated here — per the case file the
main-text composition figure already draws the object for the main cohort; the SI replication only needs the
per-row clouds to show the same shapes on the sealed cohorts. The 15 composition features have no archived
semantic labels, so a raw feature-strip panel would be undecodable and was rejected.
