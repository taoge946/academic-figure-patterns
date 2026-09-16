"""Example 12c: systems-venue sweep figure (MICRO / ASPLOS look), synthetic data.

The same author accepted a different visual language for a systems paper: heavy lines, large
markers, the gap between our method and the baseline filled, a twin axis for solver time, a
"timeout" wall, Times New Roman at large size (the figure is shrunk to column width in the paper).
Top row: one panel per device, survival against depth, gap filled, ratio printed per panel.
Bottom: SWAP count against depth (log) for baseline and ours with the ratio and its band on a twin
axis.  Content rules still hold: every panel has a comparison object and a printed number.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from afp.evidence import MM

plt.rcParams.update({"font.family": "serif", "font.serif": ["Times New Roman", "DejaVu Serif"], "mathtext.fontset": "stix",
                     "axes.linewidth": 1.4, "xtick.major.width": 1.2, "ytick.major.width": 1.2, "xtick.labelsize": 11,
                     "ytick.labelsize": 11, "axes.labelsize": 13, "legend.fontsize": 10, "axes.grid": False})
OURS, BASE, RATIO = "#1f8a4c", "#c0392b", "#2e75b6"
rng = np.random.default_rng(4)

fig = plt.figure(figsize=(180 * MM, 120 * MM))
# ---------- top row: per-device survival vs depth ----------
devices = ["device 1", "device 2", "device 3"]
depth = np.array([8, 12, 16])
for k, dev in enumerate(devices):
    ax = fig.add_axes([.08 + k * .31, .60, .26, .33])
    ours = np.array([.46, .41, .36]) * [1.0, .95, .78][k] - .02 * k
    base = np.array([.44, .20, .19]) * [1.0, 1.3, 1.1][k] - .04 * k
    eo = np.array([.02, .02, .03]); eb = np.array([.03, .05, .05])
    ax.fill_between(depth, base, ours, color=OURS, alpha=.22, lw=0)
    ax.errorbar(depth, ours, yerr=eo, fmt="-o", color=OURS, lw=3, ms=7, capsize=3, label="ours")
    ax.errorbar(depth, base, yerr=eb, fmt="--s", color=BASE, lw=3, ms=7, capsize=3, label="baseline")
    ax.set_xticks(depth); ax.set_ylim(0, .66); ax.set_xlim(7, 17)
    ax.text(7.3, .64, dev, fontsize=12, fontweight="bold", va="top")
    ax.text(16.7, .64, f"{ours[-1] / base[-1]:.1f}×", fontsize=13, fontweight="bold", color=OURS, ha="right", va="top")
    if k == 0:
        ax.set_ylabel("survival", fontweight="bold"); ax.legend(loc="lower left", frameon=True, edgecolor="#bbb")
    else:
        ax.set_yticklabels([])
    ax.set_xlabel("depth", fontweight="bold")
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)

# ---------- bottom: SWAP count vs depth with ratio band and timeout wall ----------
ax = fig.add_axes([.08, .10, .84, .40]); ax2 = ax.twinx()
d = np.array([4, 8, 16, 32, 64, 128, 256, 512, 1024], float)
ours_sw = 60 * (d / 4) ** .55; base_sw = 60 * (d / 4) ** 1.02
ratio = base_sw / ours_sw * (1 + .04 * rng.standard_normal(len(d))); band = ratio * .18
ax2.fill_between(d, ratio - band, ratio + band, color=RATIO, alpha=.18, lw=0)
ax2.plot(d, ratio, "-^", color=RATIO, lw=3, ms=7, label="ratio baseline / ours")
ax.plot(d, base_sw, "-o", color=BASE, lw=3, ms=6, label="baseline SWAP"); ax.plot(d, ours_sw, "-s", color=OURS, lw=3, ms=6, label="ours SWAP")
ax.fill_between(d, ours_sw, base_sw, color=OURS, alpha=.10, lw=0)
ax.axvline(700, color=BASE, lw=2, ls="--", alpha=.7); ax.text(720, base_sw[-1] * .35, "baseline\ntimeout", color=BASE, fontsize=11, fontweight="bold")
ax.set_xscale("log", base=2); ax.set_xticks(d); ax.set_xticklabels([str(int(v)) for v in d])
ax.set_yscale("log"); ax.set_xlabel("circuit depth (log)", fontweight="bold"); ax.set_ylabel("SWAP count", fontweight="bold")
ax2.set_ylabel("ratio baseline / ours", color=RATIO, fontweight="bold"); ax2.tick_params(axis="y", colors=RATIO); ax2.set_ylim(0, 22)
ax.legend(handles=[Line2D([], [], color=BASE, marker="o", lw=3, ms=6, label="baseline SWAP"), Line2D([], [], color=OURS, marker="s", lw=3, ms=6, label="ours SWAP"),
                   Line2D([], [], color=RATIO, marker="^", lw=3, ms=6, label="ratio (right axis), ±1 sd band")],
          loc="upper left", frameon=True, edgecolor="#bbb")
ax.text(24, ours_sw[3] * 2.4, f"{ratio[-1]:.0f}× fewer SWAPs at depth 1024", fontsize=11, fontweight="bold", color=OURS, rotation=17)
for a in (ax, ax2):
    a.spines["top"].set_visible(False)
fig.text(.02, .95, "(a)", fontsize=13, fontweight="bold"); fig.text(.02, .52, "(b)", fontsize=13, fontweight="bold")
fig.savefig("examples/figures/12c_after.png", dpi=220); fig.savefig("examples/figures/12c_after.pdf")
print("saved examples/figures/12c_after.{png,pdf}")
