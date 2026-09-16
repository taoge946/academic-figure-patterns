import numpy as np
import matplotlib.pyplot as plt

d = np.load("examples/data/11b.npz")
cohorts = [0, 1, 2]
conds = [0, 1, 2]
cond_labels = ["Cond 0", "Cond 1", "Cond 2 (control)"]

fig, axes = plt.subplots(1, 2, figsize=(10, 4))

# Left: mean absolute shift of P and Q per condition, averaged over cohorts, with std error bars
ax = axes[0]
x = np.arange(len(conds))
w = 0.35
for i, est in enumerate(["P", "Q"]):
    means, stds = [], []
    for c in conds:
        vals = np.concatenate([np.abs(d[f"shift_{est}_cohort{j}_cond{c}"]) for j in cohorts])
        means.append(vals.mean())
        stds.append(vals.std() / np.sqrt(len(vals)))
    ax.bar(x + (i - 0.5) * w, means, w, yerr=stds, capsize=3, label=f"Estimator {est}")
ax.set_xticks(x)
ax.set_xticklabels(cond_labels)
ax.set_ylabel("Mean |shift|")
ax.set_title("Mean absolute shift per condition (all cohorts)")
ax.legend()

# Right: mean clean absolute residual per cohort for P, Q, and reference predictor
ax = axes[1]
x = np.arange(len(cohorts))
w = 0.25
for i, (key, label) in enumerate([("P", "Estimator P"), ("Q", "Estimator Q"), ("mean", "Reference predictor")]):
    vals = [d[f"clean_absres_{key}_cohort{j}"].mean() for j in cohorts]
    ax.bar(x + (i - 1) * w, vals, w, label=label)
ax.set_xticks(x)
ax.set_xticklabels([f"Cohort {j}" for j in cohorts])
ax.set_ylabel("Mean absolute residual (clean)")
ax.set_title("Clean absolute residuals per cohort")
ax.legend()

plt.tight_layout()
plt.savefig("examples/figures/11b_before.png", dpi=150)
print("saved examples/figures/11b_before.png")
