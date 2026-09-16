"""Example 12b: ML hero figure -- scaling with an out-of-memory wall (synthetic).

Form of an ICML 2026 Figure 1 the author kept (see examples/gallery/lore_scaling_hero.png):
(a), (b) runtime (solid) and memory (dashed) against problem size for baseline and method on a
    log axis, twin y-axes, the baseline's out-of-memory region shaded and labelled, one gap arrow
    with the number a reader wants;
(c) speedup against size, log-log, all frameworks x tasks, a 1x reference line.
ML-venue conventions: the method in the prominent color, conclusions annotated in the panel.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from afp.evidence import evidence_style, finish, MM

evidence_style(font=8)
OURS, BASE = "#b03060", "#3b7dd8"           # prominent for the method, muted blue for the baseline
GREENA = "#1f8a4c"; RED = "#c0392b"


def panel(ax, sizes, base_rt, ours_rt, base_mem, ours_mem, oom_from, title, gap_txt, mem_txt):
    ax2 = ax.twinx()
    ax.axvspan(oom_from, sizes[-1] * 1.08, color="#fbe9e7", lw=0, zorder=0)
    ax.text(oom_from + (sizes[-1] - oom_from) * .5, ours_rt[-1] * 0.25, "baseline\nOOM", ha="center", va="center", fontsize=8.5,
            color=RED, fontweight="bold", bbox=dict(boxstyle="round,pad=.3", fc="white", ec=RED, lw=.8))
    m = sizes <= oom_from
    ax.plot(sizes[m], base_rt[m], "-o", color=BASE, lw=2, ms=4.5, label="baseline"); ax2.plot(sizes[m], base_mem[m], "--o", color=BASE, lw=1.2, ms=3.5, alpha=.5)
    ax.plot(sizes, ours_rt, "-s", color=OURS, lw=2, ms=4.5, label="ours"); ax2.plot(sizes, ours_mem, "--s", color=OURS, lw=1.2, ms=3.5, alpha=.5)
    ax.set_yscale("log"); ax2.set_yscale("log"); ax.set_xlim(0, sizes[-1] * 1.08)
    ax.set_title(title, fontsize=9, loc="left", fontweight="bold")
    ax.set_xlabel("problem size (×1000 nodes)", fontweight="bold"); ax.set_ylabel("runtime (s)", fontweight="bold")
    ax2.set_ylabel("memory (GB)", color="#666", fontweight="bold"); ax2.tick_params(axis="y", colors="#666")
    i = int(np.sum(m)) - 1
    ax.annotate("", xy=(sizes[i], ours_rt[i]), xytext=(sizes[i], base_rt[i]), arrowprops=dict(arrowstyle="-|>", color=BASE, lw=1.6, mutation_scale=12))
    ax.text(.05, .55, gap_txt, transform=ax.transAxes, color=GREENA, fontsize=9, fontweight="bold", ha="left",
            bbox=dict(boxstyle="round,pad=.25", fc="white", ec=GREENA, lw=.8))
    ax2.text(.36, .90, mem_txt, transform=ax2.transAxes, color=BASE, fontsize=8.5, fontweight="bold", ha="left",
             bbox=dict(boxstyle="round,pad=.25", fc="white", ec=BASE, lw=.8))
    ax.legend(handles=[Line2D([], [], color=BASE, marker="o", lw=2, ms=4, label="baseline"), Line2D([], [], color=OURS, marker="s", lw=2, ms=4, label="ours"),
                       Line2D([], [], color="#444", lw=2, label="runtime"), Line2D([], [], color="#888", ls="--", lw=1.2, label="memory")],
              loc="lower right", fontsize=7, frameon=True, framealpha=.9, edgecolor="#ddd")
    for a in (ax, ax2):
        a.spines["top"].set_visible(False)
    return ax2


fig = plt.figure(figsize=(180 * MM, 68 * MM))
axa = fig.add_axes([.065, .19, .20, .66]); axb = fig.add_axes([.395, .19, .20, .66]); axc = fig.add_axes([.725, .19, .255, .66])
sizes = np.array([1, 2, 4, 8, 12, 16, 20, 30, 40, 50], float)
ours_rt = 6 * sizes ** 1.45; base_rt = 8.2 * ours_rt * (sizes / 16) ** .25
ours_mem = .35 * sizes ** 1.1; base_mem = ours_mem * 9
panel(axa, sizes, base_rt, ours_rt, base_mem, ours_mem, 16, "MIS: runtime & memory", "8.2× faster", "−79 GB")
sizes_t = np.array([1, 2, 3, 4, 6, 10, 15, 20, 30], float)
ours_t = .7 * sizes_t ** 1.7; base_t = 29 * ours_t * (sizes_t / 4) ** .3
panel(axb, sizes_t, base_t, ours_t, .3 * sizes_t ** 1.2, .3 * sizes_t ** 1.2 * 7, 4, "TSP: runtime & memory", "29× faster", "−76 GB")

# (c) speedup panel
n = np.logspace(2, 4.3, 9)
series = [("framework 1, task A", BASE, "-", "o", 1.0 * (n / 100) ** .55), ("framework 1, task B", BASE, "--", "s", .9 * (n / 100) ** .75),
          ("framework 2, task A", GREENA, "-", "^", .8 * (n / 100) ** .45), ("framework 3, task A", OURS, "-", "p", .7 * (n / 100) ** .6),
          ("framework 3, task B", OURS, ":", "h", .75 * (n / 100) ** .58)]
for lab, c, ls, mk, y in series:
    y = np.minimum(y, 30) * (1 + .05 * np.sin(n)); axc.plot(n, y, ls=ls, marker=mk, color=c, lw=1.6, ms=4, mfc="white" if ls != "-" else c, label=lab)
axc.axhline(1, color="#999", lw=.8, ls=":"); axc.text(n[0], 1.08, "1×", color="#999", fontsize=7, style="italic")
axc.set_xscale("log"); axc.set_yscale("log"); axc.set_ylim(.6, 40)
axc.set_xlabel("graph size $n$ (log)", fontweight="bold"); axc.set_ylabel("speedup (×)", fontweight="bold")
axc.set_title("Speedup: frameworks & tasks", fontsize=9, loc="left", fontweight="bold")
axc.legend(fontsize=6.5, loc="upper left", ncol=1, frameon=True, framealpha=.9, edgecolor="#ddd"); finish(axc)
for ax, ch in [(axa, "a"), (axb, "b"), (axc, "c")]:
    bb = ax.get_position(); fig.text(bb.x0 - .045, bb.y1 + .02, f"({ch})", fontsize=11, fontweight="bold")
fig.savefig("examples/figures/12b_after.png", dpi=220); fig.savefig("examples/figures/12b_after.pdf")
print("saved examples/figures/12b_after.{png,pdf}")
