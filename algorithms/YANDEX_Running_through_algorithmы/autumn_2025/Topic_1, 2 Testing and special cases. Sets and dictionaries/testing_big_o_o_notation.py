# Алгоритм флойда для поиска кротчайших путей для любой пары вершин в графе
'''
dist = []
n = int(input())
for i in range(n):
    dist.append(list(map(int, input().split())))
for via in range(n):
    for fr in range(n):
        for to in range(n):
            dist[fr][to] = min(matr[fr][to], matr[fr][via] + matr[via][to])
for i in range(n):
    if dist[i][i] < 0:
        print(i)
'''

'''
# Big O, O notation
#
dist = []
n = int(input())
# две строчки сверху работают зa O(1)

#
for i in range(n): # эта строчка цикла работает за O(n)
    dist.append(list(map(int, input().split()))) # эта строчка цикла работает за O(n)
# обе строчки кода(весь цикл) сверху работают за O(n^2)

#
for via in range(n): # эта строчка цикла работает за O(n)
    for fr in range(n): # эта строчка цикла работает за O(n)
        for to in range(n): # эта строчка цикла работает за O(n)
            dist[fr][to] = min(matr[fr][to],
            matr[fr][via] + matr[via][to]) # эта строчка цикла работает за O(1)
#все строчки кода(весь цикл) сверху работают за O(n^3)

#
for i in range(n): # эта строчка цикла работает за O(n)
    if dist[i][i] < 0: # эта строчка цикла работает за O(1)
        print(i) # эта строчка цикла работает за O(1)
#весь цикл выполняется за O(n)
'''