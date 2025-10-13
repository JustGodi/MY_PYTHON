



            # ЗАДАЧА D. ОТБОРОЧНЫЙ КОНТЕСТ


        # Вася составляет отборочный контест. Всего есть N задач, Васе нужно выбрать К из них, чтобы задачи покрывали как можно больше различных тем.

        # я блять так и не понял смысл этой задачи


'''n, k = map(int, input().split()) # ситывание данных
problems = list(map(int, input().split())) # ситывание данных
uniq_problems = set(problems) # уникальные задачи - множество
tour = list(uniq_problems) # превратил множество в массив
if len(tour) < k: # если длина тура( мало на контест задач)
    for problem in problems: # пробегаемся по всем задачам
        if problem not in uniq_problems: # если задача не содержится в множестве(если вхождение не первое)
            tour.append(problem) # то мы добавляем её в тур
        else: # 
            uniq_problems.discard(problem) # если первое вхождение то убираю из множества задачу чтобы следующее ее вхождение интерпретировалосб как не первое
print(*tour[:k]) # вывожу первые k задач из тура
'''

def main():
    n, k = map(int, input().split())
    problems = list(map(int, input().split()))

    uniq_problems = set(problems)
    tour = list(uniq_problems)

    if len(tour) < k:
        for problem in problems:
            if problem not in uniq_problems:
                tour.append(problem)
            else: 
                uniq_problems.discard(problem)
    print(*tour[:k])
main()
