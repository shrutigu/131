#WORK OF @eshaant7

import csv
import numpy as np
import pandas as pd

data = []

df = pd.read_csv("merged_data_sorted.csv")

with open("merged_data_sorted.csv", 'r') as f:
    csv_reader = csv.reader(f)
    for i in csv_reader:
        data.append(i)

headers = data[0]
star_data_rows = data[1:]

headers[0] = "row_num"

print(headers)
print(star_data_rows[0])

star_names = []
star_radii = []
star_masses = []

for star_data in star_data_rows:
    star_masses.append(star_data[7])
    star_radii.append(star_data[8])
    star_names.append(star_data[1])

solar_mass_kg = []

for data in star_masses:
    kg_unit = float(data)*1.989e+30
    solar_mass_kg.append(kg_unit)

print(solar_mass_kg)

solar_radius_si = []

for data in star_radii:
    si_unit = float(data)* 6.957e+8
    solar_radius_si.append(si_unit)

print(solar_radius_si)

print(star_masses)
print(star_radii)
print(star_names)

star_gravities = []

for index, name in enumerate(star_names):
    gravity = (float(star_masses[index])*5.972e+24)/(float(star_radii[index])*float(star_radii[index])*6371000*6371000)*6.674e-11
    star_gravities.append(gravity)

print(star_names[0])
print(star_gravities[0])

df["solar_gravities"] = star_gravities

df.to_csv("new_merged.csv")




