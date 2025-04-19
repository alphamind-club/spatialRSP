import os

import matplotlib.pyplot as plt
import numpy as np

from .embedding import plot_embedding_overlay
from .rsp_curves import plot_rsp_curve


def plot_rsp_composite(
    bg_coords: np.ndarray,
    fg_coords_dict: dict[str, np.ndarray],
    angle_range: np.ndarray,
    fg_rsp_dict: dict[str, np.ndarray],
    bg_curve: np.ndarray,
    expected_fg_curve: np.ndarray = None,
    save_path: str = None,
) -> None:
    """Create a composite plot with UMAP + RSP curve side-by-side.

    Args:
        bg_coords (np.ndarray): Background points.
        fg_coords_dict (dict): Label → foreground coordinates.
        angle_range (np.ndarray): Angular bins.
        fg_rsp_dict (dict): Label → foreground RSP curves.
        bg_curve (np.ndarray): Background RSP curve.
        expected_fg_curve (np.ndarray, optional): Expected foreground (absolute mode).
        save_path (str, optional): Output path to save figure.
    """
    _, axs = plt.subplots(
        1, 2, figsize=(12, 6), subplot_kw={1: {"projection": "polar"}}
    )

    plot_embedding_overlay(bg_coords, fg_coords_dict, ax=axs[0], title="Embedding")
    plot_rsp_curve(
        angle_range,
        fg_rsp_dict,
        bg_curve,
        expected_fg_curve=expected_fg_curve,
        ax=axs[1],
        title="RSP Curve",
    )

    plt.tight_layout()
    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path, dpi=300)
    plt.show()
