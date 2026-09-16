"""Example 12d: ridge distributions + prediction curve + resolution panel (synthetic).

Form of the author-accepted "damage" figure:
(a) stacked per-sample distributions of the learner shift, control (grey) against defect (blue),
    for three cohort sizes, with the squared norm printed beside each pair;
(b) a ratio against a noise-floor variable on a log axis: light points are simulated cohorts,
    filled markers the measured cohorts with intervals, and two parameter-free prediction lines
    (dashed 1-2x, dotted 1-x) drawn without fitting;
(c) resolution panel: the control interval as a grey band and the defect interval as a bar,
    per cohort, in units of the witness.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from afp.evidence import (evidence_style, finish, letter, note, BLUE, BLUE_D, BLUE_L, GREY, GREY_D, INK, INK2, INK3, GRID, MM)

rng = np.random.default_rng(9)
evidence_style()
DATA = {}


def smooth_density(v, lim, bins=70, sigma=2.0):
    h, e = np.histogram(v, bins=bins, range=lim, density=True)
    k = np.arange(-6, 7); g = np.exp(-k ** 2 / (2 * sigma ** 2)); g /= g.sum()
    return (e[:-1] + e[1:]) / 2, np.convolve(h, g, mode="same")


fig = plt.figure(figsize=(180 * MM, 75 * MM))
# ---------- (a) ridges ----------
axa = fig.add_axes([.05, .14, .27, .78]); lim = (-.45, .45)
rows = [("12 sessions · 36 states", 36, .11, .12), ("24 sessions · 71 states", 71, .075, .09), ("108 sessions · 320 states", 320, .034, .09)]
for i, (lab, n, sc, sd) in enumerate(rows):
    y0 = (2 - i) * 1.15
    ctrl = rng.normal(0, sc, n * 5); dft = rng.normal(-.03, sd, n * 5)
    DATA[f"shift_control_row{i}"] = ctrl; DATA[f"shift_defect_row{i}"] = dft
    for v, c, cd, z in [(ctrl, GREY, GREY_D, 2), (dft, BLUE, BLUE_D, 3)]:
        xs, d = smooth_density(v, lim); d = d / d.max() * .95
        axa.fill_between(xs, y0, y0 + d, color=c, alpha=.45, lw=0, zorder=z); axa.plot(xs, y0 + d, color=cd, lw=.9, zorder=z + 1)
    axa.text(lim[0] + .01, y0 + .99, lab, fontsize=7.5, color=INK, va="bottom")
axa.axvline(0, color=INK3, lw=.6, zorder=1)
axa.set_xlim(*lim); axa.set_ylim(-.05, 4.05); axa.set_yticks([]); axa.spines["left"].set_visible(False)
axa.set_xticks([-.4, -.2, 0, .2, .4]); axa.set_xlabel(r"learner shift per state,  $\delta f(X)$", labelpad=2)
axa.legend(handles=[Line2D([], [], color=GREY_D, lw=6, alpha=.5, label="control: two clean learners"), Line2D([], [], color=BLUE_D, lw=6, alpha=.5, label="defect: record reuse")],
           loc="upper left", bbox_to_anchor=(0, 1.0), fontsize=7, handlelength=1.2, borderaxespad=0, labelspacing=.25)
finish(axa)

# ---------- (b) ratio vs noise floor with prediction lines ----------
axb = fig.add_axes([.40, .14, .36, .78])
x = np.logspace(-2.2, 0, 300)
axb.plot(x, 1 - 2 * x, color=INK, lw=1.4, ls=(0, (4, 2)), zorder=4); axb.plot(x, 1 - x, color=INK3, lw=1.0, ls=":", zorder=4)
sim_x = np.logspace(-2.1, -.4, 120); sim_y = 1 - 2 * sim_x + rng.normal(0, .05, 120) * (sim_x / .3) ** .5
axb.scatter(sim_x, sim_y, s=7, c=BLUE, alpha=.35, linewidths=0, zorder=2)
hw = [("A", .028, .97, .06, "o", (-.10, .09)), ("B", .035, .93, .09, "o", (-.10, -.17)), ("C", .046, .91, .11, "s", (.12, .06)),
      ("D", .12, .70, .22, "s", (.12, .06)), ("E", .27, .57, .32, "^", (.12, .06)), ("F", .31, .10, .40, "^", (.12, .04))]
for lab, xh, yh, e, mk, (dx, dy) in hw:
    axb.errorbar(xh, yh, yerr=e, fmt=mk, color=BLUE_D, ms=6, mfc=BLUE_D, mec="white", mew=.7, lw=1.1, capsize=0, zorder=6)
    axb.text(xh * 10 ** dx, yh + dy, f"cohort {lab}", fontsize=7, color=INK2, ha="left" if dx > 0 else "right")
axb.set_xscale("log"); axb.set_xlim(7e-3, 1.05); axb.set_ylim(-.6, 1.15)
axb.axhline(0, color=INK3, lw=.6); axb.axhline(1, color=GRID, lw=.6)
axb.set_xlabel(r"$x=v_0/\Delta W$  (noise floor over witness)", labelpad=2); axb.set_ylabel(r"price ratio  $\Delta R/\Delta W$", labelpad=2)
note(axb, .02, -.35, "prediction, no fit:  $1-2x$", size=7.5, color=INK); note(axb, .25, .85, "$1-x$", size=7.5, color=INK3)
note(axb, 8e-3, -.55, "light points: simulated cohorts, one per draw", size=7, color=BLUE_D, va="bottom")
finish(axb)

# ---------- (c) resolution panel ----------
axc = fig.add_axes([.83, .14, .15, .78])
xc = np.arange(6)
ctrl_lo = np.array([-.04, .04, .04, .05, -.65, -.6]); ctrl_hi = np.array([.02, .12, .12, .13, .20, .75])
dft_m = np.array([.97, .93, .91, .70, .57, .10]); dft_e = np.array([.06, .09, .11, .22, .32, .40])
for i in range(6):
    axc.add_patch(plt.Rectangle((i - .32, ctrl_lo[i]), .64, ctrl_hi[i] - ctrl_lo[i], color=GRID, lw=0, zorder=1))
    axc.plot([i - .32, i + .32], [(ctrl_lo[i] + ctrl_hi[i]) / 2] * 2, color=INK2, lw=1.0, zorder=2)
axc.errorbar(xc, dft_m, yerr=dft_e, fmt="o", color=BLUE_D, ms=4.5, lw=1.1, capsize=0, zorder=4)
axc.axhline(1, color=INK3, lw=.6, ls=":"); axc.axhline(0, color=INK3, lw=.6)
axc.set_xticks(xc); axc.set_xticklabels(list("ABCDEF"), fontsize=7.5); axc.set_ylim(-1.2, 1.25)
axc.set_ylabel(r"$\Delta R$ in units of $\Delta W$", labelpad=2)
note(axc, 5.3, 1.03, "full price", size=7, color=INK2, ha="right", va="bottom")
axc.legend(handles=[Line2D([], [], color=GRID, lw=8, label="zero-defect control"), Line2D([], [], marker="o", lw=0, color=BLUE_D, ms=4.5, label="record reuse")],
           loc="lower left", fontsize=7, handlelength=1.2, borderaxespad=0)
finish(axc)
letter(fig, axa, "a", dx=-.04, style="bold"); letter(fig, axb, "b", dx=-.06, style="bold"); letter(fig, axc, "c", dx=-.07, style="bold")
DATA.update(sim_x=sim_x, sim_ratio=sim_y, hw_x=np.array([h[1] for h in hw]), hw_ratio=np.array([h[2] for h in hw]), hw_err=np.array([h[3] for h in hw]),
            resolution_control_lo=ctrl_lo, resolution_control_hi=ctrl_hi, resolution_defect=dft_m, resolution_defect_err=dft_e)
np.savez("examples/data/12d.npz", **DATA)
fig.savefig("examples/figures/12d_after.png", dpi=220); fig.savefig("examples/figures/12d_after.pdf")
print("saved examples/figures/12d_after.{png,pdf}")
