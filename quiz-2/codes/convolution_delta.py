import numpy as np
import matplotlib.pyplot as plt

def output(t, T):
    return np.where((t > 0) & (t < T), 1, 0)

t = np.linspace(-5, 5, 500)
T = 2
output = output(t, T)

plt.plot(t, output, color = 'red', label = 'Output Signal')
plt.stem(0, 10, label = 'Input Signal')
plt.title('Convolution with Delta Function')
plt.xlabel('Time (t)')
plt.ylabel('Signal Amplitude')
plt.legend()
plt.grid(True)
plt.savefig('../figs/convolution_delta.png', dpi=300, bbox_inches='tight')
plt.show()