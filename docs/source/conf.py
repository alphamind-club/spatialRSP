# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

import os
import sys

sys.path.insert(0, os.path.abspath("../../"))  # So Sphinx finds spatialrsp/

project = "SpatialRSP"
copyright = "2025, Zeyu Yao, Jake Chen"
author = "Zeyu Yao, Jake Chen"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",  # Google/NumPy docstring support
    "sphinx.ext.viewcode",
    "sphinx_autodoc_typehints",
]

templates_path = ["_templates"]

exclude_patterns = []

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

autodoc_default_options = {
    "members": True,
    "undoc-members": False,
    "show-inheritance": True,
}
