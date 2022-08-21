import matplotlib.pyplot as plt

with open('Planetary_Orbital_Data/Jupiter_position_data.txt') as jup:
    lin = jup.readlines()
    times_JD = [line.split()[0] for line in lin]

with open('Lagrange_Jupiter_distances.txt') as f:
    lines = f.readlines()
    print(lines)
    L4 = [line[4] for line in lines]
    L5 = [line[3] for line in lines]

print(times_JD)
print(L4)
print(L5)

plt.scatter(times_JD, L4)

plt.show()