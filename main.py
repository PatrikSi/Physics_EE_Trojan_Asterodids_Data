import pandas as pd
import requests

df = pd.read_csv('Trojan_Asteroid_JPLQuery.csv')

main_data = df.to_dict()

print(len(main_data['spkid']))

spkid_list = []

for n in main_data['spkid'].items():
    spkid_list.append(n)

print(spkid_list[2])

# SBDB Request link: https://ssd-api.jpl.nasa.gov/sbdb.api

spkid = spkid_list[2]

req = requests.get(f'https://ssd-api.jpl.nasa.gov/sbdb.api?spk={spkid}&phys-par=1')

print(req)