# lesson 3 task 9

# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from random import randint

ROWS = 10
LINES = 10
MAX_ITEM = 100
MIN_ITEM = 0

matrix_rand = [[randint(MIN_ITEM, MAX_ITEM) for _ in range(ROWS)] for _ in range(LINES)]

for line in matrix_rand:
    print(*line, sep = '\t')
print('-'*80)

for row, _ in enumerate(matrix_rand[0]):
    minvalue = matrix_rand[0][row]
    for line, _ in enumerate(matrix_rand):
        if minvalue > matrix_rand[line][row]:
            minvalue = matrix_rand[line][row]
    if row == 0:
        maxvalue = minvalue
    elif maxvalue < minvalue:
        maxvalue = minvalue

    print(minvalue,'\t', end = '')
print()
print('-'*80)
print(f'Mаксимальный элемент среди минимальных элементов столбцов матрицы = {maxvalue}')