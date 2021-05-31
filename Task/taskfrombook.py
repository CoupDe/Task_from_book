# https://www.yuripetrov.ru/edu/python/ch_03_02.html#id4 № 3.2.2
# val = list(input('Insert x, y, z:').split())
# x, y, z = int(val[0]), int(val[1]), int(val[2])
# formula = (x ** 5 + 7 / abs(-6) * y) ** (1 / 3) / 7 - z % y
# print(round(formula, 3))
# -------------------------------------------------------------------------------------------------------
# https://www.yuripetrov.ru/edu/python/ch_03_02.html#id4 № 3.2.3
# Дана электрическая цепь, состоящая из 2-х последовательно
# соединенных проводников (сопротивление каждого известно).
# Найти общее сопротивление цепи (округление результата необходимо выполнить до 1-го знака после запятой).
# val = list(input('Insert x, y:').split())
# x, y = float(val[0]), float(val[1])
# result = x + y
# print(round(result, 1))

# --------------------------------------------------------------------------------------------------------
# https://www.yuripetrov.ru/edu/python/ch_03_02.html#id4 № 3.2.3
# № 3.2.4
# Дано двузначное и трехзначное число. Для каждого выведите на экран сумму и произведение цифр.
# val = list(input('Insert x, y:').split())
# x, y = val[0], val[1]
#
#
# def summ(z):
#     cc = 1
#     zz = 0
#     s = [int(i) for i in list(z)]
#     for z in s:
#         zz += z
#         cc *= z
#     return zz, cc
#
#
# print('Sum: x ', summ(val[0]), 'Sum: y ', summ(val[1]))

# num = int(input('Enter the num:'))
# multnum = num
# sum = 0
# while num != 0:
#     sum = sum + num % 10
#     num = num // 10
#
# mult = 1
# while multnum != 0:
#     mult = mult * (multnum % 10)
#     multnum = multnum // 10
#
# print('Sum = ', sum, mult)
# ------------------------------------------------------------------------------------------------------
# № 3.2.5
#
# С начала суток прошло m минут (0<m≤24∗60). Определите:
#
# целое количество часов, прошедших с начала суток;
#
# количество минут, прошедших с момента начала последнего часа.
#
# minute = int(input('Enter the minute'))
# print(17 % 12)
# NO RESULT TASK
# ------------------------------------------------------------------------------------------------------
# Дано уравнение ax + b = 0 и отрезок [m;n]. Ответьте на вопрос, попадает ли решение уравнения в указанный отрезок.
#
# Решение (начало и общий ход мыслей):
#
# Аналитическое решение.
#
# Коэффициенты уравнения и величина отрезка - произвольны, возьмем целые числа. Решение x при этом может быть дробным. После определения x составим логическое выражение попадания в отрезок, что и будет ответом.

# coef = list(map(int, input('Enter a, b:').split()))
# a, b = coef[0], coef[1]
# sect = list(map(int, input('Enter section m, n:').split()))
# m, n = sect[0], sect[1]
# x = -b/a
# print('Корень = ', x)
# z = max(m, n) >= x >= min(m,n)
# print(z)
# № 3.2.7
#
# Составьте программу, которая запрашивает название футбольной команды и повторяет его на экране со словами

# word = input('Input Football Team:')
#
# print(word + ' CHAMPION!!!')
# print(word.lower() + ' CHAMPION!!!')
# print('Len team:' + str(len(word)))
# print('s' in word.lower())
# print(word.lower().count('s'))

# Составьте программу, которая запрашивает название государства и его столицы, а затем выводит сообщение:

# country = input('Enter country: ')
# capital = input('Enter capital: ')
# print('The state {0}, the capital of {{1}' .format(country, capital))


# Дано слово объектно-ориентированный. Используя индексацию и срезы составьте из него слова объект, ориентир, тир, кот, рента и выведите их на экран.

# word = 'объектно-ориентированный'
#
# print(word.split('-')[0][:6], word.split('-')[0][0:8], word.split('-')[1][5:8], word[4] + word[7] + word[5])


# Программирование на языке высокого уровня (Python).
# https://www.yuripetrov.ru/edu/python
# Задание task_03_02_10.
#
# Выполнил: Фамилия И.О.
# Группа: !!!
# E-mail: !!!


# Создать 2 пустых списка
a = []
b = []

# Добавить 2 вещественных числа (4.5 и 3.4) в список 'a' с помощью append
a.append(4.5)
a.append(3.4)
        # Добавить 2 вещественных числа (8.7, 1.3) в список 'a' с помощью extend
a.extend([8.7, 1.3])


            # Добавить 2 вещественных числа (14.5, 3.4) в список 'b' с помощью append
            # Удалите комментарий и допишите код
b.append(14.5)
b.append(3.4)
            # Добавить 2 вещественных числа (8.7, 11.3) в список 'b'с помощью extend
            # Удалите комментарий и допишите код
b.extend([8.7, 11.3])
            # Вставить целое число 100 на 2-е и 4-е место списка 'a'
a.insert(1, 100)
a.insert(3, 100)

                    # Вставить целое число 200 на 1-е и 3-е место списка 'b'
                    # Удалите комментарий и допишите код
b.insert(0,200)
b.insert(2,200)
                    # Вывести списки на экран

print(a)
print(b)

# Удалить первые элементы из списков 'a' и 'b'
del a[0]
del b[0]

# Удалить элемент 100 из списка 'a'
a.remove(100)
    # Удалить элемент 200 из списка 'b'
    # Удалите комментарий и допишите код
b.remove(200)
    # Вывести списки на экран
print("\nПосле удалений:", a, b)
# Удалите комментарий и допишите код

# Создать множества из списков 'a' и 'b', а также их пересечение
sa = set(a)
sb = set(b)# Удалите комментарий и допишите код
sa_and_sb = sa & sb # Удалите комментарий и допишите код

# Вывести экран уникальные элементы каждого списка и общие
print("\nУникальные элементы:", sa, sb)
# Удалите комментарий и допишите код
print("общие:", sa_and_sb)

# Соединить списки 'a' и 'b'
c = a + b  # Удалите комментарий и допишите код

# Отсортировать список 'c' по возрастанию и убыванию
c_asc = sorted(c) # Удалите комментарий и допишите код
c_desc = sorted(c, reverse=True)# Удалите комментарий и допишите код

# Среднее арифметическое элементов списка 'c', расположенных на четных местах
sr_ar = sum(c[1::2])/len(c[::2])
# Среднее геометрическое элементов списка 'c', расположенных на нечетных местах
geom = 1
rnd = [geom * i for i in c[::2]]

for i in c[::2]:
    geom *= i

sr_geom = round(geom ** (1/(len(c[::2]))),2)


# Максимальный и минимальный элементы
c_max = max(c)
c_min = min(c)

# Вывести результаты на экран
print("\nИтоговые:", c)
print("3-й:", sr_geom, sr_ar )
# Удалите комментарий и допишите код


# --------------
# Пример вывода:
#
# Исходные списки:
# 1-й: [4.5, 100, 3.4, 100, 8.7, 1.3]
# 2-й: [200, 14.5, 200, 3.4, 8.7, 11.3]
#
# После удалений:
# 1-й: [3.4, 100, 8.7, 1.3]
# 2-й: [14.5, 3.4, 8.7, 11.3]
#
# Уникальные элементы:
# 1-й: {8.7, 1.3, 3.4, 100}
# 2-й: {8.7, 11.3, 3.4, 14.5}
# общие: {8.7, 3.4}
#
# Итоговые:
# 3-й: [3.4, 100, 8.7, 1.3, 14.5, 3.4, 8.7, 11.3]
# Сортировка (возр.): [1.3, 3.4, 3.4, 8.7, 8.7, 11.3, 14.5, 100]
# Сортировка (убыв.): [100, 14.5, 11.3, 8.7, 8.7, 3.4, 3.4, 1.3]
# Ср. арифм. = 29.00, ср. геометр. = 7.82
# Макс. и мин.: 100 1.3
