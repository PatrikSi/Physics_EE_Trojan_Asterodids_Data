import matplotlib.pyplot as plt
import numpy as np

sx = -0.6
sy = 0

ex = 1.5
ey = 0

figure, ax = plt.subplots()
plt.xlim(-2, 3)
plt.ylim(-2, 2)


sun = plt.Circle((sx, sy), 0.3, fill=False, label='Body 1')
earth = plt.Circle((ex, ey), 0.1, fill=False, label='Body 2')

so = plt.Circle((0, 0), sx, fill=False, label='Body 1 Orbit', linestyle='--')
eo = plt.Circle((0, 0), ex, fill=False, label='Body 2 Orbit', linestyle='--')

v_1 = plt.plot([0,sx], [0,sy], linestyle='-', label='v1', color='black')
v_2 = plt.plot([0,ex], [0,ey], linestyle='-', label='v2', color='black')
v_4 = plt.plot([0,(3/4)], [0,((3*np.sqrt(3))/4)], linestyle='-', label='v4', color='black')
v_5 = plt.plot([0,(3/4)], [0,-((3*np.sqrt(3))/4)], linestyle='-', label='v5', color='black')


bary = plt.plot([0], marker='o', label='Barycenter', color='black')

L1 = plt.plot([0.8*ex], [0], marker='x', label='L1', color='black')
L2 = plt.plot([1.2*ex], [0], marker='x', label='L2', color='black')
L3 = plt.plot([1.7*sx], [0], marker='x', label='L3', color='black')
L4 = plt.plot([3/4], [(3*np.sqrt(3))/4], marker='x', label='L4', color='black')
L5 = plt.plot([3/4], [-(3*np.sqrt(3))/4], marker='x', label='L5', color='black')



ax.set_aspect(1)
ax.add_artist(sun)
ax.add_artist(so)
ax.add_artist(eo)
ax.add_artist(earth)
plt.legend()
plt.show()