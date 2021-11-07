import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

from dictPopulating import avgRiskDictionary

accidentTypeToColor = {
    "Fatal": 'red',
    "Injury Possible": 'yellow',
    "Serious Injury Suspected": 'orange',
    "Property Damage Only": 'blue',
    "Minor Injury Suspected": 'green'}

columns = ["Latitude", "Longitude", "CrashSeverity",
           "AnimalRelated",
           "AnimalDeerRelated",
           "AlcoholRelated",
           "DrugRelated",
           "BicycleRelated",
           "MotorCycleRelated",
           "SpeedRelated",
           "PedestrianRelated",
           "SemiTruckRelated",
           "SmallTruckRelated",
           "YouthRelated",
           "TeenRelated",
           "DUI21Related",
           "SeniorRelated"]

xMax = 40.15
xMin = 39.75
yMax = -82.7
yMin = -83.3
step = 0.0005

df = pd.read_csv("crashclean2.csv", usecols=columns)
df = df.drop(df[df.Latitude > 90].index)
df = df.drop(df[df.Longitude < -90].index)
df = df.drop(df[pd.isna(df.Longitude)].index)
df = df.drop(df[pd.isna(df.Latitude)].index)
df = df.drop(df[df.CrashSeverity != "Property Damage Only"].index)
# df = df.drop(df[df.AnimalRelated == False].index)
# df = df.drop(df[df.AnimalDeerRelated == False].index)
# df = df.drop(df[df.AlcoholRelated == False].index)
# df = df.drop(df[df.DrugRelated == False].index)
# df = df.drop(df[df.BicycleRelated == False].index)
# df = df.drop(df[df.MotorCycleRelated == False].index)
# df = df.drop(df[df.SpeedRelated == False].index)
# df = df.drop(df[df.PedestrianRelated == False].index)
# df = df.drop(df[df.SemiTruckRelated == False].index)
# df = df.drop(df[df.SmallTruckRelated == False].index)
# df = df.drop(df[df.YouthRelated == False].index)
# df = df.drop(df[df.TeenRelated == False].index)
# df = df.drop(df[df.DUI21Related == False].index)
# df = df.drop(df[df.SeniorRelated == False].index)
colors = [accidentTypeToColor[crashtype] for crashtype in df.CrashSeverity]
plt.gca().legend(accidentTypeToColor)
print("Contents in csv file:\n", df)
heat = avgRiskDictionary(xMin, xMax, yMin, yMax, step, df)
# plt.scatter(df.Longitude, df.Latitude, c=colors, s=.25)
# plt.axis('square')
# plt.imshow(heat, cmap='hot', interpolation='nearest')
fig, ax = plt.subplots()
x = list(set([i[0] for i in heat.keys()]))
y = list(set([i[1] for i in heat.keys()]))
x.sort()
y.sort()
Z = np.array([[h for h in heat.values()]])
shape = (len(x), len(y))
Z = Z.reshape(shape)
ax.pcolormesh(y, x, Z)
ax.set_aspect('equal', adjustable='box')
# plt.axis('square')
plt.show()
