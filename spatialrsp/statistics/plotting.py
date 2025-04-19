import matplotlib.pyplot as plt
import numpy as np


def plot_coverage_boxplot(
    foregrounds: list[list[int]],
    background_sizes: list[int],
    labels: list[str],
    ax: plt.Axes = None,
) -> None:
    """Boxplot of foreground coverage across conditions.

    Args:
        foregrounds (list[list[int]]): Foreground sizes per condition.
        background_sizes (list[int]): Background sizes per condition.
        labels (list[str]): Condition labels.
        ax (plt.Axes, optional): Axis to draw on.
    """
    coverage = [
        [len(fg) / max(bg, 1) for fg, bg in zip(foregrounds[i], background_sizes)]
        for i in range(len(labels))
    ]

    if ax is None:
        _, ax = plt.subplots(figsize=(6, 5))

    ax.boxplot(coverage, labels=labels, patch_artist=True)
    ax.set_ylabel("Foreground Coverage")
    ax.set_title("Foreground Coverage Across Conditions")
    ax.axhline(0.05, color="gray", linestyle="--", linewidth=1)


def plot_rsp_comparison_barplot(
    means: list[float],
    errors: list[float],
    labels: tuple[str, str] = ("A1", "A2"),
    title: str = "Fold Change from Control",
    colors: tuple[str, str] = ("pink", "orange"),
    stars: list[str] = None,
    ax: plt.Axes = None,
) -> None:
    """Barplot of metric comparison (e.g., A1 vs A2).

    Args:
        means (list[float]): Metric means.
        errors (list[float]): Standard errors.
        labels (tuple[str]): Bar labels.
        title (str): Plot title.
        colors (tuple[str]): Bar colors.
        stars (list[str], optional): Significance stars.
        ax (plt.Axes, optional): Axis to draw on.
    """
    if ax is None:
        _, ax = plt.subplots(figsize=(4, 6))

    x = np.arange(len(means))
    bar_width = 0.5

    bar_rects = ax.bar(
        x,
        means,
        yerr=errors,
        width=bar_width,
        color=colors,
        capsize=5,
    )

    ax.axhline(1, color="black", linestyle="--", linewidth=1)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=12)
    ax.set_ylabel("Fold Change (from control)", fontsize=14)
    ax.set_title(title, fontsize=14)

    if stars:
        for rect, star in zip(bar_rects, stars):
            height = rect.get_height()
            ax.text(
                rect.get_x() + rect.get_width() / 2,
                height + 0.02,
                star,
                ha="center",
                va="bottom",
                fontsize=16,
                color="black",
            )


def plot_expression_scatter(
    x: np.ndarray,
    y: np.ndarray,
    labels: list = None,
    xlabel: str = "Gene A",
    ylabel: str = "Gene B",
    title: str = None,
    ax: plt.Axes = None,
    alpha: float = 0.5,
) -> None:
    """Scatter plot of expression or metric pairs.

    Args:
        x (np.ndarray): X values.
        y (np.ndarray): Y values.
        labels (list, optional): Point labels (color-coded).
        xlabel (str): X-axis label.
        ylabel (str): Y-axis label.
        title (str, optional): Plot title.
        ax (plt.Axes, optional): Axis to draw on.
        alpha (float): Point transparency.
    """
    if ax is None:
        _, ax = plt.subplots(figsize=(6, 5))

    if labels is not None:
        scatter = ax.scatter(x, y, c=labels, s=5, alpha=alpha, cmap="viridis")
        plt.colorbar(scatter, ax=ax)
    else:
        ax.scatter(x, y, s=5, alpha=alpha, color="black")

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    if title:
        ax.set_title(title)
