# Lesson 6 task 1


# lesson 3 task 4

# Определить, какое число в массиве встречается чаще всего.

from random import randint
from mem_tools import mem_calc
import sys

SIZE = 10000
MAX_ITEM = 30
MIN_ITEM = 1

total_memory_used = 0

array_rand = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]


def max_item(lst):
    maxitem = 0
    count = 0
    array_dict = {key: 0 for key in set(lst)}
    for i in lst:
        array_dict[i] += 1
    for k in array_dict:
#         print (i, '   ',array_dict[i])
        if count <= array_dict[k]:
            count = array_dict[k]
            maxitem = k

    global total_memory_used
    total_memory_used += mem_calc(locals())

    return maxitem
#     print('=========')
#     print(maxitem)

max_freq = max_item(array_rand)

total_memory_used += mem_calc(locals())

print(f'Total memory used: {total_memory_used} bytes')

print(f'Значение {max_freq} встретилось в массиве чаще всего.')



# print (f'Чаще всего встретилось число {maxcounter}')