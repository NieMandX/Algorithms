# Lesson1_task9-rus-

n = [float(i) for i in input('Введите пожалуйста 3, разделенных пробелами уникальных числа:').split()]

if n[1] < n[0] < n[2] or n[2] < n[0] < n[1]:
    print(f'{n[0]} - серединное число')
elif n[0] < n[1] < n[2] or n[2] < n[1] < n[0]:
    print(f'{n[1]} - серединное число')
else:
    print(f'{n[2]} - серединное число')
