import matplotlib.pyplot as plt

sx = -0.6
sy = 0

ex = 1.5
ey = 0

figure, ax = plt.subplots()
plt.xlim(-1.5, 3)
plt.ylim(-2, 2)


sun = plt.Circle((sx, sy), 0.3, fill=False, label='Body 1')
earth = plt.Circle((ex, ey), 0.1, fill=False, label='Body 2')

v_1 = plt.plot([0,sx], [0,sy], linestyle='-', label='v1', color='black')
v_2 = plt.plot([0,ex], [0,ey], linestyle='-', label='v2', color='black')

plt.plot([0], marker='x', label='Barycenter', color='black')

ax.set_aspect(1)
ax.add_artist(sun)
ax.add_artist(earth)
plt.legend()
plt.show()