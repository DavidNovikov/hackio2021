import pandas as pd
columns = ["Weather"]
df = pd.read_csv("crashclean2.csv", usecols=columns)
for x in df.Weather.unique():
    print(x)
