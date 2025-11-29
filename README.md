# Riemann Surface Visualizer
Visualization of multivalued Riemann surfaces for w = z^(1/order)
This repository provides a Python-based 3D visualizer for the multi-sheet Riemann surface of the complex root function w = z^(1/order).
The script renders each branch as a helical sheet in cylindrical coordinates, with automatic branch-cut separation.
It is intended as a research and educational tool for exploring analytic continuation, multi-sheet structures, and root-function topology in complex analysis.

<img width="434" height="372" alt="image" src="https://github.com/user-attachments/assets/9088e091-6e65-4fb5-a47c-e43a5418a864" />
<img width="434" height="372" alt="image" src="https://github.com/user-attachments/assets/df8e2355-c657-43bf-acbf-7784b9a71134" />

## Features
- Multi-sheet visualization of w = z^(1/order).
- Adjustable branching order (2, 4, 8, 16, ...).
- Smooth helical height function H = theta / order.
- Automatic branch-cut separation using small angular gaps.
- Per-sheet vertical offset to prevent surface overlap.
- Axis labeling for Re(z), Im(z), and argument (height).
- Generates separate plots for multiple orders when executed as main.

## Requirements
Python 3.8 or higher
Dependencies:
- numpy
- matplotlib
Install with:
pip install numpy matplotlib

## Installation
Using requirements.txt:
pip install -r requirements.txt

## Quick Start
Clone the repository and run the visualizer:
```bash
git clone https://github.com/KoheiAbeLab/riemann-surface-visualizer
cd riemann-surface-visualizer
python riemann_surface_visualizer.py
```

## Usage
Run the script:
python riemann_surface_visualizer.py

To change the branching order, modify the call to plot_riemann() inside the script:

plot_riemann(order=4)

## Controls inside the Matplotlib 3D window:
- Drag: rotate the view
- Scroll: zoom
- Right-drag: pan
- The window title shows the current order
- The figure title shows the root symbol (sqrt, 4th root, etc.)

## File Structure
riemann_surface_visualizer.py - main visualization script
README.md - documentation
LICENSE - MIT license
requirements.txt - dependency list

## Citation
Kohei Abe, "Riemann Surface Visualizer: Multi-Sheet Visualization of w = z^(1/order)",
GitHub repository, https://github.com/KoheiAbeLab/riemann-surface-visualizer

### BibTeX
```bibtex
@misc{abe2025_riemann,
author = {Kohei Abe},
title = {Riemann Surface Visualizer: Multi-Sheet Visualization of w = z^(1/order)},
year = {2025},
publisher = {GitHub},
howpublished = {\url{https://github.com/KoheiAbeLab/riemann-surface-visualizer}}
}
```

## License
MIT License

## Download
Stable releases are available on the GitHub Releases page:
https://github.com/KoheiAbeLab/riemann-surface-visualizer/releases

### Known Issues
- 3D rendering speed depends on Matplotlib backend and system hardware
- High-resolution displays may reduce frame rate
- Very large grids may cause slowdown
- Some Matplotlib backends may render transparency ordering imperfectly

### Limitations
- Only surfaces of w = z^(1/n) are implemented
- Branch cuts are fixed along the positive real axis
- Intended for conceptual visualization, not numerical precision

## Contact
Kohei Abe

ORCID: https://orcid.org/0009-0001-1126-3282

GitHub: https://github.com/KoheiAbeLab
