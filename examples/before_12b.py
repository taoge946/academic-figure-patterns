"""12b: runtime and memory vs problem size (ours vs baseline), and speedups."""
import numpy as np
import matplotlib.pyplot as plt

d = np.load("examples/data/12b.npz")
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(10, 4))

for task in ["mis", "tsp"]:
    s = d[f"{task}_sizes"]
    ok = s <= d[f"{task}_baseline_oom_from"]
    ax1.plot(s[ok], d[f"{task}_base_runtime"][ok], "o--", label=f"{task.upper()} baseline")
    ax1.plot(s, d[f"{task}_ours_runtime"], "s-", label=f"{task.upper()} ours")
    ax2.plot(s[ok], d[f"{task}_base_memory"][ok], "o--", label=f"{task.upper()} baseline")
    ax2.plot(s, d[f"{task}_ours_memory"], "s-", label=f"{task.upper()} ours")
ax1.set_yscale("log"); ax1.set_xlabel("problem size"); ax1.set_ylabel("runtime")
ax1.set_title("Runtime (baseline stops at OOM)"); ax1.legend(fontsize=8); ax1.grid(True, alpha=0.3)
ax2.set_yscale("log"); ax2.set_xlabel("problem size"); ax2.set_ylabel("memory")
ax2.set_title("Memory"); ax2.legend(fontsize=8); ax2.grid(True, alpha=0.3)

for k in d.files:
    if k.startswith("speedup_framework"):
        ax3.plot(d["speedup_graph_size"], d[k], "o-", label=k.replace("speedup_", ""))
ax3.axhline(1, color="k", lw=0.8, ls="--")
ax3.set_xscale("log"); ax3.set_xlabel("graph size"); ax3.set_ylabel("speedup")
ax3.set_title("Speedup"); ax3.legend(fontsize=7); ax3.grid(True, alpha=0.3)

fig.tight_layout()
fig.savefig("examples/figures/12b_before.png", dpi=150)
