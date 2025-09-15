'''
def main():
    n = input()
    n = n.split(' ')
    n = list(map(int, n))
    n.sort()
    return n[1]
'''

def main():
    n = list(map(int, input().split(' ')))
    n.sort()
    return n[1]


print(main())
