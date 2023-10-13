import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def get_data(file):
    dataset = []
    with open(file, 'r') as l:
        for line in l.readlines():
            x = line.replace("\n", "")
            x = line.replace(" ", "")

            dataset.append(int(x))
    dataset = np.asarray(dataset)
    periods = [-1]
    for x in range(1, dataset.size):
        period = dataset[x] - dataset[x - 1]
        periods.append(period)
    periods2 = dataset[1:] - dataset[:-1]
    periods2 = np.insert(periods2, 0, -1)


    df = pd.DataFrame()
    df = df.assign(Output=dataset)
    df = df.assign(Period=periods)

    overflows_corrector = (df[df['Period'] < -1]).size * (2 ** 32)
    if overflows_corrector <= 0:
        overflows_corrector = 0

    flow_rate = np.size(dataset) / (
            ((dataset[-1] + overflows_corrector) - dataset[0]) * 1e-6)

    # microseconds
    plotable_data = []

    for i in periods:
        if (i > 0):
            plotable_data.append(i* 1e-6)

    tn = []
    tn1 = []
    for i in range(len(plotable_data) - 1):
        tn.append(plotable_data[i])
        tn1.append(plotable_data[i + 1])

    return [range(len(plotable_data)),plotable_data, tn, tn1, flow_rate]

# test
file = "Main_data_par/29-09-23/25_run.csv"
# file = "Main_data_par/Main_data/148_run.csv"
test = get_data(file)

figure, axis = plt.subplots(2, 2)


axis[0, 0].scatter(test[0], test[1], marker='.')
axis[0, 0].set_title("N vs Period.Flow rate = {:.4f}".format(test[4]))
axis[0, 0].set_ylabel("Period (s)")


axis[0, 1].scatter(test[2], test[3], marker='.')
axis[0, 1].set_title("Period vs Period + 1.Flow rate = {:.4f}".format(test[4]))
axis[0, 1].set_yticks([])
axis[0, 1].set_ylabel("Period + 1")



file = "Main_data_par/29-09-23/40_run.csv"
test = get_data(file)


axis[1, 0].scatter(test[0], test[1], marker='.')
axis[1, 0].set_title("N vs Period.Flow rate = {:.4f}".format(test[4]))
axis[1, 0].set_xlabel("Drop number (n)")

axis[1, 1].scatter(test[2], test[3], marker='.')
axis[1, 1].set_title("Period vs Period + 1.Flow rate = {:.4f}".format(test[4]))
axis[1, 1].set_yticks([])
axis[1, 1].set_xlabel("Period")
axis[1, 1].set_ylabel("Period + 1")

plt.tight_layout()
plt.show()