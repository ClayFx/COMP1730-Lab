import csv
import numpy as np
import pandas as pd


with open("daily-max-temp-CBR.csv") as csvfile:
    reader = csv.reader(csvfile)
    table = [ row for row in reader ]

print(table)

pd_weather_max = pd.read_csv("daily-max-temp-CBR.csv")
print(pd_weather_max.head())