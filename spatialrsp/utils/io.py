import pandas as pd
import anndata as ad


def load_data(
    file_path: str,
    sep: str = "\t",
    index_col: int = 0,
    verbose: bool = False,
) -> ad.AnnData:
    """Load tabular or .h5ad data into an AnnData object.

    Args:
        file_path (str): Path to input file.
        sep (str): Delimiter for tabular files.
        index_col (int): Index column for tabular data.
        verbose (bool): Verbose output toggle.

    Returns:
        AnnData: Loaded data object.
    """
    if file_path.endswith(".h5ad"):
        if verbose:
            print(f"[↓] Loading AnnData from '{file_path}'.")
        return ad.read_h5ad(file_path)

    if verbose:
        print(f"[INFO] Reading tabular data from '{file_path}'.")
    data = pd.read_csv(file_path, sep=sep, index_col=index_col)
    adata = ad.AnnData(data.T)

    if verbose:
        print(f"[✓] Data shape: {adata.X.shape} (observations x features)")
    return adata


def save_data(
    adata: ad.AnnData,
    file_path: str,
    verbose: bool = False,
) -> ad.AnnData:
    """Save AnnData object to .h5ad file.

    Args:
        adata (AnnData): Annotated data object.
        file_path (str): Path to output file.
        verbose (bool): Verbose output toggle.

    Returns:
        AnnData: Saved data object.
    """
    if verbose:
        print(f"[↑] Saving AnnData to '{file_path}'.")

    adata.write(file_path)

    if verbose:
        print(f"[✓] Saved AnnData to '{file_path}'.")
    return adata
