"""setup_style must work on machines without LaTeX (tueplots bundles default to usetex=True)."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pytest

import afp.style as style
from afp import get_figsize, get_method_colors, setup_style

VENUES = ["icml", "neurips", "iclr", "cvpr", "aaai", "jmlr", "nature", "prl"]


@pytest.fixture(autouse=True)
def reset_rc():
    with plt.rc_context():
        yield


@pytest.mark.parametrize("venue", VENUES)
def test_setup_style_without_latex_renders(venue, monkeypatch):
    monkeypatch.setattr(style, "latex_available", lambda: False)
    textwidth, colwidth = setup_style(venue=venue)
    assert plt.rcParams["text.usetex"] is False
    assert textwidth == style.VENUE_WIDTHS[venue] and colwidth < textwidth
    fig, ax = plt.subplots()
    ax.set_ylabel("Score (%)")  # a bare % must survive when usetex is off
    fig.canvas.draw()
    plt.close(fig)


def test_setup_style_usetex_follows_argument():
    setup_style(venue="icml", usetex=True)
    assert plt.rcParams["text.usetex"] is True
    setup_style(venue="icml", usetex=False)
    assert plt.rcParams["text.usetex"] is False


def test_get_figsize_scales_with_rows():
    w, h1 = get_figsize("icml", nrows=1, ncols=2)
    _, h2 = get_figsize("icml", nrows=2, ncols=2)
    assert w == style.VENUE_WIDTHS["icml"] and h2 == pytest.approx(2 * h1)


def test_get_method_colors_marks_ours():
    colors = get_method_colors(["GNN", "Transformer", "Ours"])
    assert colors["Ours"] == style.COLOR_OURS
    assert len(set(colors.values())) == 3
