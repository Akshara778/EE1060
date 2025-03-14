import numpy as np
import matplotlib.pyplot as plt

# Constants
tau = 1
R = 1
L = 1
w0 = 2 * np.pi  # fixed omega_0

# Time array
t = np.linspace(0, 100, 5000)  

# Function to compute i(t)
def compute_current(t, alpha, N=200):
    i_t = (10 * alpha / R) * (1 - np.exp(-t / tau))  

    # Summation term
    sum_term = np.zeros_like(t)
    for n in range(1, N + 1):
        an = (10 * np.sin(2 * np.pi * alpha * n)) / (np.pi * n)
        bn = (20 * (np.sin(np.pi * alpha * n) ** 2)) / (np.pi * n)

        factor = 1 / ((R / L) ** 2 + (n * w0) ** 2)
        decay = np.exp(-t / tau)
        
        sum_term += factor * (
            an * (R/L * np.cos(n * w0 * t) + n * w0 * np.sin(n * w0 * t))
            + bn * (R/L * np.sin(n * w0 * t) - n * w0 * np.cos(n * w0 * t))
            - decay * (R/L * an - bn * n * w0)
        )

    return i_t + (1/L) * sum_term

# Different alpha values and case titles
alpha_values = [1/8, 1/2, 7/8]
titles = [r"$\alpha = \frac{1}{8}$", r"$\alpha = \frac{1}{2}$", r"$\alpha = \frac{7}{8}$"]

# Create subplots with shared x-axis, stacked vertically
fig, axes = plt.subplots(3, 1, figsize=(10, 8), sharex=True)

for i, alpha in enumerate(alpha_values):
    i_t = compute_current(t, alpha)
    axes[i].plot(t, i_t, color='purple', linewidth=1)
    axes[i].set_ylabel("Current (i)")
    axes[i].set_title(f"$L/R=T$, {titles[i]}")
    axes[i].grid(True)

axes[-1].set_xlabel("Time (t)")

plt.tight_layout()
plt.savefig('plot2.png')

