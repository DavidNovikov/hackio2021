import pandas as pd
from matplotlib import pyplot as plt

accidentTypeToColor = {
    "Fatal": 'red',
    "Injury Possible": 'yellow',
    "Serious Injury Suspected": 'orange',
    "Property Damage Only": 'blue',
    "Minor Injury Suspected": 'green'}

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
columns = ["Latitude", "Longitude", "CrashSeverity"]
df = pd.read_csv("crashclean2.csv", usecols=columns)
df = df.drop(df[df.Latitude > 90].index)
df = df.drop(df[df.Longitude < -90].index)
colors = [accidentTypeToColor[crashtype] for crashtype in df.CrashSeverity]
plt.gca().legend(accidentTypeToColor)
print("Contents in csv file:\n", df)
plt.scatter(df.Latitude, df.Longitude, c=colors, s=0.5)
plt.show()
