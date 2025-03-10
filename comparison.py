import numpy as np
import matplotlib.pyplot as plt


def square(t, T, alpha, amp):
    if (t % T) < T * alpha:
        return amp
    else:
        return 0

def rl_forward_euler(r, l, alpha, amp, T, h, n):
    t_coord = []
    i_coord = []
    t = 0
    i = 0
    for j in range(n):
        t_coord.append(t)
        i_coord.append(i)
        i = i + (((square(t, T, alpha, amp) / l) - ((i * r) / l)) * h)
        t += h
    return [t_coord, i_coord]

def f(r, l, t, i, T, alpha, amp):
    return (square(t, T, alpha, amp) / l) - ((i * r) / l)

def rk4(k, r, l, T, alpha, amp, h):
    t = 0
    i = 0
    i_coord = []
    i_coord.append(i)
    for j in range(k - 1):
        k1 = h * f(r, l, t, i, T, alpha, amp)
        k2 = h * f(r, l, t + (h / 2), i + (k1 / 2), T, alpha, amp)
        k3 = h * f(r, l, t + (h / 2), i + (k2 / 2), T, alpha, amp)
        k4 = h * f(r, l, t + h, i + k3, T, alpha, amp)
        i += (k1 + (2 * k2) + (2 * k3) + k4) / 6
        t += h
        i_coord.append(i)
    return i_coord

def rl_milne_simpson(r, l, alpha, amp, T, h, n):
    t_coord = []
    i_coord = []
    t = 0
    i = 0
    y = rk4(4, r, l, T, alpha, amp, h)
    f_1 = f(r, l, t + h, y[1], T, alpha, amp)
    f_2 = f(r, l, t + (2 * h), y[2], T, alpha, amp)
    f_3 = f(r, l, t + (3 * h), y[3], T, alpha, amp)
    i_coord.append(y[0])
    i_coord.append(y[1])
    i_coord.append(y[2])
    t_coord.append(t)
    t_coord.append(t + h)
    t_coord.append(t + (2 * h))
    t = (3 * h)
    i = y[3]
    for j in range(n):
        t_coord.append(t)
        i_coord.append(i)
        i = i_coord[j] + (((4 * h) / 3) * ((2 * f_1) - f_2 + (2 * f_3))) #y_4p
        t += h
        f_1 = f_2
        f_2 = f_3
        f_3 = f(r, l, t, i, T, alpha, amp) #f_4p
        i = i_coord[j + 2] + ((h / 3) * (f_1 + (4 * f_2) + f_3)) #y_4c
        f_3 = f(r, l, t, i, T, alpha, amp) #f_4
    return [t_coord, i_coord]

print("Enter the values of R, L, alpha, amplitude and Time period if the input square wave in the same order.")
r, l, alpha, amp, T = float(input()), float(input()), float(input()), float(input()), float(input())

coord_1 = rl_forward_euler(r, l, alpha, amp, T, 0.001, int(50000 * T))
coord_2 = rl_milne_simpson(r, l, alpha, amp, T, 0.001, int(50000 * T))
coord_3 = rk4(int(50000 * T), r, l, T, alpha, amp, 0.001)

plt.figure()
plt.plot(coord_1[0][:], coord_1[1][:])
plt.plot(coord_2[0][:], coord_2[1][:])
plt.plot(np.linspace(0, int(50 * T), int(50000 * T)), coord_3)
plt.plot(np.linspace(0, int(50 * T), int(50000 * T)), [((amp / (2 * r)) * (1 - np.exp((-r * t) / l))) for t in np.linspace(0, int(50 * T), int(50000 * T))])
plt.xlabel("x")
plt.ylabel("y")
plt.title("Comparison")
plt.grid(True)
plt.legend(["Forward Euler", "Milne Simpson", "RK4", "DC"])
plt.show()
