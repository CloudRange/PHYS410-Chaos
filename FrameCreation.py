import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import glob
import matplotlib.animation as animation


def plot_flow(min_flow, max_flow):
    temp_df = df[df['Flow rate'] >= min_flow]
    temp_df = temp_df[temp_df['Flow rate'] <= max_flow]

    flow_rates = temp_df['Flow rate'].unique()
    images = []
    j = 0
    flow_rates = np.sort(flow_rates)
    print(np.size(flow_rates))
    for i in flow_rates:
        print(j)
        curr_df = temp_df[temp_df['Flow rate'] == i]
        figure, axis = plt.subplots(1, 2)
        figure.set_size_inches(15, 10.5)
        plt.tight_layout()
        figure.set_size_inches(24, 13)

        x = range(1, len(curr_df['Period']) + 1)
        markers, caps, bars = axis[0].errorbar(x, curr_df['Period'], yerr=curr_df['STD Period'], fmt='.',
                                               ecolor='red')
        [bar.set_alpha(0.1) for bar in bars]
        [cap.set_alpha(0.1) for cap in caps]

        # axis[0].scatter(x, curr_df['Period'], marker='.')
        axis[0].set_title("N vs Period.Flow rate = {:.4f}".format(i))
        axis[0].set_ylabel("Period (s)")
        axis[0].set_xlabel("n")

        markers, caps, bars = axis[1].errorbar(curr_df['Period'], curr_df['Period + 1'], xerr=curr_df['STD Period'],
                                               yerr=curr_df['STD Period'], fmt='.',
                                               ecolor='red')
        [bar.set_alpha(0.1) for bar in bars]
        [cap.set_alpha(0.1) for cap in caps]
        # axis[1].scatter(curr_df['Period'], curr_df['Period + 1'], marker='.')
        axis[1].set_title("Period vs Period + 1.Flow rate = {:.4f}".format(i))
        axis[1].set_yticks([])
        axis[1].set_ylabel("Period + 1 (s)")
        axis[1].set_xlabel("Period (s)")
        images.append(figure.savefig('FiguresTesting/Graph-{}-{}.png'.format(j, i)))
        plt.close(figure)
        j += 1


df = pd.read_csv("dataframe-2Full.csv")

min_flow_rate = 0
df = df[df['Flow rate'] >= min_flow_rate]
print(df)
# plt.style.use('dark_background')

plot_flow(0, 25)
