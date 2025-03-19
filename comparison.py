import numpy as np
import matplotlib.pyplot as plt
import os
import numerical_methods as nm
import fourier_series as fs

#Creating directory for figures
os.makedirs('figs', exist_ok=True)


T = 10         # Period of the square wave
alpha = 0.5    # Duty cycle (fraction of the period the wave is "high")
h = 0.001      # Step size
amp = 10       # Amplitude of the square wave


#actual square wave 
def square(t, T, alpha, amp):
    return np.where((t % T) < T * alpha, amp, 0)

#fourier series approximation of the square wave
def fourier_series(t, T, alpha, N, amp = 10):
    sum = amp * alpha
    for k in range(1, N + 1):
        ak = (10 * np.sin(2 * k * np.pi * alpha)) / (k * np.pi)
        bk = (20 * np.sin(k * np.pi * alpha)**2) / (k * np.pi)
        sum += (ak * np.cos(k * 2 * np.pi * t / T) + bk * np.sin(k * 2 * np.pi * t / T))
    return sum


#plotting the variation of the fourier series approximation of the input wave with N
t = np.linspace(0, 2 * T, 1000)
plt.plot(t, square(t, T, alpha, amp), linestyle = "--", color = "black", label = "Square")
plt.plot(t, fourier_series(t, T, alpha, 10, amp), label = "N = 10")
plt.plot(t, fourier_series(t, T, alpha, 50, amp), label = "N = 50")
plt.plot(t, fourier_series(t, T, alpha, 100, amp), label = "N = 100")
plt.plot(t, fourier_series(t, T, alpha, 1000, amp), label = "N = 1000")
plt.title("Fourier Series approximation of input wave")
plt.xlabel("Time (t)")
plt.ylabel(r"$V_{in}(t)$")
plt.legend()
plt.grid(True)
plt.savefig("figs/input_wave.png")
plt.show()

#current response of the RL circuit to the square wave input
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

#current response of the RL circuit to the fourier series approximation of the input wave
def rl_forward_euler_fourier(r, l, alpha, amp, T, h, N, n):
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


#comparing the mean absolute error between the current response of the fourier series and the actual square wave input got through the forward euler numerical method
i1 = rl_forward_euler_square(1, 1, alpha, amp, T, h, 1000)

print("Mean Absolute Error in current when:")

i2_10 = rl_forward_euler_fourier(1, 1, alpha, amp, T, h, 10, 1000)
error_10 = np.array(i1) - np.array(i2_10)
err_10 = np.linalg.norm(error_10, ord = 1)
print("N = 10 :", err_10 / 10)

i2_50 = rl_forward_euler_fourier(1, 1, alpha, amp, T, h, 50, 1000)
error_50 = np.array(i1) - np.array(i2_50)
err_50 = np.linalg.norm(error_50, ord = 1)
print("N = 50 :", err_50 / 50)

i2_100 = rl_forward_euler_fourier(1, 1, alpha, amp, T, h, 100, 1000)
error_100 = np.array(i1) - np.array(i2_100)
err_100 = np.linalg.norm(error_100, ord = 1)
print("N = 100 :", err_100 / 100)

i2_1000 = rl_forward_euler_fourier(1, 1, alpha, amp, T, h, 1000, 1000)
error_1000 = np.array(i1) - np.array(i2_1000)
err_1000 = np.linalg.norm(error_1000, ord = 1)
print("N = 1000 :", err_1000 / 1000)

#here we can see that the error due to each term, that is the mean absolute error resuces to a great extent as N increases
