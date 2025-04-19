import numpy as np


def compute_rmsd(fg1: np.ndarray, fg2: np.ndarray) -> float:
    """Compute root-mean-square deviation (RMSD) between two distributions.

    Args:
        fg1 (np.ndarray): First vector.
        fg2 (np.ndarray): Second vector.

    Returns:
        float: RMSD between normalized versions of fg1 and fg2.
    """
    fg1 = np.asarray(fg1, dtype=float)
    fg2 = np.asarray(fg2, dtype=float)
    if fg1.sum() == 0 or fg2.sum() == 0:
        return np.nan
    fg1 /= fg1.sum()
    fg2 /= fg2.sum()
    return np.sqrt(np.mean((fg1 - fg2) ** 2))
