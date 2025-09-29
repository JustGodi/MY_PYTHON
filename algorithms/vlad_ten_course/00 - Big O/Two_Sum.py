# https://leetcode.com/problems/two-sum/

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.
"""
:type nums: List[int]
:type target: int
:rtype: List[int]
"""


# четвертая попытка не получилась, посмотрел ответ, он выше
# четвёртая попытка, пытаюсь решить проблему из третьей попытки
'''def twoSum(nums: list, target: int) -> list:
    list_of_indexes = []
    for i in range(0, len(nums) - 1):
        print(f'До условия i: {i}')
        for n in range(0, len(nums) - 1):
            print(f'До условия n: {n}')
            result = nums[i] + nums[n]
            print(f'reSAULTL: {result}')
            if result == target:
                list_of_indexes.append(i)
                list_of_indexes.append(n)
            else:
                continue
        return list_of_indexes'''


# вариант от deepse seek, с рекурсивным вызовом, сложность по времени n^2б по памяти n
'''def twoSum(nums: list, target: int) -> list:
    def find_pair(i, j):
        # Базовый случай: дошли до конца списка
        if i >= len(nums) - 1:
            return []
        
        # Если j достиг конца, переходим к следующему i
        if j >= len(nums):
            return find_pair(i + 1, i + 2)
        
        # Проверяем текущую пару
        if nums[i] + nums[j] == target:
            return [i, j]
        
        # Рекурсивно проверяем следующую пару
        return find_pair(i, j + 1)
    
    # Начинаем с первой пары (0,1)
    return find_pair(0, 1)'''

'''    i = 0
    list_of_indexes = []
    result = 0
    for n in range(0, len(nums) - 1):
        result = nums[i] + nums[n]
        print(f'До условия i: {i}')
        print(f'До условия n: {n}')
        print(' ')
        print('------------------------------------')'''
'''            i += 1
            print(f'while i: {i}')
            print(f'while n: {n}')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print(' ')'''
'''if result == target:
            list_of_indexes.append(i)
            list_of_indexes.append(n)
            print(f'Во время условия i: {i}')
            print(f'Во время условия n: {n}')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print(' ')
            return list_of_indexes
        elif n == 6:
            i = i + 1
            print(f'else i: {i}')
            print(f'else n: {n}')
            continue'''



        # теперь если первй цикл не выполнился будет выполнятся второй, который должен взять первый элеент и проверить его сложение со всеми элементами, если сумма не будет найдена, то он должен взять второй элемент и сложить его со всеми из списка и так до конца списка




'''
# третья попытка, почти итог, но не проходит тест, где числа не стоят рядом
# тут уточнил у ии как получить на выходе лист компрехеншона
# список а не список с кортежем
def twoSum(nums: list, target: int) -> list:
    list_of_indexes = [num for i in range(0, len(nums) - 1)
                      if (nums[i] + nums[i+1]) == target
                      for num in [i, i + 1]]
    return list_of_indexes
'''
'''
# вторая попытка
# почти готовый компрехеншон, но задал вопрос ии
def twoSum(nums: list, target: int) -> list:
    list_of_indexes = [(i, i+1) for i in range(0, len(nums) - 1) if (nums[i] + nums[i+1]) == target]
    return list_of_indexes'''

'''
# первая попытка рабочего кода
def twoSum(nums: list, target: int) -> list:
    list_of_indexes = []
    for i in range(0, len(nums) - 1):
        if (nums[i] + nums[i+1]) == target:
            list_of_indexes.append(i)
            list_of_indexes.append(i+1)
            return list_of_indexes
'''

#решение с leetcode и deepseek
def twoSum(nums: list, target: int):
    # Внешний цикл перебирает все элементы как первый кандидат
    for i in range(len(nums)): # i - индекс первого числа
        # Внутренний цикл перебирает ВСЕ последующие элементы как второй кандидат
        for j in range(i + 1, len(nums)): #  j - индекс второго числа (только после i)
            #  Проверка суммы и возврат результата
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

'''print("Тест 1:", twoSum([3, 2, 3], 6))  # Должно быть [0, 2]

# Тест 2  
print("Тест 2:", twoSum([2, 7, 11, 15], 9))  # Должно быть [0, 1]

# Тест 3
print("Тест 3:", twoSum([3, 3], 6))  # Должно быть [0, 1]'''


lst = [2, 7, 11, 15]
target = 9
print(twoSum(lst, target))