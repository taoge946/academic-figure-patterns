import numpy as np
import matplotlib.pyplot as plt

d = np.load("examples/data/12d.npz")
rows = [0, 1, 2]
ctrl = [d[f"shift_control_row{i}"].mean() for i in rows]
dfct = [d[f"shift_defect_row{i}"].mean() for i in rows]

x = np.arange(3)
fig, ax = plt.subplots()
plt.bar(x - 0.2, ctrl, width=0.4, label="control")
plt.bar(x + 0.2, dfct, width=0.4, label="defect")
plt.xticks(x, ["small", "medium", "large"])
plt.title("Mean model shift by cohort size")
plt.xlabel("Cohort size")
plt.ylabel("Mean model shift")
plt.legend()
plt.savefig("examples/figures/12d_before.png", dpi=150)
