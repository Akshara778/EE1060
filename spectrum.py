import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import os

# Create directory for figures
os.makedirs('figs', exist_ok=True)

alpha_vals = [0.125, 0.25, 0.5, 0.75, 0.875]
k = np.arange(-50, 51, 5)

fig = plt.figure(figsize=(12, 8))
gs = gridspec.GridSpec(3, 3, height_ratios=[1, 1.2, 1.2])  # 3 rows, 3 columns

Ck = np.zeros_like(k, dtype=float)

axes = []  # List to store subplot axes

for idx, alpha in enumerate(alpha_vals):
    for i, val in enumerate(k):
        if val != 0:
            Ck[i] = np.abs((20 / (np.pi * val)) * np.sin(np.pi * val * alpha))
        else:
            Ck[i] = 19.5

    if idx < 3:  # First 3 plots in the first row
        ax = fig.add_subplot(gs[0, idx])
    elif idx == 3:  # Last 2 plots span the entire second row
        ax = fig.add_subplot(gs[1, :])  # Span all 3 columns
    elif idx == 4:
        ax = fig.add_subplot(gs[2, :])

    ax.stem(k, Ck)
    ax.set_xlabel("k")
    ax.set_ylabel(r"$|C_k|$")
    ax.set_title(r"Magnitude Spectrum for $\alpha$ = " + str(alpha))
    ax.grid(True)
    axes.append(ax)

plt.tight_layout()
plt.savefig("figs/magnitude_spectrum.png")
plt.show()
