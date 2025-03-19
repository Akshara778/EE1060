import numpy as np
import matplotlib.pyplot as plt
import os
import numerical_methods as nm
import fourier_series as fs

#Creating directory for figures
os.makedirs('figs', exist_ok=True)

R = 1          # Resistance
L = 1          # Inductance
w0 = np.pi / 5 # Fundamental frequency
T = 10         # Period of the square wave
alpha = 0.4    # Duty cycle (fraction of the period the wave is "high")
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
plt.xticks([0, alpha * T, T, (1 + alpha) * T, 2 * T], [r"$0$", r"$\alpha T$", r"$T$", r"$(1 + \alpha)T$", r"$2T$"])
plt.show()


#plotting the current response of the RL circuit through fourier series and RK4 method for different L/R values
t = np.linspace(0, 100, 5000)
fig, axes = plt.subplots(3, 1, figsize=(10, 10))
axes[0].plot(t, fs.compute_current(R, L, w0, t, alpha), color = "purple", linewidth = 1, label = "Fourier Series")
axes[0].plot(nm.rl_rk4(R, L, alpha, amp, T, 1/50, 5000)[0][:], nm.rl_rk4(R, L, alpha, amp, T, 1/50, 5000)[1][:], label = "RK4")
axes[0].set_title("Case 1: L/R << T")
axes[0].set_ylabel("Current (i)")
axes[0].legend(loc = "best")
axes[0].grid(True)
axes[1].plot(t, fs.compute_current(R, L, w0 * 10, t, alpha), color = "purple", linewidth = 1, label = "Fourier Series")
axes[1].plot(nm.rl_rk4(R, L, alpha, amp, T/10, 1/50, 5000)[0][:], nm.rl_rk4(R, L, alpha, amp, T/10, 1/50, 5000)[1][:], label = "RK4")
axes[1].set_title("Case 2: L/R = T")
axes[1].set_ylabel("Current (i)")
axes[1].legend(loc = "best")
axes[1].grid(True)
axes[2].plot(t, fs.compute_current(R, L, w0 * 100, t, alpha), color = "purple", linewidth = 1, label = "Fourier Series")
axes[2].plot(nm.rl_rk4(R, L, alpha, amp, T/100, 1/50, 5000)[0][:], nm.rl_rk4(R, L, alpha, amp, T/100, 1/50, 5000)[1][:], label = "RK4")
axes[2].set_title("Case 3: L/R >> T")
axes[2].set_xlabel("Time (t)")
axes[2].set_ylabel("Current (i)")
axes[2].set_xlim([0, 10])
axes[2].legend(loc = "best")
axes[2].grid(True)
plt.suptitle("Current response of the RL circuit to the fourier series approximation and the numerical methods")
plt.savefig("figs/fourier_vs_numerical.png")
plt.show()


#errors with the current response of the RL circuit to the fourier series approximation and the numerical methods
print("Mean Absolute Error in current response of Numerical methods vs Fourier Series\n")
n = 10000
t = np.linspace(0, 100, n)
error_forward_euler = np.array(nm.rl_forward_euler(R, L, alpha, amp, T / 10, h, n)[1]) - np.array(fs.compute_current(R, L, w0 * 10, t, alpha))
error_forward_euler = np.linalg.norm(error_forward_euler, ord = 1)
print("For Forward Euler:", error_forward_euler / n)

error_backward_euler = np.array(nm.rl_backward_euler(R, L, alpha, amp, T / 10, h, n)[1]) - np.array(fs.compute_current(R, L, w0 * 10, t, alpha))
error_backward_euler = np.linalg.norm(error_backward_euler, ord = 1)
print("For Backward Euler:", error_backward_euler / n)

error_trapezoidal = np.array(nm.rl_trapezoidal(R, L, alpha, amp, T / 10, h, n)[1]) - np.array(fs.compute_current(R, L, w0 * 10, t, alpha))
error_trapezoidal = np.linalg.norm(error_trapezoidal, ord = 1)
print("For Trapezoidal:", error_trapezoidal / n)

error_rk4 = np.array(nm.rl_rk4(R, L, alpha, amp, T / 10, h, n)[1]) - np.array(fs.compute_current(R, L, w0 * 10, t, alpha))
error_rk4 = np.linalg.norm(error_rk4, ord = 1)
print("For RK4:", error_rk4 / n)

error_adams_bashforth_moulton = np.array(nm.rl_adams_bashforth_moulton(R, L, alpha, amp, T / 10, h, n - 3)[1]) - np.array(fs.compute_current(R, L, w0 * 10, t, alpha))
error_adams_bashforth_moulton = np.linalg.norm(error_adams_bashforth_moulton, ord = 1)
print("For Adams Bashforth Moulton:", error_adams_bashforth_moulton / n)



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

print("\n\nVariation of Mean Absolute Error between the current response with input as forward euler and input as the Fourier approximation with number of terms int eh series:\n")

i2_10 = rl_forward_euler_fourier(1, 1, alpha, amp, T, h, 10, 1000)
error_10 = np.array(i1) - np.array(i2_10)
err_10 = np.linalg.norm(error_10, ord = 1)
print("N = 10 :", err_10 / 1000)

i2_50 = rl_forward_euler_fourier(1, 1, alpha, amp, T, h, 50, 1000)
error_50 = np.array(i1) - np.array(i2_50)
err_50 = np.linalg.norm(error_50, ord = 1)
print("N = 50 :", err_50 / 1000)

i2_100 = rl_forward_euler_fourier(1, 1, alpha, amp, T, h, 100, 1000)
error_100 = np.array(i1) - np.array(i2_100)
err_100 = np.linalg.norm(error_100, ord = 1)
print("N = 100 :", err_100 / 1000)

i2_1000 = rl_forward_euler_fourier(1, 1, alpha, amp, T, h, 1000, 1000)
error_1000 = np.array(i1) - np.array(i2_1000)
err_1000 = np.linalg.norm(error_1000, ord = 1)
print("N = 1000 :", err_1000 / 1000)

#here we can see that the error due to each term, that is the mean absolute error resuces to a great extent as N increases
