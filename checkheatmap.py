import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("CrashSeverity.csv")
x = df['x'].tolist()
y = df['y'].tolist()
score = df['score'].tolist()
plt.scatter(x, y, c=score)
plt.show()
