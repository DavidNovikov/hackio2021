import pandas as pd
columns = ["CrashSeverity"]
df = pd.read_csv("crashclean2.csv", usecols=columns)
for x in df.CrashSeverity.unique():
    print(x)
