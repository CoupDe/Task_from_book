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

word = 'объектно-ориентированный'

print(word.split('-')[0][:6], word.split('-')[0][0:8], word.split('-')[1][5:8], word[4] + word[7] + word[5])
