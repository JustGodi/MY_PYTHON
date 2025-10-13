'''. | O | X | O | X | O
O | X | X | . | O | .
X | X | O | O | X | X
. | . | O | . | . | O
O | O | X | X | . | X'''

# Ограничение времени    3 секунды
# Ограничение памяти    256 Мб
# Ввод    стандартный ввод или input.txt
# Вывод    стандартный вывод или output.txt

# На большом игровом поле кто-то играл в крестики-нолики (возможно, не соблюдая правила). Цель игры — выстроить пять одинаковых фигур по горизонтали, вертикали или диагонали. Определите, найдется ли такая пятёрка фигур или нет.

# Формат ввода

# В первой строке ввода записаны числа n, m символов ”X”, ”O” или ”.”, которые задают крестик, нолик и пустую клетку, соответственно. ”X” и ”O” — заглавные английские буквы

# Формат вывода

# Выведите Yes, если найдется пять одинаковых фигур подряд, и No в противном случае.

# Пример 1

# input

# 5 6
# .OXOXO
# OXX.O.
# XXOOXX
# ..O..O
# OOXX.X

# output

# yes

# Пример 2

# input

# 2 6
# XX....
# .XXXXX

# output

# yes



            # Я БЛИН ТАК И НЕ ПОНЯЛ КАК В ТЕСТАХ ЗАПУСТИТЬ ЭТОТ КОД ДЛЯ РЕШЕНИЯ АЛГОРИТМА


            # ЗАДАЧА G. ПЯТЬ ПОДРЯД

        # Дано поле для игры в бесконечные крестики-нолики. Определить, есть ли 5 подряд одинаковых фигур по горизонтали, вертикали или диагонали




fin = open('input.txt', 'r') # чтение данных
n, m = map(int, fin.readline().split()) # 
field = fin.readlines() # 
fin.close() # 

di = [-1, -1, -1, 0] # массивы сдвигов
dj = [-1, 0, 1, -1] # массивы сдвигов
flag = False # флаг который говорит нашли ли мы решение или нет

for i in range(n): # проходим по всему полю
    for j in range(m): # проходим по всему полю
        if field[i][j] == '.': # если там тока
            continue # то пропускаем её и продолжаем
        for direction in range(len(di)): # для перебираем возможные четыре направления
            now_flag = True # говорим что сейчас мы нашли решение
            now_i = i # передаём текущие координаты
            now_j = j # передаём текущие координаты
            for steps in range(4): # проходимся по всем шагам направлений
                now_i += di[direction] # на каждом шаге сдвигаемся по каждому массиву сдвигов
                now_j += dj[direction] # на каждом шаге сдвигаемся по каждому массиву сдвигов
                if not (0 <= now_i < n and 0 <= now_j < m) or field[now_i][now_j] != field[i][j]: # если вышли за пределы поля или там стоит не такая фигура как у нас
                    now_flag = False # передаём флаг фолз, что означает что решение не найдено
                    break # прервать цикл
        flag = flag or now_flag #  передаём глобальному флагу текущее значение (старое значение флага или новое). Если хоть раз был успех то значение переменной будет истинно

if flag: # если флаг труе, что означает что нашли совпадение из пяти в ряд
    print('Yes') # вывести да
else: # в противном случае
    print('No') # нет



'''
def main():
    fin = open('input.txt', 'r')
    n, m = map(int, fin.readline().split())
    field = fin.readlines()
    fin.close()

    di = [-1, -1, -1, 0]
    dj = [-1, 0, 1, -1]
    flag = False

    for i in range(n):
        for j in range(m):
            if field[i][j] == '.':
                continue
            for direction in range(len(di)):
                now_flag = True
                now_i = i
                now_j = j
                for steps in range(4):
                    now_i += di[direction]
                    now_j += dj[direction]
                    if not (0 <= now_i < n and 0 <= now_j < m) or field[now_i][now_j] != field[i][j]:
                        now_flag = False
                        break
            flag = flag or now_flag

    if flag:
        print('Yes')
    else:
        print('No')
'''

'''

n, m = map(int, fin.readline().split())
field = fin.readlines()
fin.close()

di = [-1, -1, -1, 0]
dj = [-1, 0, 1, -1]
flag = False

for i in range(n):
    for j in range(m):
        if field[i][j] == '.':
            continue
        for direction in range(len(di)):
            now_flag = True
            now_i = i
            now_j = j
            for steps in range(4):
                now_i += di[direction]
                now_j += dj[direction]
                if not (0 <= now_i < n and 0 <= now_j < m) or field[now_i][now_j] != field[i][j]:
                    now_flag = False
                    break
        flag = flag or now_flag

if flag:
    print('Yes')
else:
    print('No')
'''