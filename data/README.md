### Downloading Data

Data required for analysis can be downloaded using the utility functions provided in the `spatialrsp.utils.io` module. This module includes functions that automate the retrieval of datasets from reliable sources, ensuring consistent and reproducible workflows.

Three primary functions are available for data acquisition: `download_hcl`, `download_kpmp`, and `download_mca`. The `download_hcl` function facilitates downloading data from the Human Cell Landscape (HCL) project, while `download_kpmp` retrieves data from the Kidney Precision Medicine Project (KPMP). Additionally, the `download_mca` function provides access to data from the Mouse Cell Atlas (MCA), supporting analyses in model organism contexts.

These functions are designed to streamline the setup process by automatically handling the download and local storage of each dataset. To use them, users should import the desired function from the `spatialrsp.utils.io` module. Once imported, calling the function will initiate the download process and save the files to an appropriate location on the local system. This allows for immediate access to the datasets required for further analysis within the `spatialrsp` framework:

```python
from spatialrsp.utils.io import download_hcl, download_kpmp, download_mca

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
