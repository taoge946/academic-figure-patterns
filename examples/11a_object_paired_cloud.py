"""Pattern 11, example A: object -> per-sample paired cloud -> endpoint (synthetic data).

Reproduces the form of an author-accepted "design channel" figure with generated data:
(a) the object itself: one measurement record, 64 settings x 6 qubits, as three blocks
    (clean / arbitrary replacement / composition-matched replacement) with axis-pair counts;
(b) per-sample paired cloud: label shift under fresh-shot replacement against the shift under
    shared-shot replacement (identity line), and the composition-matched shift (zero line);
(c) endpoint: pooled witness increment against dose, last and smallest.
Every number is synthetic; the point is the composition and the reading order.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.lines import Line2D
from afp.evidence import (evidence_style, finish, letter, note, paired_cloud, structure_strength,
                          BLUE, BLUE_D, ORANGE, ORANGE_D, INK, INK2, INK3, GRID, MM)

rng = np.random.default_rng(7)
M, Q, D = 64, 6, 16                      # settings, qubits, borrowed settings
evidence_style()

# ---------- synthetic object: axis matrix and two replacement blocks ----------
clean = rng.integers(0, 3, size=(M, Q))                       # 0=X 1=Y 2=Z
rows = rng.choice(M, D, replace=False)
arbitrary = clean.copy(); arbitrary[rows] = rng.integers(0, 3, size=(D, Q))
matched = clean.copy()
for r in rows:                                                # keep each row's axis multiset
    matched[r] = rng.permutation(clean[r])


def pair_counts(A):
    c = np.zeros((3, 3), int)
    for a, b in zip(A[:, 0], A[:, 1]):
        c[a, b] += 1
    return c


# ---------- synthetic per-sample shifts (1,600 rows) ----------
n = 1600
comp_change = np.abs(pair_counts(arbitrary) - pair_counts(clean)).sum() / (2 * D)
shared = rng.normal(0, 0.06, n) * (1 + comp_change) + rng.normal(0, 0.01, n)
disjoint = shared + rng.normal(0, 0.006, n)                    # fresh shots reproduce the shift
matchedshift = rng.normal(0, 0.008, n)                         # matching removes it
print(structure_strength(shared, disjoint, "paired"))

# ---------- synthetic dose curve ----------
doses = np.array([3, 6, 16, 32, 64]) / M
dW = 9e-3 * doses ** 1.6; ci = 0.35 * dW + 2.5e-4

fig = plt.figure(figsize=(180 * MM, 92 * MM))
cmap = ListedColormap(["#d9e6f7", "#7fa9df", BLUE_D])
titles = ["reference", "replacement A", "replacement B"]
for k, (A, t) in enumerate(zip([clean, arbitrary, matched], titles)):
    ax = fig.add_axes([.055 + k * .115, .35, .10, .55])
    ax.imshow(A, cmap=cmap, aspect="auto", interpolation="nearest")
    if k > 0:
        for r in rows:
            ax.axhspan(r - .5, r + .5, xmin=0, xmax=1, color=ORANGE if k == 2 else INK, alpha=.18, lw=0)
    ax.set_xticks(range(Q)); ax.set_xticklabels([f"c{i + 1}" for i in range(Q)], fontsize=6.5)
    ax.set_yticks([0, 31, 63]); ax.set_yticklabels(["1", "32", "64"] if k == 0 else [])
    ax.tick_params(length=0); ax.grid(False)
    for s in ax.spines.values():
        s.set_edgecolor(GRID)
    ax.set_title(t, pad=3, fontsize=8.5)
    # axis-pair counts of qubits (1,2) under each block
    axc = fig.add_axes([.055 + k * .115, .09, .10, .16])
    c = pair_counts(A)
    axc.imshow(c, cmap="Greys", vmin=0, vmax=c.max() * 1.6, aspect="auto", interpolation="nearest")
    for i in range(3):
        for j in range(3):
            axc.text(j, i, str(c[i, j]), ha="center", va="center", fontsize=7, color=INK)
    axc.set_xticks(range(3)); axc.set_yticks(range(3))
    axc.set_xticklabels(["X", "Y", "Z"], fontsize=6.5); axc.set_yticklabels(["X", "Y", "Z"] if k == 0 else [], fontsize=6.5)
    axc.tick_params(length=0); axc.grid(False)
    for s in axc.spines.values():
        s.set_edgecolor(GRID)
ax0 = fig.axes[0]
ax0.set_ylabel("row", labelpad=2)
fig.text(.055, .265, "pair counts, columns 1 and 2", fontsize=7.5, color=INK2)
fig.legend(handles=[Line2D([], [], marker="s", ms=6, lw=0, mfc=c, mec="none", label=l) for c, l in
                    [("#d9e6f7", "X"), ("#7fa9df", "Y"), (BLUE_D, "Z")]],
           loc="lower left", bbox_to_anchor=(.055, .0), ncol=3, fontsize=7, handletextpad=.3, columnspacing=.8, borderaxespad=0)

# (b) paired cloud
axb = fig.add_axes([.47, .16, .26, .74])
lim = (-.27, .27)
paired_cloud(axb, shared, disjoint, BLUE, identity=True, zero=False, lim=lim)
paired_cloud(axb, shared, matchedshift, ORANGE, identity=False, zero=True, lim=lim)
axb.axvline(0, color=INK3, lw=.5, zorder=1)
axb.set_xlabel("per-sample shift, scheme A", labelpad=2)
axb.set_ylabel("per-sample shift, other scheme", labelpad=2)
axb.set_xticks([-.2, 0, .2]); axb.set_yticks([-.2, 0, .2])
note(axb, .25, .215, "$y=x$", ha="right", size=7.5, color=INK2)
note(axb, -.25, .235, "scheme B", size=7.5, color=BLUE_D)
note(axb, -.25, .19, "scheme C (control)", size=7.5, color=ORANGE_D)
finish(axb)

# (c) endpoint, smallest and last
axc = fig.add_axes([.80, .16, .18, .74])
axc.axhspan(-2e-4, 2e-4, color=GRID, lw=0, zorder=0)
axc.errorbar(doses * .97, dW, yerr=ci, fmt="o", color=BLUE_D, ms=3.5, lw=.9, capsize=1.2, label="scheme A")
axc.errorbar(doses * 1.03, dW * 1.02, yerr=ci, fmt="o", mfc="white", color=BLUE, ms=3.5, lw=.9, capsize=1.2, label="scheme B")
axc.plot(doses, dW, color=BLUE_D, lw=.8, alpha=.6)
axc.set_yscale("symlog", linthresh=5e-4); axc.set_xscale("log")
axc.set_xticks(doses); axc.set_xticklabels(["", "", "", "", ""], fontsize=7)
axc.set_xlabel("dose (log)", labelpad=2)
axc.set_ylabel("pooled statistic", labelpad=2)
axc.legend(loc="upper left", fontsize=7, handletextpad=.3, borderaxespad=.2)
finish(axc)

letter(fig, ax0, "a", dx=-.04, dy=.04); letter(fig, axb, "b", dx=-.07); letter(fig, axc, "c", dx=-.07)
np.savez("examples/data/11a.npz", reference_matrix=clean, replacementA_matrix=arbitrary, replacementB_matrix=matched, replaced_rows=rows,
         shift_schemeA=shared, shift_schemeB=disjoint, shift_schemeC=matchedshift, dose=doses, pooled_stat=dW, pooled_stat_ci=ci)
fig.savefig("examples/figures/11a_after.png", dpi=220)
fig.savefig("examples/figures/11a_after.pdf")
print("saved examples/figures/11a_after.{png,pdf}")
