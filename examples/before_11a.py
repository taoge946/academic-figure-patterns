import numpy as np
import matplotlib.pyplot as plt

d = np.load("examples/data/11a.npz")

fig, axes = plt.subplots(1, 2, figsize=(10, 4))

# Left: histograms of per-sample shift under the three replacement schemes
ax = axes[0]
for key, label in [("shift_schemeA", "Scheme A"), ("shift_schemeB", "Scheme B"), ("shift_schemeC", "Scheme C (control)")]:
    ax.hist(d[key], bins=50, alpha=0.5, label=label)
ax.set_xlabel("Per-sample shift")
ax.set_ylabel("Count")
ax.set_title("Per-sample shift under three replacement schemes")
ax.legend()

# Right: pooled statistic vs dose with 95% CI
ax = axes[1]
ax.errorbar(d["dose"], d["pooled_stat"], yerr=d["pooled_stat_ci"], fmt="o-", capsize=3)
ax.set_xlabel("Dose (fraction of replaced rows)")
ax.set_ylabel("Pooled statistic")
ax.set_title("Pooled statistic vs dose (95% CI)")
ax.set_xscale("log")
ax.grid(True)

plt.tight_layout()
plt.savefig("examples/figures/11a_before.png", dpi=150)
print("saved examples/figures/11a_before.png")
