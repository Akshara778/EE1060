import numpy as np
import matplotlib.pyplot as plt
import os

#creting directory for figures
os.makedirs('figs', exist_ok=True)


T = 10         # Period of the square wave
alpha = 0.5    # Duty cycle (fraction of the period the wave is "high")
N = 10         # Number of Fourier series terms
amp = 10       # Amplitude of the square wave

def square(t, T, alpha, amp):
    return np.where((t % T) < T * alpha, amp, 0)
    
def fourier_series(t, T, alpha, N, amp = 10):
    sum = amp * alpha
    for k in range(1, N + 1):
        ak = (10 * np.sin(2 * k * np.pi * alpha)) / (k * np.pi)
        bk = (20 * np.sin(k * np.pi * alpha)**2) / (k * np.pi)
        sum += (ak * np.cos(k * 2 * np.pi * t / T) + bk * np.sin(k * 2 * np.pi * t / T))
    return sum

def error(T, alpha, N, amp = 10):
    err = 0
    t = np.linspace(0, T, 1000)
    for i in t:
        err += abs(square(i, T, alpha, amp) - fourier_series(i, T, alpha, N, amp))
    return err

t = np.linspace(0, 2 * T, 1000)

print("Error over one interval between the actual square wave and the Fourier series approximation:")
print("When N = 10:", error(T, alpha, N, amp))
print("When N = 100:", error(T, alpha, N * 10, amp))
print("When N = 1000:", error(T, alpha, N * 100, amp))
print("When N = 5000:", error(T, alpha, N * 500, amp))

plt.figure(figsize=(10, 5))

plt.plot(t, square(t, T, alpha, amp), label="Square Wave", color="black", linewidth=2, linestyle="dashed")
plt.plot(t, fourier_series(t, T, alpha, N), linewidth=2, label = "N = 10")
plt.plot(t, fourier_series(t, T, alpha, 10 * N), linewidth=2, label = "N = 100")
plt.plot(t, fourier_series(t, T, alpha, 100 * N), linewidth=2, label = "N = 1000")
plt.plot(t, fourier_series(t, T, alpha, 1000 * N), linewidth=2, label = "N = 5000")
plt.xlabel("t")
plt.ylabel(r"$V_{in}$" + "(t)")
plt.legend()
plt.grid(True)
plt.title("Fourier Series Approximation of a Square Wave")
plt.savefig("figs/fourier_vs_actual.png")
plt.show()