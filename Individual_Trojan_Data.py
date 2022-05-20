import csv
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np

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

with open('horizons_results_4_x-y.txt', newline='') as empherides:
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
    ax.scatter3D(x, y, z, color='red', label='Trojan Asteroid')

    xj = []
    yj = []
    zj = []

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
    ax.scatter3D(xj, yj, zj, color='orange', label='Jupiter')

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
    ax.scatter3D(xm, ym, zm, color='purple', label='Mars')

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
    ax.scatter3D(xs, ys, zs, color='blue', label='Saturn')

xe = []
ye = []
ze = []


with open('Planetary_Orbital_Data/Earth_position_data.txt', newline='') as empherides:
    reader = csv.DictReader(empherides)
    for row in reader:
        calendar_date.append(row['            Calendar Date (TDB)'])
        JDTDB.append(row['            JDTDB'])
        xe.append(float(row['                      X']))
        ye.append(float(row['                      Y']))
        ze.append(float(row['                      Z']))
    print('Position data for Earth:')
    print(xe)
    print(ye)
    print(ze)
    ax.scatter3D(xe, ye, ze, color='yellow', label='Earth')


plt.title('Orbital Data of the Solar System')
plt.legend()
plt.show()