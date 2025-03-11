import numpy as np
import matplotlib.pyplot as plt

# ----------------- Square Wave Function -----------------
def square_wave(t, T, alpha, amp):
    """Returns square wave voltage at time t."""
    return amp if (t % T) < (alpha * T) else 0

# ----------------- Differential Equation Function -----------------
def f(r, l, t, i, T, alpha, amp):
    """Defines the RL circuit differential equation."""
    return (square_wave(t, T, alpha, amp) / l) - ((i * r) / l)

# ----------------- RK4 Method -----------------
def rk4_solver(r, l, T, alpha, amp, h, n):
    """Solves RL circuit using the 4th-order Runge-Kutta method."""
    t = 0
    i = 0
    t_values = []
    i_values = []

    for j in range(n):
        t_values.append(t)
        i_values.append(i)

        k1 = h * f(r, l, t, i, T, alpha, amp)
        k2 = h * f(r, l, t + h / 2, i + k1 / 2, T, alpha, amp)
        k3 = h * f(r, l, t + h / 2, i + k2 / 2, T, alpha, amp)
        k4 = h * f(r, l, t + h, i + k3, T, alpha, amp)

        i += (k1 + 2 * k2 + 2 * k3 + k4) / 6
        t += h

    return t_values, i_values

# ----------------- User Input -----------------
print("Enter the values of R, L, alpha, amplitude, and Time period of the input square wave:")
r, l, alpha, amp, T = map(float, input().split())

# ----------------- Solve and Plot -----------------
t_max = 5 * T  # Simulate for 5 cycles
h = 0.01  # Step size
n = int(t_max / h)  # Number of iterations

t_values, i_values = rk4_solver(r, l, T, alpha, amp, h, n)

plt.figure(figsize=(10, 5))
plt.plot(t_values, i_values, label="RK4 Method", color="blue")
plt.xlabel("Time (s)")
plt.ylabel("Current (A)")
plt.title("RL Circuit Response using RK4 Method")
plt.legend()
plt.grid()
plt.show()

