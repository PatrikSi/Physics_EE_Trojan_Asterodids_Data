import matplotlib.pyplot as plt

figure, ax = plt.subplots()
plt.xlim(-1.5, 3)
plt.ylim(-2, 2)


sun = plt.Circle((-0.4, 0), 0.3, fill=False, label='Body 1')
earth = plt.Circle((1.5, 0), 0.1, fill=False, label='Body 2')


plt.plot([0], marker='x', label='Barycenter', color='black')

ax.set_aspect(1)
ax.add_artist(sun)
ax.add_artist(earth)
plt.legend()
plt.show()