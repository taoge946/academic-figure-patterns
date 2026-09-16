import numpy as np
import matplotlib.pyplot as plt

d = np.load("examples/data/12d.npz")
row_labels = ["Small cohort", "Medium cohort", "Large cohort"]

fig, axes = plt.subplots(1, 3, figsize=(13, 4))

# Left: histograms of model shift under control vs defect for the three cohort sizes
ax = axes[0]
for i, lab in enumerate(row_labels):
    ax.hist(d[f"shift_control_row{i}"], bins=30, alpha=0.4, histtype="step", lw=1.5, label=f"Control, {lab}")
    ax.hist(d[f"shift_defect_row{i}"], bins=30, alpha=0.4, label=f"Defect, {lab}")
ax.set_xlabel("Model shift")
ax.set_ylabel("Count")
ax.set_title("Model shift: control vs defect")
ax.legend(fontsize=7)

# Middle: ratio vs noise-floor variable — simulation, measurement, and theory 1 - 2x
ax = axes[1]
ax.scatter(d["sim_x"], d["sim_ratio"], s=10, alpha=0.5, label="Simulated cohorts")
ax.errorbar(d["measured_x"], d["measured_ratio"], yerr=d["measured_err"], fmt="o", color="r", capsize=3, label="Measured cohorts")
xx = np.linspace(0, 0.5, 100)
ax.plot(xx, 1 - 2 * xx, "k--", label="Theory: 1 - 2x")
ax.set_xlabel("Noise-floor variable x")
ax.set_ylabel("Ratio")
ax.set_title("Ratio vs noise floor")
ax.legend(fontsize=8)
ax.grid(True)

# Right: per-cohort control interval vs defect estimate (normalized)
ax = axes[2]
k = np.arange(6)
ax.fill_between(k, d["resolution_control_lo"], d["resolution_control_hi"], color="gray", alpha=0.3, label="Control interval")
ax.errorbar(k, d["resolution_defect"], yerr=d["resolution_defect_err"], fmt="o-", capsize=3, label="Defect estimate")
ax.set_xlabel("Cohort index")
ax.set_ylabel("Normalized value")
ax.set_title("Resolution per cohort")
ax.legend(fontsize=8)
ax.grid(True)

plt.tight_layout()
plt.savefig("examples/figures/12d_before.png", dpi=150)
print("saved examples/figures/12d_before.png")
