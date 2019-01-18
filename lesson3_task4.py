# lesson 3 task 4

# Определить, какое число в массиве встречается чаще всего.

from random import randint

SIZE = 100
MAX_ITEM = 100
MIN_ITEM = 0

array_rand = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
array_dict = {key: 1 for key in set(array_rand)}

maxcounter = 0
maxval = 0

while len(array_rand):
    item = array_rand.pop()
    for index, val in enumerate(array_rand):
        if val != None and val == item:
            array_dict[val] += 1
            array_rand[index] = None


for i in array_dict:
    if array_dict[i] > maxval:
        maxval = array_dict[i]
        maxcounter = i
    
print (f'Чаще всего встретилось число {maxcounter}')
