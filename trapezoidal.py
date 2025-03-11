import numpy as np
import matplotlib.pyplot as plt

def square_wave(t, T, alpha, amp):
    return np.where((t % T) < T * alpha, amp, 0)

def rl_trapezoidal(r, l, alpha, amp, T, n_periods=10):
    tau = l / r  # Time constant of RL circuit
    h = min(0.01 * tau, T / 500)  # Adaptive step size
    n = int(n_periods * T / h)  # Total steps
    
    t_vals = np.linspace(0, n_periods * T, n)
    v_in_vals = square_wave(t_vals, T, alpha, amp)
    i_vals = np.zeros_like(t_vals)
    
    for j in range(1, n):
        i_vals[j] = ((i_vals[j-1] * (2 * l - h * r)) + h * (v_in_vals[j] + v_in_vals[j-1])) / (2 * l + h * r)
    
    return t_vals, i_vals

# User input
r, l, alpha, amp, T = map(float, input("Enter R, L, alpha, amplitude, and T: ").split())

t_vals, i_vals = rl_trapezoidal(r, l, alpha, amp, T)

# Plot
plt.figure(figsize=(10, 5))
plt.plot(t_vals, i_vals, label="Current (A)")
plt.xlabel("Time (s)")
plt.ylabel("Current (A)")
plt.title("RL Circuit Response using Trapezoidal Method")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

