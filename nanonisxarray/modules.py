#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
modules.py - Common imports for nanonisxarray

This module centralizes imports used throughout the nanonisxarray package.
It provides core scientific computing libraries and utilities.

Dependencies:
    - numpy: Array operations
    - pandas: DataFrames for tabular header data
    - xarray: Labeled multi-dimensional arrays
    - tqdm: Progress bars for batch operations
    - matplotlib-scalebar: Scale bars for SPM images
    - pyperclip: Clipboard utilities (optional)

@author: Petro Maksymovych
"""

# Core scientific computing
import numpy as np
import pandas as pd
import xarray as xr

# Standard library utilities
import inspect
import re
import os
import sys
import copy
import subprocess
import base64
import datetime
from time import time

# Progress bar for batch processing
from tqdm import tqdm

# Clipboard support (optional, for copying file paths)
import pyperclip

# Scale bar for SPM image visualization
from matplotlib_scalebar.scalebar import ScaleBar
