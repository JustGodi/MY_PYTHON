# https://leetcode.com/problems/two-sum/

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.
"""
:type nums: List[int]
:type target: int
:rtype: List[int]
"""

# четвёртая попытка, пытаюсь решить проблему из третьей попытки
'''def twoSum(nums: list, target: int) -> list:
    list_of_indexes = []
    for i in range(0, len(nums) - 1):
        if (nums[i] + nums[i+1]) == target:
            list_of_indexes.append(i)
            list_of_indexes.append(i+1)
    if not list_of_indexes:'''
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


lst = [1,2,3]
target = 9

print(twoSum(lst, target))