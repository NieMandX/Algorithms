# Lesson1_task1-rus-

number = int(input('Введите трехзначное число:'))

rd = (number // 10 ** 0) % 10
md = (number // 10 ** 1) % 10
ld = (number // 10 ** 2) % 10

print(f'Сумма цифр введенного числа = {rd + md +ld}')
print(f'Произведение цифр введенного числа = {rd * md *ld}')
