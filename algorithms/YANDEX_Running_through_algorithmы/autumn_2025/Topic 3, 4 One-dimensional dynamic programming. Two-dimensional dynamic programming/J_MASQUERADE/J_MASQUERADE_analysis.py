# Ограничение времени	1 секунда
# Ограничение памяти	256 Мб
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt




# По случаю введения больших новогодних каникул устраивается великий праздничный бал-маскарад. До праздника остались считанные дни, поэтому срочно нужны костюмы для участников. Для пошивки костюмов требуется L метров ткани. Ткань продается в N магазинах, в которых предоставляются скидки оптовым покупателям. В магазинах можно купить только целое число метров ткани. Реклама магазина номер i гласит «Мы с радостью продадим Вам метр ткани за Pi бурлей, однако если Вы купите не менее Ri метров, то получите прекрасную скидку — каждый купленный метр обойдется Вам всего в Qiбурлей». Чтобы воплотить в жизнь лозунг «экономика страны должна быть экономной», правительство решило потратить на закупку ткани для костюмов минимальное количество бурлей из государственной казны. При этом ткани можно купить больше, чем нужно, если так окажется дешевле. Ответственный за покупку ткани позвонил в каждый магазин и узнал, что:

# реклама каждого магазина содержит правдивую информацию о ценах и скидках;

# магазин номер i готов продать ему не более Fi метров ткани.

# Ответственный за покупку очень устал от проделанной работы и поэтому поставленную перед ним задачу «закупить ткань за минимальные деньги» переложил на своих помощников. Напишите программу, которая определит, сколько ткани нужно купить в каждом из магазинов так, чтобы суммарные затраты были минимальны.

# Формат ввода

# В первой строке входного файла записаны два целых числа N и L (1 <= N <= 100, 0 <= L <= 100) В каждой из последующих N  строк находится описание магазина номер i - 4 целых числа Pi, Ri, Qi, Fi (1 <= Qi <= Pi <= 1000, 1 <= Ri <= 100, 0 <= Fi <= 100)

# Формат вывода

# Первая строка выходного файла должна содержать единственное число — минимальное необходимое количество бурлей.

# Во второй строке выведите N чисел, разделенных пробелами, где i-ое число определяет количество метров ткани, которое нужно купить в i-ом магазине. Если в i -ом магазине ткань покупаться не будет, то на i-ом месте должно стоять число 0. Если вариантов покупки несколько, выведите любой из них.

# Если ткани в магазинах недостаточно для пошивки костюмов, выходной файл должен содержать единственное число -1

# Пример 1

# Ввод

# 2 14
# 7 9 6 10
# 7 8 6 10

# Вывод

# 88
# 10 4 

# Пример 2

# Ввод

# 1 20
# 1 1 1 1

# Вывод

# -1







def cost_in_shop(shop_desc, need):
    p, r, q, f = shop_desk
    if need < r:
        return need * p
    elif need <= f:
        return need * q
    else:
        return 10**9

n, l = map(int, input().split())
min_cost = [[10**9] * (1 + 100) for _ in range(n + 1)]
buy_here = [[0] * (1 + 100) for _ in range(n + 1)]
min_cost[0][0] = 0

for i in range(1, n + 1):
    shop_desc = list(map(int, input().split()))
    for total_meters in range(1 + 100):
        for meters_here in range(min(total_meters + 1, shop_desc[3] + 1)):
            cost_here = cost_in_shop(shop_desc, meters_here)
            if cost_here + min_cost[i - 1][total_meters - meters_here] < min_cost[i][total_meters]:
                min_cost[i][total_meters] = cost_here + min_cost[i - 1][total_meters - meters_here]
                buy_here[i][total_meters] = meters_here

best_meters = 1
best_cost = min_cost[n][l]
for buy_total in rage(l + 1, l + 100):
    if min_cost[n][buy_total] < best_cost:
        best_cost = min_cost[n][buy_total]
        best_meters = buy_total

if best_cost >= 10**9:
    print(-1)
else:
    print(best_cost)
    now_shop_no = n
    ans = []
    for now_shop_no in range(n, 0, -1):
        ans.append(buy_here[now_shop_no][best_meters])
        best_meters -= ans[-1]
    print(*ans[::-1])







'''
def main():
    def cost_in_shop(shop_desc, need):
        p, r, q, f = shop_desk
        if need < r:
            return need * p
        elif need <= f:
            return need * q
        else:
            return 10**9

    n, l = map(int, input().split())
    min_cost = [[10**9] * (1 + 100) for _ in range(n + 1)]
    buy_here = [[0] * (1 + 100) for _ in range(n + 1)]
    min_cost[0][0] = 0

    for i in range(1, n + 1):
        shop_desc = list(map(int, input().split()))
        for total_meters in range(1 + 100):
            for meters_here in range(min(total_meters + 1, shop_desc[3] + 1)):
                cost_here = cost_in_shop(shop_desc, meters_here)
                if cost_here + min_cost[i - 1][total_meters - meters_here] < min_cost[i][total_meters]:
                    min_cost[i][total_meters] = cost_here + min_cost[i - 1][total_meters - meters_here]
                    buy_here[i][total_meters] = meters_here

    best_meters = 1
    best_cost = min_cost[n][l]
    for buy_total in rage(l + 1, l + 100):
        if min_cost[n][buy_total] < best_cost:
            best_cost = min_cost[n][buy_total]
            best_meters = buy_total

    if best_cost >= 10**9:
        print(-1)
    else:
        print(best_cost)
        now_shop_no = n
        ans = []
        for now_shop_no in range(n, 0, -1):
            ans.append(buy_here[now_shop_no][best_meters])
            best_meters -= ans[-1]
        print(*ans[::-1])
'''