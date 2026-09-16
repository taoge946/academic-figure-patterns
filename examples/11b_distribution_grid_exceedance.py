"""Pattern 11, example B: distribution grid + exceedance column (synthetic data).

Form of an author-accepted "input representation" figure: rows = cohorts, columns = three
conditions, each cell two peak-normalized per-sample distributions of a learner's shift
(estimator P wide, estimator Q narrow; both collapse under the control condition), with the
mean squared shift printed; a fourth column shows on clean data the fraction of samples whose
error exceeds x (log y), where Q has fewer large errors.  Pooled statistics live in a table.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from afp.evidence import (evidence_style, finish, letter, note, peak_normalized_hist, exceedance_curve,
                          BLUE, BLUE_D, GREEN, GREEN_D, GREY_D, INK, INK2, GRID, MM)

rng = np.random.default_rng(3)
evidence_style()
COHORTS = [("cohort A, development", 1600), ("cohort B, sealed", 1600), ("cohort C, sealed", 1000)]
CONDS = [("condition 1", 1.0), ("condition 2", 1.5), ("control (matched)", 0.18)]
sd_P, sd_Q = 0.040, 0.013

fig = plt.figure(figsize=(180 * MM, 98 * MM))
x0s = [.05, .315, .565, .80]; w = [.245, .23, .15, .185]; y0s = [.625, .36, .095]; h = .235
edges = np.arange(-0.24, 0.2401, 0.008)
axes = {}
for j, (name, n) in enumerate(COHORTS):
    scale = [1.0, 1.05, 1.35][j]
    for ci, (cname, f) in enumerate(CONDS):
        ax = fig.add_axes([x0s[ci], y0s[j], w[ci], h]); axes[(ci, j)] = ax
        sP = rng.standard_t(4, n) * sd_P * f * scale * 0.8 + (0.01 * f if f > .5 else 0)
        sQ = rng.normal(0, sd_Q * (f if f < .5 else 1.0) * scale, n)
        peak_normalized_hist(ax, sP, edges, BLUE, edge_color=BLUE_D)
        peak_normalized_hist(ax, sQ, edges, GREEN, edge_color=GREEN_D)
        ax.axvline(0, color=INK, lw=.6, zorder=1)
        ax.set_xlim(edges[0], edges[-1])
        ax.set_xticks([-.2, -.1, 0, .1, .2]); ax.set_xticklabels(["−0.2", "−0.1", "0", "0.1", "0.2"] if j == 2 else [])
        finish(ax)
        note(ax, edges[-1] - .004, .80, f"{np.mean(sP ** 2) * 1e3:.2f}", ha="right", size=8.5, color=BLUE_D)
        note(ax, edges[-1] - .004, .50, f"{np.mean(sQ ** 2) * 1e3:.2f}", ha="right", size=8.5, color=GREEN_D)
        if ci == 0:
            note(ax, edges[0], 1.27, f"{name}  ·  {n:,} rows", va="top", size=8, color=INK)
        if j == 0:
            ax.set_title(cname, pad=5, fontsize=9)
axes[(1, 2)].set_xlabel(r"learner shift per row,  $\delta f = f_{\rm cond} - f_{\rm clean}$", labelpad=2)
note(axes[(0, 0)], edges[-1] - .004, .90, r"$\langle\delta f^2\rangle$  ($10^{-3}$)", ha="right", va="bottom", size=8, color=INK2)

# (d) exceedance of the clean residual
xs = np.linspace(0, 0.3, 301)
for j, (name, n) in enumerate(COHORTS):
    ax = fig.add_axes([x0s[3], y0s[j], w[3], h]); axes[(3, j)] = ax
    rP = np.abs(rng.standard_t(3, n) * 0.035 * [1, 1, 1.3][j])
    rQ = np.abs(rng.normal(0, 0.045, n))
    rM = np.abs(rng.standard_t(3, n) * 0.048 * [1, 1, 1.3][j])
    exceedance_curve(ax, rM, GREY_D, xs=xs, lw=.9, ls=(0, (2, 1.5)))
    exceedance_curve(ax, rP, BLUE_D, xs=xs)
    exceedance_curve(ax, rQ, GREEN_D, xs=xs)
    ax.set_yscale("log"); ax.set_ylim(1e-3, 1); ax.set_xlim(0, .3)
    ax.set_yticks([1, .1, .01, .001]); ax.set_yticklabels(["1", "0.1", "0.01", "0.001"], fontsize=7.5)
    ax.set_xticks([0, .1, .2, .3]); ax.set_xticklabels(["0", "0.1", "0.2", "0.3"] if j == 2 else [])
    ax.axvline(.1, color=GRID, lw=.6, zorder=1)
    finish(ax)
    note(ax, .295, .55, f"{(rP > .1).mean():.3f}", ha="right", size=8.5, color=BLUE_D)
    note(ax, .295, .22, f"{(rQ > .1).mean():.3f}", ha="right", size=8.5, color=GREEN_D)
    if j == 0:
        ax.set_title("clean data", pad=5, fontsize=9)
        note(ax, .295, .085, "rows above 0.1", ha="right", size=7.5, color=INK2)
axes[(3, 1)].set_ylabel("fraction of rows above", labelpad=2)
axes[(3, 2)].set_xlabel(r"clean residual  $|f_{\rm clean}-Y|$", labelpad=2)

fig.legend(handles=[Line2D([], [], color=BLUE_D, lw=6, alpha=.45, label="estimator P"),
                    Line2D([], [], color=GREEN_D, lw=6, alpha=.45, label="estimator Q"),
                    Line2D([], [], color=GREY_D, lw=.9, ls=(0, (2, 1.5)), label="training mean, (d)")],
           loc="upper right", bbox_to_anchor=(.985, .998), ncol=3, fontsize=8, handlelength=1.4, handletextpad=.4, columnspacing=1.0, borderaxespad=0)
for ci, ch in enumerate("abcd"):
    fig.text(x0s[ci] - .04, .905, f"({ch})", fontsize=11, fontweight="bold", va="bottom", color=INK)
fig.savefig("examples/figures/11b_after.png", dpi=220); fig.savefig("examples/figures/11b_after.pdf")
print("saved examples/figures/11b_after.{png,pdf}")
