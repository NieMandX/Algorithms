# Lesson1_task7-rus-

t = [float(i) for i in input('Задайте стороны треугольника, 3мя положительными числами разделенных пробелами:').split()]

if t[0] + t[1] > t[2] and t[1] + t[2] > t[0] and t[2] + t[0] > t[1]:
    if t[0] == t[1] == t[2]:
        print('Треугольник - равносторонний')
    elif t[0] == t[1] or t[1] == t[2] or t[2] == t[0]:
        print('Треугольник - равнобедренный')
    else:
        print('Треугольник - разносторонний')
else:
    print('Треугольник не существует')
