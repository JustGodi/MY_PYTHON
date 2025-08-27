#преобразование в целые числа
"""txt1 = '1'
txt2 = '2'
sum1 = int(txt1) + int(txt2)
print(sum1)"""
"""txt3 = ' 1.4 '
txt4 = ' 2.9 '
print( int(txt3), int(txt4) ) #ошибка, т.к. в тексте не целые числа"""

#строки с цифрами
"""txt1 = '123'
print( txt1[0] + txt1[1], int(txt1[0]) + int(txt1[1]), (int(txt1[0]) + int(txt1[1])) * int(txt1[2]) )"""

#получение символов из числа
"""num1 = 123
num2 = 4567
letter1 = str(num1)[0]
letter2 = str(num1)[1]
letter3 = str(num1)[2]

letter4 = str(num2)[0]
letter5 = str(num2)[1]
letter6 = str(num2)[2]
letter7 = str(num2)[3]
sum1 = int(letter1) + int(letter2)
sum2 = int(letter1) + int(letter2) + int(letter3)
sum3 = ( int(letter4) + int(letter5) ) - int(letter7)
print( sum1, sum2, sum3 )"""

#преобразование к числу с плавающей точкой
"""txt1 = '12.1'
txt2 = '1.1'
txt3 = '2.8'
num1 = 2
num2 = 4
sum1 = float(txt2) + float(txt3)
sum2 = float(num1) - float(num2)
print( float(txt1), sum1, sum2 )"""
"""txt4 = '3.75606'
txt5 = '123454'
num3 = float( txt4[3] )
num4 = int( txt5[3] )
print( num3, num4 )"""

#функция инпут
"""tst1 = input('введите текс: ')
tst2 = int(input('Введите первое число: '))
tst3 = int(input('Введите второе число: '))
sum1 = tst2 + tst3
txt1 = 'Сумма ваших чисел ровна: ' + str(sum1)
print( tst1, tst2, txt1, type(tst1), type(tst2), type(sum1) )"""

#списки
"""list1 = [ 1, 2, 3, '1', '2', '3', True, False, [1, 2], ['1', '2'] ]
print(list1, type(list1))"""