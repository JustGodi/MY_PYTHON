'''
def main():
    n = input()
    n = n.split(' ')
    n = list(map(int, n))
    n.sort()
    return n[1]
'''
'''
def n_logn():
    n = list(map(int, input().split(' ')))
    n.sort()
    return n[1]

print(n_logn())
'''
'''
def n():
    n = list(map(int, input().split(' ')))
    print(n)


    if n[0] > n[1] and n[0] > n[2]:
        del n[0]
    elif n[1] > n[0] and n[1] > n[2]:
        del n[1]
    elif n[2] > n[0] and n[2] > n[1]:
        del n[2]


    if n[0] < n[1]:
        x = n[1]
        return int(x)
    elif n[1] < n[0]:
        x = n[0]
        return int(x)

print(n())
'''


def find_avarage():
    list_of_nums = list(map(int, input().split(' ')))


    max_num = float('-inf')
    for num in list_of_nums:
        if num > max_num:
            max_num = num

    min_num = float('+inf')
    for num in list_of_nums:
        if num < min_num:
            min_num = num

    for num in list_of_nums:
        if min_num < num < max_num:
            return num
        else:
            continue


print(find_avarage())
















