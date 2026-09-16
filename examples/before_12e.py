import numpy as np
import matplotlib.pyplot as plt

d = np.load("examples/data/12e.npz")
p1, p2, meas = d["parameter1"], d["parameter2"], d["measured"]

fig, ax = plt.subplots()
for i in range(len(p2)):
    plt.plot(p1, meas[i], label=f"parameter 2 = {p2[i]}")
plt.title("Measured quantity vs parameter 1")
plt.xlabel("Parameter 1")
plt.ylabel("Measured quantity")
plt.legend()
plt.savefig("examples/figures/12e_before.png", dpi=150)
