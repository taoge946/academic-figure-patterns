"""11d: learner vs baseline mean error vs budget K, and squared error of four predictors."""
import numpy as np
import matplotlib.pyplot as plt

d = np.load("examples/data/11d.npz")
Ks = [8, 32, 128, 1024]
cohorts = [0, 1, 2]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

for j in cohorts:
    base = [d[f"baseline_err_cohort{j}_K{K}"].mean() for K in Ks]
    learn = [d[f"learner_err_cohort{j}_K{K}"].mean() for K in Ks]
    ax1.plot(Ks, base, "o--", label=f"baseline, cohort {j}")
    ax1.plot(Ks, learn, "s-", label=f"learner, cohort {j}")
ax1.set_xscale("log")
ax1.set_yscale("log")
ax1.set_xlabel("budget K")
ax1.set_ylabel("mean absolute error")
ax1.set_title("Error vs budget")
ax1.legend(fontsize=8)
ax1.grid(True, which="both", alpha=0.3)

preds = ["baseline", "clean", "reused", "repaired"]
w = 0.2
for i, p in enumerate(preds):
    arrs = [d[f"sqerr_{p}_cohort{j}"] for j in cohorts]
    vals = [a.mean() for a in arrs]
    errs = [a.std() / np.sqrt(len(a)) for a in arrs]
    ax2.bar(np.array(cohorts) + (i - 1.5) * w, vals, w, yerr=errs, capsize=2, label=p)
ax2.set_xticks(cohorts)
ax2.set_xticklabels([f"cohort {j}" for j in cohorts])
ax2.set_ylabel("mean squared error")
ax2.set_title("Four predictors at one budget")
ax2.legend()

fig.tight_layout()
fig.savefig("examples/figures/11d_before.png", dpi=150)
