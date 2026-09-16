import numpy as np
import matplotlib.pyplot as plt

d = np.load("examples/data/11c.npz")
x = d["explanatory_x"]
effect = d["effect"]
control = d["control_effect"]
size_index = d["size_index"]
sizes = d["sizes"]

fig, axes = plt.subplots(1, 2, figsize=(10, 4), sharey=True)

# Left: effect vs explanatory variable, colored by size
ax = axes[0]
for i, s in enumerate(sizes):
    m = size_index == i
    ax.scatter(x[m], effect[m], s=8, alpha=0.5, label=f"size = {s}")
ax.set_xlabel("Explanatory variable x")
ax.set_ylabel("Effect")
ax.set_title("Effect vs explanatory variable")
ax.legend()
ax.grid(True)

# Right: control effect vs explanatory variable
ax = axes[1]
for i, s in enumerate(sizes):
    m = size_index == i
    ax.scatter(x[m], control[m], s=8, alpha=0.5, label=f"size = {s}")
ax.set_xlabel("Explanatory variable x")
ax.set_title("Control effect vs explanatory variable")
ax.legend()
ax.grid(True)

plt.tight_layout()
plt.savefig("examples/figures/11c_before.png", dpi=150)
print("saved examples/figures/11c_before.png")
