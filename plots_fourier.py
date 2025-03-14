import numpy as np
import matplotlib.pyplot as plt
import fourier_series as fs
import os


# Create directory for figures
os.makedirs('figs', exist_ok=True)

# Constants
tau = 1
R = 1
L = 1
w0 = np.pi / 5  # Fixed omega_0

# Time array
t = np.linspace(0, 100, 5000)

# Different alpha values
alpha_values = [1/8, 1/2, 7/8]
titles = [r"$\alpha = \frac{1}{8}$", r"$\alpha = \frac{1}{2}$", r"$\alpha = \frac{7}{8}$"]
case = ["<<", "=", ">>"]


for j in range(3):
    # Create subplots with shared x-axis, stacked vertically
    fig, axes = plt.subplots(3, 1, figsize=(10, 8), sharex=True)
    for i, alpha in enumerate(alpha_values):
        i_t = fs.compute_current(R, L, w0, t, alpha)
        axes[i].plot(t, i_t, color='purple', linewidth=1)
        axes[i].set_ylabel("Current (i)")
        axes[i].set_title("Case " + str(j + 1) + ": L/R " + case[j] + " T, " + titles[i])
        axes[i].grid(True)
    axes[-1].set_xlabel("Time (t)")
    plt.tight_layout()
    plt.savefig('figs/fourier_plot_' + str(j + 1) + '.png')
    plt.show()
    w0 *= 10
    if j == 1:
        t = np.linspace(0, 5, 5000)