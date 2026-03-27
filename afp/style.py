"""
Publication-quality figure style configuration.

Integrates SciencePlots (academic aesthetics) and tueplots (venue-aware sizing)
with semantic color palettes designed for academic papers.

Usage:
    from afp import setup_style, get_method_colors
    TEXTWIDTH, COLWIDTH = setup_style(venue='icml')
"""
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

# ============================================================
# SciencePlots integration
# ============================================================
try:
    import scienceplots
    HAS_SCIENCEPLOTS = True
except ImportError:
    HAS_SCIENCEPLOTS = False

# ============================================================
# tueplots integration — venue-aware figure sizing
# ============================================================
try:
    from tueplots import bundles, figsizes
    HAS_TUEPLOTS = True
except ImportError:
    HAS_TUEPLOTS = False

# ============================================================
# Venue-specific text widths (inches)
# ============================================================
VENUE_WIDTHS = {
    'neurips': 5.5, 'icml': 6.75, 'icml_half': 3.25,
    'iclr': 5.5, 'nature': 7.09, 'nature_half': 3.54,
    'prl': 3.375, 'prl_full': 6.75, 'pra': 3.375,
    'qst': 3.375, 'quantum': 5.5, 'cvpr': 6.875,
    'aaai': 7.0, 'jmlr': 6.0, 'tmlr': 6.0,
}

# tueplots venue mapping
_TUEPLOTS_BUNDLES = {
    'neurips': lambda: bundles.neurips2024(),
    'icml': lambda: bundles.icml2024(),
    'iclr': lambda: bundles.iclr2024(),
    'cvpr': lambda: bundles.cvpr2024(),
    'aaai': lambda: bundles.aaai2024(),
    'jmlr': lambda: bundles.jmlr2001(),
}

# ============================================================
# Color palettes (colorblind-friendly)
# ============================================================
COLORS_PRIMARY = {
    'ours':      '#E24A33',  # Red/orange — your method (most prominent)
    'baseline1': '#348ABD',  # Blue
    'baseline2': '#988ED5',  # Purple
    'baseline3': '#8EBA42',  # Green
    'baseline4': '#FFB5B8',  # Pink
    'baseline5': '#777777',  # Gray
    'baseline6': '#FBC15E',  # Yellow
    'baseline7': '#8C564B',  # Brown
}

# Semantic colors
COLOR_OURS = '#E24A33'
COLOR_POSITIVE = '#2ecc71'    # Good / improvement
COLOR_NEGATIVE = '#e74c3c'    # Bad / degradation
COLOR_NEUTRAL = '#95a5a6'     # Neutral / reference
COLOR_HIGHLIGHT = '#f39c12'   # Attention / highlight

# Grayscale palette (print-friendly)
COLORS_GRAYSCALE = ['#2d2d2d', '#666666', '#999999', '#cccccc', '#e5e5e5']

# Colormaps
CMAP_SEQUENTIAL = 'viridis'
CMAP_DIVERGING = 'RdBu_r'


def setup_style(venue='icml', fontsize=8, use_scienceplots=True,
                use_tueplots=True):
    """Configure matplotlib for publication-quality figures.

    Applies three layers of configuration:
    1. SciencePlots base academic style
    2. tueplots venue-specific overrides
    3. AFP custom refinements (highest priority)

    Args:
        venue: Target venue ('icml', 'neurips', 'iclr', 'nature', etc.)
        fontsize: Base font size in points
        use_scienceplots: Enable SciencePlots academic style
        use_tueplots: Enable tueplots venue-aware configuration

    Returns:
        (textwidth, colwidth) in inches
    """
    # Layer 1: SciencePlots base
    if use_scienceplots and HAS_SCIENCEPLOTS:
        plt.style.use(['science', 'no-latex'])

    # Layer 2: tueplots venue overrides
    if use_tueplots and HAS_TUEPLOTS and venue in _TUEPLOTS_BUNDLES:
        bundle = _TUEPLOTS_BUNDLES[venue]()
        plt.rcParams.update(bundle)

    # Layer 3: AFP custom (highest priority)
    textwidth = VENUE_WIDTHS.get(venue, 5.5)
    colwidth = textwidth * 0.48

    plt.rcParams.update({
        'font.size': fontsize,
        'axes.labelsize': fontsize,
        'axes.titlesize': fontsize + 1,
        'xtick.labelsize': fontsize - 1,
        'ytick.labelsize': fontsize - 1,
        'legend.fontsize': fontsize - 1,
        'axes.linewidth': 0.6,
        'axes.spines.top': False,
        'axes.spines.right': False,
        'xtick.direction': 'in',
        'ytick.direction': 'in',
        'xtick.major.width': 0.5,
        'ytick.major.width': 0.5,
        'xtick.minor.visible': True,
        'ytick.minor.visible': True,
        'lines.linewidth': 1.2,
        'lines.markersize': 5,
        'legend.frameon': False,
        'legend.handlelength': 1.5,
        'figure.dpi': 150,
        'savefig.dpi': 300,
        'savefig.format': 'pdf',
        'savefig.bbox': 'tight',
        'savefig.pad_inches': 0.02,
        'figure.constrained_layout.use': True,
    })

    return textwidth, colwidth


def get_figsize(venue='icml', nrows=1, ncols=1, ratio='golden'):
    """Calculate venue-aware figure dimensions.

    Args:
        venue: Target venue
        nrows, ncols: Subplot grid dimensions
        ratio: 'golden' (1.618), 'square' (1.0), 'wide' (2.0), or float

    Returns:
        (width, height) tuple in inches
    """
    textwidth = VENUE_WIDTHS.get(venue, 5.5)
    ratio_map = {'golden': 1.618, 'square': 1.0, 'wide': 2.0, 'ultrawide': 3.0}
    r = ratio_map.get(ratio, ratio) if isinstance(ratio, str) else ratio
    width = textwidth
    height = (width / ncols) / r * nrows
    return (width, height)


def get_method_colors(method_names, ours_name='Ours'):
    """Assign colors to methods. 'Ours' always gets the prominent red.

    Args:
        method_names: List of method names
        ours_name: Substring to identify your method (case-insensitive)

    Returns:
        Dict mapping method names to hex color strings
    """
    palette = list(COLORS_PRIMARY.values())
    colors = {}
    ours_idx = None
    for i, name in enumerate(method_names):
        if ours_name.lower() in name.lower():
            colors[name] = COLORS_PRIMARY['ours']
            ours_idx = i
        else:
            baseline_idx = i if ours_idx is None else i - 1
            colors[name] = palette[min(baseline_idx + 1, len(palette) - 1)]
    return colors
