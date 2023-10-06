import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import glob

# Data Base creation
# folders = glob.glob("All-Data/*")
folders = glob.glob("Main_data_par/*")
df = pd.DataFrame(columns=['Raw time', 'Period', 'Period + 1', 'Flow rate'])

for i in folders:
    files = glob.glob(i + "/*.csv")
    for j in files:
        dataset = []
        with open(j, 'r') as l:
            for line in l.readlines():
                x = line.replace("\n", "")
                x = line.replace(" ", "")

                dataset.append(int(x))

        dataset = np.asarray(dataset)

        periods = (dataset[1:] - dataset[:-1]) * 1e-6
        periods = np.insert(periods, 0, -1)

        period_second = np.copy(periods[1:])
        period_second = np.append(period_second, -1)

        split = 9

        dataset = np.array_split(dataset, split)
        periods = np.array_split(periods, split)
        period_second = np.array_split(period_second, split)

        for k in range(split):
            df_temp = pd.DataFrame(columns=['Raw time', 'Period', 'Period + 1', 'Flow rate'])
            df_temp['Raw time'] = dataset[k]

            df_temp['Period'] = periods[k]

            df_temp['Period + 1'] = period_second[k]

            overflows_corrector = (df_temp[df_temp['Period'] < -1]).size * (2 ** 32)
            if overflows_corrector <= 0:
                overflows_corrector = 0

            df_temp['Flow rate'] = np.size(dataset[k]) / (
                        ((dataset[k][-1] + overflows_corrector) - dataset[k][0]) * 1e-6)
            df = pd.concat([df, df_temp], ignore_index=True)


# Data filtering

min_sec_limit = -1
filtered_df = df[df['Period'] > min_sec_limit]
filtered_df = filtered_df[filtered_df['Period + 1'] > min_sec_limit]

max_sec_limit = 2
filtered_df = filtered_df[filtered_df['Period + 1'] < max_sec_limit]
filtered_df = filtered_df[filtered_df['Period'] < max_sec_limit]


# Get Std for same flowrates
flow_rates = (filtered_df['Flow rate'].unique()).copy()

final_df = pd.DataFrame(columns=['Raw time', 'Period', 'Period + 1', 'Flow rate', 'STD Period'])
for i in flow_rates:
    df_temp = pd.DataFrame(columns=['Raw time', 'Period', 'Period + 1', 'Flow rate', 'STD Period'])

    df_temp['Raw time'] = (filtered_df[filtered_df['Flow rate'] == i])['Raw time']
    df_temp['Period'] = (filtered_df[filtered_df['Flow rate'] == i])['Period']
    df_temp['Period + 1'] = (filtered_df[filtered_df['Flow rate'] == i])['Period + 1']
    df_temp['Flow rate'] = (filtered_df[filtered_df['Flow rate'] == i])['Flow rate']

    df_temp['STD Period'] = np.std(df_temp['Period'])
    final_df = pd.concat([final_df, df_temp], ignore_index=True)

# Logistic Equation plot Code
#plt.scatter(final_df['Flow rate'], final_df['Period'], marker='.')

markers, caps, bars = plt.errorbar(final_df['Flow rate'], final_df['Period'], yerr=final_df['STD Period'], fmt='.',
                                   ecolor='black')

[bar.set_alpha(0.1) for bar in bars]
[cap.set_alpha(0.1) for cap in caps]
print(final_df)
plt.xlabel("Flow Rate (drops/s)")
plt.ylabel("Period")
plt.tight_layout()
plt.show()


