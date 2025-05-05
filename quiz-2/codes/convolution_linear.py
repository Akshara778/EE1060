import numpy as np
import matplotlib.pyplot as plt

def output(t, T, n):
    return ((t)**(n + 1) - (t - T)**(n + 1)) / (n + 1)

T = 2
n = 1
t = np.linspace(-10, 10, 10000)
output = output(t, T, n)
input = t**n

plt.title('Convolution of Linear Function : t')
plt.plot(t, input, color = 'blue', label = 'Input Signal')
plt.plot(t, output, color = 'red', label = 'Output Signal')
plt.xlabel('Time (t)')
plt.ylabel('Signal Amplitude')
plt.grid(True)
plt.legend()
plt.savefig('../figs/convolution_linear.png')
plt.show()