import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import os

# Create directory for figures
os.makedirs('figs', exist_ok=True)

alpha_vals = [0.125, 0.25, 0.5, 0.75, 0.875]
k = np.arange(-10, 11, 1)

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


# 3D plot of the magnitude spectrum
alpha_vals = np.linspace(0, 1, 15)
k_vals = np.arange(-10, 11, 1)

fig = plt.figure(figsize=(10, 7))
ax1 = fig.add_subplot(111, projection='3d')

for alpha in alpha_vals:
    Ck = np.zeros_like(k_vals, dtype=float)
    for i, val in enumerate(k_vals):
        if val != 0:
            Ck[i] = np.abs((20 / (np.pi * val)) * np.sin(np.pi * val * alpha))
        else:
            Ck[i] = 10 * alpha
    for i in range(len(k_vals)):
        ax1.plot([alpha, alpha], [k_vals[i], k_vals[i]], [0, Ck[i]], color = 'gray', linewidth = '1')  # Stem line
        ax1.scatter(alpha, k_vals[i], Ck[i], color='b', s=10)  # Marker at the top

ax1.set_xlabel(r"$\alpha$")
ax1.set_ylabel("k")
ax1.set_zlabel(r"$|C_k|$")
ax1.view_init(elev = 19, azim = 165)
ax1.set_title("3D plot of Magnitude Spectrum")
plt.savefig("figs/3d_magnitude_spectrum.png")
plt.show()


# Phase spectrum
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