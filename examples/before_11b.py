import numpy as np
import matplotlib.pyplot as plt

d = np.load("examples/data/11b.npz")
conds = [0, 1, 2]
mean_P = [np.concatenate([d[f"shift_P_cohort{j}_cond{c}"] for j in range(3)]).mean() for c in conds]
mean_Q = [np.concatenate([d[f"shift_Q_cohort{j}_cond{c}"] for j in range(3)]).mean() for c in conds]

x = np.arange(3)
fig, ax = plt.subplots()
plt.bar(x - 0.2, mean_P, width=0.4, label="P")
plt.bar(x + 0.2, mean_Q, width=0.4, label="Q")
plt.xticks(x, ["cond 0", "cond 1", "cond 2"])
plt.title("Mean prediction change, P vs Q")
plt.xlabel("Condition")
plt.ylabel("Mean per-sample change")
plt.legend()
plt.savefig("examples/figures/11b_before.png", dpi=150)
