import csv
name_list = []
JDTDB = []
calendar_date = []
x = []
y = []
z = []

with open('2000624_empherides.txt', newline='') as empherides:
    reader = csv.DictReader(empherides)
    for row in reader:
        calendar_date.append(row['            Calendar Date (TDB)'])
        JDTDB.append(row['            JDTDB'])
        print(row)