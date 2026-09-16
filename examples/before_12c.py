"""12c: compiler vs baseline -- survival on three devices, SWAP counts vs depth."""
import numpy as np
import matplotlib.pyplot as plt

d = np.load("examples/data/12c.npz")
depth = d["depth"]
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

x = np.arange(len(depth))
w = 0.13
i = 0
for dev in [1, 2, 3]:
    for meth, name in [("ours", "ours"), ("base", "baseline")]:
        ax1.bar(x + (i - 2.5) * w, d[f"survival_{meth}_device {dev}"], w,
                yerr=d[f"survival_{meth}_err_device {dev}"], capsize=2, label=f"{name}, device {dev}")
        i += 1
ax1.set_xticks(x)
ax1.set_xticklabels([f"depth {v}" for v in depth])
ax1.set_ylabel("survival")
ax1.set_title("Survival probability")
ax1.legend(fontsize=7, ncol=2)

ax2.plot(d["sweep_depth"], d["swap_base"], "o--", label="baseline SWAPs")
ax2.plot(d["sweep_depth"], d["swap_ours"], "s-", label="ours SWAPs")
ax2.axvline(d["baseline_timeout_depth"], color="r", ls=":", label="baseline timeout")
ax2.set_xscale("log"); ax2.set_yscale("log")
ax2.set_xlabel("circuit depth"); ax2.set_ylabel("SWAP count")
ax2.set_title("SWAP count vs depth")
ax2.legend(fontsize=8); ax2.grid(True, which="both", alpha=0.3)

fig.tight_layout()
fig.savefig("examples/figures/12c_before.png", dpi=150)
