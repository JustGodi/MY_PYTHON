    # 1

# Пусть у вас есть переменные, принимающие имя и фамилию студента, номер его курса. Создайте функцию, которая выведет на экран значения этих переменных. При этом пусть фамилия выводится в верхнем регистре, а имя - только с заглавной буквы.

'''
def out_student_info(dct):

    txt = ''

    for key, value in dct.items():

        if key == 'second_name':
            txt += 'Student ' + value.upper()
        elif key == 'name':
            txt += ' ' + value.title()
        elif key == 'course':
            txt += ' studies on ' +  value + ' course'
    
    return print(txt)

out_student_info(student_info)
'''
#спорное решение т.к. полноценно не смог задать тип аргумента для функции и тип вывода, + решение кажется громоздким, грубым и глупым

# дальше решение которое попросил у дипсика, забыл совсем про  метод .get()
'''
def print_student_info(dct: dict) -> str:

    formated_second_name = dct.get('second_name', '').upper()
    formated_name = dct.get('name', '').title()
    course = dct.get('course', '')

    return print(f"Студент {formated_second_name} {formated_name} учится на {course} курсе")


student_info = {
    'second_name': 'levchenko',
    'name': 'oleg',
    'course': '3',
}

print_student_info(student_info)
'''

    # 2

# Сделайте функцию, которая будет выводить площадь прямоугольника.
'''
def square(a: int, b: int):

    square = a * b
    
    return print('Площадь фигуры ровна:', square)

square(5, 6)

def input_numbers() -> int:

    a = input('Введите сторону фигуры: ')

    if a.isdigit():
        return int(a)
#        return print(c, d)
    else:
        print('Введены некорректные данные')

#input_numbers()
square(input_numbers(), input_numbers())
'''

    # 3

# Сделайте функцию, которая параметром будет принимать строку и возвращать кортеж ее символов.
'''
def str_in_tpl(txt: str) -> tuple:

    tpl = tuple(txt)

    return tpl

print(str_in_tpl('erty 123 ff'))

def str_input() -> str:

    txt = input('Введите текст: ')
    txt = txt.replace(' ', '')

    return(txt)

print(str_in_tpl(str_input()))
'''

    # 4

# Создайте функцию, которая будет проверять два числа. Пусть она выводит сообщения о том, какое из них больше другое или если они равны друг другу по значению.
'''
def compare(a: int, b: int):

    if a > b:
        print(f"{a} больше {b}")
    elif a < b:
        print(f"{b} больше {a}")
    elif a == b:
        print(f"{a} и {b} ровны")

#compare(5, 5)

def input_num() -> int:

    a = input('Введите число ')

    if a.isdigit():
        return int(a)
    else:
        print('Введены некорректное число')

#compare(input_num(), input_num())

def infinit_compare():
    
    while True:
        compare(input_num(), input_num())
        txt = input('Введите quit чтобы закончить или нажмите Enter чтобы продолжить ')

        if txt == quit:
            break

infinit_compare()
'''

    # 5

# Сделайте функцию, которая будет проверять тип переменной и если она является числом, то преобразует ее в строку.
'''
def int_in_str(a):

    if isinstance(a, int | float):
        a = str(a)
    else:
        print(a, type(a))

int_in_str('1')
int_in_str(1)
# сделал только при помощи предыдущих лекций
'''

    # 6

# Сделайте функцию, заполняющую список четными числами от 1 до заданного.
'''
# не правильный код
def even_numbers(a):
    list_of_even_numbers = []


    if isinstance(a, str | dict | list | bool | set):
        return print('Incorrect enter')
    else:
        for num in range(1, a):
            if num % 2 == 0:
                list_of_even_numbers.append(num)
            else:
                continue
        return list_of_even_numbers

print(even_numbers('1'))
'''
'''
#эта часть кода работает
list_of_even_numbers = []
for num in range(1, 10):
    if num % 2 == 0:
        list_of_even_numbers.append(num)

print(list_of_even_numbers)
'''
'''
# эта часть кода тоже работает
list_of_even_numbers = []
for num in range(1, 10):
    if num % 2 == 0:
        list_of_even_numbers.append(num)
    else:
        continue

print(list_of_even_numbers)
'''
'''
# решение которое подсказал deep seeck
def even_numbers(a: int) -> list[int] | None:
# Возвращает список четных чисел от 1 до a (исключительно). Если a не целое число, возвращает None.
    if not isinstance(a, int):
        print('Incorrect enter: expected integer')
        return list()
    return [num for num in range(1, a) if num % 2 == 0]

print(even_numbers(5))
print(even_numbers(50))
print(even_numbers('5'))
'''

    #  7

# Пусть у вас есть словарь, в котором в качестве ключей хранятся имена пользователей, а в качестве значений - их возраст. Создайте функцию, которая выведет все пары ключ-значение в виде кортежа.
'''
dct_name_age = {
    'Oleg': 25,
    'Sergey': 24,
    'John': 20,
    'Julia': 18,
}

def pair_of_dct(dct: dict) -> set:

    for value in dct.items():
        print(value)

#pair_of_dct(dct_name_age)


# проба использования тернарного оператора

#def pair_of_dict_2(dct: dict) -> set:

#    return (value for value in dct.items())

#print(pair_of_dict_2(dct_name_age))

#неудача


# что подсказал deep seek
def pair_of_dict_2(dct: dict) -> None:

    [print((k, v)) for k, v in dct.items()] if dct else print("Словарь пуст")

pair_of_dict_2(dct_name_age)
pair_of_dict_2({})
# это просто охуенно
'''

    # 8

# Сделайте функцию, которая параметром будет принимать число, а возвращать строку с соответствующим днем недели.
'''
def day_of_week(num):

    match num:
        case 1 | '1': print('Понедельник')
        case 2 | '2': print('Вторник')
        case 3 | '3': print('Среда')
        case 4 | '4': print('Четверг')
        case 5 | '5': print('Пятница')
        case 6 | '6': print('Суббота')
        case 7 | '1': print('Воскресенье')

day_of_week('4')

def input_day_of_week():

    txt = input('Введите число от 1 до 7 ')

    if txt.isdigit() and 1 <= int(txt) <= 7:
        return txt
    else:
        return print('EROR EROR EROR')

#print(input_day_of_week())

day_of_week(input_day_of_week())
'''





























































