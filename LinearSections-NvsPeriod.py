import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import glob


df = pd.read_csv("dataframe-2FUll.csv")
#print(df)
# plt.style.use('dark_background')

# plt.style.use('dark_background')

mins = [5.7]
maxes = [5.8]


for i in range(len(mins)):
    filtered_df = df[df['Flow rate'] > mins[i]]
    filtered_df = filtered_df[filtered_df['Flow rate'] < maxes[i]]
    flow_rates = filtered_df['Flow rate'].unique()

    for j in flow_rates:
        figure, axis = plt.subplots(1, 2)
        temp_df = filtered_df[filtered_df['Flow rate'] == j]
        plt.title(j)
        m, b = np.polyfit(range(len(temp_df['Period'])), temp_df['Period'], 1)
        axis[0].scatter(range(len(temp_df['Period'])), temp_df['Period'], marker='.')
        axis[0].plot(range(len(temp_df['Period'])), m * range(len(temp_df['Period'])) + b, color='C1')
        axis[0].set_ylabel("Period (s)")
        axis[0].set_xlabel("n")
        periods_normalized = (temp_df['Period'] - (m * temp_df['Flow rate'] + b))
        std = np.std(periods_normalized)
        print(std)

        axis[1].scatter(range(len(temp_df['Period'])), periods_normalized, marker='.')
        axis[1].scatter(range(len(temp_df['Period'])), periods_normalized * 0, marker='.')
        axis[1].set_ylabel("Period - (m (Period) + b) (s)")
        axis[1].set_xlabel("n")
        plt.show()








    #plt.show()





