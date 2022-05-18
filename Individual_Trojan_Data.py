import csv
name_list = []

with open('2000624_empherides.txt', newline='') as empherides:
    spamreader = csv.reader(empherides, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(', '.join(row))