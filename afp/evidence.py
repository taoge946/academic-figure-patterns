"""Per-sample evidence helpers (Pattern 11).

Small, dependency-free functions that draw the forms an author kept accepting in place of
point-and-interval panels: paired clouds with null references, binned medians, peak-normalized
overlaid distributions, ECDF and exceedance curves, plus a numeric load-bearing check to run
*before* drawing.  Nothing here fits or resamples; inputs are the archived per-sample arrays.
"""
import numpy as np

INK = "#2b2b2b"
INK2 = "#6e6e6e"


def structure_strength(x, y, kind="paired", nbins=10):
    """Numeric load-bearing test from docs/FORM_LADDER.md.

    kind="paired":     passes when |corr| > 0.9 (or the caller argues the non-diagonal shape is the claim).
    kind="mechanism":  passes when |corr| > 0.5 OR the rise of binned medians exceeds the median IQR width.
    Returns a dict with the numbers and a boolean 'passes'.
    """
    x = np.asarray(x, float); y = np.asarray(y, float)
    m = np.isfinite(x) & np.isfinite(y); x, y = x[m], y[m]
    r = float(np.corrcoef(x, y)[0, 1]) if len(x) > 2 else float("nan")
    out = dict(n=int(len(x)), corr=r)
    if kind == "paired":
        out["passes"] = abs(r) > 0.9
        return out
    q = np.quantile(x, np.linspace(0, 1, nbins + 1))
    med, iqr = [], []
    for lo, hi in zip(q[:-1], q[1:]):
        s = (x >= lo) & (x <= hi)
        if s.sum() >= 5:
            med.append(np.median(y[s])); iqr.append(np.subtract(*np.percentile(y[s], [75, 25])))
    rise = float(np.max(med) - np.min(med)) if med else float("nan")
    band = float(np.median(iqr)) if iqr else float("nan")
    out.update(median_rise=rise, median_iqr=band, passes=(abs(r) > 0.5) or (rise > band))
    return out


def paired_cloud(ax, x, y, color, s=3.4, alpha=0.32, identity=True, zero=False, lim=None, zorder=3):
    """Per-sample x-y cloud with null references (identity line and/or zero line)."""
    ax.scatter(x, y, s=s, c=color, alpha=alpha, linewidths=0, rasterized=True, zorder=zorder)
    if lim is None:
        v = np.nanmax(np.abs(np.concatenate([np.asarray(x, float), np.asarray(y, float)])))
        lim = (-1.05 * v, 1.05 * v)
    if identity:
        ax.plot(lim, lim, color=INK, lw=0.9, ls=(0, (3, 1.8)), zorder=zorder + 1)
    if zero:
        ax.axhline(0, color=INK, lw=0.6, zorder=zorder + 1)
    ax.set_xlim(*lim); ax.set_ylim(*lim)
    return lim


def binned_median(ax, x, y, nbins=10, color="k", lw=1.0, band=True, band_alpha=0.12, min_count=5):
    """Binned medians (quantile bins in x) with an optional IQR band; returns the bin centers and medians."""
    x = np.asarray(x, float); y = np.asarray(y, float)
    m = np.isfinite(x) & np.isfinite(y); x, y = x[m], y[m]
    q = np.quantile(x, np.linspace(0, 1, nbins + 1))
    xc, med, lo, hi = [], [], [], []
    for a, b in zip(q[:-1], q[1:]):
        s = (x >= a) & (x <= b)
        if s.sum() >= min_count:
            xc.append(np.median(x[s])); med.append(np.median(y[s]))
            p25, p75 = np.percentile(y[s], [25, 75]); lo.append(p25); hi.append(p75)
    if band and xc:
        ax.fill_between(xc, lo, hi, color=color, alpha=band_alpha, lw=0, zorder=4)
    ax.plot(xc, med, color=color, lw=lw, marker="o", ms=3, mfc="white", mew=0.8, zorder=5)
    return np.array(xc), np.array(med)


def peak_normalized_hist(ax, values, edges, color, edge_color=None, alpha=0.32, lw=0.9, zorder=2):
    """One overlaid distribution on a common bin grid, scaled to unit peak (compare widths, not counts)."""
    h, _ = np.histogram(np.asarray(values, float), bins=edges, density=True)
    if h.max() > 0:
        h = h / h.max()
    xa = (edges[:-1] + edges[1:]) / 2
    ax.fill_between(xa, 0, h, step="mid", color=color, alpha=alpha, lw=0, zorder=zorder)
    ax.step(xa, h, where="mid", color=edge_color or color, lw=lw, zorder=zorder + 2)
    ax.set_ylim(0, 1.3); ax.set_yticks([]); ax.spines["left"].set_visible(False)
    return h


def ecdf(ax, values, color, lw=1.2, ls="-", label=None, zorder=3):
    """Empirical CDF over samples (higher curve = more samples below a given value)."""
    v = np.sort(np.asarray(values, float)); v = v[np.isfinite(v)]
    y = np.arange(1, len(v) + 1) / len(v)
    ax.step(v, y, where="post", color=color, lw=lw, ls=ls, label=label, zorder=zorder)
    if ax.get_yscale() == "linear":
        ax.set_ylim(0, 1)
    return v, y


def exceedance_curve(ax, values, color, xs=None, floor=1e-4, lw=1.2, ls="-", label=None, zorder=3):
    """Fraction of samples whose value exceeds x, for a grid of x.  Draw on a log y axis to read the tails."""
    v = np.asarray(values, float); v = v[np.isfinite(v)]
    if xs is None:
        xs = np.linspace(0, np.percentile(v, 99.5), 301)
    frac = np.array([(v > x).mean() for x in xs])
    ax.plot(xs, np.maximum(frac, floor), color=color, lw=lw, ls=ls, label=label, zorder=zorder)
    return xs, frac


def fraction_below_diagonal(x_err, y_err):
    """Share of samples where the y-axis method has the smaller error (for error-vs-error clouds)."""
    x = np.asarray(x_err, float); y = np.asarray(y_err, float)
    m = np.isfinite(x) & np.isfinite(y)
    return float((y[m] < x[m]).mean())
