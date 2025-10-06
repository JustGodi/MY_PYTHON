# Ограничение времени    1 секунда
# Ограничение памяти    256 Мб
# Ввод    стандартный ввод или input.txt
# Вывод    стандартный вывод или output.txt

# На табло было написано число n. Каждую секунду к числу прибавляется последняя цифра этого числа. Определите, какое число будет отображаться на табло через k секунд

# Формат ввода

# В единственной строке записаны два числа n, k (0 <= n, k <= 10^9) — начальное число и количество секунд соответственно.

# Формат вывода

# Выведите одно число x , которое будет отображаться на табло через k секунд

# Пример 1

# input

# 1 10

# output

# 44

# Пример 2

# input

# 5 1

# output

# 10



def main():
    n, k = list(map(int, input().split()))

    base = (n // 10) * 10
    num = n - base
    loop = [2, 4, 8, 16]

    if num == 0 or k == 0:
        return n
    
    if num == 5:
        return n + 5
  
    while num != 2 and k != 0:
        n += num
        k -= 1

        base = (n // 10) * 10
        num = n - base

    result = n
  
    if num == 2:
        twenty_count = k // 4
        over_loop = k % 4

    result = base + twenty_count * 20 + loop[over_loop]

    return result



'''
    base = (n // 10) * 10
    num = n - base

    if num == 0 or k == 0:
        return n

    if num == 5:
        return n + 5

    while n -(n // 10) * 10 != 2 or k != 0:
        base = (n // 10) * 10
        num = n - base

        n += num
        k -= 1


    loop = [2, 4, 8, 16]

    result = n



    if num == 1:
        num = 2
        k -= 1

    if num == 2:
        tw_count = k // 4
        over_loop = k

        result = base + tw_count * 20 + loop[over_loop]
    return result
'''
print(main())



'''
    for i in range(k):
        n_str = str(n)
        n = n + int(n_str[-1])
    return n
'''

#print(main())