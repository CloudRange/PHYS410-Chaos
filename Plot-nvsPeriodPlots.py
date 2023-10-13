import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import glob


df = pd.read_csv("dataframe-2FUll.csv")
#print(df)
# plt.style.use('dark_background')

mins = [3.16, 3.74, 4.77, 4.81, 4.92, 5.36, 5.52, 5.85, 6.45, 7.1, 8.02, 8.2, 11.4, 12.76]
maxes = [3.32, 3.86, 4.81, 4.92, 4.99, 5.40, 5.6, 6.025, 6.7, 7.45, 8.18, 8.55, 11.95, 12.86]


for j in range(len(mins)):


    temp_df = df[df['Flow rate'] > mins[j]]
    temp_df = temp_df[temp_df['Flow rate'] < maxes[j]]

    flow_rates = temp_df['Flow rate'].unique()
    images = []
    j = 0
    flow_rates = np.sort(flow_rates)
    for i in flow_rates:
        print(i)
        figure, axis = plt.subplots(1, 2)
        figure.set_size_inches(18.5, 10.5)
        plt.tight_layout()

        curr_df = temp_df[temp_df['Flow rate'] == i]
        x = range(1, len(curr_df['Period']) + 1)

        axis[0].scatter(x, curr_df['Period'], marker='.')
        axis[0].set_title("N vs Period.Flow rate = {:.4f}".format(i))
        axis[0].set_ylabel("Period (s)")
        axis[0].set_xlabel("n")

        axis[1].scatter(curr_df['Period'], curr_df['Period + 1'], marker='.')
        axis[1].set_title("Period vs Period + 1.Flow rate = {:.4f}".format(i))
        axis[1].set_yticks([])
        axis[1].set_ylabel("Period + 1")
        axis[1].set_xlabel("Period (s)")
        plt.show()
        plt.close(figure)



