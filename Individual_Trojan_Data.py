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
    ax.scatter3D(x, y, z, color='red')

    xj = []
    yj = []
    zj = []

with open('Jupiter_position_data.txt', newline='') as empherides:
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
    ax.scatter3D(xj, yj, zj, color='orange')

xm = []
ym = []
zm = []

with open('Mars_position_data.txt', newline='') as empherides:
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



plt.title('Scatter')
plt.show()