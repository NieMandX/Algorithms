# Lesson 2 Task 9 -rus-

# Среди натуральных чисел, которые были введены,
# найти наибольшее по сумме цифр. Вывести на экран
# это число и сумму его цифр.

def digits_sum(number):
    if number == 0:  # Очень хотелось написать 'if not number:', но бью себя по рукам ;)
        return number
    else:
        return (number % 10) + digits_sum(number // 10)


max_num = 0
max_sum = 0
number = 0

print(f'+{"":-^78}+')
print(f'|{"Введите несколько натуральных чисел, подтверждая ввод нажатием Enter.":^78}|')
print(f'|{"(Для завершения работы программы, нажмите Enter в пустой строке.) ":^78}|')
print(f'+{"":-^78}+')

while number != '':
    if digits_sum(int(number)) > max_sum:
        max_sum = digits_sum(int(number))
        max_num = number
    number = input('Введите число:')

print(f'+{"":-^78}+')
print(f'Число с максимальной суммой цифр - {max_num}, cумма его цифр = {max_sum}')
