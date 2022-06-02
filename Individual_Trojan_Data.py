import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
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

xv = []
yv = []
zv = []

with open('Planetary_Orbital_Data/Venus_position_data.txt', newline='') as empherides:
    reader = csv.DictReader(empherides)
    for row in reader:
        calendar_date.append(row['            Calendar Date (TDB)'])
        JDTDB.append(row['            JDTDB'])
        xv.append(float(row['                      X']))
        yv.append(float(row['                      Y']))
        zv.append(float(row['                      Z']))
    print('Position data for Saturn:')
    print(xv)
    print(yv)
    print(zv)

xr = []
yr = []
zr = []

with open('Planetary_Orbital_Data/Mercury_position_data.txt', newline='') as empherides:
    reader = csv.DictReader(empherides)
    for row in reader:
        calendar_date.append(row['            Calendar Date (TDB)'])
        JDTDB.append(row['            JDTDB'])
        xr.append(float(row['                      X']))
        yr.append(float(row['                      Y']))
        zr.append(float(row['                      Z']))
    print('Position data for Saturn:')
    print(xr)
    print(yr)
    print(zr)

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

# Barycenter position
ax.scatter3D(0, 0, 0, color='black', s=10, marker='o', label='Barycenter')

# ------------------------------------------------Collecting SPKID from Horizons Index---------------------------------

# df = pd.read_csv('Trojan_Asteroid_JPLQuery.csv')
# main_data = df.to_dict()
#
# spkid_list = []
#
# for n in main_data['spkid'].items():
#     spkid_list.append(n)
#
# low_e = []
# low_i = []
# for o in main_data['e'].items():
#     if o[1] < 0.075:
#         low_e.append(spkid_list[o[0]])
#
# for o in main_data['i'].items():
#     if o[1] < 10:
#         low_i.append(spkid_list[o[0]])
#
# print(low_i)
# print(len(low_e))
# print(len(spkid_list))

trojan_list = [2000624, 2000911, 2001437, 2001583, 2001647,
               2001867, 2001869, 2389331, 2355776, 2187656,
               54252384, 2335574, 2392454, 54122590, 3793796,
               54084410, 2326123, 2569986, 3481067, 2187657,
               54258691, 2188844, 2591781, 3427659, 2467635,
               2007152, 2263827, 2489934, 2013229, 2490014,
               2578694, 54126688, 54265512, 54122687, 54123919,
               3994824, 2267099, 54216154, 2204847, 2591015,
               2420741, 2312775, 2485416, 2051339, 2022008,
               54117609, 3870183, 2391792, 3794538, 54217870,
               54132471, 2295630, 54007319, 2257202, 2433275,
               2022009, 2222785, 2595533, 2430375, 2200036,
               3908420, 2352666, 2021371, 2195308, 2353350,
               2602133, 3471434, 2051405, 3628995, 2359975,
               2392207, 2603835, 2233600, 2347148, 2241581,
               2392208, 2321599, 3615689, 3792728, 2111736,
               2231572, 2282711, 2127846, 54255690, 2004827,
               2456110, 2222862, 2392700, 2285236, 2576430,
               2182541, 2380893, 3793059, 3793354, 54203822,
               3626283, 3756883, 2397790, 2257415, 2353196,
               2486686, 54014108, 2023114, 2542399, 2124696,
               3481811, 54141466, 54179270, 2353197, 2284442,
               2211992, 2077906, 2376869, 3946716, 2490834,
               2576527, 54156609, 2546827, 2065227, 2596258,
               2190352, 2490835, 54263463, 2568425, 2436072,
               3794753, 2550600, 54265356, 2391804, 2432629,
               2321513, 2347407, 2599267, 2008241, 2265294,
               54270990, 2389327, 2589366, 2432288, 2595238,
               2389332, 2157470, 2579712, 2111770, 54012105,
               2187659, 2387386, 2004902, 3625119, 54262638,
               54224927, 2344014, 54157864, 54020793, 54120383,
               2111771, 2301000, 54098651, 54096411, 2392456,
               2315923, 2488230, 2392223, 2599178, 2106091,
               3718530, 2263829, 2274773, 2392224, 3994689,
               54214129, 54199989, 2577971, 54089079, 3793416,
               2353203, 3494724, 3999399, 3793762, 54024935,
               3718412, 54218364, 2591017, 2098153, 3778348,
               2359961, 3769971, 2207892, 2353209, 2216291,
               2321628, 2053469, 54224831, 2022010, 2436151,
               2500784, 2607689, 2144840, 2433277, 54201142,
               2289285, 2275322, 2603743, 54255617, 3842989,
               2111571, 3825687, 2312472, 3846883, 54219426,
               2547957, 2391536, 2228098, 54213107, 2602136,
               2316134, 2356215, 2341857, 2496168, 2436405,
               3792901, 2393108, 2491868, 2020961, 2356425,
               54186865, 2009713, 2223272, 2335184, 2598398,
               2065590, 2264048, 2392462, 2471008, 54007989,
               54145702, 2350451, 2356426]

troj4_x = []
troj4_y = []
troj4_z = []

troj5_x = []
troj5_y = []
troj5_z = []

L4 = []
L5 = []

xs = []
ys = []
zs = []

tx = []
ty = []
tz = []

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
            # try:
            #     xs.append(float(row['             X_s'])/float(row['                      X']))
            #     ys.append(float(row['             Y_s'])/float(row['                      Y']))
            #     zs.append(float(row['             Z_s'])/float(row['                      Z']))
            # except KeyError:
            #     print('Missing uncertainty')

        print('Position data for Trojan Asteroid:')
        print(x)
        print(y)
        print(z)
        tx.append(x[t])
        ty.append(y[t])
        tz.append(z[t])
        if y[t] < 0:
            troj4_x.append(x[t])
            troj4_y.append(y[t])
            troj4_z.append(z[t])
            L4.append(spkid)
        else:
            troj5_x.append(x[t])
            troj5_y.append(y[t])
            troj5_z.append(z[t])
            L5.append(spkid)


def trojan_average_positon():
    L4avgx = sum(troj4_x) / len(troj4_x)
    L4avgy = sum(troj4_y) / len(troj4_y)
    L4avgz = sum(troj4_z) / len(troj4_z)

    L5avgx = sum(troj5_x) / len(troj5_x)
    L5avgy = sum(troj5_y) / len(troj5_y)
    L5avgz = sum(troj5_z) / len(troj5_z)

    # avgxs = sum(xs)/len(xs)
    # avgys = sum(ys)/len(ys)
    # avgzs = sum(zs)/len(zs)

    print(f'L4 Trojans: {L4}')
    print(f'L5 Trojans: {L5}')
    # print(f'Average position uncertainty in trojan positions (km): [{avgxs}, {avgys}, {avgzs}]')
    print(f'Trojans in L4: {len(troj4_x)}. Trojans in L5: {len(troj5_x)}')
    print(f'The average position of trojans in L4 is [{L4avgx}, {L4avgy}, {L4avgz}]')
    print(f'The average position of trojans in L5 is [{L5avgx}, {L5avgy}, {L5avgz}]')
    print(f'Jupiter position is [{xj[t]}, {yj[t]}, {zj[t]}]')

    ax.plot(L4avgx, L4avgy, L4avgz, marker='x', markersize=10, color='green', label='L4')
    ax.plot(L5avgx, L5avgy, L5avgz, marker='x', markersize=10, color='blue', label='L5')

    ax.plot([L4avgx, 0], [L4avgy, 0], [L4avgz, 0], linestyle='--')
    ax.plot([L5avgx, 0], [L5avgy, 0], [L5avgz, 0], linestyle='--')
    ax.plot([xj[t], 0], [yj[t], 0], [zj[t], 0], linestyle='--')
    ax.plot([xj[t], L4avgx], [yj[t], L4avgy], [zj[t], L4avgz], linestyle='--')
    ax.plot([xj[t], L5avgx], [yj[t], L5avgy], [zj[t], L5avgz], linestyle='--')


    L4v = [L4avgx, L4avgy, L4avgz]
    L5v = [L5avgx, L5avgy, L5avgz]
    Jupv = [xj[t], yj[t], zj[t]]

    def unit_vector(vec):
        return vec/np.linalg.norm(vec)

    L4v_u = unit_vector(L4v)
    L5v_u = unit_vector(L5v)
    Jupv_u = unit_vector(Jupv)

    def angle(vec1, vec2):
        dot = np.dot(vec1, vec2)
        ang = np.arccos(dot)
        return np.degrees(ang)

    L4_angle = angle(L4v_u, Jupv_u)
    L5_angle = angle(L5v_u, Jupv_u)

    print(f'The angle for L4 is: {L4_angle} degrees. And the angle for L5 is {L5_angle} degrees')


trojan_average_positon()

# ---------------------------------------------plotting-----------------------------------------------------------------

ax.scatter3D(xj[t], yj[t], zj[t], color='orange', label='Jupiter', s=25)
ax.scatter3D(xj, yj, zj, color='orange', s=0.25)

ax.scatter3D(xm[t], ym[t], zm[t], color='purple', label='Mars', s=25)
ax.scatter3D(xm, ym, zm, color='purple', s=0.25)

# ax.scatter3D(xs[t], ys[t], zs[t], color='blue', label='Saturn', s=25)
# ax.scatter3D(xs, ys, zs, color='blue', s=0.25)

ax.scatter3D(xe[t], ye[t], ze[t], color='yellow', label='Earth', s=25)
ax.scatter3D(xe, ye, ze, color='yellow', s=0.25)

ax.scatter3D(xv[t], yv[t], zv[t], color='pink', label='Venus', s=25)
ax.scatter3D(xv, yv, zv, color='pink', s=0.25)

ax.scatter3D(xr[t], yr[t], zr[t], color='red', label='Mercury', s=25)
ax.scatter3D(xr, yr, zr, color='red', s=0.25)

ax.scatter3D(xsu[t], ysu[t], zsu[t], color='yellow', label='Sun', s=25)
ax.scatter3D(xsu, ysu, zsu, color='yellow', s=0.25)

ax.scatter3D(tx, ty, tz, color='red', s=1)

plt.title(f'Orbital Data of the Solar System')
ax.view_init(elev=70, azim=-80)
plt.legend()
plt.show()


# print(low_i)
# print(low_e[2][1])
#
# low_e_i = list(set(low_e).intersection(low_i))
#
# print(low_e_i)
#
# trojans = []
#
# for n in low_e_i:
#     trojans.append(n[1])
#
# print(trojans)
