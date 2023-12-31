import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import glob


df = pd.read_csv("dataframe-2FUll.csv")
#print(df)
# plt.style.use('dark_background')

mins = [3.16, 3.74, 4.77, 4.81, 4.92, 5.36, 5.52, 5.85, 6.45, 7.1, 8.02, 8.2, 11.4, 12.76]
maxes = [3.32, 3.86, 4.81, 4.92, 4.99, 5.40, 5.6, 6.025, 6.7, 7.45, 8.18, 8.55, 11.95, 12.86]


for i in range(len(mins)):
    filtered_df = df[df['Flow rate'] > mins[i]]
    filtered_df = filtered_df[filtered_df['Flow rate'] < maxes[i]]
    m, b = np.polyfit(filtered_df['Flow rate'], filtered_df['Period'], 1)
    figure, axis = plt.subplots(1, 2)

    axis[0].scatter(filtered_df['Flow rate'], filtered_df['Period'], marker='.')
    axis[0].plot(filtered_df['Flow rate'], m*filtered_df['Flow rate'] + b, color='C1')
    axis[0].set_ylabel("Period (s)")
    axis[0].set_xlabel("Flow rate (drops/s)")

    # plt.show()

    periods_normalized = (filtered_df['Period'] - (m*filtered_df['Flow rate'] + b))
    std = np.std(periods_normalized)
    print(std)


    axis[1].scatter(filtered_df['Flow rate'], periods_normalized, marker='.')
    axis[1].scatter(filtered_df['Flow rate'], periods_normalized * 0, marker='.')
    axis[1].set_ylabel("Period - (m (Period) + b) (s)")
    axis[1].set_xlabel("Flow rate (drops/s)")
    plt.show()

