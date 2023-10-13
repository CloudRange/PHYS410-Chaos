import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import glob

df = pd.read_csv("dataframe-FullData.csv")

print(df)
plt.style.use('dark_background')

plt.scatter(df['Flow rate'], df['Period'], marker='.', lw=0, s=1)

plt.xlabel("Flow Rate (drops/s)")
plt.ylabel("Period")
plt.tight_layout()
plt.show()