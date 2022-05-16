import pandas as pd

df = pd.read_csv('Trojan_Asteroid_JPLQuery.csv')

main_data = df.to_dict()

print(len(main_data['spkid']))

e_list = []

for n in main_data['e'].items():
    e_list.append(n)

print(e_list[20])