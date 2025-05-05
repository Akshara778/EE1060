import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

omega = 2

t = np.linspace(-5, 5, 500)
T = np.linspace(0, 2 * np.pi, 100)

T_grid, t_grid = np.meshgrid(T, t)

output_signal = ((2 * np.sin(omega * T_grid)) / omega) * np.cos((omega * t_grid) - ((omega * T_grid) / 2))

fig = plt.figure(figsize=(14,8))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(t_grid, T_grid, output_signal, cmap='viridis')

ax.set_title("Convolution with cos(ωt) and variation wrt T")
ax.set_xlabel('Time (t)')
ax.set_ylabel('Pulse Half-width (T)')
ax.set_zlabel('Signal')


norm = plt.Normalize(output_signal.min(), output_signal.max())
colors = cm.viridis(norm(output_signal))


m = cm.ScalarMappable(cmap=cm.viridis, norm=norm)
m.set_array([])
fig.colorbar(m, ax=ax, shrink=0.5, aspect=10, label='Amplitude')

#plt.savefig('../figs/convolution_cos.png')
plt.show()
