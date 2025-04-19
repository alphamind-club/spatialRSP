from typing import Tuple
import numpy as np


def cartesian_to_polar(
    coordinates: np.ndarray,
    vantage_point: Tuple[float, float] = (0, 0),
    verbose: bool = False,
) -> Tuple[np.ndarray, np.ndarray]:
    """Convert Cartesian coordinates to polar coordinates.

    Args:
        coordinates (np.ndarray): Array of shape (n_points, 2) with (x, y) pairs.
        vantage_point (tuple): Origin for polar transformation.
        verbose (bool): If True, print debug information.

    Returns:
        tuple: Angular (theta) and radial (r) coordinates.
    """
    coordinates = np.atleast_2d(np.asarray(coordinates))
    if coordinates.shape[1] != 2:
        raise ValueError("Each coordinate must be 2D (x, y).")

    dx = coordinates[:, 0] - vantage_point[0]
    dy = coordinates[:, 1] - vantage_point[1]
    theta = np.arctan2(dy, dx)
    r = np.hypot(dx, dy)

    if verbose:
        print(
            f"[cartesian_to_polar] Converted {coordinates.shape[0]} points relative to {vantage_point}."
        )

    return theta, r
