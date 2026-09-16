"""Pattern 11, example D: error-vs-error cloud grid + ECDF row (synthetic data).

Form of an author-accepted "budget" figure: (a) a grid of log-log clouds, one per cohort (rows)
and budget K (columns), each point one sample with learner error against baseline error; the
percentage of points below the diagonal is printed and falls with K -- the whole argument is
the drift of the clouds across the diagonal.  (b) ECDFs of squared error per cohort for the
baseline, the clean learner, the learner damaged by reuse and the repaired learner; higher
curves have more samples below a given error.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from afp.evidence import (evidence_style, finish, letter, note, ecdf, fraction_below_diagonal,
                          BLUE, BLUE_D, GREEN_D, GREY_D, INK, INK2, GRID, MM)

rng = np.random.default_rng(5)
evidence_style()
COHORTS = [("cohort A", 1600, 1.0), ("cohort B", 1600, 1.1), ("cohort C", 1000, 1.4)]
KS = [8, 32, 128, 1024]

fig = plt.figure(figsize=(180 * MM, 135 * MM))
x0s = [.09, .315, .54, .765]; w = .21; y0s = [.78, .615, .45]; h = .15
for j, (name, n, sc) in enumerate(COHORTS):
    for ci, K in enumerate(KS):
        base = np.abs(rng.normal(0, .8 / np.sqrt(K), n) * sc) + 1e-3          # baseline error shrinks with K
        learn = np.abs(rng.normal(0, .045 * sc, n)) * (1 + .3 * rng.standard_t(5, n) ** 2 / 10) + 1e-3
        ax = fig.add_axes([x0s[ci], y0s[j], w, h])
        ax.fill_between([1e-3, 1], [1e-3, 1], [1, 1], color="#f4f3f0", lw=0, zorder=0)
        ax.scatter(base, learn, s=3.2, c=BLUE, alpha=.30, linewidths=0, rasterized=True, zorder=3)
        ax.plot([1e-3, 1], [1e-3, 1], color=INK, lw=.8, zorder=4)
        ax.set_xscale("log"); ax.set_yscale("log"); ax.set_xlim(2e-3, .6); ax.set_ylim(2e-3, .6)
        ax.set_xticks([.01, .1]); ax.set_xticklabels(["0.01", "0.1"] if j == 2 else [])
        ax.set_yticks([.01, .1]); ax.set_yticklabels(["0.01", "0.1"] if ci == 0 else [])
        note(ax, .5, 3e-3, f"{100 * fraction_below_diagonal(base, learn):.0f} %", ha="right", va="bottom", size=8)
        finish(ax)
        if j == 0:
            ax.set_title(f"$K={K}$", pad=3, fontsize=8.5)
        if ci == 0:
            note(ax, 2.4e-3, .5, name, va="top", size=7.5)
fig.text(.5, .385, "baseline error per row", ha="center", fontsize=9)
fig.text(.03, .69, "learner error per row", rotation=90, va="center", fontsize=9)
note(fig.axes[3], .5, .4, "shaded: learner worse", ha="right", va="top", size=7, color=INK2)

# (b) ECDF row
yb, hb = .10, .17
for j, (name, n, sc) in enumerate(COHORTS):
    ax = fig.add_axes([.09 + j * .31, yb, .27, hb])
    base = rng.normal(0, .06 * sc, n) ** 2
    clean = rng.normal(0, .045 * sc, n) ** 2
    reused = rng.normal(0, .055 * sc, n) ** 2
    repaired = rng.normal(0, .046 * sc, n) ** 2
    ecdf(ax, base, GREY_D, ls=(0, (2, 1.5)), lw=1.0)
    ecdf(ax, clean, INK, lw=1.3)
    ecdf(ax, reused, BLUE, lw=1.2)
    ecdf(ax, repaired, GREEN_D, lw=1.2)
    ax.set_xscale("log"); ax.set_xlim(1e-5, .1); ax.set_yticks([0, .5, 1])
    ax.set_xticks([1e-4, 1e-3, 1e-2, 1e-1]); ax.set_xticklabels(["$10^{-4}$", "$10^{-3}$", "$10^{-2}$", "$10^{-1}$"], fontsize=7.5)
    if j > 0:
        ax.set_yticklabels([])
    finish(ax)
    note(ax, 1.3e-5, .93, f"{name},  $n={n:,}$", size=7.5, va="top")
fig.axes[-3].set_ylabel("fraction of rows", labelpad=2)
fig.axes[-2].set_xlabel("squared error per row", labelpad=2)
fig.legend(handles=[Line2D([], [], color=GREY_D, ls=(0, (2, 1.5)), label="baseline"), Line2D([], [], color=INK, lw=1.3, label="clean learner"),
                    Line2D([], [], color=BLUE, label="reused learner"), Line2D([], [], color=GREEN_D, label="repaired")],
           loc="lower right", bbox_to_anchor=(.985, .285), ncol=4, fontsize=7.5, handlelength=1.6, columnspacing=1.0, borderaxespad=0)
fig.text(.03, .955, "(a)", fontsize=11, fontweight="bold", color=INK)
fig.text(.03, .29, "(b)", fontsize=11, fontweight="bold", color=INK)
fig.savefig("examples/figures/11d_after.png", dpi=220); fig.savefig("examples/figures/11d_after.pdf")
print("saved examples/figures/11d_after.{png,pdf}")
