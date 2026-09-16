import numpy as np
import matplotlib.pyplot as plt

d = np.load("examples/data/11c.npz")

fig, ax = plt.subplots()
plt.scatter(d["explanatory_x"], d["effect"])
plt.title("Effect vs explanatory variable")
plt.xlabel("Explanatory variable")
plt.ylabel("Effect")
plt.savefig("examples/figures/11c_before.png", dpi=150)
