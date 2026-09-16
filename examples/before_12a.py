import numpy as np
import matplotlib.pyplot as plt

d = np.load("examples/data/12a.npz")

fig, axes = plt.subplots(1, 3, figsize=(12, 4))

# Left: input shift vs model shift scatter for the two defect types
ax = axes[0]
for t in [1, 2]:
    ax.scatter(d[f"input_shift_type{t}"], d[f"model_shift_type{t}"], s=6, alpha=0.4, label=f"Type {t}")
lim = [-0.4, 0.4]
ax.plot(lim, lim, "k--", lw=1)
ax.set_xlabel("Input shift")
ax.set_ylabel("Model shift")
ax.set_title("Input shift vs model shift")
ax.legend()

# Middle: stacked bars of the statistic decomposition per cohort, type 1 and type 2
ax = axes[1]
x = np.arange(4)
w = 0.35
for i, t in enumerate([1, 2]):
    off = (i - 0.5) * w
    ax.bar(x + off, d[f"bar_intercept_type{t}"], w, label=f"Intercept, type {t}")
    ax.bar(x + off, d[f"bar_nonconstant_type{t}"], w, bottom=d[f"bar_intercept_type{t}"],
           yerr=d["bar_err"], capsize=2, alpha=0.6, label=f"Non-constant, type {t}")
ax.set_xticks(x)
ax.set_xticklabels([f"Cohort {k}" for k in range(4)])
ax.set_ylabel("Statistic")
ax.set_title("Decomposition per cohort")
ax.legend(fontsize=7)

# Right: bias per cohort with error bars
ax = axes[2]
for t in [1, 2]:
    ax.errorbar(x, d[f"bias_type{t}"], yerr=d[f"bias_type{t}_err"], fmt="o-", capsize=3, label=f"Type {t}")
ax.axhline(0, color="k", lw=0.8)
ax.set_xticks(x)
ax.set_xticklabels([f"Cohort {k}" for k in range(4)])
ax.set_ylabel("Bias")
ax.set_title("Bias per cohort")
ax.legend()

plt.tight_layout()
plt.savefig("examples/figures/12a_before.png", dpi=150)
print("saved examples/figures/12a_before.png")
