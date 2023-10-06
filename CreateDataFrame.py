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
one = 0
two = 0
three = 0
four = 0
chaos = 0

for i in flow_rates:
    df_temp = pd.DataFrame(columns=['Raw time', 'Period', 'Period + 1', 'Flow rate', 'STD Period'])

    df_temp['Raw time'] = (filtered_df[filtered_df['Flow rate'] == i])['Raw time']
    df_temp['Period'] = (filtered_df[filtered_df['Flow rate'] == i])['Period']
    df_temp['Period + 1'] = (filtered_df[filtered_df['Flow rate'] == i])['Period + 1']
    df_temp['Flow rate'] = (filtered_df[filtered_df['Flow rate'] == i])['Flow rate']

    df_temp['STD Period'] = np.std(df_temp['Period'])

    hist, bins = np.histogram(df_temp['Period'], bins=20)

    # If statements to determine n-periodic
    final_df = pd.concat([final_df, df_temp], ignore_index=True)

    maxes = np.sort(hist)
    maximum_1 = maxes[-1]

    if maximum_1 / len(df_temp['Period']) >= 0.75:
        one += 1
    else:
        maximum_2 = maxes[-2]
        maximum_3 = maxes[-3]
        maximum_4 = maxes[-4]

        indexes = [np.where(hist == maximum_1)[0], np.where(hist == maximum_2)[0],
                   np.where(hist == maximum_3)[0], np.where(hist == maximum_4)[0]]


        if (indexes[0] == indexes[1]):
            indexes[0] = indexes[0][0]
            indexes[1] = indexes[0][1]



        print(indexes)
        if (maximum_1 + maximum_2) / len(df_temp['Period']) >= 0.75:
            index_diff12 = abs(indexes[0] - indexes[1])
            if index_diff12 == 1:
                one += 1
            else:
                two += 1
        elif (maximum_1 + maximum_2 + maximum_3) / len(df_temp['Period']) >= 0.75:
            index_diff_12 = abs(indexes[0] - indexes[1])
            index_diff_13 = abs(indexes[0] - indexes[2])
            index_diff_23 = abs(indexes[1] - indexes[2])

            if (index_diff_12 == 1) and (index_diff_13 == 1) and index_diff_23 == 1:
                one += 1
            elif index_diff_12 == 1 or index_diff_13 == 1 or index_diff_23 == 1:
                two += 1
            else:
                three += 1

        elif (maximum_1 + maximum_2 + maximum_3 + maximum_4) / len(df_temp['Period']) >= 0.75:
            four += 1
        else:
            chaos += 1

print(one)
print(two)
print(three)
print(four)
print(chaos)

# print(final_df)
