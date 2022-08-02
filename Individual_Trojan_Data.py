import csv
import matplotlib.pyplot as plt
import numpy as np
import math

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
t = 68  # Time to show all the objects
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
               54145702, 2350451, 2356426, 3794764, 54143686,
               2356254, 3778449, 2249241, 2436124, 2164208,
               2387382, 54233097, 2340992, 2390334, 2356449,
               2291348, 3600676, 2163196, 2513251, 2105904,
               54260358, 2393170, 54219535, 54098766, 2129142,
               2437728, 2249486, 2063272, 3792500, 2103989,
               2257196, 54029191, 2026763, 54074344, 2131635,
               3793232, 2274506, 2058479, 2588733, 54200622,
               3596407, 54074355, 2103508, 2591034, 2001869,
               2009817, 2595538, 2320286, 2386649, 2225624,
               2266644, 54014103, 54122166, 2335178, 3829619,
               54071980, 2577188, 2229902, 2355818, 54218737,
               3890395, 2243314, 2389335, 2228111, 3756853,
               3435645, 2039287, 2001647, 2298614, 2432285,
               2487539, 54068829, 54155755, 3756858, 2589370,
               2316552, 2356245, 2039288, 3756859, 2257388,
               54271566, 2263803, 2379984, 3793427, 3778177,
               2257389, 2591738, 3904067, 3716800, 54067054,
               2310439, 2599180, 54209170, 2195415, 2576628,
               2295413, 2349923, 2591020, 3794298, 54131051,
               2531555, 2353205, 2225211, 2432264, 2183309,
               2269549, 54207747, 3792812, 2603745, 2204927,
               54225538, 2155327, 2262002, 2389572, 54156783,
               2607653, 2614047, 54201545, 3862776, 2420289,
               3917891, 2228101, 2269327, 2436403, 2353753,
               2031344, 2493531, 2377493, 54222436, 2219866,
               2275371, 3998106, 54122568, 2233790, 3981821,
               2185485, 2158336, 2264051, 54121993, 54220442,
               54215414, 2356427, 2514587, 2588160, 54199205,
               2065243, 2282336, 2473684, 2098139,
               2572622, 2301013, 54215162, 2360071, 54133941,
               2312636, 54224968, 54087003, 54228777, 2315952,
               2222056, 2599234, 2382264, 3999933, 2307569,
               2355842, 2042182, 54123375, 54251345, 2138031,
               54121954, 54051214, 2321113, 54259589, 54127428,
               3793294, 2088775, 2353178, 2360088, 54163170,
               2228148, 54209291, 2574428, 54097551, 54156604,
               54231385, 2257198, 54218709, 54096236, 2163245,
               2116567, 54219322, 2316692, 2392239, 2213119,
               2341008, 2546526, 2291437, 54186875, 3793420,
               2341052, 2001871, 2433286, 2284219, 2358981,
               3989476, 54154878, 54205815, 54222242, 2036265,
               2376536, 2358992, 2360143, 2296817, 2433287,
               2489535, 2376543, 2192390, 2589909, 2599823,
               2374564, 54264709, 54036247, 54138793, 54253399,
               54100875, 2163216, 2388940, 54104506, 3610095,
               54074847, 54222512, 2591783, 54201976, 2606989,
               2393206, 54118540, 2322540, 2510632, 54011278,
               2386854, 2316159, 2359940, 2251744, 54225088,
               2129130, 2166285, 54253316, 2390328, 2350191,
               54015993, 2328764, 54276334, 2349919, 2591066,
               2214506, 2184284, 2379531, 2599055, 2349920,
               2432261, 3609963, 54121981, 3999342, 2225213,
               3794662, 54200732, 3627183, 2343794, 54223677,
               3460086, 2426289, 2297160, 3792706, 54230379,
               2231636, 54213676, 3981248, 2396405, 2389574,
               3991925, 2355758, 2491403, 54103918, 2603709,
               2435560, 54149745, 2545598, 2156252, 2312477,
               54269558, 54183556, 54257393, 2599259, 54063833,
               54082501, 54220359, 2228103, 54104246, 2024452,
               2574785, 54047106, 3625838, 3993579, 3480947,
               2493533, 2228104, 2315905, 2343999, 3981745,
               2024453, 2259343, 2355310, 2428347, 2060421,
               2237025, 2355774, 2322068, 3794652, 2359000,
               54218938, 2532484, 2546590, 3794740, 2589882,
               2598361, 54218634, 2060388, 2589326, 2088241,
               2188842, 2263812, 54063553, 2099464, 2297144,
               2396350, 2542316, 2596801, 2356273, 2042179,
               2054596, 2315954, 54087877, 2296581, 54073985,
               2589279, 54078004, 2187478, 2347318, 54239174,
               2249258, 3624861, 54157678, 2572403, 54216867,
               2485414, 2225220, 2322553]

L4_spkid = [2000624, 2000911, 2001437, 2001583, 2001647, 2001869, 2389331, 2355776, 54252384, 2392454, 54122590, 3793796, 54084410, 2326123, 3481067, 54258691, 2591781, 3427659, 2467635, 2007152, 2263827, 2489934, 2013229, 2490014, 2578694, 54126688, 54265512, 54122687, 54123919, 2267099, 54216154, 2204847, 2591015, 2312775, 2022008, 54117609, 2391792, 3794538, 54217870, 54132471, 2295630, 54007319, 2257202, 2433275, 2022009, 2222785, 2595533, 2430375, 2200036, 2352666, 2021371, 2195308, 2353350, 2602133, 3471434, 2051405, 3628995, 2359975, 2392207, 2603835, 2233600, 2347148, 2241581, 2392208, 2321599, 3792728, 2111736, 2231572, 2127846, 54255690, 2222862, 2392700, 2285236, 3793059, 3793354, 54203822, 3626283, 3756883, 2257415, 2353196, 54014108, 2023114, 2542399, 3481811, 54141466, 54179270, 2353197, 2490834, 54156609, 2546827, 2065227, 2596258, 2190352, 2490835, 54263463, 2436072, 3794753, 54265356, 2391804, 2432629, 2321513, 2599267, 2008241, 2265294, 54270990, 2389327, 2589366, 2432288, 2595238, 2389332, 2111770, 54012105, 2387386, 2004902, 3625119, 54262638, 54224927, 2344014, 54157864, 54020793, 2111771, 54096411, 2392456, 2315923, 2392223, 2599178, 3718530, 2263829, 2274773, 2392224, 3994689, 54214129, 54199989, 54089079, 2353203, 3494724, 3793762, 54024935, 3718412, 54218364, 2591017, 3778348, 2359961, 2207892, 2353209, 2321628, 2053469, 54224831, 2022010, 2436151, 2500784, 2607689, 2144840, 2433277, 54201142, 2275322, 2603743, 54255617, 2111571, 3825687, 2312472, 3846883, 54219426, 2547957, 2391536, 2228098, 54213107, 2602136, 2316134, 2356215, 2496168, 2436405, 3792901, 2393108, 2491868, 2020961, 2356425, 54186865, 2009713, 2223272, 2598398, 2264048, 2392462, 2471008, 54007989, 2350451, 2356426, 3794764, 54143686, 2356254, 2249241, 2436124, 2164208, 2387382, 54233097, 2390334, 2356449, 3600676, 2163196, 54260358, 2393170, 54219535, 54098766, 2437728, 2249486, 2063272, 3792500, 2103989, 2257196, 54029191, 2026763, 3793232, 2274506, 2058479, 2588733, 54200622, 3596407, 2103508, 2591034, 2001869, 2009817, 2595538, 2320286, 2386649, 2225624, 2266644, 54014103, 54122166, 3829619, 2577188, 2229902, 2355818, 54218737, 3890395, 2243314, 2389335, 2228111, 3756853, 3435645, 2039287, 2001647, 2432285, 54068829, 54155755, 3756858, 2589370, 2316552, 2356245, 2039288, 3756859, 2257388, 54271566, 2263803, 3793427, 3778177, 2257389, 2591738, 3716800, 2310439, 2599180, 54209170, 2195415, 2349923, 2591020, 3794298, 54131051, 2353205, 2225211, 2432264, 2269549, 54207747, 3792812, 2603745, 2204927, 54225538, 2262002, 2389572, 54156783, 2607653, 2614047, 54201545, 3862776, 3917891, 2228101, 2269327, 2436403, 2353753, 2493531, 54222436, 2219866, 2275371, 3998106, 54122568, 2233790, 3981821, 2264051, 54121993, 54220442, 54215414, 2356427, 2588160, 2065243, 2572622, 54215162, 2360071, 2312636, 54224968, 54087003, 54228777, 2315952, 2222056, 2599234, 2307569, 2355842, 2042182, 54123375, 54251345, 2138031, 54121954, 54051214, 2321113, 54259589, 54127428, 3793294, 2353178, 2360088, 2228148, 54209291, 54097551, 54156604, 54231385, 2257198, 54218709, 54096236, 2163245, 54219322, 2392239, 2213119, 2546526, 54186875, 3793420, 2433286, 2358981, 54154878, 54205815, 54222242, 2036265, 2358992, 2360143, 2296817, 2433287, 2489535, 2376543, 2192390, 2589909, 2599823, 54264709, 54036247, 54138793, 54253399, 54100875, 2163216, 2388940, 54104506, 54222512, 2591783, 54201976, 2606989, 2393206, 54118540, 2322540, 54011278, 2386854, 2316159, 2359940, 2251744, 54225088, 2166285, 54253316, 2390328, 2350191, 54015993, 2328764, 2349919, 2591066, 2379531, 2599055, 2349920, 2432261, 54121981, 2225213, 3794662, 54200732, 3627183, 2343794, 54223677, 2297160, 3792706, 54230379, 2231636, 54213676, 3981248, 2396405, 2389574, 2355758, 2491403, 54103918, 2603709, 2435560, 54149745, 2312477, 54269558, 54183556, 54257393, 2599259, 54220359, 2228103, 54104246, 2574785, 3625838, 3480947, 2493533, 2228104, 2315905, 3981745, 2259343, 2355310, 2428347, 2060421, 2237025, 2355774, 2322068, 3794652, 2359000, 54218938, 2546590, 3794740, 2589882, 2598361, 54218634, 2060388, 2589326, 2088241, 2263812, 2099464, 2297144, 2396350, 2542316, 2356273, 2042179, 2315954, 54087877, 2296581, 2589279, 54078004, 54239174, 2249258, 3624861, 54157678, 54216867, 2225220, 2322553]

L5_spkid = [2001867, 2187656, 2335574, 2569986, 2187657, 2188844, 3994824, 2420741, 2485416, 2051339, 3870183, 3908420, 3615689, 2282711, 2004827, 2456110, 2576430, 2182541, 2380893, 2397790, 2486686, 2124696, 2284442, 2211992, 2077906, 2376869, 3946716, 2576527, 2568425, 2550600, 2347407, 2157470, 2579712, 2187659, 54120383, 2301000, 54098651, 2488230, 2106091, 2577971, 3793416, 3999399, 2098153, 3769971, 2216291, 2289285, 3842989, 2341857, 2335184, 2065590, 54145702, 3778449, 2340992, 2291348, 2513251, 2105904, 2129142, 54074344, 2131635, 54074355, 2335178, 54071980, 2298614, 2487539, 2379984, 3904067, 54067054, 2576628, 2295413, 2531555, 2183309, 2155327, 2420289, 2031344, 2377493, 2185485, 2158336, 2514587, 54199205, 2282336, 2473684, 2098139, 2301013, 54133941, 2382264, 3999933, 2088775, 54163170, 2574428, 2116567, 2316692, 2341008, 2291437, 2341052, 2001871, 2284219, 3989476, 2376536, 2374564, 3610095, 54074847, 2510632, 2129130, 54276334, 2214506, 2184284, 3609963, 3999342, 3460086, 2426289, 3991925, 2545598, 2156252, 54063833, 54082501, 2024452, 54047106, 3993579, 2343999, 2024453, 2532484, 2188842, 54063553, 2596801, 2054596, 54073985, 2187478, 2347318, 2572403, 2485414]


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

tx4 = []
ty4 = []
tz4 = []

for spkid in L4_spkid:
    x4 = []
    y4 = []
    z4 = []
    with open(f'Asteroid_Orbital_Data/{spkid}.txt', newline='') as empherides:
        print(f'Going through {spkid}')
        reader = csv.DictReader(empherides)
        for row in reader:
            calendar_date.append(row['            Calendar Date (TDB)'])
            JDTDB.append(row['            JDTDB'])
            x4.append(float(row['                      X']))
            y4.append(float(row['                      Y']))
            z4.append(float(row['                      Z']))
            # try:
            #     xs.append(float(row['             X_s'])/float(row['                      X']))
            #     ys.append(float(row['             Y_s'])/float(row['                      Y']))
            #     zs.append(float(row['             Z_s'])/float(row['                      Z']))
            # except KeyError:
            #     print('Missing uncertainty')

        print('Position data for Trojan Asteroid:')
        print(x4)
        print(y4)
        print(z4)
        tx4.append(x4[t])
        ty4.append(y4[t])
        tz4.append(z4[t])
        troj4_x.append(x4[t])
        troj4_y.append(y4[t])
        troj4_z.append(z4[t])

tx5 = []
ty5 = []
tz5 = []

for spkid in L5_spkid:
    x5 = []
    y5 = []
    z5 = []
    with open(f'Asteroid_Orbital_Data/{spkid}.txt', newline='') as empherides:
        print(f'Going through {spkid}')
        reader = csv.DictReader(empherides)
        for row in reader:
            calendar_date.append(row['            Calendar Date (TDB)'])
            JDTDB.append(row['            JDTDB'])
            x5.append(float(row['                      X']))
            y5.append(float(row['                      Y']))
            z5.append(float(row['                      Z']))
            # try:
            #     xs.append(float(row['             X_s'])/float(row['                      X']))
            #     ys.append(float(row['             Y_s'])/float(row['                      Y']))
            #     zs.append(float(row['             Z_s'])/float(row['                      Z']))
            # except KeyError:
            #     print('Missing uncertainty')

        print('Position data for Trojan Asteroid:')
        print(x5)
        print(y5)
        print(z5)
        tx5.append(x5[t])
        ty5.append(y5[t])
        tz5.append(z5[t])
        troj5_x.append(x5[t])
        troj5_y.append(y5[t])
        troj5_z.append(z5[t])

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

    L4_dist = math.dist([L4avgx, L4avgy, L4avgz], [xj[t], yj[t], zj[t]])
    L5_dist = math.dist([L5avgx, L5avgy, L5avgz], [xj[t], yj[t], zj[t]])

    print(f'L4 Trojans: {L4}')
    print(f'L5 Trojans: {L5}')
    # print(f'Average position uncertainty in trojan positions (km): [{avgxs}, {avgys}, {avgzs}]')
    print(f'Trojans in L4: {len(troj4_x)}. Trojans in L5: {len(troj5_x)}')
    print(f'The average position of trojans in L4 is [{L4avgx}, {L4avgy}, {L4avgz}]')
    print(f'The average position of trojans in L5 is [{L5avgx}, {L5avgy}, {L5avgz}]')
    print(f'Jupiter position is [{xj[t]}, {yj[t]}, {zj[t]}]')
    print(f'Jupiter-L4 distance is: {L4_dist}')
    print(f'Jupiter-L5 distance is: {L5_dist}')

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

ax.scatter3D(tx4, ty4, tz4, color='red', s=1)
ax.scatter3D(tx5, ty5, tz5, color='red', s=1)

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
