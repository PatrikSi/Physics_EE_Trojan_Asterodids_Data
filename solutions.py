import numpy as np
import matplotlib.pyplot as plt
import csv

xj = []
yj = []
zj = []
calendar_date = []
JDTDB = []

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

javgx = (sum(xj)/len(xj))*10**3
javgy = (sum(yj)/len(yj))*10**3
javgz = (sum(zj)/len(zj))*10**3

r_j = np.sqrt((javgx)**2 +(javgy)**2 + (javgz)**2)

xsu = []
ysu = []
zsu = []

with open('Planetary_Orbital_Data/Sun_position_data.txt', newline='') as empherides:
    reader = csv.DictReader(empherides)
    for row in reader:
        calendar_date.append(row['            Calendar Date (TDB)'])
        JDTDB.append(row['            JDTDB'])
        xsu.append(float(row['                      X']))
        ysu.append(float(row['                      Y']))
        zsu.append(float(row['                      Z']))
    print('Position data for Saturn:')
    print(xsu)
    print(ysu)
    print(zsu)

savgx = sum(xsu)/len(xsu)
savgy = sum(ysu)/len(ysu)
savgz = sum(zsu)/len(zsu)

r_s = np.sqrt((savgx)**2 +(savgy)**2 + (savgz)**2)


G = 6.67*10**-11

M_s = 1988500*10**24
M_j = 1898*10**24

print(f'Mean Orbital Radius of Jupiter is: {r_j} m')
print(f'Mean Orbital Radius of sun is : {r_s} m')