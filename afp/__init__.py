"""
Academic Figure Patterns (AFP)
Design patterns for publication-quality academic figures.

Provides:
- Venue-aware figure sizing (via tueplots integration)
- Publication-ready matplotlib style (via SciencePlots integration)
- Color palettes with semantic meaning
- Helper functions for annotations, reference lines, and visual storytelling
"""

from afp.style import (
    setup_style,
    get_figsize,
    get_method_colors,
    COLORS_PRIMARY,
    COLOR_OURS,
    COLOR_POSITIVE,
    COLOR_NEGATIVE,
    COLOR_NEUTRAL,
    COLOR_HIGHLIGHT,
    COLORS_GRAYSCALE,
    CMAP_SEQUENTIAL,
    CMAP_DIVERGING,
    VENUE_WIDTHS,
    HAS_SCIENCEPLOTS,
    HAS_TUEPLOTS,
)

from afp.helpers import (
    save_fig,
    add_panel_labels,
    add_reference_line,
    add_vref_line,
    annotate_best,
    annotate_gap,
    significance_bracket,
    add_shaded_region,
    add_inset_zoom,
    sorted_bar_data,
)

from afp.evidence import (
    structure_strength,
    paired_cloud,
    binned_median,
    peak_normalized_hist,
    ecdf,
    exceedance_curve,
    fraction_below_diagonal,
)

__version__ = "0.2.1"
__all__ = [
    # Style
    "setup_style", "get_figsize", "get_method_colors",
    # Colors
    "COLORS_PRIMARY", "COLOR_OURS", "COLOR_POSITIVE", "COLOR_NEGATIVE",
    "COLOR_NEUTRAL", "COLOR_HIGHLIGHT", "COLORS_GRAYSCALE",
    "CMAP_SEQUENTIAL", "CMAP_DIVERGING", "VENUE_WIDTHS",
    # Flags
    "HAS_SCIENCEPLOTS", "HAS_TUEPLOTS",
    # Helpers
    "save_fig", "add_panel_labels", "add_reference_line", "add_vref_line",
    "annotate_best", "annotate_gap", "significance_bracket",
    "add_shaded_region", "add_inset_zoom", "sorted_bar_data",
    # Per-sample evidence (Pattern 11)
    "structure_strength", "paired_cloud", "binned_median", "peak_normalized_hist",
    "ecdf", "exceedance_curve", "fraction_below_diagonal",
]
