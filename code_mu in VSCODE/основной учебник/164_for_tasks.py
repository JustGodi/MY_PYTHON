    # 164 Практикум на циклы в Python
    # 1
'''
dct = {
    '1': 'a',
    '2': 'b',
    '3': 'c',
    '4': 'd'
}
lst = list(range(0, len(dct) - 1))
lst_items = []


for key, value in zip(lst, dct.values()):
    lst_items.append(key)
    lst_items.append(value)

print(lst_items)
'''

    # 2 Дана пустая строка. Заполните с помощью цикла четными числами от 1 до 20.
'''
lst_num = list(range(1, 20))
txt = ''

for num in lst_num:
    
    if num % 2 == 0:
        txt += ' ' + str(num)

print(txt)
'''

    # 3 Выведите с помощью цикла столбец нечетных чисел от 100 до 1.
'''
lst_num = list(range(100, 0, -1))

for num in lst_num:

    if num % 2 != 0:
        print(num)
'''

    # 4 Заполните список 10-ю иксами с помощью цикла.
'''
txt = ''
i = 0

while i < 10:
    txt += 'x'
    i += 1

print(txt, len(txt))
'''

    # 5 Заполните множество с помощью цикла первыми 10-ю буквами английского алфавита.
'''
alphabet = [chr(i) for i in range(97, 123)]
#это решение нагуглил
st = set()
i = 0

for let in alphabet:
    st.add(let)
    i += 1

    if i == 10:
        break

print(len(st), st)
'''

    # 6 Дан кортеж с числами. С помощью цикла выведите только те элементы, которые меньше меньше 10 и больше 5.
'''
tpl = tuple(range(1, 21))
lst = []

for num in tpl:
    if num > 5 and num < 10:
        lst.append(num)

print(lst)
'''

    # 7 Дана строка. С помощью цикла проверьте, есть ли в ней буква 'c'.
'''
txt = 'sdascdasdsacsadasdc'
i = 0

for let in txt:
    
    if let == 'c':
        i += 1

print('В данной строке английская буква "c" встречается:', i, 'раз(-а)')
'''

    # 8 Дан список с числами. Найдите среднее арифметическое его элементов.
'''
lst = list(range(1, 50))
res_sum = 0

for num in lst:
    res_sum += num

res_middle = res_sum / len(lst)

print(res_middle)
'''

    # 9 Дан список с числами. Переберите все его элементы до тех пор, пока не обнаружится положительное число.
'''
lst = [-1, -3, -5, -4, 2, -3, -5]

for num in lst:

    if num > 0:
        print('Обнаружено положительное число с иднексом: ', lst.index(num))
        print('Поиск остановлен')
        break
'''

    # 10 Дан словарь с именем, фамилией и возрастом пяти пользователей. Выведите все элементы словаря в виде кортежа ключ-значение.
'''
dct = {
    'Oleg': 'Levchenko',
    'Sergey': 'Arhipov',
    'Artem': "Olar'",
    'John': 'Smith',
    'Mary': 'Jane'
}
lst = []

for item in zip(dct.keys(), dct.values()):
    print(item)
#прошлая версия была чере два for и со списком, корявая крч. тут я вспоминл что метод кейс и валуес для зипа будет как два отдельных множества :3
'''

    # 11 Из словаря в предыдущей задачи выведите в столбик все имена пользователей. При этом пусть они все будут написаны с большой буквы.
'''
dct = {
    'oleg': 'Levchenko',
    'sergey': 'Arhipov',
    'artem': "Olar'",
    'john': 'Smith',
    'mary': 'Jane'
}

for name in dct.keys():
    print(name.title())
'''