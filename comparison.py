import numpy as np
import matplotlib.pyplot as plt
import os
import numerical_methods as nm
import fourier_series as fs

#creting directory for figures
os.makedirs('figs', exist_ok=True)


T = 10         # Period of the square wave
alpha = 0.5    # Duty cycle (fraction of the period the wave is "high")
N = 1000        # Number of Fourier series terms
h = 0.001      # Step size
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

def rl_forward_euler_square(r, l, alpha, amp, T, h, n):
    t_coord = []
    i_coord = []
    t = 0
    i = 0
    for j in range(n):
        t_coord.append(t)
        i_coord.append(i)
        i = i + (((square(t, T, alpha, amp) / l) - ((i * r) / l)) * h)
        t += h
    return i_coord

def rl_forward_euler_fourier(r, l, alpha, amp, T, h, n):
    t_coord = []
    i_coord = []
    t = 0
    i = 0
    for j in range(n):
        t_coord.append(t)
        i_coord.append(i)
        i = i + (((fourier_series(t, T, alpha, N) / l) - ((i * r) / l)) * h)
        t += h
    return i_coord


i1 = rl_forward_euler_fourier(1, 1, alpha, amp, T, h, 1000)
i2 = rl_forward_euler_square(1, 1, alpha, amp, T, h, 1000)
error = np.array(i1) - np.array(i2)
err = np.linalg.norm(error, ord = 1)
print("Max error: ", err)