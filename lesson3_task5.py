# lesson 3 task 5

# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

from random import randint

SIZE = 100
MAX_ITEM = 100
MIN_ITEM = -100

array_rand = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
dict_negative = {negative: index for index, negative in enumerate(array_rand) if negative < 0}

print (array_rand)

maxnegative = dict_negative.popitem()
for _ in range(len(dict_negative)):
    value = dict_negative.popitem()
    if value[0] > maxnegative[0]:
        maxnegative = value

print(f'\nМаксимальный отрицательный эллемент массива: {maxnegative[0]}, с позицией: {maxnegative[1]}')