from DataParser import *
import sys
import csv
import matplotlib.pyplot as plt

index = int(sys.argv[1])

dp = DataParser('dataframe.csv')
t = dp.get_trip(index)
time_vals = t.timestamps
acc_x = t.acc_xs

print('trip: ' + t.trip_id)
print('group id: ' + t.group_id)

color_gps = 'tab:red'
color_acc = 'tab:blue'

fig, ax1 = plt.subplots()
plt.xlabel('Time (s)')
plt.ylabel('Acceleration')
ax1.plot(time_vals, acc_x, color=color_acc)
ax1.tick_params(axis='y', labelcolor=color_acc)
plt.show()
