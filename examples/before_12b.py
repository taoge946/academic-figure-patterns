import numpy as np
import matplotlib.pyplot as plt

d = np.load("examples/data/12b.npz")

fig, ax = plt.subplots()
plt.plot(d["taskA_sizes"], d["taskA_base_runtime"], label="baseline")
plt.plot(d["taskA_sizes"], d["taskA_ours_runtime"], label="ours")
plt.title("Runtime vs problem size (task A)")
plt.xlabel("Problem size")
plt.ylabel("Runtime")
plt.legend()
plt.savefig("examples/figures/12b_before.png", dpi=150)
