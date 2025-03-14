import numpy as np

# Function to compute i(t)
def compute_current(R, L, w0, t, alpha, N=200):
    tau = L / R
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