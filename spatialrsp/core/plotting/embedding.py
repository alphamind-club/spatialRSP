import matplotlib.pyplot as plt
import numpy as np


def plot_embedding_overlay(
    bg_coords: np.ndarray,
    fg_coords_dict: dict[str, np.ndarray],
    ax: plt.Axes = None,
    title: str = None,
) -> None:
    """Plot a 2D embedding with background and one or more foreground overlays.

    Args:
        bg_coords (np.ndarray): Background coordinates (N x 2).
        fg_coords_dict (dict): Label → foreground coordinates.
        ax (plt.Axes, optional): Axis to plot on. Creates new if None.
        title (str, optional): Plot title.
    """
    if ax is None:
        _, ax = plt.subplots(figsize=(6, 6))

    ax.scatter(bg_coords[:, 0], bg_coords[:, 1], c="lightgray", s=1, label="Background")
    colors = ["red", "green", "orange", "blue", "purple"]

    for i, (label, coords) in enumerate(fg_coords_dict.items()):
        ax.scatter(
            coords[:, 0],
            coords[:, 1],
            s=1,
            alpha=0.6,
            label=label,
            color=colors[i % len(colors)],
        )

    ax.set_xlabel("UMAP 1")
    ax.set_ylabel("UMAP 2")
    if title:
        ax.set_title(title, fontsize=14)
    ax.legend(markerscale=5, fontsize=10)
