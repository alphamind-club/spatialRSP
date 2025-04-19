import numpy as np

from spatialrsp.core.cdf import compute_area_under_cdf


def compute_angular_area(
    theta_fg1: np.ndarray,
    theta_bg: np.ndarray,
    scanning_window: float,
    resolution: int,
    scanning_range: np.ndarray,
    theta_fg2: np.ndarray = None,
    mode: str = "absolute",
) -> tuple:
    """Compute angular bias curves from foreground/background angular distributions.

    Args:
        theta_fg1 (np.ndarray): Foreground 1 angular values (radians).
        theta_bg (np.ndarray): Background angular values (radians).
        scanning_window (float): Width of the angular scanning window (radians).
        resolution (int): Number of bins within the scanning window.
        scanning_range (np.ndarray): List of center angles to scan over.
        theta_fg2 (np.ndarray, optional): Foreground 2 angular values (for relative mode).
        mode (str): Either "absolute" or "relative".

    Returns:
        tuple: In absolute mode: (fg_area, expected_fg_area, bg_area).
               In relative mode: (fg1_area, fg2_area, bg_area).
    """
    bins = np.linspace(-scanning_window / 2, scanning_window / 2, resolution + 1)
    coverage = len(theta_fg1) / len(theta_bg)

    abs_area_fg1 = np.zeros(len(scanning_range))
    abs_area_fg2 = np.zeros(len(scanning_range)) if theta_fg2 is not None else None
    abs_area_bg = np.zeros(len(scanning_range))
    abs_area_exp_fg = np.zeros(len(scanning_range)) if theta_fg2 is None else None

    for i, center in enumerate(scanning_range):
        rel_theta_fg1 = ((theta_fg1 - center + np.pi) % (2 * np.pi)) - np.pi
        rel_theta_bg = ((theta_bg - center + np.pi) % (2 * np.pi)) - np.pi

        mask_fg1 = np.abs(rel_theta_fg1) <= scanning_window / 2
        mask_bg = np.abs(rel_theta_bg) <= scanning_window / 2

        hist_fg1_obs, _ = np.histogram(rel_theta_fg1[mask_fg1], bins=bins)
        hist_bg_obs, _ = np.histogram(rel_theta_bg[mask_bg], bins=bins)

        eps = np.finfo(float).eps
        hist_fg1_obs = hist_fg1_obs.astype(float)
        hist_fg1_obs[hist_fg1_obs == 0] = eps
        hist_bg_obs = hist_bg_obs.astype(float)
        hist_bg_obs[hist_bg_obs == 0] = eps

        area_bg, _ = compute_area_under_cdf(hist_bg_obs, bins, coverage, mode)
        area_fg1, _ = compute_area_under_cdf(hist_fg1_obs, bins, coverage, mode)

        abs_area_fg1[i] = np.sqrt(area_fg1 / area_bg)
        abs_area_bg[i] = np.sqrt(area_bg / area_bg)

        if mode == "absolute" and abs_area_exp_fg is not None:
            area_exp_fg, _ = compute_area_under_cdf(
                hist_fg1_obs * coverage, bins, coverage, mode
            )
            abs_area_exp_fg[i] = np.sqrt(area_exp_fg / area_bg)

        if theta_fg2 is not None:
            rel_theta_fg2 = ((theta_fg2 - center + np.pi) % (2 * np.pi)) - np.pi
            mask_fg2 = np.abs(rel_theta_fg2) <= scanning_window / 2
            hist_fg2_obs, _ = np.histogram(rel_theta_fg2[mask_fg2], bins=bins)
            hist_fg2_obs = hist_fg2_obs.astype(float)
            hist_fg2_obs[hist_fg2_obs == 0] = eps
            area_fg2, _ = compute_area_under_cdf(hist_fg2_obs, bins, coverage, mode)
            abs_area_fg2[i] = np.sqrt(area_fg2 / area_bg)

    if theta_fg2 is not None:
        return abs_area_fg1, abs_area_fg2, abs_area_bg
    return abs_area_fg1, abs_area_exp_fg, abs_area_bg
