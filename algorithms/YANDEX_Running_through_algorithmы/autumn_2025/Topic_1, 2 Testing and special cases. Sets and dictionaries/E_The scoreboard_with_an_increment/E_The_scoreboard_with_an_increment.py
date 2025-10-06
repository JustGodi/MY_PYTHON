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