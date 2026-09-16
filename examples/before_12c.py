import numpy as np
import matplotlib.pyplot as plt

d = np.load("examples/data/12c.npz")
sizes = d["input_size"]

fig, axes = plt.subplots(1, 2, figsize=(10, 4))

# Left: grouped bars, metric of ours vs baseline on three devices at three input sizes
ax = axes[0]
x = np.arange(len(sizes))
w = 0.13
i = 0
for dev in [1, 2, 3]:
    for who, label in [("ours", "Ours"), ("base", "Baseline")]:
        ax.bar(x + (i - 2.5) * w, d[f"metric_{who}_device {dev}"], w,
               yerr=d[f"metric_{who}_err_device {dev}"], capsize=2, label=f"{label}, device {dev}")
        i += 1
ax.set_xticks(x)
ax.set_xticklabels([str(s) for s in sizes])
ax.set_xlabel("Input size")
ax.set_ylabel("Metric")
ax.set_title("Method vs baseline on three devices")
ax.legend(fontsize=7, ncol=2)

# Right: cost vs sweep size (log-log) with baseline limit, plus cost ratio on twin axis
ax = axes[1]
ax.plot(d["sweep_size"], d["cost_ours"], "s-", label="Cost, ours")
ax.plot(d["sweep_size"], d["cost_base"], "o--", label="Cost, baseline")
ax.axvline(float(d["baseline_limit"]), color="r", ls=":", label="Baseline limit")
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlabel("Input size")
ax.set_ylabel("Cost")
ax.set_title("Cost vs input size and cost ratio")
ax2 = ax.twinx()
ax2.errorbar(d["sweep_size"], d["cost_ratio"], yerr=d["cost_ratio_band"], fmt="^-", color="g", capsize=2, label="Cost ratio")
ax2.set_ylabel("Cost ratio (baseline / ours)")
h1, l1 = ax.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
ax.legend(h1 + h2, l1 + l2, fontsize=8, loc="upper left")

plt.tight_layout()
plt.savefig("examples/figures/12c_before.png", dpi=150)
print("saved examples/figures/12c_before.png")
