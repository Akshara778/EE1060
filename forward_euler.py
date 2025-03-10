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

print("Enter the values of R, L, alpha, amplitude and Time period if the input square wave in the same order.")
r, l, alpha, amp, T = float(input()), float(input()), float(input()), float(input()), float(input())

coord = rl_forward_euler(r, l, alpha, amp, T, 0.001, int(50000 * T))
plt.figure()
plt.plot(coord[0][:], coord[1][:])
plt.xlabel("x")
plt.ylabel("y")
plt.title("RL Forward Euler")
plt.grid(True)
plt.show()
