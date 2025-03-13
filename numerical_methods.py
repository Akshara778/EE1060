import numpy as np


def square(t, T, alpha, amp):
    if (t % T) < T * alpha:
        return amp
    else:
        return 0

def f(r, l, t, i, T, alpha, amp):
    return (square(t, T, alpha, amp) / l) - ((i * r) / l)

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

def rl_backward_euler(r, l, alpha, amp, T, h, n):
    t_coord = []
    i_coord = []
    t = 0
    i = 0
    for j in range(n):
        t_coord.append(t)
        i_coord.append(i)
        i = (i + (h * square(t + h, T, alpha, amp) / l)) / (1 + (h * r / l))
        t += h
    return [t_coord, i_coord]

def rl_trapezoidal(r, l, alpha, amp, T, h, n):
    t_vals = np.linspace(0, n * h, n)
    v_in_vals = []
    for i in range(n):
        v_in_vals.append(square(t_vals[i], T, alpha, amp))

    i_vals = np.zeros_like(t_vals)
    
    for j in range(1, n):
        i_vals[j] = ((i_vals[j-1] * (2 * l - h * r)) + h * (v_in_vals[j] + v_in_vals[j-1])) / (2 * l + h * r)
    
    return [t_vals, i_vals]

def rl_rk4(r, l, alpha, amp, T, h, n):
    t = 0
    i = 0
    i_coord = []
    t_coord = []
    t_coord.append(t)
    i_coord.append(i)
    for j in range(n - 1):
        k1 = h * f(r, l, t, i, T, alpha, amp)
        k2 = h * f(r, l, t + (h / 2), i + (k1 / 2), T, alpha, amp)
        k3 = h * f(r, l, t + (h / 2), i + (k2 / 2), T, alpha, amp)
        k4 = h * f(r, l, t + h, i + k3, T, alpha, amp)
        i += (k1 + (2 * k2) + (2 * k3) + k4) / 6
        t += h
        t_coord.append(t)
        i_coord.append(i)
    return [t_coord, i_coord]

def rl_milne_simpson(r, l, alpha, amp, T, h, n):

    t_coord = []
    i_coord = []
    t = 0
    i = 0
    y = rl_rk4(r, l, alpha, amp, T, h, 4)
    f_1 = f(r, l, t + h, y[1][1], T, alpha, amp)
    f_2 = f(r, l, t + (2 * h), y[1][2], T, alpha, amp)
    f_3 = f(r, l, t + (3 * h), y[1][3], T, alpha, amp)
    i_coord.append(y[1][0])
    i_coord.append(y[1][1])
    i_coord.append(y[1][2])
    t_coord.append(t)
    t_coord.append(t + h)
    t_coord.append(t + (2 * h))
    t = (3 * h)
    i = y[1][3]
    for j in range(n):
        t_coord.append(t)
        i_coord.append(i)
        i_pred = i_coord[j] + (((4 * h) / 3) * ((2 * f_1) - f_2 + (2 * f_3)))
        f_pred = f(r, l, t + h, i_pred, T, alpha, amp)
        i = i_coord[j + 2] + ((h / 3) * (f_pred + (4 * f_3) + f_2))
        t += h
        f_1 = f_2
        f_2 = f_3
        f_3 = f(r, l, t, i, T, alpha, amp)
    return [t_coord, i_coord]

def rl_adams_bashforth_moulton(r, l, alpha, amp, T, h, n):
    t_coord = []
    i_coord = []
    t = 0
    i = 0
    y = rl_rk4(r, l, alpha, amp, T, h, 4)
    f_1 = f(r, l, t + h, y[1][0], T, alpha, amp)
    f_2 = f(r, l, t + (2 * h), y[1][1], T, alpha, amp)
    f_3 = f(r, l, t + (3 * h), y[1][2], T, alpha, amp)
    f_4 = f(r, l, t + (4 * h), y[1][3], T, alpha, amp)
    i_coord.append(y[1][0])
    i_coord.append(y[1][1])
    i_coord.append(y[1][2])
    t_coord.append(t)
    t_coord.append(t + h)
    t_coord.append(t + (2 * h))
    t = (3 * h)
    i = y[1][3]
    for j in range(n):
        t_coord.append(t)
        i_coord.append(i)
        i_pred = i_coord[j + 3] + ((h / 24) * ((55 * f_4) - (59 * f_3) + (37 * f_2) - (9 * f_1)))
        f_pred = f(r, l, t + h, i_pred, T, alpha, amp)
        i = i_coord[j + 3] + ((h / 24) * ((9 * f_pred) + (19 * f_4) - (5 * f_3) + f_2))
        t += h
        f_1 = f_2
        f_2 = f_3
        f_3 = f_4
        f_4 = f(r, l, t, i, T, alpha, amp)
    return [t_coord, i_coord]