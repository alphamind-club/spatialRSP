import numpy as np


def compute_area_under_cdf(
    hist: np.ndarray, bins: np.ndarray, coverage: float = None, mode: str = "absolute"
) -> tuple[float, np.ndarray]:
    """Compute scaled area under the CDF of a histogram.

    Args:
        hist (np.ndarray): Histogram counts.
        bins (np.ndarray): Bin edges.
        coverage (float, optional): Foreground-to-background ratio. Used in absolute mode.
        mode (str): Either "absolute" or "relative".

    Returns:
        tuple[float, np.ndarray]: Scaled area under the CDF and the CDF array.
    """
    cdf = np.cumsum(hist)
    bin_centers = (bins[:-1] + bins[1:]) / 2
    area = np.trapezoid(cdf, x=bin_centers)
    window_width = bins[-1] - bins[0]
    scaled_area = area * (2 / window_width)
    if mode == "absolute" and coverage is not None:
        scaled_area *= coverage
    return scaled_area, cdf
