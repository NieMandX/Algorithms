# Lesson1_task5-rus-

letters = [ord(i) for i in input('Введите, отделив пробелом, 2 строчные буквы английского алфавита:').split()]
print(f'Порядковые номера введеных букв соответственно: {letters[0] - ord("a") + 1} и {letters[1] - ord("a") + 1}')
if letters[0]-letters[1]:
    print(f'Колличество букв между ними = {abs(letters[0] - letters[1]) - 1}')
else:
    print(f'Колличество букв между ними = 0')
