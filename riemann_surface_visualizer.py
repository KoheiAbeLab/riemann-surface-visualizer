"""
Riemann Surface Visualizer: w = z^(1/n) Multi-Sheet Structure
------------------------------------------------------------

This script generates 3D visualizations of the Riemann surface of
    w = z^(1/order)
by explicitly stacking its multiple analytic sheets.  
The surface is represented in cylindrical coordinates and rendered as a 
helical multi-sheet structure, with branch cuts automatically inserted 
between sheets.

Features:
- Visualization of the multi-sheet Riemann surface for w = z^(1/order).
- Adjustable number of sheets (order = 2, 4, 8, 16, ...).
- Smooth helical height function H = θ/order to unfold the sheets.
- Automatic branch-cut separation using infinitesimal angular gaps.
- Per-sheet offset rendering to avoid surface overlap.
- Axis labeling for Re(z), Im(z), and sheet height (argument θ).
- Generates a separate plot for multiple orders when run as __main__.

Usage:
Modify the 'order' parameter in plot_riemann() or the loop in 
the main block to generate surfaces of arbitrary branching order.
"""
import numpy as np
import matplotlib.pyplot as plt

# Riemann surface of w = z**(1/order)
def plot_riemann(order: int,
                 theta_max: float | None = None,
                 sheets: int | None = None,
                 title: str = "") -> None:
    if theta_max is None:
        theta_max = 2 * np.pi * order
    if sheets is None:
        sheets = order

    # grid
    r = np.linspace(0.15, 2.0, 160)
    th = np.linspace(0.0, theta_max, 1600)
    R, TH = np.meshgrid(r, th)

    # Cartesian + height
    X = R * np.cos(TH)
    Y = R * np.sin(TH)
    H = TH / order

    # which sheet (0..sheets-1)
    sheet_idx = (TH // (2 * np.pi)).astype(int) % sheets

    fig = plt.figure(figsize=(7, 6))
    fig.canvas.manager.set_window_title(f"Riemann Surface Visualizer (order={order})")
    ax = fig.add_subplot(111, projection="3d")
    ax.view_init(elev=25, azim=35)
    ax.set_box_aspect((1, 1, 0.6))

    gap = 1e-3  # small cut at sheet edges [rad]

    # draw from top sheets first to avoid z-fighting
    for s in range(sheets - 1, -1, -1):
        lo = 2 * np.pi * s + gap
        hi = 2 * np.pi * (s + 1) - gap
        in_sheet = (sheet_idx == s) & (TH > lo) & (TH < hi)

        Xm = np.where(in_sheet, X, np.nan)
        Ym = np.where(in_sheet, Y, np.nan)
        Hm = np.where(in_sheet, H + 0.03 * s, np.nan)

        ax.plot_surface(Xm, Ym, Hm,
                        rstride=30, cstride=30,
                        linewidth=0, antialiased=True, alpha=0.9)

    # z-axis ticks: 0, π/2, π, 3π/2, 2π
    ticks = [0, 0.5 * np.pi, 1 * np.pi, 1.5 * np.pi, 2 * np.pi]
    ax.set_zticks(ticks)
    ax.set_zticklabels([r"$0$", r"$\frac{\pi}{2}$", r"$\pi$",
                        r"$\frac{3\pi}{2}$", r"$2\pi$"])

    ax.set_xlabel("Re(z)")
    ax.set_ylabel("Im(z)")
    ax.set_zlabel(r"z ~ $\theta/{%d}$" % order)
    ax.set_title(title)
    ax.set_zlim(0, theta_max / order + 0.1 * (sheets - 1))
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # order = 2, 4, 8, 16 ... (k-th root; sheets = k)
    for order in (2, 4, 8, 16):
        root_sign = "√" * int(np.log2(order))
        ttl = f"Riemann surface of {root_sign}z ({order} sheets)"
        plot_riemann(order=order, title=ttl)
