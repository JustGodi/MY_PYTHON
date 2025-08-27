# 146 Цикл for. Циклы предназначены для многократного выполнения одной и той же операции например для перебора элементов итерируемых объектов. К таким объектам относятся строки, кортежи, списки, множества и словари
'''
lst = list(range(1,6))

for num in lst:
    print(num)
    print(num ** 2)
'''

    # 147 накопление результата в цикле. Чтобы найти сумму всех элементов, необходимо их складывать в каждой итерации цикла, а результат записать в отедльную переменную
'''
lst = list(range(1, 6))
res = 0
for num in lst:
    res += num
print(res)
#или просто:
print(sum(lst))
'''
'''
lst = list('12345')
res = ''

for let in lst:
    res += let
print(res, type(res))
'''
'''
lst = list(range(1, 6))
res = 0

for num in lst:
    res += num ** 2
print(res)
'''
'''
lst = list(range(1, 6))
txt = ''

for num in lst:
    txt += str(num)
print(txt, type(txt))
'''

    # 148 циклы for и условие if
'''
lst = list(range(1, 6))

for num in lst:
    if num % 2 == 0:
        print(num)
'''
'''
st = {-2, 1, 3, -5, 4, -8}

for num in st:
    if num > 0:
        print(num)
'''
'''
lst_1 = [7, 1, 2, 5, 3, 9]
lst_2 = []

for num in lst_1:
    if 2 < num < 5:
        lst_2.append(num)
print(lst_2)
'''
'''
lst = list(range(1, 8))
res = 0

for num in lst:
    if num % 2 == 0:
        res += num
print(res)
'''
'''
num_1 = 1234567
lst_1 = []
txt_1 = str(num_1)

for let in txt_1:
    if int(let) % 2 == 1:
        lst_1.append(int(let))
print(lst_1)
'''

    # 149 инструкция break позволяет прервать выполнение цикла
#выведем из него все элементы до числа 3, на котором прервется выполнение цикла
'''
lst = list(range(1, 6))

for num in lst:
    print(num)
    if num == 3:
        break
'''
#Инструкция break может завершать любые циклы: for, while.
'''
st = {1, 3, 6, 7, -9, 12}

for num in st:
    print(num)
    if num < 0:
        break
'''
'''
lst = [7, 1, 2, 5, 0, 3, 9]
res = 0

for num in lst:
    if num == 0:
        break
    res += num
print(res)
'''
'''
num_1 = 897654
txt_1 = str(num_1)
lst_1 = []

for let in txt_1:
    if let == '6':
        break
    lst_1.append(int(let))
print(lst_1)
'''

    # 150 инструкция continue, в отличие от break, позволяет запускать новую итерацию цикла.
#Давайте выведем из него все элементы кроме числа 3. Для этого под блоком с условием прописываем инструкцию continue. При этом функцию print укажем в первом блоке цикла:
'''
lst = list(range(1, 6))

for num in lst:
    if num == 3:
        continue
    print(num)
'''
'''
st = {'a', 'b', 'c', 'd', 'e'}

for let in st:
    if let == 'd':
        continue
    print(let)
'''
'''
lst = [6, 3, -2, 8, -4, 9]

for num in lst:
    if num < 0:
        continue
    print(num)
'''
'''
lst = list('abcde')
txt_1 =''

for let in lst:
    if let == 'b':
        continue
    txt_1 += let
print(txt_1)
'''

    # 151 получение элементов и их индексов. Из итерируемого объекта можно вывести не только элементы, но и их индексы. Для этого применяется функция enumerate. В ее параметре указываем нужный итерируемый объект.
'''
lst = list('abc')

for item in  enumerate(lst):
    print(item, type(item))
'''
'''
lst = list('abc')

#for item in enumerate(lst):
#    key, value = item
#    print(key, value)
#    print()
#сокращённая форма кода сверху

for key, value in enumerate(lst):
    print(key, value)
    print()
'''
'''
# Выведите в консоль значения элементов и их индексы до первого отрицательного числа.
lst = [8, 6, -4, 2, -1]

for key, value in enumerate(lst):
    if value < 0:
        break
    print(key, value)
'''
'''
#Выведите в консоль значения элементов и их индексы:
lst = list('abcde')

for key, value in enumerate(lst):
    print(f"'{value}" + f"{str(key)}'")
'''
'''
#Элементы, стоящие на четных позициях возведите в квадрат, а нечетных - в куб.
lst = list(range(1, 6))

for key, value in enumerate(lst):
    if key % 2 == 0:
        value = value ** 2
    else:
        value = value ** 3
    print(key, value)
'''

    # 152 Ключи словаря через for, При переборе словаря циклом for по умолчанию всегда выводятся его ключи.

'''
dct = dict(a = 1, b = 2, c = 3)

for key in dct:
    print(key)
'''
'''
#Получить ключи словаря можно и с помощью метода keys. Метод возвращает специальный объект, который можно перебрать циклом:
dct = dict(a = 1, b = 2, c = 3)

for key in dct.keys():
    print(key)
'''
'''
dct = dict(a = 1, b = 2, c = 3, d = 4, e = 5)

for key in dct.keys():
    print(f"'{key}'")
'''
'''
#Выведите в консоль его ключи, кроме 8.
dct = {
    2: 'a',
    4: 'b',
    6: 'c',
    8: 'd'
}

for key in dct.keys():
    if key == 8:
        continue
    print(key)
'''
'''
dct = {
    '1': 'a',
    '2': 'b',
    '3': 'c',
    '4': 'd'
}
txt = ''

for key in dct.keys():
    if key == '1':
        continue
    txt += key
tpl = tuple(txt)
print(tpl)
'''

    # 153 Значения словаря через for, Для получения значений словаря, можно обратиться к ним по ключу.
'''
dct = dict(a = 1, b = 2, c = 3)

for key in dct:
    print(dct[key])
'''

#Вывести значения словаря можно и с помощью метода values. Он возвращает специальный объект, который перебирается циклом:
'''
dct = dict(a = 1, b = 2, c = 3)

for val in dct.values():
    print(val)
'''
'''
dct = dict(a = 1, b = 2, c = 3, d = 4, e = 5)

for val in dct.values():
    print(val)
'''
'''
dct = dict(a = 1, b = 2, c = 3, d = 4, e = 5)
res = 0

for val in dct.values():
    res += val
print(res)
'''
'''
dct = {
    '1': 'a',
    '2': 'b',
    '3': 'c',
    '4': 'd'
}
txt = ''

for val in dct.values():
    txt += val
print(txt)
'''

# 154 Пара ключ-значение словаря через for
'''
dct = dict(a = 1, b = 2, c = 3)

for key in dct:
    print(key, dct[key])
'''
'''
dct = dict(a = 1, b = 2, c = 3)

for coup in dct.items():
    print(coup, type(coup))
'''
'''
dct = dict(a = 1, b = 2, c = 3, d = 4, e = 5)

for key in dct:
    print(key, dct[key])
'''
'''
dct = {
    1: 'Январь',
    2: 'Февраль',
    3: 'Март',
    4: 'Апрель',
    5: 'Май',
    6: 'Июнь',
    7: 'Июль',
    8: 'Август',
    9: 'Сентябрь',
    10: 'Октябрь',
    11: 'Ноябрь',
    12: 'Декабрь',
}

for key in dct:
    print(str(key) + ' это ' + dct[key])
'''

    # 155 Пары индекс-элемент словаря, Чтобы получить индексы и элементы словаря в виде кортежа, следует использовать функцию enumerate.
'''
dct = dict(a = 1, b = 2, c = 3)

for item in enumerate(dct):
    print(item, type(item))
'''
#Можно распаковать кортеж на две переменные:
'''
dct = dict(a = 1, b = 2, c = 3)

for key, index in enumerate(dct):
    print(key, index, type(key), type(index))
'''
'''
dct = dict(a = 1, b = 2, c = 3, d = 4, e = 5)

for item in enumerate(dct):
    print(item)
'''
'''
dct = {
    '1': 11,
    '2': 12,
    '3': 13,
    '4': 14
}

print(dct)
for index, key in enumerate(dct):
    print(index, key)
'''

    # 156 Генерация чисел через for, Для последовательного вывода чисел из заданного диапазона следует использовать функцию range в цикле for.
'''
for num in range(1, 10):
    print(num)
'''
'''
for num in range(20, 9, -1):
    print(num)
'''
'''
res = 0

for num in range(1, 101):
    res += num
print(res)
'''

    # 157 Генерация чисел с шагом через for, тобы вывести числа через определенный шаг, в функцию range нужно передать третий параметр.
'''
for num in range(1, 10, 2):
    print(num)
'''

#Если задать шаг с отрицательным числом, то числа будут выводится в обратном порядке.
'''
for num in range(1, 101):
    print(num)
'''
'''
for num in range(-10, 10):
    print(num)
'''
'''
for num in range(2, 21, 3):
    print(num)
'''

    # 158 Одновременный перебор последовательностей, Чтобы перебрать сразу несколько последовательностей, можно применить функцию zip. При этом все элементы последовательностей будут выводиться в виде кортежей, состоящего из элементов с одинаковым индексом.
'''
lst_1 = ['a', 'b', 'c']
lst_2 = [1, 2, 3]

for el in zip(lst_1, lst_2):
    print(el)
'''
'''
st = {'a', 'b', 'c'}
tpl = (1, 2, 3)

for el in zip(st, tpl):
    print(el)
'''

#если длина одной последовательности больше другой то перебор будет выполняться по меньшей
'''
lst_1 = list('abcde')
lst_2 = [1, 2, 3, 4]

for el in zip(lst_1, lst_2):
    print(el)
'''
#с помощью функции zip можно перебрать и три последовательности
'''
lst_1 = list('abcde')
lst_2 = list(range(1, 6))
lst_3 = list('FGHIJ')

for el in zip(lst_1, lst_2, lst_3):
    print(el)
'''
'''
lst_1 = [1, 2, 3]
lst_2 = [4, 5, 6]

for el in zip(lst_1, lst_2):
    print(el)
'''
'''
lst_1 = list('abc')
lst_2 = list('def')
lst_3 = []
n = 0
m = 1

for el in zip(lst_1, lst_2):
    lst_3.append(el[n])
    lst_3.append(el[m])
print(lst_3)
'''
'''
#Даны три списка. Сложите соответствующие элементы этих списков и результат запишите в новый список. Суммирование будет идти по следующему принципу: 11 + 21 + 31, 12 + 22 + 32, 13 + 23 + 33, 14 + 24 + 34,
lst_1 = list(range(11, 15))
lst_2 = list(range(21, 25))
lst_3 = list(range(31, 35))
res = 0
n = 0
m = 0
lst_sum = []

for el in zip(lst_1, lst_2, lst_3):
    for num in el:
        if n > 2:
            lst_sum.append(res)
#            print(lst_sum)
            n = 0
            res = 0
        res += num
#        print(res)
        n += 1
lst_sum.append(res)
print(lst_sum)
#очень понравилась задачка
'''

    # 159 цикл while, особенностью цикла while явдяется то что он будет выполнен до тех пор пока верно выражение переданное ему, синтаксис:
'''
while expression is true:
		code that executes until
		the condition becomes false
'''
    # В словии цикла while необходимо использовать динамически меняющиеся значения, например счетчик иначе может происходить бесконечный вывод значений в консоль. выполнение цикла пока счетчик будет меньше 5
'''
i = 0
n = 0

while i < 5:
    i += 1
    print(i)

while n < 5:
    print(n)
    n += 1
#первый цикл начинает отсчёт с 1 и заканчивает на 5, хотя условие меньше 5, а второй выполнаяется логично
'''
'''
i = 0

while i < 11:
    print(i)
    i += 1
'''
'''
i = 100

while i > 0:
    print(i)
    i -= 1
'''
'''
i = -1

while i > -101:
    print(i)
    i -= 1
'''

    # 160 цикл while без счетчика, в цикле while можно выполнять операции до тех пор пока они истинны
'''
num = 10.5

while num > 1:
    num = num / 2

print(num)
'''
'''
num = 100

while num > 20:
    num = num / 3

print(num)
'''
'''
num = 1

while num < 20:
    num = num * 2.5
    print(num)

print(num)
'''

    # 161 условие if в цикле while, в цикле while можно также использовать условие if и break. Давайте будем делить 10.5 на 2 пока результат не станет меньше единицы
'''
num = 10.5

while True:
    num = num / 2
    print(num)

    if num < 2:
        break

print(num)
'''
'''
num = 100000

while True:
    print(num)
    num = num / 2

    if num < 10:
        break

print(num)
'''
'''
#Дано целое число. Получите список делителей этого числа.
from functools import lru_cache
import timeit
import time

#n = 10
#n = int(input('Введите цесло число: '))
lst = []


#@lru_cache(maxsize = 1)
def delet(n):
    while True:
        for i in range(1, n+1):
            if n % i == 0:
                lst.append(i)
                print(i)

        if i == n:
            break

start_time = time.perf_counter()
delet(int(input('Введите цесло число: ')))
print('Список делителей: ', lst)
end_time = time.perf_counter()
total_time = end_time - start_time
print(total_time)
#поигрался с лру кеш и таймером. код без @lru_cache поему то выполняется быстрее, почему? я расстроен
#задачка понравилась очень и до функции
'''

    # 162 работа с флагами. Флаг - это специальная переменная, которая может принимать только два значения: True или False. С помощью флагов можно решать задачи, проверяющие отсутствие чего-либо: к примеру, можно проверить, что в списке нет элемента с определенным значением.
    # Давайте решим следующую задачу: дан список с числами, нужно проверить, все ли элементы в нем являются положительными. Для этого зададим специальную переменную flag, которая до начала цикла будет истинна. А при попадании в цикл отрицательного числа, поменяем ей значение на False. Для того, чтобы узнать результат проверки, выведем переменную flag после цикла в консоль:
'''
lst = list(range(1, 6))
flag = True

for el in lst:
    if el < 0:
        flag = False

print(flag)
'''
#Хорошей практикой является назначение для переменной с флагом имени, отражающего заданное условие. Давайте переименуем flag в isAllPositive. И для наглядности изменим одно число из списка на отрицательное:
'''
lst = [1, 2, 3, -4, 5]
is_all_positive = True

for el in lst:

    if el < 0:
        is_all_positive = False

print(is_all_positive)
'''
#Если в перебираемом списке много значений и нужно остановить цикл после обнаружения первого отрицательного числа, то следует применить инструкцию break:
'''
lst = [1, 2, 3, -4, 5]
is_all_positive = True

for el in lst:

    if el < 0:
        is_all_positive = False
        print(el)
        print(lst.index(el))
        break

print(is_all_positive)
'''
#При работе с флагами, чтобы узнать результат выполнения цикла, можно вывести не значение флага, а произвольное сообщение с помощью дополнительного if. Давайте перепишем предыдущий пример. Если все элементы положительные, то пусть выведется '+++', если нет - '---':
'''
lst = [1, 2, 3, -4, 5]
is_all_positive = True

for el in lst:

    if el < 0:
        is_all_positive = False
        break

if is_all_positive:
    print('+')
else:
    print('-')
'''
#Дано целое число. Проверьте, является ли оно простым, то есть делится только на единицу и на само себя.
'''
#lst = [1, 2, 3, 4, 5]
lst = list(range(1, 51))
lst_not_simple = []
lst_simple = []
is_all_simple = True

for el in lst:
    
    if el % 1 == 0  and el % el == 0 and el % 2 == 0 and el != 1 and el != 2:
        is_all_simple = False
        lst_not_simple.append(el)
#        print('Индекс непростого числа:', lst.index(el), 'Не простое:', el, is_all_simple)
        continue
    else:
        is_all_simple = True
        lst_simple.append(el)
#        print('Простое:', el, is_all_simple)
#понравилось, закоментировал старый код вместо него добавил два списка в которые добавляются все числа
print('Список простых чисел:', lst_simple)
print('Список непростых чисел:', lst_not_simple)
'''
    # 163 Перехват выхода из цикла. Чтобы сократить код при работе с флагами, можно использовать альтернативный синтаксис - без объявления специальной переменной с булевыми значениями. Давайте перепишем пример из предыдущего урока. В блоке if при встрече первого отрицательного числа задаем вывод '---' и инструкцию break. В случае, когда все элементы списка являются положительными, в блоке else цикла выведется '+++':
'''
lst = [1, 2, 3, -4, 5]

for el in lst:

    if el < 0:
        print('-')
        break
else:
    print('+')
'''
'''
lst = [1, 2, 3, 4, 5]

for el in lst:

    if el < 0:
        print('-')
        break
else:
    print('+')
'''
'''
txt = 'abcdef'

for let in txt:

    if let == 'd':
        print('Буква "d" находится в строке и имеет индекс', txt.index('d'))
        continue
'''





