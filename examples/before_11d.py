import numpy as np
import matplotlib.pyplot as plt

d = np.load("examples/data/11d.npz")
cohorts = [0, 1, 2]
budgets = [1, 2, 3, 4]

fig, axes = plt.subplots(1, 2, figsize=(10, 4))

# Left: mean absolute error vs budget, method vs baseline, one line per cohort
ax = axes[0]
for j in cohorts:
    base = [d[f"baseline_err_cohort{j}_budget{b}"].mean() for b in budgets]
    meth = [d[f"method_err_cohort{j}_budget{b}"].mean() for b in budgets]
    ax.plot(budgets, base, "o--", label=f"Baseline, cohort {j}")
    ax.plot(budgets, meth, "s-", label=f"Method, cohort {j}")
ax.set_xlabel("Budget level")
ax.set_ylabel("Mean absolute error")
ax.set_title("Method vs baseline error across budgets")
ax.set_xticks(budgets)
ax.legend(fontsize=7)
ax.grid(True)

# Right: mean squared error of four predictors per cohort (one budget)
ax = axes[1]
preds = [("sqerr_baseline", "Baseline"), ("sqerr_method", "Method"),
         ("sqerr_method_perturbed", "Method (perturbed)"), ("sqerr_method_repaired", "Method (repaired)")]
x = np.arange(len(cohorts))
w = 0.2
for i, (key, label) in enumerate(preds):
    vals = [d[f"{key}_cohort{j}"].mean() for j in cohorts]
    errs = [d[f"{key}_cohort{j}"].std() / np.sqrt(len(d[f"{key}_cohort{j}"])) for j in cohorts]
    ax.bar(x + (i - 1.5) * w, vals, w, yerr=errs, capsize=2, label=label)
ax.set_xticks(x)
ax.set_xticklabels([f"Cohort {j}" for j in cohorts])
ax.set_ylabel("Mean squared error")
ax.set_title("Squared error of four predictors")
ax.legend(fontsize=8)

plt.tight_layout()
plt.savefig("examples/figures/11d_before.png", dpi=150)
print("saved examples/figures/11d_before.png")
