# Lesson1_task8-rus-

year = int(input('Введите год для проверки на високосность (целое число больше 1582):'))

if year % 400:
    if year % 100 == 0:
        print('Год не високосный')
    elif year % 4:
        print('Год не високосный')
    else:
        print('Год високосный')

else:
    print('Год високосный')
