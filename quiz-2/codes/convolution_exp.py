import numpy as np
import matplotlib.pyplot as plt

def output(t, T, a):
    return (1 / a) * (np.exp(-a * (t - T)) - np.exp(-a * (t)))

T = 2
a = 0.1
t = np.linspace(-5, 15, 10000)
output = output(t, T, a)
input = np.exp(-a * t)

plt.title('Convolution of Exponential Function : '+ r'$e^{-at}$')
plt.plot(t, input, color = 'blue', label = 'Input Signal')
plt.plot(t, output, color = 'red', label = 'Output Signal')
plt.xlabel('Time (t)')
plt.ylabel('Signal Amplitude')
plt.grid(True)
plt.legend()
plt.savefig('../figs/convolution_exp.png')
plt.show()