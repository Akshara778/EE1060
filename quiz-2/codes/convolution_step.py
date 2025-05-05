import numpy as np
import matplotlib.pyplot as plt

def output(t, T):
    return np.where((t >= 0) & (t <= T), t, np.where(t < 0, 0, T))

T = 2
t = np.linspace(-10, 10, 1000)
output = output(t, T)
input = np.where(t < 0, 0, 1)

plt.title('Convolution of Step Function : u(t)')
plt.plot(t, input, color = 'blue', label = 'Input Signal')
plt.plot(t, output, color = 'red', label = 'Output Signal')
plt.xlabel('Time (t)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.savefig('../figs/convolution_step.png')
plt.show()