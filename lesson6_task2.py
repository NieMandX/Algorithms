# Lesson 6 task 2

# lesson 3 task 2

# Во втором массиве сохранить индексы четных элементов
# первого массива. Например, если дан массив со значениями
# 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить
# значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация
# начинается с нуля), т.к. именно в этих позициях
# первого массива стоят четные числа.

from random import randint
from mem_tools import mem_calc

SIZE = 10
MAX_ITEM = 100
MIN_ITEM = 0

array_rand = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
array_index_even = [index for index, item in enumerate(array_rand) if item % 2 == 0]
print(array_rand)
print(array_index_even)


print(f'Total memory used: {mem_calc(locals())} bytes')