import numpy as np
import matplotlib.pyplot as plt

d = np.load("examples/data/11d.npz")
budgets = [1, 2, 3, 4]
base = [np.concatenate([d[f"baseline_err_cohort{j}_budget{b}"] for j in range(3)]).mean() for b in budgets]
meth = [np.concatenate([d[f"method_err_cohort{j}_budget{b}"] for j in range(3)]).mean() for b in budgets]

fig, ax = plt.subplots()
plt.plot(budgets, base, label="baseline")
plt.plot(budgets, meth, label="method")
plt.title("Mean error vs budget")
plt.xlabel("Budget level")
plt.ylabel("Mean absolute error")
plt.legend()
plt.savefig("examples/figures/11d_before.png", dpi=150)
