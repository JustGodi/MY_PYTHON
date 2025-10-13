# Ограничение времени	1 секунда
# Ограничение памяти	256 Мб
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt



# Группа школьников решила сходить в поход вдоль Москвы-реки. У Москвы-реки существует множество притоков, которые могут впадать в неё как с правого, так и с левого берега.

# Школьники хотят начать поход в некоторой точке на левом берегу и закончить поход в некоторой точке на правом берегу, возможно, переправляясь через реки несколько раз. Как известно, переправа как через реку, так и через приток представляет собой определённую сложность, поэтому они хотят минимизировать число совершённых переправ. Переправляться через реку и притоки можно только перпендикулярно их течению (т.е. нельзя переправиться через реку и приток «по диагонали»).

# Школьники заранее изучили карту и записали, в какой последовательности в Москву-реку впадают притоки на всём их маршруте.

# Помогите школьникам по данному описанию притоков определить минимальное количество переправ, которое им придётся совершить во время похода.

# Формат ввода

# Единственная строка содержит описание Москвы-реки между начальной и конечной точкой похода. Длина строки не превосходит 200 символов.

# Каждый символ строки может быть одной из трёх латинских букв L, R или B. Буква L означает, что очередной приток впадает в реку с левого берега, R — приток впадает в реку с правого берега и B — притоки впадают с обоих берегов реки в одном месте. Поход начинается на левом берегу перед описанной частью реки и заканчивается на правом берегу после описанной части.

# Формат вывода

# Выведите одно целое число — минимальное количество переправ.

# Пример

# Ввод

# LLBLRRBRL

# Вывод

# 5







'''
l = input()
prev = [0] * (2 * len(l))
count = 0
flag = 'L'

#print(flag, count)

for i in range(0, len(l)):
    prev[i] = l[i]
    print(prev[i])

for i in range(0, len(l)):
    print(prev[i])
for i in range(0, len(l)):
    print(f'Текущая i вначале каждого цикла:  {i}, буква ровна: {prev[i]}')
    if flag == 'L' and prev[i] == prev[i + 1] == 'L':
        flag = 'R'
        count += 1
        print('flag = li = li+1 = L', 'space', flag, count)
    if flag == 'R' and prev[i] == prev[i + 1] == 'R':
        flag = 'L'
        count += 1
        print('flag = li = li+1 = R', 'space', flag, count)
    if flag == prev[i + 1] == 'L' and prev[i + 2] == 'R':
        count += 1
    if flag == prev[i + 1] == 'R' and prev[i + 2] == 'L':
        count += 1
    if prev[i] == prev[i + 2] and prev[i + 1] == 'B':
        count += 1
        print('li = li + 2 and li + 1 = B', 'space', flag, count)
    if flag == prev[i + 1] == 'L':
        count += 1
        flag = 'R'
    if flag == prev[i + 1] == 'R':
        count += 1
        flag = 'L'
    


print(count)
'''











'''
    if flag == 'R' and l[i + 1] == 'B' and l[i + 2] == 'L':
        count += 1
        print('flag = R; li+1 = B, li+2 = L', flag, count)
    if flag == 'L' and l[i + 1]== 'B' and l[i + 2] == 'R':
        count += 1
        print('flag = L; li+1 = B, li+2 = R', flag, count)
    if flag == l[i] == 'L' and l[i + 1] == 'R':
        flag = 'R'
        count += 1
        print('flag = li = L; li+1 = R', flag, count)
    if flag == l[i] == 'L' and l[i + 1] == 'L':
        flag = 'R'
        count += 1
        print('flag = L; li+1 = L', flag, count)
'''
# print(count)







'''if l[0] == 'L' and l[1] == 'L':
    flag = 'R'
    count += 1

for let in l:
    prev.append(let)
for i in range(0, len(l) - 1):
    if l[i] == l[i + 1] == 'L':
        flag = 'R'
        count += 1
    elif l[i] == l[i + 1] == 'R':
        continue
    if l[i + 1] == 'B' and l[i + 2] =='''


'''for let in l:
    print(let)
    prev.append(let)
    if let == prev[n]:
        print(n)
        n += 1
        print(n)
        continue'''

#print(n)
#print(prev)
#print(flag)

'''
def main():

    l = input()
    prev = [0] * (2 * len(l))
    count = 0
    flag = 'L'

    for i in range(0, len(l)):
        prev[i] = l[i]

    for i in range(0, len(l)):
        if flag == 'L' and prev[i] == prev[i + 1] == 'L':
            flag = 'R'
            count += 1
        if flag == 'R' and prev[i] == prev[i + 1] == 'R':
            flag = 'L'
            count += 1
        if prev[i] == prev[i + 2] and prev[i + 1] == 'B':
            count += 1
        if flag == prev[i + 1] == 'L':
            count += 1
            flag = 'R'
        if flag == prev[i + 1] == 'R':
            count += 1
            flag = 'L'
        if flag == 'R' and prev[i + 1] == 'R':
            count += 1
        if flag == 'R' and prev[i + 1] == 'R':
            count += 1
            flag == 'L'
        if flag == 'L' and prev[i + 1] == 'L':
            count += 1
            flag == 'R' 
    print(count)

#main()
'''










'''
river = input()
n = len(river)

dp = [[0] * (n + 1) for _ in range(2)]

# левый берег
dp[0][0] = 0
# правый берег
dp[1][0] = 1

for i in range(1, n+1):
    step = river[i-1]

    if step == 'L':
        dp[0][i] = min(dp[0][i-1], dp[1][i-1]) + 1
        dp[1][i] = min(dp[0][i-1] + 1, dp[1][i-1])
    elif step == 'R':
        dp[0][i] = min(dp[0][i-1], dp[1][i-1] + 1)
        dp[1][i] = min(dp[0][i-1], dp[1][i-1]) + 1
    else:
        dp[0][i] = min(dp[0][i-1], dp[1][i-1] + 1) + 1
        dp[1][i] = min(dp[1][i-1], dp[0][i-1] + 1) + 1


print(min(dp[1][n], dp[0][n] + 1))
'''