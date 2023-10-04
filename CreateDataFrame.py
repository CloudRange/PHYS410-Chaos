import numpy as np
import pandas as pd
import glob

folders = glob.glob("All-Data/*")
df = pd.DataFrame(columns=['Raw time', 'Period', 'Period + 1', 'Flow rate'])

# Folder Iteration
for i in folders:
    files = glob.glob(i + "/*.csv")
    # File iteration
    for j in files:
        # File reader
        dataset = []
        with open(j, 'r') as l:
            for line in l.readlines():
                x = line.replace("\n", "")
                x = line.replace(" ", "")

                dataset.append(int(x))

        # Data Calculation
        dataset = np.asarray(dataset)
        periods = (dataset[1:] - dataset[:-1]) * 1e-6
        periods = np.insert(periods, 0, -1)

        period_second = np.copy(periods[1:])
        period_second = np.append(period_second, -1)

        # Array Splitting

        split = 9

        dataset = np.array_split(dataset, split)
        periods = np.array_split(periods, split)
        period_second = np.array_split(period_second, split)

        # Split iteration
        for k in range(split):
            # Create temp dataframe
            df_temp = pd.DataFrame(columns=['Raw time', 'Period', 'Period + 1', 'Flow rate'])
            df_temp['Raw time'] = dataset[k]

            df_temp['Period'] = periods[k]

            df_temp['Period + 1'] = period_second[k]

            # This counts how many negative periods we have to detect how many overflows of the internal clock happened
            # during the data collection process, in order to determine how long has the data collection progress
            overflows_corrector = (df_temp[df_temp['Period'] < -1]).size * (2 ** 32)
            if overflows_corrector <= 0:
                overflows_corrector = 0

            # n/(time_{max} - time_{min})
            df_temp['Flow rate'] = np.size(dataset[k]) / (
                    ((dataset[k][-1] + overflows_corrector) - dataset[k][0]) * 1e-6)

            # Atatch temp dataframe to dataframe
            df = df.append(df_temp, ignore_index=True)

# Data filtering

min_sec_limit = -1
filtered_df = df[df['Period'] > min_sec_limit]
filtered_df = filtered_df[filtered_df['Period + 1'] > min_sec_limit]

max_sec_limit = 2
filtered_df = filtered_df[filtered_df['Period + 1'] < max_sec_limit]
filtered_df = filtered_df[filtered_df['Period'] < max_sec_limit]
