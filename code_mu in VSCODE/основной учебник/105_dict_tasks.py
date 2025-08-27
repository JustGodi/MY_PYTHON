#1 (тема 105)
#задачи по словарям
'''
dct1 = dict(x = '2', y = '3', z = '4')
lst1_str = list(dct1.values())
print(lst1_str)
lst2_num = []
for num in lst1_str:
    lst2_num.append(int(num))
print(lst2_num)
summ1 = 0
for num in lst2_num:
    summ1 = summ1 + num**2
print(summ1)
'''
#охуеть первый раз циклы использовал и полуилось, раньше их не изучал)0)

#2
'''dct1 = {
    '1': 12,
    '2': 24,
    '3': 36
}
dct2 = dict(a = '3', b = '6', c = '9')
lst_dct1_values = list(dct1.values())
summ_dct1_values = 0
for num in lst_dct1_values:
    summ_dct1_values = summ_dct1_values + num
print(summ_dct1_values)
lst_dct2_values_str = list(dct2.values())
lst_dct2_values_int = []
summ_dct2_values = 0
for num in lst_dct2_values_str:
    lst_dct2_values_int.append(int(num))
for num in lst_dct2_values_int:
    summ_dct2_values = summ_dct2_values + num
print(summ_dct2_values)
res_1 = summ_dct1_values - summ_dct2_values
print(res_1)'''

#3
'''dct_1 = {
    1: '4',
    2: '5',
    3: '6'
}'''
#снизу правильное мышление, yj ytghfdbkmyfz htfkbpfwbz, пересмотрел примеры которые делал раньше по лекциям и сделал норм:
'''lst_dct_1_keys = list(dct_1.keys())
lst_dct_1_keys_str = []
for txt in lst_dct_1_keys:
    lst_dct_1_keys_str.append(str(txt))
print(lst_dct_1_keys_str)
lst_dct_1_values = list(dct_1.values())
print(lst_dct_1_values)
lst_dct_2 = []
for i, n in lst_dct_1_keys, lst_dct_1_values:
    lst_dct_2.append([i, n])
print(lst_dct_2)'''
#сверху правильное мышление, yj ytghfdbkmyfz htfkbpfwbz, пересмотрел примеры которые делал раньше по лекциям и сделал норм:
'''lst_dct_2 = []
for key, val in dct_1.items():
    lst_dct_2.append([str(key), val])
print(lst_dct_2)
dct_2 = dict(lst_dct_2)
print(dct_2)'''
#ебать оно работает и всего в несколько строк кода, кайф)

#4
'''dct_1 = dict(x = '1', y = '2', z = '3')
lst_dct_1_values = list(dct_1.values())
lst_dct_1_res = []
i = 0
n = 2
for txt in lst_dct_1_values:
    lst_dct_1_res.append(lst_dct_1_values[i]*n)
    n +=1
    i +=1
print(lst_dct_1_res)'''

#5
'''dct_1 = dict(x = 1, y = 2, z =3)
lst_dct_1_values = list(dct_1.values())
txt_1 = ''
for txt in lst_dct_1_values:
    txt_1 = txt_1 + str(txt)
print(type(txt_1), txt_1)'''

#6
'''dct_1 = dict(a = 7, b = 6, c = 5)
lst_dct_1_values = list(dct_1.values())
lst_dct_1_values.sort()
lst_dct_1_values_str = []
for txt in lst_dct_1_values:
    lst_dct_1_values_str.append(str(txt))
str_dct_1_values = '/'.join(lst_dct_1_values_str)
print(str_dct_1_values, type(str_dct_1_values))'''

#7
'''dct_1 = {
    'y': 2025,
    'm': 4,
    'd': 12
}
lst_dct_1_values = list(dct_1.values())
lst_dct_1_values_str = []
for txt in lst_dct_1_values:
    lst_dct_1_values_str.append(str(txt))
str_dct_1_values = '-'.join(lst_dct_1_values_str)
print(str_dct_1_values, type(str_dct_1_values))'''