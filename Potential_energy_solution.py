import numpy as np
import matplotlib.pyplot as plt

mu = 0.0953
R = 1
sun_pos = np.array([-mu*R, 0])
earth_pos = np.array([(1-mu)*R, 0])

N = 1000
x, y = np.meshgrid(np.linspace(-1.5, 1.5, N), np.linspace(-1.5, 1.5, N))

term1 = -(1-mu) / ((x + mu)**2 + y**2)**0.5
term2 = -mu / ((x - (1-mu))**2 + y**2)**0.5
term3 = -0.5 * (x**2 + y**2)

u = term1 + term2 + term3

plt.figure(figsize=(5, 5))
levels = np.linspace(-1.8, -1.4, 50)
plt.contour(x, y, u, levels=levels)
plt.scatter([sun_pos[0]], [sun_pos[1]], c='y', s=50, label='Sun')
plt.scatter([earth_pos[0]], [earth_pos[1]], c='b', s=30, label='Jupiter')
plt.scatter([0], [0], c='black', marker='x')
plt.axis('equal')
plt.legend()
plt.show()