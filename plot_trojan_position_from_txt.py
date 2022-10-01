import matplotlib.pyplot as plt
import csv

JD_times = []
L4 = []
L5 = []
times = []

with open('Lagrange_Jupiter_distances.txt', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        JD_times.append(row['JD_time'])
        L4.append(float(row['L4_distance']))
        L5.append(float(row['L5_distnace']))
        times.append(float(row['time']))

print(JD_times)
print(L4)
print(L5)

plt.scatter(times, L4, label='L4-Jupiter Distance')
plt.scatter(times, L5, label='L5-Jupiter Distance')
plt.legend()
plt.ylim(0, 10**9)
plt.ylabel("distance (m)")
plt.xlabel("time (days)")

plt.show()
