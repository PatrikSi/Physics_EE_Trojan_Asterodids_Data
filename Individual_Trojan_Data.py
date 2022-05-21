import csv
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
import pandas as pd

name_list = []
JDTDB = []
calendar_date = []
x = []
y = []
z = []
ax = plt.axes(projection="3d")

# All be started from 1800-01-01
# Step size = 60 days
# Coordinate center = Solar System Barycenter

# -------------------------------Position Data for Planets--------------------------------------------------------------

xj = []
yj = []
zj = []
t = 20  # Time to show all the objects
# JDTDB time to de determined by JDTDB = 2378496.5 + 60t

with open('Planetary_Orbital_Data/Jupiter_position_data.txt', newline='') as empherides:
    reader = csv.DictReader(empherides)
    for row in reader:
        calendar_date.append(row['            Calendar Date (TDB)'])
        JDTDB.append(row['            JDTDB'])
        xj.append(float(row['                      X']))
        yj.append(float(row['                      Y']))
        zj.append(float(row['                      Z']))
    print('Position data for Jupiter:')
    print(xj)
    print(yj)
    print(zj)
    ax.scatter3D(xj[t], yj[t], zj[t], color='orange', label='Jupiter', s=25)
    ax.scatter3D(xj, yj, zj, color='orange', s=0.25)

xm = []
ym = []
zm = []

with open('Planetary_Orbital_Data/Mars_position_data.txt', newline='') as empherides:
    reader = csv.DictReader(empherides)
    for row in reader:
        calendar_date.append(row['            Calendar Date (TDB)'])
        JDTDB.append(row['            JDTDB'])
        xm.append(float(row['                      X']))
        ym.append(float(row['                      Y']))
        zm.append(float(row['                      Z']))
    print('Position data for Mars:')
    print(xm)
    print(ym)
    print(zm)
    ax.scatter3D(xm[t], ym[t], zm[t], color='purple', label='Mars', s=25)
    ax.scatter3D(xm, ym, zm, color='purple', s=0.25)

xs = []
ys = []
zs = []

with open('Planetary_Orbital_Data/Saturn_position_data.txt', newline='') as empherides:
    reader = csv.DictReader(empherides)
    for row in reader:
        calendar_date.append(row['            Calendar Date (TDB)'])
        JDTDB.append(row['            JDTDB'])
        xs.append(float(row['                      X']))
        ys.append(float(row['                      Y']))
        zs.append(float(row['                      Z']))
    print('Position data for Saturn:')
    print(xs)
    print(ys)
    print(zs)
    ax.scatter3D(xs[t], ys[t], zs[t], color='blue', label='Saturn', s=25)
    ax.scatter3D(xs, ys, zs, color='blue', s=0.25)

xe = []
ye = []
ze = []
Calendar_Date = []

with open('Planetary_Orbital_Data/Earth_position_data.txt', newline='') as empherides:
    reader = csv.DictReader(empherides)
    for row in reader:
        calendar_date.append(row['            Calendar Date (TDB)'])
        JDTDB.append(row['            JDTDB'])
        xe.append(float(row['                      X']))
        ye.append(float(row['                      Y']))
        ze.append(float(row['                      Z']))
        calendar_date.append(row['            Calendar Date (TDB)'])

    print('Position data for Earth:')
    print(xe)
    print(ye)
    print(ze)
    print(f'Showing Positions for time {calendar_date[t]}')
    ax.scatter3D(xe[t], ye[t], ze[t], color='yellow', label='Earth', s=25)
    ax.scatter3D(xe, ye, ze, color='yellow', s=0.25)

# ------------------------------------------------Collecting SPKID from Horizons Index---------------------------------

df = pd.read_csv('Trojan_Asteroid_JPLQuery.csv')
main_data = df.to_dict()

spkid_list = []

for n in main_data['spkid'].items():
    spkid_list.append(n)

low_e = []
low_i = []
for o in main_data['e'].items():
    if o[1] < 0.075:
        low_e.append(spkid_list[o[0]])

for o in main_data['i'].items():
    if o[1] < 10:
        low_i.append(spkid_list[o[0]])


print(low_i)
print(len(low_e))
print(len(spkid_list))


trojan_list = [2000624, 2000911, 2001437, 2001583, 2001647,
               2001867, 2001869, 2389331, 2355776, 2187656,
               54252384, 2335574, 2392454, 54122590, 3793796,
               54084410, 2326123, 2569986, 3481067, 2187657,
               54258691, 2188844, 2591781]

for spkid in trojan_list:
    x = []
    y = []
    z = []
    with open(f'Asteroid_Orbital_Data/{spkid}.txt', newline='') as empherides:
        print(f'Going through {spkid}')
        reader = csv.DictReader(empherides)
        for row in reader:
            calendar_date.append(row['            Calendar Date (TDB)'])
            JDTDB.append(row['            JDTDB'])
            x.append(float(row['                      X']))
            y.append(float(row['                      Y']))
            z.append(float(row['                      Z']))
        print('Position data for Trojan Asteroid:')
        print(x)
        print(y)
        print(z)
        print(len(x))
        ax.scatter3D(x, y, z, color='black', s=0.001)
        ax.scatter3D(x[t], y[t], z[t], color='black', s=3)


plt.title(f'Orbital Data of the Solar System at time {calendar_date[t][:18]}')
plt.legend()
plt.show()

print(low_i)
print(low_e[2][1])

low_e_i = list(set(low_e).intersection(low_i))

print(low_e_i)

trojans = []

for n in low_e_i:
    trojans.append(n[1])

print(trojans)