import numpy as np
import matplotlib.pyplot as plt

d = np.load("examples/data/12c.npz")
devices = [1, 2, 3]
ours = [d[f"metric_ours_device {k}"].mean() for k in devices]
base = [d[f"metric_base_device {k}"].mean() for k in devices]

x = np.arange(3)
fig, ax = plt.subplots()
plt.bar(x - 0.2, ours, width=0.4, label="ours")
plt.bar(x + 0.2, base, width=0.4, label="baseline")
plt.xticks(x, ["device 1", "device 2", "device 3"])
plt.title("Mean metric per device")
plt.xlabel("Device")
plt.ylabel("Metric (mean over input sizes)")
plt.legend()
plt.savefig("examples/figures/12c_before.png", dpi=150)
