"""Pattern 11, example C: per-sample effect against an explanatory variable (synthetic data).

Form of an author-accepted "boundary" figure: (a) one cloud of per-state risk ratio against a
mechanism variable the reader can name (number of filled cells), three system sizes drawn with
different marker shapes but the same color, all falling on one curve that crosses zero near a
boundary; binned medians with an IQR band mark the crossing.  (b) the control condition,
compressed to a narrow strip because it says "nothing happens".  (c) endpoint per size, last
and smallest.  The mean-lines-only version of the same data was rejected as "too crude".
"""
import numpy as np
import matplotlib.pyplot as plt
from afp.evidence import (evidence_style, finish, letter, note, paired_cloud, binned_median, structure_strength,
                          BLUE, BLUE_D, ORANGE, INK, INK2, INK3, GRID, MM)

rng = np.random.default_rng(11)
evidence_style()
SIZES = [(6, "o", 900), (12, "D", 900), (24, "s", 900)]
BOUNDARY = 12.0

cells, ratio, size_id = [], [], []
for k, (M, mk, n) in enumerate(SIZES):
    c = rng.integers(2, 30, n) + rng.uniform(-.4, .4, n)
    r = 0.12 * np.log(c / BOUNDARY) + rng.normal(0, 0.09, n)
    cells.append(c); ratio.append(r); size_id.append(np.full(n, k))
cells = np.concatenate(cells); ratio = np.concatenate(ratio); size_id = np.concatenate(size_id)
print(structure_strength(cells, ratio, "mechanism"))
control = rng.normal(0, 0.03, len(cells))

fig = plt.figure(figsize=(180 * MM, 82 * MM))
# (a) mechanism cloud
axa = fig.add_axes([.07, .17, .50, .73])
for k, (M, mk, n) in enumerate(SIZES):
    s = size_id == k
    axa.scatter(cells[s], ratio[s], s=7 if mk != "o" else 6, marker=mk, c=BLUE, alpha=.30, linewidths=0, rasterized=True, zorder=3)
axa.axhline(0, color=INK, lw=.6, zorder=2)
axa.axvline(BOUNDARY, color=INK3, lw=.6, ls=(0, (2, 2)), zorder=2)
xc, med = binned_median(axa, cells, ratio, nbins=14, color=BLUE_D)
axa.set_xlim(1, 31); axa.set_ylim(-.45, .45)
axa.set_xlabel("explanatory variable", labelpad=2)
axa.set_ylabel("effect", labelpad=2)
note(axa, 1.8, .40, "markers: three system sizes", size=7.5)
finish(axa)
# (b) control strip, compressed
axb = fig.add_axes([.62, .17, .10, .73])
axb.scatter(np.full(len(control), 0) + rng.uniform(-.3, .3, len(control)), control, s=4, c=ORANGE, alpha=.25, linewidths=0, rasterized=True)
axb.axhline(0, color=INK, lw=.6); axb.set_ylim(-.45, .45); axb.set_xlim(-.6, .6)
axb.set_xticks([0]); axb.set_xticklabels([""]); axb.set_yticks([])
axb.spines["left"].set_visible(False); finish(axb)
note(axb, 0, .40, "control", ha="center", size=7.5, color=INK2)
# (c) endpoint per size, smallest and last
axc = fig.add_axes([.79, .17, .19, .73])
for k, (M, mk, n) in enumerate(SIZES):
    s = size_id == k
    above = ratio[s][cells[s] > BOUNDARY]; below = ratio[s][cells[s] <= BOUNDARY]
    for x, v, mfc in [(k - .15, below, "white"), (k + .15, above, BLUE_D)]:
        m = v.mean(); ci = 1.96 * v.std(ddof=1) / np.sqrt(len(v))
        axc.plot([x, x], [m - ci, m + ci], color=BLUE_D, lw=1.1)
        axc.plot([x], [m], marker=mk, ms=4.5, mfc=mfc, mec=BLUE_D, mew=.8, lw=0)
axc.axhline(0, color=INK, lw=.6)
axc.set_xticks(range(3)); axc.set_xticklabels(["small", "medium", "large"], fontsize=7.5)
axc.set_ylim(-.25, .25); axc.set_xlim(-.6, 2.6)
axc.set_ylabel("mean effect", labelpad=2)
note(axc, -.5, .22, "open: below boundary   filled: above", size=7, color=INK2)
finish(axc)
letter(fig, axa, "a", dx=-.055); letter(fig, axb, "b", dx=-.05); letter(fig, axc, "c", dx=-.06)
np.savez("examples/data/11c.npz", explanatory_x=cells, effect=ratio, size_index=size_id, sizes=np.array([6, 12, 24]),
         control_effect=control)
fig.savefig("examples/figures/11c_after.png", dpi=220); fig.savefig("examples/figures/11c_after.pdf")
print("saved examples/figures/11c_after.{png,pdf}")
