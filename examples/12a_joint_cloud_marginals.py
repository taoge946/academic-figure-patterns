"""Example 12a: joint per-sample cloud with contours and marginals, plus decomposition bars (synthetic).

Form of the author's reference "hardware" figure (npj-style lowercase letters):
(a) two defect types on the same rows: label shift (x) against learner shift (y); one follows the
    diagonal row by row, the other is a constant offset that a learner absorbs in its intercept.
    Contours at 25 % and 60 % of the peak density, marginal densities on top and right,
    reference lines y = x and y = 0, short annotations with the key numbers.
(b) per-cohort decomposition bars: solid = intercept part, hatched = non-constant part, with
    the label bias plotted below on its own axis.
(c) contour small multiples for further cohorts (same axes, no points).
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from afp.evidence import (evidence_style, finish, letter, note, BLUE, BLUE_D, BLUE_L, ORANGE, ORANGE_D, INK, INK2, INK3, GRID, MM)

rng = np.random.default_rng(21)
evidence_style()


def blur_hist2d(x, y, lim, bins=60, sigma=1.6):
    H, xe, ye = np.histogram2d(x, y, bins=bins, range=[lim, lim])
    k = np.arange(-4, 5); g = np.exp(-k ** 2 / (2 * sigma ** 2)); g /= g.sum()
    H = np.apply_along_axis(lambda r: np.convolve(r, g, mode="same"), 0, H)
    H = np.apply_along_axis(lambda r: np.convolve(r, g, mode="same"), 1, H)
    xc = (xe[:-1] + xe[1:]) / 2; yc = (ye[:-1] + ye[1:]) / 2
    return xc, yc, H.T


def density1d(v, lim, bins=80, sigma=2.0):
    h, e = np.histogram(v, bins=bins, range=lim, density=True)
    k = np.arange(-6, 7); g = np.exp(-k ** 2 / (2 * sigma ** 2)); g /= g.sum()
    return (e[:-1] + e[1:]) / 2, np.convolve(h, g, mode="same")


def cohort(n, kind, seed):
    r = np.random.default_rng(seed)
    if kind == "reuse":                       # learner follows each row
        lab = r.normal(0.02, 0.09, n); lea = lab * 0.85 + r.normal(0, 0.035, n)
    else:                                     # constant offset, absorbed by the intercept
        lab = r.normal(-0.07, 0.045, n); lea = np.full(n, -0.06) + r.normal(0, 0.012, n)
    return lab, lea


lim = (-.32, .32)
fig = plt.figure(figsize=(180 * MM, 100 * MM))
# ---------- (a) joint cloud ----------
ax = fig.add_axes([.095, .12, .38, .70]); axt = fig.add_axes([.095, .83, .38, .10]); axr = fig.add_axes([.48, .12, .06, .70])
for kind, c, cd, z in [("reuse", BLUE, BLUE_D, 2), ("offset", ORANGE, ORANGE_D, 3)]:
    lab, lea = cohort(1600, kind, 1 if kind == "reuse" else 2)
    ax.scatter(lab, lea, s=3.4, c=c, alpha=.28, linewidths=0, rasterized=True, zorder=z)
    xc, yc, H = blur_hist2d(lab, lea, lim)
    ax.contour(xc, yc, H, levels=[.25 * H.max(), .60 * H.max()], colors=[cd], linewidths=1.1, zorder=5)
    xs, d = density1d(lab, lim); axt.fill_between(xs, 0, d, color=c, alpha=.35, lw=0); axt.plot(xs, d, color=cd, lw=.9)
    ys, d = density1d(lea, lim); axr.fill_betweenx(ys, 0, d, color=c, alpha=.35, lw=0); axr.plot(d, ys, color=cd, lw=.9)
ax.plot(lim, lim, color=INK, lw=.8, ls=(0, (3, 2)), zorder=6); ax.axhline(0, color=INK3, lw=.6); ax.axvline(0, color=INK3, lw=.6)
ax.set_xlim(*lim); ax.set_ylim(*lim); ax.set_xticks([-.3, -.15, 0, .15, .3]); ax.set_yticks([-.3, -.15, 0, .15, .3])
ax.set_xlabel("label shift per row,  $Y_{\\rm defect}-Y_{\\rm clean}$", labelpad=2)
ax.set_ylabel("learner shift per row,  $f_{\\rm defect}-f_{\\rm clean}$", labelpad=2)
note(ax, -.30, .29, "record reuse", size=9, color=BLUE_D, fontweight="bold")
note(ax, -.30, .245, "learner follows each row", size=7.5, color=BLUE_D)
note(ax, .30, -.24, "readout offset", size=9, color=ORANGE_D, fontweight="bold", ha="right")
note(ax, .30, -.285, "one constant, absorbed by the intercept", size=7.5, color=ORANGE_D, ha="right")
note(ax, .235, .29, "$y=x$", size=7.5, ha="right", va="bottom")
note(ax, .30, -.31, "1,600 rows;  contours at 25 % and 60 % of peak", size=7, color=INK2, ha="right", va="bottom")
finish(ax)
for a in (axt, axr):
    a.set_xticks([]); a.set_yticks([]); [s.set_visible(False) for s in a.spines.values()]
axt.set_xlim(*lim); axr.set_ylim(*lim)
note(axt, .31, axt.get_ylim()[1] * .9, "label shift", size=7.5, ha="right", va="top", color=INK2)
note(axr, axr.get_xlim()[1] * .95, .31, "learner shift", size=7.5, ha="right", va="top", color=INK2, rotation=-90)

# ---------- (b) decomposition bars + bias below ----------
names = ["cohort A", "cohort B", "cohort C", "cohort D"]
inter_b = np.array([.0004, .0003, .0006, .0004]); nonc_b = np.array([.0080, .0092, .0125, .0130])
inter_o = np.array([.0062, .0075, .0048, .0028]); nonc_o = np.array([.0010, .0012, .0009, .0007])
err = np.array([.0022, .0018, .0035, .0026])
axb = fig.add_axes([.62, .50, .36, .40]); xb = np.arange(4)
axb.bar(xb - .18, inter_b, .32, color=BLUE_D, lw=0); axb.bar(xb - .18, nonc_b, .32, bottom=inter_b, facecolor="white", edgecolor=BLUE_D, hatch="////", lw=.8)
axb.bar(xb + .18, inter_o, .32, color=ORANGE, lw=0); axb.bar(xb + .18, nonc_o, .32, bottom=inter_o, facecolor="white", edgecolor=ORANGE_D, hatch="////", lw=.8)
axb.errorbar(xb - .18, inter_b + nonc_b, yerr=err, fmt="none", ecolor=INK2, lw=.8, capsize=0)
axb.errorbar(xb + .18, inter_o + nonc_o, yerr=err * .6, fmt="none", ecolor=INK2, lw=.8, capsize=0)
axb.set_xticks(xb); axb.set_xticklabels([]); axb.set_ylabel(r"$\Delta W$", labelpad=2); axb.set_ylim(0, .02)
axb.legend(handles=[Patch(facecolor=INK2, label="intercept part"), Patch(facecolor="white", edgecolor=INK2, hatch="////", label="non-constant part")],
           loc="upper left", fontsize=7, handlelength=1.4, borderaxespad=.2)
finish(axb)
axc = fig.add_axes([.62, .30, .36, .17])
axc.axhline(0, color=INK3, lw=.6)
axc.errorbar(xb - .18, [.002, .001, -.02, .003], yerr=[.008, .006, .012, .01], fmt="o", color=BLUE_D, ms=3.5, lw=.9)
axc.errorbar(xb + .18, [-.085, -.088, -.072, -.054], yerr=[.006, .005, .012, .01], fmt="s", color=ORANGE_D, ms=3.5, lw=.9)
axc.set_xticks(xb); axc.set_xticklabels(names, fontsize=7.5); axc.set_ylim(-.13, .03)
axc.set_ylabel(r"$\mathbb{E}[Y_{\rm defect}-Y_C]$", labelpad=2, fontsize=7.5)
finish(axc)

# ---------- (c) contour small multiples ----------
for k in range(4):
    a = fig.add_axes([.62 + k * .095, .06, .078, .16])
    for kind, cd in [("reuse", BLUE_D), ("offset", ORANGE_D)]:
        lab, lea = cohort(900, kind, 10 + k + (0 if kind == "reuse" else 50))
        sc = [1.0, .6, .8, 1.1][k]
        xc, yc, H = blur_hist2d(lab * sc, lea * sc, lim, bins=40, sigma=1.4)
        a.contour(xc, yc, H, levels=[.25 * H.max(), .60 * H.max()], colors=[cd], linewidths=.9)
    a.plot(lim, lim, color=INK, lw=.5, ls=(0, (3, 2))); a.axhline(0, color=INK3, lw=.4); a.axvline(0, color=INK3, lw=.4)
    a.set_xlim(*lim); a.set_ylim(*lim); a.set_xticks([-.3, 0, .3]); a.set_yticks([-.3, 0, .3])
    a.set_xticklabels(["", "0", ""], fontsize=6); a.set_yticklabels(["−0.3", "0", "0.3"] if k == 0 else [], fontsize=6)
    note(a, -.29, .28, names[k], size=6.5, va="top"); finish(a)
letter(fig, ax, "a", dx=-.055, dy=.11, style="bold"); letter(fig, axb, "b", dx=-.06, style="bold"); letter(fig, fig.axes[-4], "c", dx=-.06, style="bold")
fig.savefig("examples/figures/12a_after.png", dpi=220); fig.savefig("examples/figures/12a_after.pdf")
print("saved examples/figures/12a_after.{png,pdf}")
