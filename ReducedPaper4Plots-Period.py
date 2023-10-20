import matplotlib.pyplot as plt
import matplotlib.text as txt

import numpy as np
import pandas as pd
import glob


def get_data(flow_rate):
    return df[df['Flow rate'] == flow_rate]

## 13.66 -
df = pd.read_csv("dataframe-2FUll.csv")

tnr_font = {'fontname': 'Times New Roman'}

flow_rates = [5.719670833401112, 6.177258304946978, 9.807763134831008, 9.854420061171115, 10.363508560848793,
              13.268496735578289]

figure, axis = plt.subplots(3, 2)

axis[1][0].set_ylabel("Period$_{n}$ (s)", **tnr_font)
axis[2][0].set_xlabel("Number of Drops ($n$) ", **tnr_font)
axis[2][1].set_xlabel("Number of Drops ($n$) ", **tnr_font)

temp_df = get_data(flow_rates[0])
markers, caps, bars = axis[0][0].errorbar(range(1, len(temp_df['Period'])+1), temp_df['Period'],
                                       yerr=temp_df['STD Period'], fmt='.',
                                       ecolor='red')
[bar.set_alpha(0.1) for bar in bars]
[cap.set_alpha(0.1) for cap in caps]

temp_df = get_data(flow_rates[1])
markers, caps, bars = axis[0][1].errorbar(range(1, len(temp_df['Period'])+1), temp_df['Period'],
                                       yerr=temp_df['STD Period'], fmt='.',
                                       ecolor='red')
[bar.set_alpha(0.1) for bar in bars]
[cap.set_alpha(0.1) for cap in caps]

temp_df = get_data(flow_rates[2])
markers, caps, bars = axis[1][0].errorbar(range(1, len(temp_df['Period'])+1), temp_df['Period'],
                                       yerr=temp_df['STD Period'], fmt='.',
                                       ecolor='red')
[bar.set_alpha(0.1) for bar in bars]
[cap.set_alpha(0.1) for cap in caps]

temp_df = get_data(flow_rates[3])
markers, caps, bars = axis[1][1].errorbar(range(1, len(temp_df['Period'])+1), temp_df['Period'],
                                       yerr=temp_df['STD Period'], fmt='.',
                                       ecolor='red')
[bar.set_alpha(0.1) for bar in bars]
[cap.set_alpha(0.1) for cap in caps]

temp_df = get_data(flow_rates[4])
markers, caps, bars = axis[2][0].errorbar(range(1, len(temp_df['Period'])+1), temp_df['Period'],
                                       yerr=temp_df['STD Period'], fmt='.',
                                       ecolor='red')
[bar.set_alpha(0.1) for bar in bars]
[cap.set_alpha(0.1) for cap in caps]

temp_df = get_data(flow_rates[5])
markers, caps, bars = axis[2][1].errorbar(range(1, len(temp_df['Period'])+1), temp_df['Period'],
                                       yerr=temp_df['STD Period'], fmt='.',
                                       ecolor='red')
[bar.set_alpha(0.1) for bar in bars]
[cap.set_alpha(0.1) for cap in caps]

figure.set_size_inches(5, 5)
plt.tight_layout()





plt.text(0.03, 0.90, 'a)', **tnr_font,
         horizontalalignment='center',
         verticalalignment='center',
         transform=axis[0][0].transAxes)




plt.text(0.03, 0.90, 'b)', **tnr_font,
         horizontalalignment='center',
         verticalalignment='center',
         transform=axis[0][1].transAxes)




plt.text(0.03, 0.90, 'c)', **tnr_font,
         horizontalalignment='center',
         verticalalignment='center',
         transform=axis[1][0].transAxes)



plt.text(0.03, 0.90, 'd)', **tnr_font,
         horizontalalignment='center',
         verticalalignment='center',
         transform=axis[1][1].transAxes)



plt.text(0.03, 0.90, 'e)', **tnr_font,
         horizontalalignment='center',
         verticalalignment='center',
         transform=axis[2][0].transAxes)



plt.text(0.03, 0.90, 'f)', **tnr_font,
         horizontalalignment='center',
         verticalalignment='center',
         transform=axis[2][1].transAxes)



plt.show()
