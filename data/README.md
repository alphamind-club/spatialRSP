### Downloading Data

Data required for analysis can be downloaded using the utility functions provided in the `spatialrsp.utils.fetchers` module.

The datasets are primarily sourced from the Human Cell Landscape (HCL), the Kidney Precision Medicine Project (KPMP), and the Mouse Cell Atlas (MCA). Three primary functions are available for data acquisition: `download_hcl`, `download_kpmp`, and `download_mca`.

These functions are designed to streamline the setup process by automatically handling the download and local storage of each dataset. To use them, users should import the desired function from the `spatialrsp.utils.fetchers` module:

```python
from spatialrsp.utils.fetchers import download_hcl, download_kpmp, download_mca

# Download HCL dataset
download_hcl(verbose=True)

# Download KPMP dataset (single-nucleus)
download_kpmp(data_type="sn", verbose=True)
# Download KPMP dataset (single-cell)
download_kpmp(data_type="sc", verbose=True)

# Download MCA dataset
download_mca(verbose=True)
```

In addition to these real-world datasets, an upcoming testing suite will support the generation of synthetic spatial transcriptomics data. This feature is intended for unit testing, benchmarking, and experimentation. The synthetic data generation tools will be integrated into the core utilities and designed for flexibility and ease of use across different simulation scenarios.
