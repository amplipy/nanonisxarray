#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
nanonisxarray - Parse Nanonis SPM data files into xarray datasets

This package provides tools to load and convert Nanonis SPM controller
data files (.3ds, .sxm, .dat) into xarray datasets for analysis.

Classes:
    Grid: Load grid spectroscopy files (.3ds)
    Scan: Load scan/topography files (.sxm)
    Spectrum: Load point spectroscopy files (.dat)

Functions:
    GetData.find_data(): Find and optionally load Nanonis files
    FindGrids(): Find .3ds files in a directory
    FindScans(): Find .sxm files in a directory
    FindData(): Find and load files by extension
    walk_depth(): Depth-limited directory walker

Example:
    >>> from nanonisxarray import Grid, Scan, Spectrum
    >>> grid = Grid("path/to/file.3ds")
    >>> print(grid.ds)  # xarray Dataset
"""

from .file_io import *
from .nanonisio import *

__version__ = "0.1.0"
__author__ = "Petro Maksymovych"