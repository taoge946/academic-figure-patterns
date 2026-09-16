"""Example 12e: 2-D parameter-grid heat map of a *measured* quantity with a prediction contour (synthetic).

A form common in PRX Quantum papers: the measured quantity over a grid of two experimental
parameters as a heat map, the theory boundary drawn as a parameter-free contour on top, and
two line cuts on the right that show the same crossing with error bars.  Note the difference
from the rejected "tiles of binned means": every cell here is a measurement on its own grid
point, and the contour is a prediction, not a fit.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import TwoSlopeNorm, LinearSegmentedColormap
from afp.evidence import (evidence_style, finish, letter, note, BLUE, BLUE_D, ORANGE, ORANGE_D, INK, INK2, INK3, GRID, MM)

rng = np.random.default_rng(13)
evidence_style()
overlap = np.linspace(0, 1, 21)          # fraction of borrowed settings
budget = np.array([4, 8, 16, 32, 64, 128, 256, 512, 1024])  # shots per setting
O, B = np.meshgrid(overlap, budget)
true = 0.9 * O ** 1.5 / (1 + (B / 64.0) ** .8) - 0.12 * (1 - O) / np.sqrt(B / 8.0)   # crosses zero along a curve
meas = true + rng.normal(0, 0.02, true.shape)
cmap = LinearSegmentedColormap.from_list("ow", [ORANGE_D, ORANGE, "white", BLUE, BLUE_D])
norm = TwoSlopeNorm(vmin=-.25, vcenter=0, vmax=.75)

fig = plt.figure(figsize=(180 * MM, 72 * MM))
axa = fig.add_axes([.07, .16, .50, .66])
im = axa.pcolormesh(np.arange(len(overlap) + 1) - .5, np.arange(len(budget) + 1) - .5, meas, cmap=cmap, norm=norm, shading="flat", rasterized=True)
# prediction contour (zero crossing of the model) on the same grid, no fit
cs = axa.contour(np.arange(len(overlap)), np.arange(len(budget)), true, levels=[0], colors=[INK], linewidths=1.3, linestyles="--")
axa.set_xticks(np.arange(0, 21, 5)); axa.set_xticklabels(["0", "0.25", "0.5", "0.75", "1"])
axa.set_yticks(np.arange(len(budget))); axa.set_yticklabels([str(i + 1) for i in range(len(budget))])
axa.set_xlabel("parameter 1", labelpad=2); axa.set_ylabel("parameter 2", labelpad=2)
axa.tick_params(length=0); axa.grid(False)
for s in axa.spines.values():
    s.set_edgecolor(GRID)
note(axa, 4.3, 8.0, "prediction: zero crossing", size=7.5, color=INK, va="center")
cax = fig.add_axes([.07, .885, .25, .025])
cb = fig.colorbar(im, cax=cax, orientation="horizontal", ticks=[-.2, 0, .2, .4, .6]); cb.ax.tick_params(length=2, labelsize=7)
cb.ax.set_title("measured quantity", fontsize=7.5, pad=2, loc="left")
for s in cb.ax.spines.values():
    s.set_visible(False)
# two line cuts
for k, (irow, c, cd, lab) in enumerate([(1, ORANGE, ORANGE_D, "cut A"), (5, BLUE, BLUE_D, "cut B")]):
    axa.plot([-.5, 20.5], [irow, irow], color=cd, lw=.9, ls=(0, (2, 2)), zorder=5)
    ax = fig.add_axes([.68, .58 - k * .42, .30, .34])
    y = meas[irow]; e = np.full_like(y, .02) * (1 + rng.uniform(0, .6, len(y)))
    ax.fill_between(overlap, true[irow] - .02, true[irow] + .02, color=GRID, lw=0, zorder=1)
    ax.plot(overlap, true[irow], color=INK, lw=1.0, ls="--", zorder=3)
    ax.errorbar(overlap, y, yerr=e, fmt="o", color=cd, ms=3, lw=.8, capsize=0, zorder=4)
    ax.axhline(0, color=INK3, lw=.6)
    ax.set_xlim(-.02, 1.02); ax.set_ylim(-.3, .8); ax.set_yticks([0, .4, .8])
    ax.set_xticks([0, .5, 1]); ax.set_xticklabels(["0", "0.5", "1"] if k == 1 else [])
    note(ax, .02, .72, lab, size=7.5, color=cd); finish(ax)
    zero = overlap[np.argmin(np.abs(true[irow]))]
    ax.axvline(zero, color=cd, lw=.7, ls=":"); note(ax, zero + .02, -.22, "crossing", size=7, color=INK2)
    if k == 1:
        ax.set_xlabel("parameter 1", labelpad=2)
    if k == 0:
        ax.set_ylabel("measured quantity", labelpad=2)
fig.text(.015, .93, "(a)", fontsize=11, fontweight="bold", color=INK); letter(fig, fig.axes[-2], "b", dx=-.07); letter(fig, fig.axes[-1], "c", dx=-.07)
np.savez("examples/data/12e.npz", parameter1=overlap, parameter2=budget, measured=meas, model=true)
fig.savefig("examples/figures/12e_after.png", dpi=220); fig.savefig("examples/figures/12e_after.pdf")
print("saved examples/figures/12e_after.{png,pdf}")
