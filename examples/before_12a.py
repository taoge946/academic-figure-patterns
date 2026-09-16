"""12a: label shift vs learner shift for two defect types; decomposition and bias per cohort."""
import numpy as np
import matplotlib.pyplot as plt

d = np.load("examples/data/12a.npz")
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(10, 4))

for kind in ["reuse", "offset"]:
    ax1.scatter(d[f"label_shift_{kind}"], d[f"learner_shift_{kind}"], s=6, alpha=0.4, label=kind)
lim = [-0.4, 0.4]
ax1.plot(lim, lim, "k--", lw=0.8)
ax1.set_xlabel("label shift")
ax1.set_ylabel("learner shift")
ax1.set_title("Per-row shifts")
ax1.legend()

x = np.arange(4)
w = 0.35
for i, kind in enumerate(["reuse", "offset"]):
    off = (i - 0.5) * w
    ax2.bar(x + off, d[f"bar_intercept_{kind}"], w, label=f"{kind}: intercept")
    ax2.bar(x + off, d[f"bar_nonconstant_{kind}"], w, bottom=d[f"bar_intercept_{kind}"],
            yerr=d["bar_err"], capsize=2, alpha=0.6, label=f"{kind}: non-constant")
ax2.set_xticks(x)
ax2.set_xticklabels([f"cohort {k}" for k in range(4)])
ax2.set_title("Decomposition")
ax2.legend(fontsize=7)

for kind in ["reuse", "offset"]:
    ax3.errorbar(x, d[f"bias_{kind}"], yerr=d[f"bias_{kind}_err"], fmt="o", capsize=3, label=kind)
ax3.axhline(0, color="k", lw=0.8)
ax3.set_xticks(x)
ax3.set_xticklabels([f"cohort {k}" for k in range(4)])
ax3.set_ylabel("label bias")
ax3.set_title("Bias per cohort")
ax3.legend()

fig.tight_layout()
fig.savefig("examples/figures/12a_before.png", dpi=150)
