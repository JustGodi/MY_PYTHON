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
        del n[0]
        return n[0]
    elif n[1] < n[0]:
        del n[1]
        return n[0]
    print(n)

print(n())
'''


def n():
    n = list(map(int, input().split(' ')))

















