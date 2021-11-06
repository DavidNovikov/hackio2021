import pandas as pd
columns = ["Latitude", "Longitude", "CrashSeverity"]
df = pd.read_csv("crashclean2.csv", usecols=columns)
df = df.drop(df[df.Latitude > 90].index)
df = df.drop(df[df.Longitude < -90].index)
