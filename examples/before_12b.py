import numpy as np
import matplotlib.pyplot as plt

d = np.load("examples/data/12b.npz")

fig, axes = plt.subplots(1, 3, figsize=(13, 4))

# Left: runtime vs problem size for both tasks (baseline only up to its limit)
ax = axes[0]
for task in ["A", "B"]:
    sizes = d[f"task{task}_sizes"]
    lim = int(d[f"task{task}_baseline_limit"])
    m = sizes <= lim
    ax.plot(sizes[m], d[f"task{task}_base_runtime"][m], "o--", label=f"Baseline, task {task}")
    ax.plot(sizes, d[f"task{task}_ours_runtime"], "s-", label=f"Ours, task {task}")
ax.set_xlabel("Problem size")
ax.set_ylabel("Runtime")
ax.set_yscale("log")
ax.set_title("Runtime vs problem size")
ax.legend(fontsize=8)
ax.grid(True)

# Middle: memory vs problem size
ax = axes[1]
for task in ["A", "B"]:
    sizes = d[f"task{task}_sizes"]
    lim = int(d[f"task{task}_baseline_limit"])
    m = sizes <= lim
    ax.plot(sizes[m], d[f"task{task}_base_memory"][m], "o--", label=f"Baseline, task {task}")
    ax.plot(sizes, d[f"task{task}_ours_memory"], "s-", label=f"Ours, task {task}")
ax.set_xlabel("Problem size")
ax.set_ylabel("Memory")
ax.set_yscale("log")
ax.set_title("Memory vs problem size")
ax.legend(fontsize=8)
ax.grid(True)

# Right: speedup factors for the five framework/task pairs
ax = axes[2]
for key in [k for k in d.files if k.startswith("speedup_framework")]:
    ax.plot(d["speedup_problem_size"], d[key], "o-", label=key.replace("speedup_", ""))
ax.axhline(1, color="k", lw=0.8, ls=":")
ax.set_xscale("log")
ax.set_xlabel("Problem size")
ax.set_ylabel("Speedup factor")
ax.set_title("Speedup vs problem size")
ax.legend(fontsize=8)
ax.grid(True)

plt.tight_layout()
plt.savefig("examples/figures/12b_before.png", dpi=150)
print("saved examples/figures/12b_before.png")
