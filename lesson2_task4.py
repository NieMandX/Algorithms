# Lesson 2 Task 4 -rus-

# Найти сумму n элементов следующего ряда
# чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

def sum_progression(num):
    #   return (1 - (-0.5)**n) / 1.5 (оптимальное решение)

    result = 0
    for i in range(num):
        result += (-0.5) ** i
    return result


num = int(input('Введите количество элементов ряда "1 -0.5 0.25 -0.125 ...": '))
print(f'Сумма первых {num} членов этого ряда = {sum_progression(num)} ')
