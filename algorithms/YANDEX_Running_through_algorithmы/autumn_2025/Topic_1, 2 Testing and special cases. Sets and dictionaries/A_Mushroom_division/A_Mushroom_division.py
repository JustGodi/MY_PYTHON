def main():
    n = int(input())
    a_list = list(map(int, input().split()))

    vasya_a_sum, masha_a_sum = 0, 0

    min_vasya, max_masha = 1000, 0
    for idx in range(n):
        a = a_list[idx]

        if idx % 2 == 0:
            min_vasya = min(min_vasya, a)
            vasya_a_sum += a
        else:
            max_masha = max(max_masha, a)
            masha_a_sum += a

    if min_vasya >= max_masha:
        return vasya_a_sum - masha_a_sum

    return (vasya_a_sum - min_vasya + max_masha) - (masha_a_sum - max_masha + min_vasya)

print(main())