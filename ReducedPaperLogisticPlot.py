import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import glob

df = pd.read_csv("dataframe-2Full.csv")

tnr_font = {'fontname': 'Times New Roman'}
fig, ax = plt.subplots()

ax.set_xlabel("Flow Rate (drops/s)", **tnr_font)
ax.set_ylabel("Period (s)", **tnr_font)

flow_rates = df['Flow rate'].unique()
min_flow_rate = 4.81
df_Zoom = df[df['Flow rate'] > min_flow_rate]
print(df_Zoom)

markers, caps, bars = ax.errorbar(df['Flow rate'], df['Period'], yerr=df['STD Period'], fmt='.',
                                  ecolor='red')
markers.set_markersize(1)
[bar.set_alpha(0.1) for bar in bars]
[cap.set_alpha(0.1) for cap in caps]

x1, x2, y1, y2 = 4.81, 20.7, .030, .22  # subregion of the original image
axins = ax.inset_axes(
    [.3, .25, .8, 0.8],
    xlim=(x1, x2), ylim=(y1, y2))
markers, caps, bars = axins.errorbar(df['Flow rate'], df['Period'], yerr=df['STD Period'], fmt='.',
                                  ecolor='red')

markers.set_markersize(.5)
[bar.set_alpha(0.1) for bar in bars]
[cap.set_alpha(0.1) for cap in caps]

ax.indicate_inset_zoom(axins, edgecolor="black")

plt.tight_layout()
plt.show()
