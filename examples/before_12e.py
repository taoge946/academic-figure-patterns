import numpy as np
import matplotlib.pyplot as plt

d = np.load("examples/data/12e.npz")
p1 = d["parameter1"]
p2 = d["parameter2"]
measured = d["measured"]
model = d["model"]

fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))

# Left: heatmap of the measured quantity over the 2-D grid, with model zero-crossing contour
ax = axes[0]
im = ax.imshow(measured, aspect="auto", origin="lower", cmap="coolwarm",
               extent=[p1[0], p1[-1], -0.5, len(p2) - 0.5])
ax.contour(p1, np.arange(len(p2)), model, levels=[0], colors="k", linestyles="--")
ax.set_yticks(np.arange(len(p2)))
ax.set_yticklabels([str(v) for v in p2])
ax.set_xlabel("Parameter 1")
ax.set_ylabel("Parameter 2")
ax.set_title("Measured quantity (dashed: model = 0)")
fig.colorbar(im, ax=ax, label="Measured")

# Right: measured (points) vs model (lines) along parameter 1 for a few parameter-2 values
ax = axes[1]
for i in [0, 2, 4, 6, 8]:
    line, = ax.plot(p1, model[i], "-", label=f"Model, p2 = {p2[i]}")
    ax.plot(p1, measured[i], "o", color=line.get_color(), ms=3, label=f"Measured, p2 = {p2[i]}")
ax.axhline(0, color="k", lw=0.8)
ax.set_xlabel("Parameter 1")
ax.set_ylabel("Quantity")
ax.set_title("Measured vs model along parameter 1")
ax.legend(fontsize=6, ncol=2)
ax.grid(True)

plt.tight_layout()
plt.savefig("examples/figures/12e_before.png", dpi=150)
print("saved examples/figures/12e_before.png")
