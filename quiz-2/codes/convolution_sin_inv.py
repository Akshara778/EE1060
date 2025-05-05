import numpy as np
import matplotlib.pyplot as plt

omega = 2
T = 2

t = np.linspace(-2, 2, 1000)
input = np.arcsin(np.clip(omega * t, -1, 1))

kernel = np.where(t >= T, 0, np.where(t <= 0, 0, 1))

output = np.convolve(input, kernel, mode='same') * (t[1] - t[0])

plt.title('Convolution of Inverse Sine Function : '+ r'$sin^{-1}(\omega t)$')
plt.plot(t, input, label='Input Signal')
plt.plot(t, output, label='Output Signal')
plt.xlabel('Time (t)')
plt.ylabel('Signal Amplitude')
plt.legend()
plt.grid(True)
plt.savefig('../figs/convolution_sin_inv.png')
plt.show()
