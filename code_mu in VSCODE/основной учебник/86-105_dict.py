    #Словарь представляет собой специальный тип хранения данных в виде пар ключ-значение. Для создания словарей нужно использовать фигурные скобки. Давайте сделаем пустой словарь:
'''dct1 = {
    'a':1,
    'b':2,
    'c':3
}
print(dct1)
dct2 = {
    1:'a',
    2:'b',
    3:'c'
}
print(dct2)
dct3 = {
    'ab':2,
    'cd':4,
    'ef':6
}
print(dct3)
dct4 = {
    'Name':'Oleg',
    'Surname':'Levchenko',
    'Age':'25'
}
print(dct4)
dct5 = {
    1:'Январь',
    2:'Февраль',
    3:'Март',
    4:'Апрель',
    5:'Май',
    6:'Июнь',
    7:'Июль',
    8:'Август',
    9:'Сентябрь',
    10:'Октябрь',
    11:'Ноябрь',
    12:'Декабрь',
}
print(dct5)'''

    #альтернативный способ создания словаря при помощи функции dict(). В ее параметры нужно передать пару ключ-значения. Если же в параметрах ничего не указать, созданный словарь будет пустым
'''
dct1 = dict(a = '1', b = '2')
print(dct1)
dct2 = dict(a = 1, b = 2)
print(dct2)
'''

#передавать числа в качестве ключей в функции dict нельзя. В таком случае вернется ошибка:
'''
dct1 = (1 = 'a', 2 = 'b')
print(dct1)
'''
'''dct1 = dict(a = 1, b = 2, c = 3)
print(dct1)'''

#передавать строки в качестве ключей в функции dict нельзя. В таком случае вернется ошибка:

'''dct1 = dict('1' = 'a', '2' = 'b', '3' = 'c')
print(dct1)'''
'''dct1 = dict(a = '12', b = '34', c = '56')
print(dct1)'''

    #значение одного элемента словаря(dictionary)
    
'''dct1 = dict(a = 1, b = 2, c = 3)
res1 = dct1['a']
print(res1)
#Если же обратиться к ключу, которого нет словаре, то вернется ошибка:
#res2 = dct1['x']
#print(res2)
key1 = 'b'
print(dct1[key1])'''
'''dct1 = dict(x = 1, y = 2, z = 3)
res1 = dct1['x']
key2 = 'y'
print(res1, type(dct1[key2]), dct1[key2], dct1['z'])
total1 = res1 + dct1[key2] + dct1['z']
print(total1)'''
'''dct1 = {
    1:'a',
    2:'b',
    3:'c'
}
key1 = 1
res1 = dct1[2]
txt1 = dct1[key1] + res1 + dct1[3]
print(txt1, type(txt1)) 
print(dct1[key1] + res1 + dct1[3])'''

    #изменение значения элемента словаря при обращени по ключу
'''
dct1 = dict(a = 1, b = 2, c = 3)
print(dct1)
dct1['a'] = 'a'
print(dct1)
'''
'''dct1 = dict(x = 1, y = 2, z = 3)
print(dct1)
dct1['x'] +=1
print(dct1)'''
'''dct1 = dict(surn = 'smith', name = 'john')
print(dct1)
dct1['surn'] = 'Levchenko'
dct1['name'] = 'Oleg'
print(dct1)'''

    #Добавление элемента в словарь в Python. Можно добавлять новые элементы в словарь. Для этого нужно записать значение в тот ключ, которого еще нет в словаре.
'''dct1 = dict(a = 1, b = 2, c = 3)
print(dct1)
dct1['d'] = 4
print(dct1)'''
#элемент с новым ключом, которого не было в словаре, был добавлен в конец словаря
'''dct1 = dict(a = 1, b = 2, c = 3)
print(dct1)
dct1['1'] = 'a'
dct1['2'] = 'b'
dct1['3'] = 'c'
print(dct1)'''

    #длину словаря можно узнать при помощи функиции len()
'''
dct1 = dict(a = 1, b = 2, c = 3)
res1= len(dct1)
print(res1)
'''
'''dct1 = dict(a = 12, b = 34, c = 56, d = 78, e = 90)
dct2 = dict(dct1 = len(dct1))
print(dct1)
print(dct2)'''

    #объединение словарей
#при помощи оператора + выдаст ошибку
'''dct1 = dict(a = 1, b = 2, c = 3)
dct2 = dict(d = 4, e = 5, f = 6)
dct3 = dct1 + dct2
print(type(dct3), dct3)'''
#а вот при помощи метода .update(Название словаря который добавляем) всё будет работать, добавляемый словарь будет добавлен вконец первого словаря
'''
dct1 = dict(a = 1, b = 2, c = 3)
dct2 = dict(d = 4, e = 5, f = 6)
print(dct1, dct2)
dct1.update(dct2)
print(dct1)
'''
'''dct1 = dict(a = 1, b = 2, c = 3)
dct2 = dict(d = 4, e = 5, f = 6)
dct3 = dict(g = 7, h = 8, i = 9)
print(dct1)
print(dct2)
print(dct3)
dct1.update(dct2)
dct1.update(dct3)
print(dct1)
print(dct2)
print(dct3)'''

    #объединение словарей с одинаковыми ключами. Есл в словарях находятся одинаковые элементы, то при объединении останется только один из них.
'''dct1 = dict(a = 1, b = 2, c = 3)
dct2 = dict(a = 4, b = 5, c = 6)
print(dct1)
print(dct2)
dct1.update(dct2)
print(dct1)
print(dct2)'''
#остался последний словарь, т.е. тот который добавляли

    #удаление элементо из словаря по ключу del dict[key]
'''dct1 = dict(a = 1, b = 2, c = 3)
print(dct1)
del dct1['a']
print(dct1)'''
'''dct1 = {
    1: 'a',
    2: 'b',
    3: 'c',
    4: 'd',
    5: 'e'
}
print(dct1)
del dct1[2], dct1[4]
print(dct1)'''

    #извлечение элемента из словаря по ключу. Можно извлекать элемент из словаря. В этом случае элемент из словаря удалится и мы при этом получим его в переменную. Для такой операции нужно применить метод pop. В его параметре задается ключ извлекаемого элемента.
'''dct1 = dict(a = 1, b = 2, c = 3)
print(dct1)
print(dct1.pop('a'))
print(dct1)
res1 = dct1.pop('c')
print(res1)
print(dct1)'''
'''dct1 = {
    1: 'ab',
    2: 'cd',
    3: 'ef'
}
res1 = dct1.pop(2)#del dct1[2]
print(dct1.items())'''

#извлечение последнего элемента словаря. С помощью метода popitem можно извлечь последний элемент из словаря. Он возвращает кортеж из пары ключ-значение извлеченного элемента.
'''
dct1 = dict(a = 1, b = 2, c = 3)
print(dct1)
res1 = dct1.popitem()
print(dct1)
print(res1)
'''
'''dct1 = {
    1: 'a',
    2: 'b',
    3: 'c',
    4: 'd',
    5: 'e'
}
print(dct1)
res1 = dct1.popitem()
print(dct1)
print(res1)
lst1 = list(dct1.keys())
lst1.reverse()
print(lst1)'''

#удаление всех элементов из словаря при помощи метода .clear()
'''dct1 = dict(a = 1, b = 2, c = 3)
print(dct1)
dct1.clear()
print(dct1)'''
'''dct1 = {
    1: 'text1',
    2: 'text2',
    3: 'text4'
}
dct1.clear()
dct1[4] = 'text4'
print(dct1)'''

#проверка наличия ключа при помощи оператора in
'''dct1 = dict(a = 1, b = 2, c = 3)
res1 = 'a' in dct1
res2 = 'd' in dct1
print(res1, res2)'''
'''dct1 = {
    1: 'x',
    2: 'y',
    3: 'z',
    4: 'w'
}
print('x' in dct1)
dct2 = {
    1: 'x',
    2: 'y',
    3: 'z',
    4: 'w'
}
print('x' not in dct1)'''

#ещё один метод получения элемента списка при помощи метода .get(key, value), value(необязательно) — значение, которое будет возвращено, если ключ не найденб если не задать value в противном случае вернёт - None
'''
dct1 = dict(a = 1, b = 2, c = 3)
print(dct1)
res1 = dct1.get('a', 0)
print(res1)
print(dct1.get('b'))
print(dct1)
print(dct1.get('d'))
print(dct1.get('e', 1234))
'''
'''dct1 = {
    1:'a',
    2:'b',
    3:'c',
    4:'d',
    5:'e',
    6:'f'
}
print(dct1)
res1 = dct1.get(1, 0)
print(res1)
print(dct1.get(2))
print(dct1)
print(dct1.get(7))
print(dct1.get(8, 1234))'''
'''dct1 = dict(a = 1, b = 2, c = 3)
print(dct1)
dct1['d'] = '!'
res1 = dct1.get('d', 0)
res2 = dct1['d']
print(dct1)
print(res1, res2)'''

#преоьразование ключей словаря в список (бонусом и значений)
'''dct1 = dict(a = 1, b = 2, c = 3, d = 4, e = 5)
lst_dict_keys = list(dct1)#lst_dict_keys = list(dct1.keys)
lst_dict_values = list(dct1.values())
#если надо упорядочить списки это надо делать только после функции лист отдельной строкой
print(lst_dict_keys, lst_dict_values)'''

#получение всех ключей из словаря при помощи метода .keys(). Возвращает метод специальный объект dict_keys.
'''dct1 = dict(a = 1, b = 2, c = 3)
res1 = dct1.keys()
print(res1)'''
#Для удобства работы с объектом dict_keys можно преобразовать его в список. Это делается с помощью функции list:
'''dct1 = dict(a = 1, b = 2, c = 3)
res1 = list(dct1.keys())
print(res1)
#В данном случае не Возвращает специальный объект dict_keys.
#только чем это отличается от обычного list(имя словаря например как ниже)
res2 = list(dct1)
res3 = list(dct1.values())
res4 = dct1.values()
res5 = dct1.keys()
print(res2)
print(res3)
print(res4)
print(res5)
print(type(res4), type(res5))'''
'''dct1 = {
    2: 'a',
    4: 'b',
    6: 'c'
}
res1 = list(dct1)
res2 = res1[0] * res1[1] * res1[2]
print(res2)'''
'''dct1 = {
    1: 'x',
    2: 'y',
    3: 'z',
    4: 'w'
}
res1 = list(dct1)
res1.sort(reverse = True)
print(res1)'''

#получение всех значений словаря при помощи .values()
'''dct1 = dict(a = 1, b = 2, c = 3, d = 'd', e = True, f = 5.01)
res1 = dct1.values()
res2 = list(dct1.values())
print(res1)
print(res2)'''
#Возвращает метод специальный объект dict_values
'''dct1 = dict(a = 1, b = 2, c = 3)
dct2 = {
    1: 'a',
    2: 'b',
    3: 'c'
}
lst_dct1_keys = list(dct1.keys())
lst_dct1_values = list(dct1.values())
lst_dct2_keys = list(dct2.keys())
lst_dct2_valus = list(dct2.values())
res1 = lst_dct1_values + lst_dct2_valus
res2 = lst_dct2_keys + lst_dct1_keys
print(res1)
print(res2)'''

#получение пары ключ-значение при помощи метода .items(), который возвращает специальный объект dict_items.
'''dct1 = dict(a = 1, b = 2, c = 3)
res1 = dct1.items()
print(res1)
res2 = list(dct1.items())
print(res2)
print(type(res2[0]))'''
'''
dct1 = dict(a = 12, b = 34, c = 56, d = 78, e = 90)
lst1 = []
for key, val in dct1.items():
    lst1.append(key)
    lst1.append(val)
print(lst1)
'''

#преобразование в словарь при помощи функции dict()
'''
txt1 = '12345'
dct1 = dict(txt1)
print(dct1)
'''
'''
lst1 = ['1', '2', '3', '4', '5']
dct2 = dict(lst1)
print(dct2)
'''
#весь код выше приведёт к ошибке
#ниже приведеён код который создёт словарь из вложенных списков
'''lst1 = [['a', 1], ['b', 2], ['c', 3]]
dct1 = dict(lst1)
print(dct1)'''
#так же в коде ниже показано как это сделать из вложенных кортежей
'''tpl1 = ((1, 'a'), (2, 'b'), (3, 'c'))
dct1 = dict(tpl1)
print(dct1)'''