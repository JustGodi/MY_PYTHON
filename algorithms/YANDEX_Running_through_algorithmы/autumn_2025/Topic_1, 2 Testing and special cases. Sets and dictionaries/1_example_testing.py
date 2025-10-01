# квадратное уравнение ax^2 + bx + c = 0
# D = b^2 - 4ac
# x1,2 = (-b +/- sqrt(D))/2a

'''
def square_equation(a: int, b: int, c: int):
    d = b ** 2 - 4 * a * c
    x_1 = -b - (d ** (1/2)/)(2 * a)
    x_2 = -b + (d ** (1/2)/)(2 * a)
    return print(x_1, x_2)
square_equation(1, -2, 0) # output 1, 3 is wrong
# ошибка произошла потому что не стоят скобки в числителе x_1 и x_2
#в следующем шаге исправление
'''

'''
# добавлены скобки в уравнениях x_1 и x_2
def square_equation(a: int, b: int, c: int):
    d = b ** 2 - 4 * a * c
    x_1 = (-b - (d ** (1/2)))/(2 * a)
    x_2 = (-b + (d ** (1/2)))/(2 * a)
    return print(x_1, x_2)
#square_equation(1, -2, 0) # output 1, 2 correct
#square_equation(1, 2, 1) # после добавления проверки из комментария вначале # output -1, -1 wrong потому то в уравнении с заданными параметрами всего один x
# в следующем шаге исправлено
'''

'''
# добавлена проверка на случай если дискриминант равен нулю
def square_equation(a: int, b: int, c: int):
    d = b ** 2 - 4 * a * c
    if d == 0:
        x_1 = -b/(2 * a)
        return print(x_1)
    else:
        x_1 = (-b - (d ** (1/2)))/(2 * a)
        x_2 = (-b + (d ** (1/2)))/(2 * a)
        return print(x_1, x_2)
#square_equation(1, -2, 0)
#square_equation(1, 2, 1)
#square_equation(1, 1, 1) # после добавления проверки из комментария вначале # ответ в python странный, но у уровнения нет корней, т.к. дискриминант меньше нуля
# в следующем шаге исправлено
'''

'''
# добавлена проверка условия, что дискриминант больше нуля
def square_equation(a: int, b: int, c: int):
    d = b ** 2 - 4 * a * c
    if d == 0:
        x_1 = -b/(2 * a)
        return print(x_1)
    elif d > 0:
        x_1 = (-b - (d ** (1/2)))/(2 * a)
        x_2 = (-b + (d ** (1/2)))/(2 * a)
        return print(x_1, x_2)
#square_equation(1, -2, 0)
#square_equation(1, 2, 1)
#square_equation(1, 1, 1) # ничего не вывеет, даже None
#square_equation(0, 1, 1) # после добавления проверки из комментария вначале # ZeroDivisionError: float division by zero на ноль делить нельзя Тут квадратное уравнение превратилось в линейное т.к. а = 0, но мне выдаёт ошибку(
'''

'''
# добавлена проверка а ровно нулю, если так то решается линейное уравнение
def square_equation(a: int, b: int, c: int):
    if a == 0:
        print(-c/b)
    else:
        d = b ** 2 - 4 * a * c
        if d == 0:
            x_1 = -b/(2 * a)
            return print(x_1)
        elif d > 0:
            x_1 = (-b - (d ** (1/2)))/(2 * a)
            x_2 = (-b + (d ** (1/2)))/(2 * a)
            return print(x_1, x_2)
#square_equation(1, -2, 0)
#square_equation(1, 2, 1)
#square_equation(1, 1, 1)
#square_equation(0, 1, 1) # output -1, т.к. решилось линейное уравнение
#square_equation(0, 0, 1) # после добавления проверки из комментария вначале # ZeroDivisionError: division by zero, уравнение получет вид 1 = 0, следовательно ошибка
'''

'''
# добавлена проверка если b не ровно нулю
def square_equation(a: int, b: int, c: int):
    if a == 0:
        if b != 0:
            print(-c/b)
    else:
        d = b ** 2 - 4 * a * c
        if d == 0:
            x_1 = -b/(2 * a)
            return print(x_1)
        elif d > 0:
            x_1 = (-b - (d ** (1/2)))/(2 * a)
            x_2 = (-b + (d ** (1/2)))/(2 * a)
            return print(x_1, x_2)
#square_equation(1, -2, 0)
#square_equation(1, 2, 1)
#square_equation(1, 1, 1)
#square_equation(0, 1, 1) # output -1, т.к. решилось линейное уравнение
#square_equation(0, 0, 1) # ничего т.к. не прошло проверку b
#square_equation(0, 0, 0) # после добавления проверки из комментария вначале # в консоль ниего не вывелось т.к. уровнение стало вида 0 = 0, а это и так истина. Но в лекции говорят про ошибку runtime error, но я хз
'''

'''
# добавил проверку при котором все переменные равны нулю, с ответом many soluions
def square_equation(a: int, b: int, c: int):
    if a == 0:
        if b != 0:
            return print(-c/b)
        if b == 0 and c == 0:
            return print('Many solutions')
    else:
        d = b ** 2 - 4 * a * c
        if d == 0:
            x_1 = -b/(2 * a)
            return print(x_1)
        elif d > 0:
            x_1 = (-b - (d ** (1/2)))/(2 * a)
            x_2 = (-b + (d ** (1/2)))/(2 * a)
            return print(x_1, x_2)
#square_equation(1, -2, 0)
#square_equation(1, 2, 1)
#square_equation(1, 1, 1)
#square_equation(0, 1, 1) # output -1, т.к. решилось линейное уравнение
#square_equation(0, 0, 1) # ничего т.к. не прошло проверку b
#square_equation(0, 0, 0) # Many solutions теперь всё работает
#square_equation(-5, 4, 1) # вывод 1.0 -0.2 а должно быть -0.2, 1
'''

'''
# добаил проверку переменных при дискриминанте боьше нуля, для корректного вывода
def square_equation(a: int, b: int, c: int):
    if a == 0:
        if b != 0:
            return print(-c/b)
        if b == 0 and c == 0:
            return print('Many solutions')
    else:
        d = b ** 2 - 4 * a * c
        if d == 0:
            x_1 = -b/(2 * a)
            return print(x_1)
        elif d > 0:
            x_1 = (-b - (d ** (1/2)))/(2 * a)
            x_2 = (-b + (d ** (1/2)))/(2 * a)
            if x_1 > x_2:
                return print(x_2, x_1)
            else:
                return print(x_1, x_2)
#square_equation(1, -2, 0)
#square_equation(1, 2, 1)
#square_equation(1, 1, 1)
#square_equation(0, 1, 1) 
#square_equation(0, 0, 1) 
#square_equation(0, 0, 0) 
# square_equation(-5, 4, 1) # -0.2 1.0
'''