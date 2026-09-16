import numpy as np
import matplotlib.pyplot as plt

d = np.load("examples/data/11a.npz")
schemes = ["A", "B", "C"]
means = [d[f"shift_scheme{s}"].mean() for s in schemes]

fig, ax = plt.subplots()
plt.bar(schemes, means)
plt.title("Per-sample change by replacement scheme")
plt.xlabel("Replacement scheme")
plt.ylabel("Mean per-sample change")
plt.savefig("examples/figures/11a_before.png", dpi=150)
