import pandas as pd
from matplotlib import pyplot as plt

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

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
df = pd.read_csv("crashclean2.csv", usecols=columns)
df = df.drop(df[df.Latitude > 90].index)
df = df.drop(df[df.Longitude < -90].index)
# df = df.drop(df[df.AnimalRelated == False].index)
# df = df.drop(df[df.AnimalDeerRelated == False].index)
# df = df.drop(df[df.AlcoholRelated == False].index)
# df = df.drop(df[df.DrugRelated == False].index)
# df = df.drop(df[df.BicycleRelated == False].index)
df = df.drop(df[df.MotorCycleRelated == False].index)
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
plt.scatter(df.Latitude, df.Longitude, c=colors, s=1.5)
plt.axis('square')
plt.show()
