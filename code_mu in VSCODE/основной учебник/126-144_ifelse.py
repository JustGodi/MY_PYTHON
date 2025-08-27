#в python есть специальная конструкци if-else которая позволяет выполнять код в зависимости от его соответствия какому-либо условию
'''
if операция сравнения:
	
		#код
	
else:
	
		#код
	
'''

#отступы в конструкции if-else. В Python отступы определяют, какие блоки конструкции if-else объединены в пару. Поэтому строки под каждым блоком должны находится на расстоянии одного отступа. Он равен четырем пробелам или одной табуляции.
'''
if операция сравнения:
	код 
else:
	код

Если же убрать отступ, то Python вернет ошибку:

if операция сравнения:
код
else:
код
'''

#операторы > и <. Для сравнения двух значений между собой, используются операторы больше, больше или ровно, меньше, меньше или ровно(>, >=, <, <=)
'''
num_1 = 0
if num_1 >= 0:
    print('+++')
else:
    print('---')
'''
'''
num_1 = 5
if num_1 > 10:
    print('+')
else:
    print('-')
'''
'''
age = int(input('Введите ваш возраст '))
if age >= 18:
    print('You have access to the site')
else:
    print('Hou do not have access to the site')
'''

#проверка на равенство при помощи оператора ==
'''
num_1 = 3
num_2 = 0
if num_2 == 0:
    print('+')
else:
    print('-')
'''
'''
txt_1 = '123'
if txt_1 == 123:
    print('+')
else:
    print('-')
'''
'''
lst_1 = ['a', 'b', 'c', 'd']
if len(lst_1) == 5:
    print('+')
else:
    print('-')
lst_1.append('e')
if len(lst_1) == 5:
    print('+')
else:
    print('-')
'''

#проверка на неравенство при помощи оператора !=
'''
num_1 = 5
num_2 = 0
if num_2 != 0:
    print('+')
else:
    print('-')
'''
'''
num_1 = -4
if num_1 != 4:
    print('+')
else:
    print('-')
'''
'''
num_1 = 123
if num_1 != 123:
    print('+')
else:
    print('-')
'''
'''
lst_1 = ['a', 'b', 'c']
if lst_1[1] != 'c':
    print('+')
else:
    print('-')
'''
'''
lst_1 = [3, 4, 5, 6]
lst_2 = ['3456']
if lst_1 != lst_2:
    print('+')
else:
    print('-')
'''

#логическое И при помощи оператора and (&)
'''
num_1 = 5
if num_1 > 0 and num_1 < 10:
    print('+')
else:
    print('-')
'''
'''
num_1 = 2
num_2 = 3

if num_1 == 2 and num_2 == 3:
    print('+')
else:
    print('-')

if num_1 == 2 & num_2 == 3:
    print('++')
else:
    print('--')
'''
#почему со знаком & не работает так же как с оператором and, если поменять & на and то отработает правильно
#upd от 25.06.2025 потому что and логическое сравнение а & побитовое сравнение
'''
num_1 = -3
num_2 = 3
if num_2 > 0 and num_2 < 5:
    print('+')
else:
    print('-')
if num_1 > 0 & num_1 < 5:
    print('++')
else:
    print('--')
#опять & не работает как надо, как должен работать and, почему
'''
'''
num_1 = 6
num_2 = 10
if num_1 < 8 and num_2 >= 10:
    print('+')
else:
    print('-')
'''

#логическое или оператор or
'''
num_1 = 10
num_2 = -5
if num_1 > 0 or num_2 > 0:
    print('+')
else:
    print('-')
'''
'''
num_1 = -1
num_2 = 4
if num_1 <= 1 or num_2 >= 3:
    print('+')
else:
    print('-')
'''

#логическое НЕТ оператор not
'''
num_1 = 2
if num_1 > 0 and not num_1 < 1:
    print('+')
else:
    print('-')
'''
'''
num_1 = 15
if num_1 > 20 and not num_1 < 10:
    print('+')
else:
    print('-')
'''

#приоритет операций сравнения. Операция and имеет приоритет над or
'''
num_1 = 3
if num_1 > 0 and num_1 < 5 or num_1 > 10 and num_1 < 20:
    print('+')
else:
    print('-')
'''

#группировка условий. Хотя and имеет приоритет над or удобнее использовать группирующие круглые скобки чтобы показать явный приоритет
'''
#
num_1 = 3
if (num_1 > 0 and num_1 < 5) or (num_1 > 10 and num_1 < 20):
    print('+')
else:
    print('-')
'''
# В приведенном ниже коде укажите приоритет операций в явном виде:
'''
tst = 3
	
if tst > 2 and tst < 10 or tst == 20:
	print('+++')
else:
    print('---')
'''
'''
num_1 = 3

if (num_1 > 2 and num_1 < 10) or num_1 == 20:
    print('+')
else:
    print('-')
'''
'''
num_1 = 3

if (num_1 > 5 and num_1 > 0) and num_1 < 3:
    print('+')
else:
    print('-')
'''

#двойное сравнение
'''
num_1 = 3

if 2 < num_1 < 10:
    print('+')
else:
    print('-')
'''
'''
num_1 = 15

if 10 < num_1 < 20:
    print('+')
else:
    print('-')
'''
'''
num_1 = -5

if (-10 < num_1 < 0) or (-8 < num_1 < 30):
    print('+')
else:
    print('-')
'''
'''
lst_1 = list('abcde')

if 0 < len(lst_1) < 6:
    print('+')
else:
    print('-')
'''

#проверка наличия при помощи оператора in
'''
num_1 = 3
num_2 = 1
lst_1 = [1, 2, 3]

if num_1 in lst_1:
    print('+')
else:
    print('-')

if num_2 not in lst_1:
    print('+')
else:
    print('-')
'''
'''
lst_1 = [1, 2, 3, 'x', 'y', 'z']
txt_1 = 'x'
txt_2 = '1'

if txt_1 in lst_1 and txt_2 not in lst_1:
    print('+')
else:
    print('-')
'''
'''
txt_1 = '123456'
let_1 = '3'

if let_1 in txt_1:
    print('+')
else:
    print('-')
'''
'''
lst_1 = ['a', 'b', 'c', 'd', 'e']
tpl_1 = tuple('abc')
num_1 = 3
res_1 = lst_1[num_1]

if res_1 in tpl_1:
    print('+')
else:
    print('-')
'''

#проверка на специальные символы(None, False, True)
'''
num_1 = 3

if num_1 == None:
    print('+')
else:
    print('-')
if num_1 is None:
    print('++')
else:
    print('--')
if num_1 is not None:
    print('+++')
else:
    print('---')
'''

    #конструкцию if-else можно применять в сокращённом виде, если нужно проверить истинная ли переменная, т.е. ровна ли переменая булевому значению True. 
'''
bln_1 = True

if bln_1:
    print('+')
else:
    print('-')
'''
    #так же сокращённую форму можно использовать со значениями которые прироаненны к булевым
    #Значения, приравниваемые к False
    #None
    #целое число 0
    #число с плавающей точкой 0.0
    #пустая строка ''
    #пустой список []
    #пустой кортеж ()
    #пустой словарь {}
    #пустое множество set()
    #Все остальные значения приравниваются к True.
'''
num_1 = 5

if num_1:
    print('+')
else:
    print('-')
'''
'''
lst_1 = []
nothing_1 = None
num_1 = -1
bln_1 = False
bln_2 = True
txt_1 = 'False'
txt_2 = ''
txt_3 = ' '
tpl_1 = tuple()
num_2 = 1 - 1
st_1 = set()
dct_1 = dict()

if dct_1:
    print('+')
else:
    print('-')
'''

#конструкция elif. elif позволяет задать дополнительное сравнение для блока else
'''
num_1 = int(input('Введите ваше число: '))
if num_1 >=0 and num_1 <= 9:
    print('Вы ввели число меньше 10')
elif num_1 > 9 and num_1 <=20:
    print('Вы ввели число больше 10')
else:
    print('Я таких чисел не знаю')
'''
'''


num_1 = 5
num_2 = 8
if num_1 > num_2:
    print('Первое число больше второго')
elif num_2 > num_1:
    print('Второе число больше первого')
'''
'''
age = int(input('Введите ваш возраст: '))

if age >= 3 and age < 18:
    print('Вам запрещен доступ на этот ресурс')
elif age >= 18 and age <= 60:
    print('Добро пожаловать')
else:
    print('Возможно введено некоректное значение')
'''
'''
num_1 = int(input('Введите число от 1 до 31 '))

if num_1 >= 1 and num_1 <= 10:
    print('Первая декада месяца ')
elif num_1 >= 11 and num_1 <= 20:
    print('Вторая декада месяца ')
elif num_1 >= 21 and num_1 <= 31:
    print('Третья декада месяца ')
else:
    print('Введено некорректное значения')
'''

#вложенные if. Конструкции if else можно вкладывать друг в друга произвольным образом. Только при этом нужно собязательно соблюдать отступы
#Давайте сравним нашу переменную с нулем. В первом if зададим условие, если переменная меньше или равна 0. Внутри этого if пропишем еще одно условие - если число меньше или равно 0. Для него укажем также блок else. В конце первой конструкции if else пропишем сообщение на случай, если число меньше 0:
'''


num_1 = int(input('Введите число '))

if num_1 >= 0:
    if num_1 <=5:
        print('Меньше или ровно 5')
    else:
        print('Больше 5')
else:
    print('Меньше нуля')
'''
'''
month = int(input('Введите число от 1 до 12 '))

if month >= 1:
    if month <= 12:
        if month == 12 or 1 <= month < 3:
            print('Зима')
        elif 3 <= month < 6:
            print('Весна')
        elif 6 <= month < 9:
            print('Лето')
        elif 9 <= month < 12:
            print('Осень')
    else:
        print('Введено неверное значение')
else:
    print('Введено неверное значение')
'''
'''
num_1 = int(input('Введите число от 10 до 99 '))

if num_1 >= 10:
    if num_1 <= 99:
        txt_1 = str(num_1)
        sm_1 = int(txt_1[0]) + int(txt_1[1])
        if 1 <= sm_1 < 10:
            print('Сумма цифр однозначна и ровна = ', sm_1)
        elif 10 <= sm_1 < 100:
            print('Сумма цифр двухзначна и ровна = ', sm_1)
    else:
        print('Введене некоректное значение')
else:
    print('Введене некоректное значение')
'''

#констркция match-case. В python 3.10 была добавлена специальа конструкиця match-case которая используется для выбора одного значения из некоторого ряда значений
'''
txt_1 = input('Введите a или b или c или d ')

match txt_1:
    case 'a': print('a')
    case 'b': print('b')
    case _: print('unknown')
#Также с помощью оператора | можно в каждом варианте задать выборку нужных значений:
match txt_1:
    case 'a' | 'c': print('a or c')
    case 'b' | 'd': print('b or d')
    case _: print('unknown')
'''
'''
num_1 = int(input('Введите число от 1 до 4 '))

match num_1:
    case 1: print('Зима')
    case 2: print('Весна')
    case 3: print('Лето')
    case 4: print('Осень')
    case _: print('Некорректное значение')
'''
'''
num_1 = int(input('Введите цифру месяца: '))

match num_1:
    case 1: print('Январь')
    case 2: print('Февраль')
    case 3: print('Март')
    case 4: print('Апрель')
    case 5: print('Май')
    case 6: print('Июнь')
    case 7: print('Июль')
    case 8: print('Август')
    case 9: print('Сентябрь')
    case 10: print('Октябрь')
    case 11: print('Ноябрь')
    case 12: print('Декабрь')
    case _: print('Некорректный ввод')
'''
'''
tst_1 = ' '

match tst_1:
    case str(): print('Строка')
    case int() | float(): print('Число')
    case _: print('unk')
'''

#тернарный оператор (сокращённая версия конструкции else-if)
'''
num_1 = 5
num_2 = 10

print('+++' if num_1 > num_2 else '---')
'''

'''tst = 12

if tst > 0:
	print('+++')
else:
	print('---')'''
'''
num_1 = 12

print('+' if num_1 > 0 else '-')
'''

'''tst = 'abcde'

if 'a' in tst:
	print('+++')
else:
	print('---')'''
'''
txt_1 = 'abcde'

print('+' if 'a' in txt_1 else '-')
'''

#проверка на тип элемента при помощи функции isinstance(). Она первым параметром принимает элемент, а вторым - тип, на который он проверяется. При этом в качестве названия для второго параметра берутся имена функций, преобразующие данные в соответствующий тип: для строк - str, чисел - int, списков - list и т.д. Функция isinstance возвращает булевые значения: если элемент соответствует типу, то вернется True, в противном случае - False.
#Пусть у нас есть переменная tst. Давайте проверим, является ли ее значение строкой. Для этого справа от if записываем функцию isinstance. В ее параметры передаем tst и тип str. Если значение и тип данных совпали, то пусть выведется соответствующее сообщение:
'''
txt_1 = 'a'

if isinstance(txt_1, str):
    print('string')
'''
'''
num_1 = 12.0

if isinstance(num_1, int | float):
    print('Число')
'''
'''
lst_1 = [1, 2, 3]

if isinstance(lst_1, list):
    print('Список')
'''
'''


tpl_1 = (1, 2, 3)

if isinstance(tpl_1, tuple):
    print('Кортеж')
'''
'''
dct_1 = dict(a = 1, b = 2, c = 3)

print('словарь' if isinstance(dct_1, dict) else '')
'''
'''
num_1 = 5

print('число' if isinstance(num_1, int) else '')

fl_1 = 5.01

match fl_1:
    case float(): print('число с плавающей точкой')
    case _: print('unk')

txt_1 = '123'

if isinstance(txt_1, str):
    print('Строка')

'''