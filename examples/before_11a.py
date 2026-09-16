"""11a: label shift under three replacement schemes + pooled statistic vs dose."""
import numpy as np
import matplotlib.pyplot as plt

d = np.load("examples/data/11a.npz")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

bins = np.linspace(-0.3, 0.3, 61)
for key, label in [("shift_shared", "shared shots"),
                   ("shift_disjoint", "fresh shots"),
                   ("shift_matched", "composition-matched")]:
    ax1.hist(d[key], bins=bins, alpha=0.5, label=label)
ax1.set_xlabel("per-row label shift")
ax1.set_ylabel("count")
ax1.set_title("Label shift per replacement scheme")
ax1.legend()

ax2.errorbar(d["dose_fraction"], d["dW"], yerr=d["dW_ci"], fmt="o-", capsize=3)
ax2.set_xlabel("fraction of replaced settings")
ax2.set_ylabel("pooled statistic dW")
ax2.set_title("Pooled statistic vs dose (95% CI)")
ax2.grid(True)

fig.tight_layout()
fig.savefig("examples/figures/11a_before.png", dpi=150)
