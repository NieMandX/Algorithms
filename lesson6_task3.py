# Lesson 6 task 3

# lesson 3 task 3

# В массиве случайных целых чисел поменять
# местами минимальный и максимальный элементы.

from random import randint
from mem_tools import mem_calc

SIZE = 10
MAX_ITEM = 100
MIN_ITEM = 0

array_rand = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
minval = maxval = array_rand[0]
posmax = posmin = 0

for pos, i in enumerate(array_rand[1::], 1):
    if i > maxval:
        maxval = i
        posmax = pos
    if i < minval:
        minval = i
        posmin = pos

print(array_rand)
print(maxval, minval)
array_rand[posmax], array_rand[posmin] = array_rand[posmin], array_rand[posmax]
print(array_rand)

print(f'Total memory used: {mem_calc(locals())} bytes')
