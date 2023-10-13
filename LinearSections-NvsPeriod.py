import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import glob


df = pd.read_csv("dataframe-2FUll.csv")
#print(df)
# plt.style.use('dark_background')

mins = [3.81, 5.52, 5.85, 6.45, 7.1, 8.02, 8.2, 11.4, 12.76]
maxes = [3.85, 5.6, 6.025, 6.7, 7.45, 8.18, 8.55, 11.95, 12.86]


for j in range(len(mins)):


    temp_df = df[df['Flow rate'] > mins[j]]
    temp_df = temp_df[temp_df['Flow rate'] < maxes[j]]

    flow_rates = temp_df['Flow rate'].unique()
    images = []
    j = 0
    flow_rates = np.sort(flow_rates)
    for i in flow_rates:
        print("start")
        print(i)
        plt.tight_layout()

        curr_df = temp_df[temp_df['Flow rate'] == i]
        x = range(1, len(curr_df['Period']) + 1)

        m, b = np.polyfit(x, curr_df['Period'], 1)
        periods_normalized = (curr_df['Period'] - (m * curr_df['Flow rate'] + b))
        std = np.std(periods_normalized)
        print(std)
        plt.scatter(x, curr_df['Period'], marker='.')
        plt.plot(x, x * m + b)
        plt.show()
        plt.scatter(x, periods_normalized, marker='.')
        plt.show()

        plt.scatter(periods_normalized[:-1], periods_normalized[1:], marker='.')
        plt.show()



