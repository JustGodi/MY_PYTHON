# Ограничение времени 1 секунда

# Ограничение памяти 256 Мб

# Ввод стандартный ввод или input.txt

# Вывод стандартный вывод или output.txt

# Вася и Маша ходили в лес и собрали n грибов, для каждого гриба известен его вес ai. Они выложили их в один ряд и решили делить следующим образом: первый гриб берёт Вася, второй — Маша, третий — Вася, четвёртый — Маша и т.д.

# ВСЁ ТЗ В ONENOTE, РАЗДЕЛ:

# AUTUMN 2025 YANDEX ALGORITMS TRAINING

# TASKS Topic_1, 2 Testing and special cases. Sets and dictionaries

# Вася очень любит грибы и не очень любит Машу. Количество радости Васи равно разности суммарного веса грибов, доставшихся Васе, и суммарного веса грибов, доставшихся Маше. Т.е. радость вычисляется по формуле: (алгебраическая сумма) (-1)^(i-1)*ai=a1 - a2 + a3 - ...

# Маша отвлеклась на минутку, и за это время Вася может выбрать любые два гриба и поменять их местами (а может и не менять). Определите максимальную радость Васи, которую можно достичь не более чем одним обменом.

# Формат ввода

# В первой строке содержится одно натуральное число n - количество грибов (2 <= n <= 10^5)

# Во второй строке содержится n чисел ai - вес грибов (1 <= ai <= 1000)

# Формат вывода

# Выведите максимальную радость Васи.

# Пример 1

# Inptut

# 2

# 1 2

# output

# 1

# Пример 2

# Input

# 3

# 2 2 2

# output

# 2

# Example 3

# Input

# 11

# 4 10 7 5 4 5 3 8 3 2 5
'''
def main():
    pass
'''
'''
n = int(input())
a_list = list(map(int, input().split()))

vasya_a = []
masha_a = []

vasya_a_sum = 0
masha_a_sum = 0

for idx, a in enumerate(a_list):
    if idx % 2 == 0:
        vasya_a.append(a)
        vasya_a_sum += a
    else:
        masha_a.append(a)
        masha_a_sum += a

vasya_a.sort(reverse=True)
masha_a.sort()

if vasya_a[-1] >= masha_a[-1]:
    print(vasya_a_sum - masha_a_sum)
else:
    print((vasya_a_sum - vasya_a[-1] + masha_a[-1]) - (masha_a_sum - masha_a[-1] + vasya_a[-1]))
'''
'''
def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    vasya_a = []
    masha_a = []
    vasya_a_sum = 0
    masha_a_sum = 0
    for idx, a in enumerate(a_list):
        if idx % 2 == 0:
            vasya_a.append(a)
            vasya_a_sum += a
        else:
            masha_a.append(a)
            masha_a_sum += a
    vasya_a.sort(reverse=True)
    masha_a.sort()
    if vasya_a[-1] >= masha_a[-1]:
        return vasya_a_sum - masha_a_sum
    else:
        return ((vasya_a_sum - vasya_a[-1] + masha_a[-1]) - (masha_a_sum - masha_a[-1] + vasya_a[-1]))

print(main())
'''
'''
def main():
    n = int(input())
    a_list = list(map(int, input().split()))

    vasya_a_sum, masha_a_sum = 0, 0

    min_vasya, max_masha = 1000, 0
    for idx in range(n):
        a = a_list[idx]

        if idx % 2 == 0:
            min_vasya = min(min_vasya, a)
            vasya_a_sum += a
        else:
            max_masha = max(max_masha, a)
            masha_a_sum += a

    if min_vasya >= max_masha:
        return vasya_a_sum - masha_a_sum

    return (vasya_a_sum - min_vasya + max_masha) - (masha_a_sum - max_masha + min_vasya)

print(main())
'''