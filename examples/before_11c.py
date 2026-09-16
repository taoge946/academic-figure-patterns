"""11c: log risk ratio vs number of filled cells, by system size, with control."""
import numpy as np
import matplotlib.pyplot as plt

d = np.load("examples/data/11c.npz")
fc = d["filled_cells"]
rr = d["risk_ratio_log"]
idx = d["system_size_index"]
sizes = d["system_sizes"]

fig, ax = plt.subplots(figsize=(8, 5))
ax.scatter(fc, d["control_risk_ratio"], s=8, c="lightgray", label="control condition")
for k, n in enumerate(sizes):
    m = idx == k
    ax.scatter(fc[m], rr[m], s=10, alpha=0.6, label=f"system size {n}")
ax.axhline(0, color="k", lw=0.8, ls="--")
ax.set_xlabel("filled cells per state")
ax.set_ylabel("log risk ratio")
ax.set_title("Effect vs number of filled cells")
ax.legend()
ax.grid(True, alpha=0.3)

fig.tight_layout()
fig.savefig("examples/figures/11c_before.png", dpi=150)
