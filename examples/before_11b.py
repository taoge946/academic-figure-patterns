"""11b: estimators P vs Q -- mean |shift| per condition, clean residuals per cohort."""
import numpy as np
import matplotlib.pyplot as plt

d = np.load("examples/data/11b.npz")
conds = ["cond 0", "cond 1", "cond 2 (control)"]
cohorts = [0, 1, 2]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

x = np.arange(3)
w = 0.35
for i, est in enumerate(["P", "Q"]):
    per = [[np.abs(d[f"shift_{est}_cohort{j}_cond{c}"]).mean() for j in cohorts] for c in range(3)]
    ax1.bar(x + (i - 0.5) * w, np.mean(per, axis=1), w, yerr=np.std(per, axis=1),
            capsize=3, label=f"estimator {est}")
ax1.set_xticks(x)
ax1.set_xticklabels(conds)
ax1.set_ylabel("mean |prediction shift| (avg over cohorts)")
ax1.set_title("Shift from clean fit")
ax1.legend()

w = 0.25
for i, (key, label) in enumerate([("P", "P"), ("Q", "Q"), ("mean", "training mean")]):
    vals = [d[f"clean_absres_{key}_cohort{j}"].mean() for j in cohorts]
    ax2.bar(np.array(cohorts) + (i - 1) * w, vals, w, label=label)
ax2.set_xticks(cohorts)
ax2.set_xticklabels([f"cohort {j}" for j in cohorts])
ax2.set_ylabel("mean absolute residual (clean)")
ax2.set_title("Clean-data residuals")
ax2.legend()

fig.tight_layout()
fig.savefig("examples/figures/11b_before.png", dpi=150)
