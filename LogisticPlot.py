import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import glob

df = pd.read_csv("dataframe-2Full.csv")

print(df)
#plt.style.use('dark_background')

#plt.scatter(df['Flow rate'], df['Period'], marker='.', lw=0, s=1)

min_flow_rate = 4.92
df = df[df['Flow rate'] > min_flow_rate]

print(df)
plt.figure(figsize=(18.5, 10.5))


markers, caps, bars = plt.errorbar(df['Flow rate'], df['Period'], yerr=df['STD Period'], fmt='.',
                                   ecolor='red')
markers.set_markersize(1)
[bar.set_alpha(0.1) for bar in bars]
[cap.set_alpha(0.1) for cap in caps]

plt.xlabel("Flow Rate (drops/s)")
plt.ylabel("Period")

plt.tight_layout()
plt.show()