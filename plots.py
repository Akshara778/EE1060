import numerical_methods as nm
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

#Initializing the variables
r = 1
l = 1
amp = 1
T = 10
h = 0.001
n = 100000
cases = ["<<", "=", ">>"]

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
    #plt.plot(nm.rl_milne_simpson(r, l, alpha, amp, T, h, n)[0], nm.rl_milne_simpson(r, l, alpha, amp, T, h, n)[1], label = "Milne Simpson")
    ax1.legend()
    case = "Case " + str(i + 1) + ": l/r " + cases[i] + " T, alpha = 1/8"
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
    #plt.plot(nm.rl_milne_simpson(r, l, alpha, amp, T, h, n)[0], nm.rl_milne_simpson(r, l, alpha, amp, T, h, n)[1], label = "Milne Simpson")
    ax1.legend()
    case = "Case " + str(i + 1) + ": l/r " + cases[i] + " T, alpha = 1/2"
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
    #plt.plot(nm.rl_milne_simpson(r, l, alpha, amp, T, h, n)[0], nm.rl_milne_simpson(r, l, alpha, amp, T, h, n)[1], label = "Milne Simpson")
    ax1.legend()
    case = "Case " + str(i + 1) + ": l/r " + cases[i] + " T, alpha = 7/8"
    ax1.set_title(case)
    ax1.grid(True)
    #saving the plots
    plt.savefig("figs/Case_" + str(i + 1) + ".png")
    plt.show()

    T /= 10
    if(i == 0):
        n = 10000
    elif(i == 1):
        h = 0.0001
        n = 50000