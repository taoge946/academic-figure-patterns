"""Numeric checks for afp.evidence: the quantities the example figures print and plot."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pytest

from afp.evidence import (binned_median, ecdf, exceedance_curve, fraction_below_diagonal,
                          paired_cloud, peak_normalized_hist, structure_strength)


@pytest.fixture
def ax():
    fig, ax = plt.subplots()
    yield ax
    plt.close(fig)


def test_structure_strength_paired():
    rng = np.random.default_rng(0)
    x = rng.normal(size=2000)
    assert structure_strength(x, x + rng.normal(0, 0.05, 2000))["passes"]
    out = structure_strength(x, rng.normal(size=2000))
    assert not out["passes"] and abs(out["corr"]) < 0.1 and out["n"] == 2000


def test_structure_strength_ignores_nonfinite():
    x = np.array([0.0, 1.0, 2.0, 3.0, np.nan, 5.0])
    y = np.array([0.0, 1.0, 2.0, np.inf, 4.0, 5.0])
    out = structure_strength(x, y)
    assert out["n"] == 4 and out["corr"] == pytest.approx(1.0)


def test_structure_strength_mechanism_uses_median_rise():
    rng = np.random.default_rng(1)
    x = rng.uniform(0, 1, 5000)
    # step function: weak linear correlation is not required when binned medians rise clearly
    y = np.where(x > 0.5, 1.0, 0.0) + rng.normal(0, 0.3, 5000)
    out = structure_strength(x, y, kind="mechanism")
    assert out["median_rise"] > out["median_iqr"] and out["passes"]
    flat = structure_strength(x, rng.normal(size=5000), kind="mechanism")
    assert not flat["passes"]


def test_fraction_below_diagonal():
    assert fraction_below_diagonal([1, 1, 1, 1], [0, 0, 2, 2]) == 0.5
    assert fraction_below_diagonal([1, np.nan, 1], [0, 0, 0]) == 1.0


def test_binned_median_recovers_trend(ax):
    rng = np.random.default_rng(2)
    x = rng.uniform(0, 10, 4000)
    y = 2 * x + rng.normal(0, 0.5, 4000)
    xc, med = binned_median(ax, x, y, nbins=8)
    assert len(xc) == 8
    np.testing.assert_allclose(med, 2 * xc, atol=0.3)


def test_peak_normalized_hist_has_unit_peak(ax):
    h = peak_normalized_hist(ax, np.random.default_rng(3).normal(size=1000),
                             np.linspace(-4, 4, 41), color="k")
    assert h.max() == pytest.approx(1.0) and h.min() >= 0


def test_ecdf_and_exceedance_are_complementary(ax):
    v = np.array([0.1, 0.2, 0.2, 0.5, 1.0])
    xs_sorted, y = ecdf(ax, v, color="k")
    np.testing.assert_allclose(y, [0.2, 0.4, 0.6, 0.8, 1.0])
    xs, frac = exceedance_curve(ax, v, color="k", xs=np.array([0.0, 0.2, 0.5, 1.0]))
    np.testing.assert_allclose(frac, [1.0, 0.4, 0.2, 0.0])


def test_paired_cloud_symmetric_limits(ax):
    lim = paired_cloud(ax, [1.0, -2.0], [0.5, 0.0], color="k")
    assert lim[0] == pytest.approx(-lim[1]) and lim[1] == pytest.approx(2.1)
