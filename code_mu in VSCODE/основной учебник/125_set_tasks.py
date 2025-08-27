#Узнайте в каком из них большее количество элементов.
'''
st_1 = {'x', '1', 'y', '2', 'z'}
st_2 = {1, 2, 3, 4, 5, 6}
print(len(st_1) > len(st_2), len(st_2) > len(st_1)) 
'''

#Проверьте, что все цифры второго числа есть в первом числе.
'''
num_1 = 12345
num_2 = 12321
lst_num_1 = list(str(num_1))
st_num_2 = set(str(num_2))
print(st_num_2.issubset(lst_num_1))
'''

#Создайте из всех их элементов множество.
'''
num_1 = 34
lst_1 = [1, 2, 5]
tpl_1 = (6, 7, 8)
st_num_1 = set(str(num_1))
st_lst_1 = set(lst_1)
st_tpl_1 = set(tpl_1)
print(st_num_1, st_lst_1, st_tpl_1)
'''

#Проверьте входят ли элементы каждой из переменной в множество.
'''
st_1 = {'18', '24', '34', '47', '81', '63'}
txt_1 = '34'
tpl_1 = ('81', '12', '46')
st_txt_1 = set()
st_txt_1.add(txt_1)
st_tpl_1 = set(tpl_1)
res_1 = st_txt_1.issubset(st_1)
res_2 = st_tpl_1.issubset(st_1)
print(res_1, res_2)
'''

#Проверьте, что оба числа состоят из одинаковых цифр.
'''
num_1 = 12345
num_2 = 45123
st_num_1 = set(str(num_1))
st_num_2 = set(str(num_2))
print(st_num_1 == st_num_2)
'''

#Получите число, состоящее из общих цифр наших чисел.
'''
num_1 = 12345
num_2 = 45678
lst_num_1 = list(str(num_1))
lst_num_2 = list(str(num_2))
n = 0
for i in lst_num_2:
    lst_num_1.append(lst_num_2[n])
    n += 1
print(lst_num_1)
txt_1 = ''
n = 0
for i in lst_num_1:
    txt_1 = txt_1 + lst_num_1[n]
    n += 1
num_3 = int(txt_1)
print(txt_1, num_3, type(txt_1), type(num_3))
'''

#Найдите общие элементы для первых двух множеств. А затем объедините полученное множество с st3.
'''
st_1 = {'ab', 'b', 'ce', 'de', 'd'}
st_2 = {'ef', 'd', 'ab', 'bc'}
st_3 = {'a', 'g', 'b', 'c'}
res_1 = st_1.intersection(st_2)
print(res_1, st_3)
st_3.update(res_1)
print(st_3)
'''