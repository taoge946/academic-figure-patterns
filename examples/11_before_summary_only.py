"""Pattern 11, the "before": the same synthetic data as example B, drawn as summary statistics only.

Three panels of means with 95 % intervals -- the form an author rejected as "too crude, I could
read the table" (AP-15).  Kept here as the counterpart of 11b_after.png.
"""
import numpy as np
import matplotlib.pyplot as plt
from afp.evidence import evidence_style, finish, BLUE_D, GREEN_D, INK, MM

rng = np.random.default_rng(3)
evidence_style()
COHORTS = [("cohort A", 1600), ("cohort B", 1600), ("cohort C", 1000)]
CONDS = ["condition 1", "condition 2", "control"]
fig, axes = plt.subplots(1, 3, figsize=(180 * MM, 55 * MM), sharey=True)
for ax, (name, n), scale in zip(axes, COHORTS, [1.0, 1.05, 1.35]):
    for ci, f in enumerate([1.0, 1.5, 0.18]):
        sP = rng.standard_t(4, n) * 0.040 * f * scale * 0.8 + (0.01 * f if f > .5 else 0)
        sQ = rng.normal(0, 0.013 * (f if f < .5 else 1.0) * scale, n)
        for x, s, c in [(ci - .12, sP, BLUE_D), (ci + .12, sQ, GREEN_D)]:
            m = np.mean(s ** 2) * 1e3; ci95 = 1.96 * np.std(s ** 2, ddof=1) / np.sqrt(n) * 1e3
            ax.errorbar(x, m, yerr=ci95, fmt="o", color=c, ms=4, lw=1, capsize=2)
    ax.set_xticks(range(3)); ax.set_xticklabels(CONDS, fontsize=7.5)
    ax.set_title(name, fontsize=8.5); finish(ax)
axes[0].set_ylabel(r"mean squared shift ($10^{-3}$)")
axes[0].legend(handles=[plt.Line2D([], [], marker="o", lw=0, color=BLUE_D, label="estimator P"),
                        plt.Line2D([], [], marker="o", lw=0, color=GREEN_D, label="estimator Q")], fontsize=7.5, loc="upper right")
fig.subplots_adjust(left=.08, right=.98, bottom=.16, top=.86, wspace=.12)
fig.savefig("examples/figures/11_before.png", dpi=220)
print("saved examples/figures/11_before.png")
