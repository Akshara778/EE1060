import numerical_methods as nm
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import os


#creting directory for figures
os.makedirs('figs', exist_ok=True)

#Initializing the variables
r = 1
l = 1
amp = 10
T = 10
h = 0.01
n = 1000000
n_alpha = 20000
cases = ["<<", "=", ">>"]
titles = [r"$\alpha = \frac{1}{8}$", r"$\alpha = \frac{1}{2}$", r"$\alpha = \frac{7}{8}$"]

#plotting for the 3 cases of l/r
for i in range(3):
    fig = plt.figure(figsize=(10, 8))
    gs = gridspec.GridSpec(2, 2, height_ratios=[1, 0.8])
    #Sub Case 1: alpha = 1/8
    alpha = 1/8
    ax1 = fig.add_subplot(gs[0, 0])
    ax1.plot(nm.rl_forward_euler(r, l, alpha, amp, T, h, n)[0], nm.rl_forward_euler(r, l, alpha, amp, T, h, n)[1], label = "Forward Euler")
    ax1.plot(nm.rl_backward_euler(r, l, alpha, amp, T, h, n)[0], nm.rl_backward_euler(r, l, alpha, amp, T, h, n)[1], label = "Backward Euler")
    ax1.plot(nm.rl_trapezoidal(r, l, alpha, amp, T, h, n)[0], nm.rl_trapezoidal(r, l, alpha, amp, T, h, n)[1], label = "Trapezoidal")
    ax1.plot(nm.rl_rk4(r, l, alpha, amp, T, h, n)[0][:], nm.rl_rk4(r, l, alpha, amp, T, h, n)[1][:], label = "RK4")
    ax1.plot(nm.rl_adams_bashforth_moulton(r, l, alpha, amp, T, h, n)[0], nm.rl_adams_bashforth_moulton(r, l, alpha, amp, T, h, n)[1], label = "Adams Bashforth Moulton")
    #ax1.plot(nm.rl_milne_simpson(r, l, alpha, amp, T, h, n)[0], nm.rl_milne_simpson(r, l, alpha, amp, T, h, n)[1], label = "Milne Simpson")
    ax1.legend()
    case = "Case " + str(i + 1) + ": L/R " + cases[i] + " T, " + titles[0]
    ax1.set_xlabel("Time (t)")
    ax1.set_ylabel("Current (i)")
    ax1.set_title(case)
    ax1.grid(True)

    #Sub Case 2: alpha = 1/2
    alpha = 1/2
    ax1 = fig.add_subplot(gs[0, 1])
    ax1.plot(nm.rl_forward_euler(r, l, alpha, amp, T, h, n)[0], nm.rl_forward_euler(r, l, alpha, amp, T, h, n)[1], label = "Forward Euler")
    ax1.plot(nm.rl_backward_euler(r, l, alpha, amp, T, h, n)[0], nm.rl_backward_euler(r, l, alpha, amp, T, h, n)[1], label = "Backward Euler")
    ax1.plot(nm.rl_trapezoidal(r, l, alpha, amp, T, h, n)[0], nm.rl_trapezoidal(r, l, alpha, amp, T, h, n)[1], label = "Trapezoidal")
    ax1.plot(nm.rl_rk4(r, l, alpha, amp, T, h, n)[0][:], nm.rl_rk4(r, l, alpha, amp, T, h, n)[1][:], label = "RK4")
    ax1.plot(nm.rl_adams_bashforth_moulton(r, l, alpha, amp, T, h, n)[0], nm.rl_adams_bashforth_moulton(r, l, alpha, amp, T, h, n)[1], label = "Adams Bashforth Moulton")
    #ax1.plot(nm.rl_milne_simpson(r, l, alpha, amp, T, h, n)[0], nm.rl_milne_simpson(r, l, alpha, amp, T, h, n)[1], label = "Milne Simpson")
    ax1.legend()
    case = "Case " + str(i + 1) + ": L/R " + cases[i] + " T, " + titles[1]
    ax1.set_xlabel("Time (t)")
    ax1.set_ylabel("Current (i)")
    ax1.set_title(case)
    ax1.grid(True)

    #Sub Case 3: alpha = 7/8
    alpha = 7/8
    ax1 = fig.add_subplot(gs[1, :])
    ax1.plot(nm.rl_forward_euler(r, l, alpha, amp, T, h, n)[0], nm.rl_forward_euler(r, l, alpha, amp, T, h, n)[1], label = "Forward Euler")
    ax1.plot(nm.rl_backward_euler(r, l, alpha, amp, T, h, n)[0], nm.rl_backward_euler(r, l, alpha, amp, T, h, n)[1], label = "Backward Euler")
    ax1.plot(nm.rl_trapezoidal(r, l, alpha, amp, T, h, n)[0], nm.rl_trapezoidal(r, l, alpha, amp, T, h, n)[1], label = "Trapezoidal")
    ax1.plot(nm.rl_rk4(r, l, alpha, amp, T, h, n)[0][:], nm.rl_rk4(r, l, alpha, amp, T, h, n)[1][:], label = "RK4")
    ax1.plot(nm.rl_adams_bashforth_moulton(r, l, alpha, amp, T, h, n)[0], nm.rl_adams_bashforth_moulton(r, l, alpha, amp, T, h, n)[1], label = "Adams Bashforth Moulton")
    #ax1.plot(nm.rl_milne_simpson(r, l, alpha, amp, T, h, n)[0], nm.rl_milne_simpson(r, l, alpha, amp, T, h, n)[1], label = "Milne Simpson")
    ax1.legend()
    case = "Case " + str(i + 1) + ": L/R " + cases[i] + " T, " + titles[2]
    ax1.set_xlabel("Time (t)")
    ax1.set_ylabel("Current (i)")
    ax1.set_title(case)
    ax1.grid(True)
    #saving the plots
    plt.savefig("figs/numerical_methods_plot_" + str(i + 1) + ".png")
    plt.show()

    #General case for all values of alpha
    plt.figure()
    ax = plt.axes(projection='3d')
    alpha = np.linspace(0, 1, 50)
    time = np.linspace(0, 20, n_alpha)
    for j in alpha:
        ax.plot3D(time, np.full_like(time, j), nm.rl_rk4(r, l, j, amp, T, h, n_alpha)[1][:])
    ax.set_xlabel("Time (t)")
    ax.set_ylabel("Alpha (" + r"$\alpha$" + ")")
    ax.set_zlabel("Current (i)")
    ax.set_title("General Case: L/R " + cases[i] + " T")
    ax.view_init(elev = 25, azim = -108)
    plt.savefig("figs/general_plot_" + str(i + 1) + ".png")
    plt.show()

   