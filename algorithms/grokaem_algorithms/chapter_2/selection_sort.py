def find_smallest(arr):
    # функция ищет наименьший элемент массива(списка)
    smallest = arr[0] # по дефолту задаётся нулевой элемент списка, после чего если будет найден элемент меньше то он присвоется в эту переменную
    smallest_index = 0 # соответственно нулевой индекс нулевого элемента, задается тоже по дефолту но потом менется на индекс числа которое окажется меньше smallest, если такое вообще будет
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

# теперь на основании этой функции можно создать сортировку выбором:

def selection_sort(arr):
    new_arr = [] # сюда будут добавлятся элементы в порядке убывания, при помощи метода поп куда задаётся индекс наименьшего числа из списка из функции find_smallest
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr

print(selection_sort([5, 3, 6, 2, 10]))
lst = [3, 2, 1, 9, 0, 5, 1]
print(selection_sort(lst))
