import os
from typing import List

import requests
from tqdm import tqdm


def _download_file(
    url: str, dest_path: str, verbose: bool = False, desc: str = "Downloading"
) -> str:
    """Download a file from URL with progress bar.

    Args:
        url (str): Source URL.
        dest_path (str): Target local path.
        verbose (bool): Verbose output toggle.
        desc (str): Progress bar description.

    Returns:
        str: Path to downloaded file.
    """
    if os.path.exists(dest_path):
        if verbose:
            print(f"[✓] File exists: {dest_path}")
        return dest_path

    response = requests.get(url, stream=True, timeout=10)
    response.raise_for_status()
    total = int(response.headers.get("content-length", 0))

    with open(dest_path, "wb") as f, tqdm(
        total=total, unit="iB", unit_scale=True, desc=desc
    ) as progressbar:
        for chunk in response.iter_content(chunk_size=1024):
            f.write(chunk)
            progressbar.update(len(chunk))

    if verbose:
        print(f"[✓] Downloaded: {dest_path}")

    return dest_path


def download_hcl(verbose: bool = False) -> str:
    """Download the HCL dataset (hcl.h5ad)."""
    return _download_file(
        "https://datasets.cellxgene.cziscience.com/ae0c62a1-a30f-4033-97d2-0edb2e146c53.h5ad",
        "data/hcl.h5ad",
        verbose,
        "Downloading HCL",
    )


def download_kpmp(data_type: str = "sn", verbose: bool = False) -> str:
    """Download the KPMP dataset (sn or sc)."""
    urls = {
        "sn": "https://datasets.cellxgene.cziscience.com/7d8af09a-2f96-49f9-a473-f561a332f25d.h5ad",
        "sc": "https://datasets.cellxgene.cziscience.com/f5b6d620-76df-45c5-9524-e5631be0e44a.h5ad",
    }
    if data_type not in urls:
        raise ValueError("Invalid data_type. Must be 'sn' or 'sc'.")
    return _download_file(
        urls[data_type],
        f"data/kpmp_{data_type}.h5ad",
        verbose,
        f"Downloading KPMP-{data_type}",
    )


def download_mca(verbose: bool = False) -> List[str]:
    """Download MCA data and metadata.

    Returns:
        list[str]: Paths to downloaded files.
    """
    files = [
        (
            "mca.h5ad",
            "https://figshare.com/ndownloader/files/37560595?private_link=340e8e7f349559f61ef6",
        ),
        (
            "mca_cell_info.csv",
            "https://figshare.com/ndownloader/files/36222822?private_link=340e8e7f349559f61ef6",
        ),
    ]
    os.makedirs("data", exist_ok=True)
    return [
        _download_file(
            url, os.path.join("data", fname), verbose, f"Downloading {fname}"
        )
        for fname, url in files
    ]
