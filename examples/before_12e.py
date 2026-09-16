"""12e: measured quantity vs model over a 2-D grid (overlap fraction x shots per setting)."""
import numpy as np
import matplotlib.pyplot as plt

d = np.load("examples/data/12e.npz")
of = d["overlap_fraction"]
shots = d["shots_per_setting"]
vmax = max(abs(d["measured"]).max(), abs(d["model"]).max())

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
for ax, key in zip(axes, ["measured", "model"]):
    im = ax.imshow(d[key], aspect="auto", origin="lower", cmap="RdBu_r", vmin=-vmax, vmax=vmax,
                   extent=[of[0], of[-1], -0.5, len(shots) - 0.5])
    ax.contour(of, np.arange(len(shots)), d["model"], levels=[0], colors="k", linewidths=1)
    ax.set_yticks(np.arange(len(shots)))
    ax.set_yticklabels(shots)
    ax.set_xlabel("overlap fraction")
    ax.set_ylabel("shots per setting")
    ax.set_title(key + " (black: model zero crossing)")
    fig.colorbar(im, ax=ax)

fig.tight_layout()
fig.savefig("examples/figures/12e_before.png", dpi=150)
