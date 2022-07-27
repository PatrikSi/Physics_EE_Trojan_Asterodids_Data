import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

M_s = 1988500*10**24
M_j = 1898*10**24

sc = 2
mu = (M_j/M_s)*10**sc
R = 1
sun_pos = np.array([-mu*R, 0])
earth_pos = np.array([(1-mu)*R, 0])

N = 100
x, y = np.meshgrid(np.linspace(-1.5, 1.5, N), np.linspace(-1.5, 1.5, N))

term1 = -(1-mu) / ((x + mu)**2 + y**2)**0.5
term2 = -mu / ((x - (1-mu))**2 + y**2)**0.5
term3 = -0.5 * (x**2 + y**2)

u = term1 + term2 + term3

lw = 0.3
level = 200
plt.figure(figsize=(5, 5))
plt.ylim(-1.5, 1.5)
levels = np.linspace(-4, -1, level)
plt.contour(x, y, u, levels=levels, cmap=cm.jet, linewidths=lw)
plt.scatter([sun_pos[0]], [sun_pos[1]], c='y', s=50, label='Sun')
plt.scatter([earth_pos[0]], [earth_pos[1]], c='b', s=30, label='Jupiter')
plt.scatter([0], [0], c='black', marker='x')
plt.axis('equal')
plt.colorbar()
plt.title(f'scale factor: {sc}, layers: {level}')
plt.savefig(f'Potential_energy_plots/scale_{sc}_layers_{level}', dpi=300)
plt.show()