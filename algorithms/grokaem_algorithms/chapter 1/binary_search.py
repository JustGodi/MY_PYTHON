def binary_search(lst, item):
    low = 0
    high = len(lst) - 1 # В переменных low and high хранятся границы той части списка, в которой выполняется поиск

    while low <= high: # пока эта часть не сократится до одного элемента ->
        mid = (low + high) // 2 # -> проверяем средний элемент
        guess = lst[mid] # -> проверяем средний элемент
        if guess == item: # если значение найлено
            return mid № вернуть это знаение
        elif guess > item: # если значение больше искомого
            high = mid - 1 # верхняя граница становится на одно меньше от среднего
        else: # если значение меньше искомого
            low = mid + 1 # то нижняя граница становится на одно меньше от среднего
    return None

lst = list(range(1, 100))

item = 99
print(binary_search(lst, item))