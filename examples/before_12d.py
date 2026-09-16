"""12d: learner shift control vs defect at three cohort sizes; ratio vs noise floor; resolution."""
import numpy as np
import matplotlib.pyplot as plt

d = np.load("examples/data/12d.npz")
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(10, 4))

sizes = [36, 71, 320]
x = np.arange(3)
w = 0.35
for i, cond in enumerate(["control", "defect"]):
    m = [np.abs(d[f"shift_{cond}_row{r}"]).mean() for r in range(3)]
    s = [np.abs(d[f"shift_{cond}_row{r}"]).std() for r in range(3)]
    ax1.bar(x + (i - 0.5) * w, m, w, yerr=s, capsize=3, label=cond)
ax1.set_xticks(x); ax1.set_xticklabels([f"{n} states" for n in sizes])
ax1.set_ylabel("mean |learner shift|"); ax1.set_title("Shift by cohort size"); ax1.legend()

ax2.scatter(d["sim_x"], d["sim_ratio"], s=10, alpha=0.5, label="simulation")
ax2.errorbar(d["hw_x"], d["hw_ratio"], yerr=d["hw_err"], fmt="o", color="C3", capsize=3, label="hardware")
xx = np.linspace(0, 0.5, 50)
ax2.plot(xx, 1 - 2 * xx, "k--", label="theory 1-2x")
ax2.set_xlabel("noise-floor variable x"); ax2.set_ylabel("ratio")
ax2.set_title("Ratio vs noise floor"); ax2.legend(fontsize=8); ax2.grid(True, alpha=0.3)

c = np.arange(6)
ax3.fill_between(c, d["resolution_control_lo"], d["resolution_control_hi"], color="gray", alpha=0.3,
                 label="control interval")
ax3.errorbar(c, d["resolution_defect"], yerr=d["resolution_defect_err"], fmt="o-", capsize=3,
             label="defect estimate")
ax3.set_xlabel("cohort"); ax3.set_ylabel("statistic"); ax3.set_title("Resolution"); ax3.legend(fontsize=8)

fig.tight_layout()
fig.savefig("examples/figures/12d_before.png", dpi=150)
