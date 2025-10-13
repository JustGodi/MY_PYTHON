def main():
    n = int(input())
    dp = [0] * (n*3)
    dp[0] = 1
    dp[1] = 2
    dp[2] = 4
    if n == 1 or n == 2 or n == 3:
        print(dp[n - 1])
    else:
        for i in range(3, n):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
        print(dp[n - 1])
main()