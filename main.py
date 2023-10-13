import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#15,16 is periodic
#18,19,21,22,24, 26, 27, 30 perfectish
#23 start of bifurcation
#25 bifurcation
#29 weird split
#31 chaos

#NEW START 170


#Allan deviation
# double period 28
#Arro 19
#35 really cool
#40 diode
file = "Main_data_par/29-09-23/55_run.csv"
dataset = []
with open(file, 'r') as l:
    for line in l.readlines():
        x = line.replace("\n","")
        x = line.replace(" ","")

        dataset.append(int(x))
dataset = np.asarray(dataset)
periods = [-1]
for x in range(1, dataset.size):
    period = dataset[x] - dataset[x - 1]
    periods.append(period)
periods2 = dataset[1:] - dataset[:-1]
periods2 = np.insert(periods2, 0, -1)

# print(periods == periods2)

df = pd.DataFrame()
df = df.assign(Output=dataset)
df = df.assign(Period=periods)

print(df)
print(df["Output"].size/((df["Output"][df["Output"].size - 1] - df["Output"][0])*1e-6))
#microseconds
plotable_data = []

min_sec_limit = -1
filtered_df = df[df['Period'] > min_sec_limit]
filtered_df = filtered_df[filtered_df['Period + 1'] > min_sec_limit]

max_sec_limit = 2
filtered_df = filtered_df[filtered_df['Period + 1'] < max_sec_limit]
filtered_df = filtered_df[filtered_df['Period'] < max_sec_limit]


plotable_data = np.asarray(plotable_data)
plotable_data = plotable_data*1e-6
plt.scatter(range(plotable_data.size), plotable_data, marker='.')
plt.xlabel("n")
plt.ylabel("$T_n$")
plt.show()


tn = []
tn1 = []
for i in range(plotable_data.size - 1):
    tn.append(plotable_data[i])
    tn1.append(plotable_data[i + 1])

plt.scatter(tn, tn1,  marker='.')
plt.xlabel("$T_n$")
plt.ylabel("$T_{n+1}$")
plt.show()
