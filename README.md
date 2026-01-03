# nanonisxarray

A Python library to parse and convert Nanonis SPM (Scanning Probe Microscopy) data files into [xarray](https://xarray.pydata.org/) datasets, enabling rapid import of experimental data from Nanonis and Tramea controllers into Python workspaces.

## Features

- **Multi-format support**: Parse `.3ds` (grid spectroscopy), `.sxm` (scan/topography), and `.dat` (point spectroscopy) files
- **xarray integration**: Automatic conversion to labeled, multi-dimensional `xarray.Dataset` objects
- **Header parsing**: Context-aware extraction of experimental metadata
- **Batch processing**: Directory crawling utilities to find and load multiple files
- **MLS support**: Handles Multi-Line Spectroscopy (MLS) grid files

## Installation

```bash
# Clone the repository
git clone https://github.com/amplipy/nanonisxarray.git
cd nanonisxarray

# Install in development mode
pip install -e .
```

Or install dependencies manually:

```bash
pip install numpy pandas xarray tqdm matplotlib matplotlib-scalebar pyperclip
```

## Quick Start

### Loading Individual Files

```python
from nanonisxarray import Grid, Scan, Spectrum

# Load a grid spectroscopy file (.3ds)
grid = Grid("path/to/file.3ds")
print(grid.header)           # Parsed header metadata
print(grid.signals.keys())   # Available signal channels
print(grid.ds)               # xarray Dataset

# Load a scan/topography file (.sxm)
scan = Scan("path/to/file.sxm")
print(scan.header)           # Scan parameters
print(scan.signals.keys())   # Channel names (Z, Current, etc.)
print(scan.ds)               # xarray Dataset with forward/backward images

# Load a point spectrum file (.dat)
spec = Spectrum("path/to/file.dat")
print(spec.header)           # Spectrum metadata
print(spec.signals.keys())   # Recorded channels
```

### Batch Processing

```python
from nanonisxarray import GetData, FindData, FindGrids, FindScans

# Find all .3ds files in a directory (returns file paths)
grid_files = GetData.find_data(topdir="/path/to/data", ext="3ds", get_data=False)

# Load all grid files at once
grids = GetData.find_data(topdir="/path/to/data", ext="3ds", get_data=True)

# Find and load scan files
scans = FindScans(topdir="/path/to/data", get_data=True)

# Find files with depth-limited search
from nanonisxarray import walk_depth
for root, dirs, files in walk_depth("/path/to/data", maxdepth=2):
    print(root, files)
```

### Working with xarray Datasets

```python
# Grid data is organized as (x, y, sweep_signal)
grid = Grid("spectroscopy.3ds")

# Access the sweep signal (typically bias voltage)
bias = grid.signals['sweep_signal']

# Access spectroscopy data
didv = grid.signals['OC D1 X (m)']  # Lock-in dI/dV signal

# Use the xarray dataset for analysis
ds = grid.ds
ds.sel(bias=0.1, method='nearest')  # Select data at specific bias
ds.mean(dim=['x', 'y'])              # Average over spatial dimensions
```

## Module Structure

```
nanonisxarray/
├── __init__.py      # Package exports
├── nanonisio.py     # Core file parsers (Grid, Scan, Spectrum classes)
├── file_io.py       # File discovery and batch loading utilities
├── modules.py       # Common imports (numpy, pandas, xarray, etc.)
└── examples/        # Jupyter notebook examples
    └── read_grid.ipynb
```

### Core Classes

| Class | File Extension | Description |
|-------|---------------|-------------|
| `Grid` | `.3ds` | Grid spectroscopy data (spatial + spectral dimensions) |
| `Scan` | `.sxm` | Topography/scan images (forward and backward channels) |
| `Spectrum` | `.dat` | Point spectroscopy (single location, ASCII format) |

### Utility Functions

| Function | Description |
|----------|-------------|
| `GetData.find_data()` | Find/load files by extension |
| `FindGrids()` | Find `.3ds` grid files |
| `FindScans()` | Find `.sxm` scan files |
| `CrawlDir()` | Crawl directory tree by extension |
| `walk_depth()` | Depth-limited directory walker |

## Signal Channel Mapping

The library maps common Nanonis channel names to shorter keys in xarray datasets:

| Nanonis Channel | Dataset Key |
|-----------------|-------------|
| `Current` | `c` |
| `Z` | `z` |
| `OC D1 X (m)` | `lix` (lock-in X) |
| `OC D1 Y (m)` | `liy` (lock-in Y) |
| `Phase` | `phi` |
| `Amplitude` | `amp` |
| `Frequency Shift` | `omega` |

Forward scans are suffixed with `f`, backward with `r` or `b`.

## Requirements

- Python 3.7+
- numpy
- pandas
- xarray
- tqdm
- matplotlib
- matplotlib-scalebar
- pyperclip (optional, for clipboard support)

## License

MIT License - see [LICENSE](LICENSE)

## Credits

Originally based on [nanonispy](https://github.com/underchemist/nanonispy) by underchemist.  
Modified by Petro Maksymovych to add context-aware header parsing and xarray packaging.
