import numpy as np

from setting import PATH_FILE_STAT
import matplotlib.pyplot as plt


def read_file(filename):
    with open(filename, encoding='UTF-8') as f:
        data = f.readlines()
    return data


my_data = read_file(PATH_FILE_STAT)
total = [int(i.split()[0]) for i in my_data]
timer = [float(i.split()[1]) for i in my_data]
missed = [int(i.split()[2]) for i in my_data]

print(total, missed, timer, sep='\n')

width = 0.4
x_list = list(range(10))
y1_list = total
y2_list = missed
y3_list = timer
x_indexes = np.arange(len(x_list))
# print(type(x_indexes))

plt.figure()
plt.subplot(1, 2, 1)
plt.title('Line graph')
plt.xticks(x_list, [str(i) for i in range(len(y1_list))])
plt.xlabel('levels')
plt.ylabel('stats')

plt.plot(x_list, y1_list, label='Total', marker='o')
plt.plot(x_list, y2_list, label='Missed', marker='^')
plt.plot(x_list, y3_list, label='Timer', marker='1')

plt.subplot(1, 2, 2)
plt.title('Bar graph')
plt.xticks(x_list, [str(i) for i in range(len(y1_list))])
plt.xlabel('levels')
plt.ylabel('stats')

plt.bar(x_indexes - (width / 2), y1_list, label='Total', width=width)
plt.bar(x_indexes + (width / 2), y2_list, label='Missed', width=width)
plt.bar(x_indexes - (width / 2), y3_list, label='Timer', width=width)
plt.legend()
plt.show()

