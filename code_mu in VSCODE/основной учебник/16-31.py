#числа с плавающей точкой
"""num1 = 1.5
num2 = 0.75
num3 = 9
num4 = 2
print(num1-num2, num1+num2, num1*num2, num3/num4, num3//num4)"""

#отрицательные числа
"""num1 = 2
num2 = 3
num3 = -5
print(num1-num2, num3-num2, num2-num3)"""

#остаток деления
'''num1 = 10
num2 = 6
print(num1/num2, num1//num2, num1%num2)'''

#возведение в степень
"""num1 = 5
num2 = 2
print(num1**num2)"""

#возведение в степень имеет приоритет перед умн и дел
"""res = (7 + 4) * (3 - 1) ** 3
print(res)"""

#строки 
"""txt = 'lorem ipsum'
print(txt, 'ipsum lorem')"""

#сложение строк
"""text1 = 'Двадцать '
text2 = 'Три'
text3 = text1 + text2
print(text3, text1+text2, 'Двадцать '+'Три')"""

#умножение строк
"""text1 = 'a1b2'
text2 = 'ab'
text3 = '1213'
num1 = 1213
print(text1*4, text2*2+text3)"""

#символы строки, [] обозначается индекс символа, с нулевого старт
"""text1 = 'АБВГД'
print(text1[2], text1[-2])"""

#экранирование символов строки с помощью /
"""text1 = 'abc\'abc'
text2 = "\"abcd\"fr'23"
print(text1, text2)"""

#длина строки с помощью функции len()
"""txt1 = '1234 qwerty'
print(len(txt1))"""
"""num1 = 1234
print( len(str(num1)) )"""

#многострочные строки
"""text1 = '''
1
2
3
'''
text2 = """
#1
#2
#3
"""
print(text1, text2, text1+text2, text1*3)"""

#логические значения boolean (True/False)
"""logic1 = True
logic2 = False
print(logic1, logic2, True, False)"""

#none
"""test1 = None
print(test1, None)"""

#строгая типизация, нельзя мат операции строк с числами и наоборот
"""num1 = 123
text1 = 'abc'
print( num1 + text1 )"""

#преобразование к строке с помощью ф-ии str()
"""text1 = 'ABC'
num1 = 123
print( text1 + str(num1), len(str(num1)) )"""
'''txt1 = 'abc'
num1 = 456
num2 = str(num1)
num3 = 1
num4 = 2
sum_txt = str(num3) + str(num4) 
sum1 = int( num2[0]) + int(num2[1]) + int(num2[2])
print( sum1, len(num2), txt1+num2, sum_txt)'''