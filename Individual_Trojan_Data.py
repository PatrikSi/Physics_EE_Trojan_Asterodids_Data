import csv
import matplotlib.pyplot as plt
name_list = []
JDTDB = []
calendar_date = []
x = []
y = []
z = []

with open('2001437.txt', newline='') as empherides:
    reader = csv.DictReader(empherides)
    for row in reader:
        calendar_date.append(row['            Calendar Date (TDB)'])
        JDTDB.append(row['          JDTDB'])
        x.append(row['                      X'])
        y.append(row['                      Y'])
        z.append(row['                      Z'])
        xs = []
    plt.scatter(x, y)
    plt.show()