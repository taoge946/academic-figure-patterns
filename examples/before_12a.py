import numpy as np
import matplotlib.pyplot as plt

d = np.load("examples/data/12a.npz")
types = [1, 2]
inp = [d[f"input_shift_type{t}"].mean() for t in types]
mod = [d[f"model_shift_type{t}"].mean() for t in types]

x = np.arange(2)
fig, ax = plt.subplots()
plt.bar(x - 0.2, inp, width=0.4, label="input shift")
plt.bar(x + 0.2, mod, width=0.4, label="model shift")
plt.xticks(x, ["type 1", "type 2"])
plt.title("Mean shift by defect type")
plt.xlabel("Defect type")
plt.ylabel("Mean shift")
plt.legend()
plt.savefig("examples/figures/12a_before.png", dpi=150)
