import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import os

# Create directory for figures
os.makedirs('figs', exist_ok=True)

alpha_vals = [0.125, 0.25, 0.5, 0.75, 0.875]  # Different alpha values
n = np.arange(-50, 51, 1)  # Range for n

fig = plt.figure(figsize=(12, 8))
gs = gridspec.GridSpec(3, 3, height_ratios=[1, 1.2, 1.2])  # 3 rows, 3 columns

axes = []  # List to store subplot axes

for idx, alpha in enumerate(alpha_vals):
    phase_spectrum = np.arctan2(1 - np.cos(2 * np.pi * n * alpha), -np.sin(2 * np.pi * n * alpha))

    if idx < 3:  # First 3 plots in the first row
        ax = fig.add_subplot(gs[0, idx])
    elif idx == 3:  # Next two plots span the entire second row
        ax = fig.add_subplot(gs[1, :])
    elif idx == 4:  # Final plot spans the entire third row
        ax = fig.add_subplot(gs[2, :])

    ax.stem(n, np.unwrap(phase_spectrum), basefmt=" ", linefmt='b-', markerfmt='bo')
    ax.axhline(0, color='red', linewidth=0.8)  # Reference line at zero
    ax.set_xlabel("n")
    ax.set_ylabel("Phase (radians)")
    ax.set_title(r"Phase Spectrum for $\alpha$ = " + str(alpha))
    ax.grid(True)
    axes.append(ax)

plt.tight_layout()
plt.savefig("figs/phase_spectrum.png")
plt.show()

