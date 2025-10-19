# Ограничение времени	1 секунда
# Ограничение памяти	256 Мб
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt





# У Васи на клавиатуре не работает клавиша пробел. Поэтому все тексты он теперь набирает слитно. Напишите программу, которая будет разделять набранный Васей текст на слова из данного словаря.

# Формат ввода

# Сначала на вход программы поступает текст, введенный Васей — одна строка из не более чем 100 латинских строчных букв.

# В следующей строке входных данных задается значение N - количество слов в словаре (N - натуральное число, не превосходящее 2000)

# В следующих N строках записаны слова из словаря — по одному слову в строке, каждое слово содержит не более 20 латинских строчных букв. Слова записаны в алфавитном порядке.

# Формат вывода

# Выведите Васин текст с пробелами между словами (пробел после последнего слова допустим). Если возможно несколько вариантов разбиения строки на слова, выведите любой из них. Гарантируется, что хотя бы один способ разбиения строки на словарные слова существует.

# Пример

# Ввод

# whatcanido
# 6
# a
# an
# can
# do
# i
# what

# Вывод

# what can i do 

# решение от Серёжи

'''
def main(string, word_list):
    n = len(string)
    dp = [False] * (n + 1)
    prev_word = [None] * (n + 1)

    dp[0] = True
    
    for i in range(n):
        if not dp[i]:
            continue

        for word in word_list:
            word_len = len(word)
            if i + word_len <= n and string[i:i + word_len] == word:
                dp[i + word_len] = True
                prev_word[i + word_len] = word

    result = []
    pos = n
    while pos > 0:
        word = prev_word[pos]
        result.append(word)
        pos -= len(word)

    return ' '.join(result[::-1])


if __name__ == '__main__':
    word_list = []
    with open('input.txt') as f:
        string = f.readline().strip()
        n = int(f.readline().strip())
        for _ in range(n):
            word_list.append(f.readline().strip())

    print(main(string, word_list))
'''



s = '#' + input() # добавлена решётка чтобы нумерация начиналась с единицы
s_len = len(s) # 
poss_end = [False] * s_len # массив может ли здесь закончится строка тру или фолз
prev_word = [''] * s_len # список дл хранения слов которые совпали
poss_end[0] = True # инициализация, начальный/базовый элемент, который совпадает с решёткой
words = set() #
n = int(input()) # 
max_len = 0 # 

for i in range(n): # 
    word = input() # 
    max_len = max(max_len, len(word)) # посчитал максимальную длину слова
    words.add(word) # добавил в множество


for i in range(1, s_len): # иду по всем позициям строки начиная с единицы
    for j in range(min(max_len, i)): # смотрюсколько последних сиволов нужно взять, если я рассматриваю подстроку из трёх букв, то нет смысла искать 4 буквы в строке
        if poss_end[i - j - 1] and s[i - j:i + 1] in words: # если можно закончить в токе(poss_end), т.е. поствить туда тру что означает что слово совпадает, и слово(подстрока/срез) содержится в множестве
            poss_end[i] = True # то можно поставить тру 
            prev_word[i] = s[i - j:i + 1] # и предыдущее слово ровняется тому что мы вырезали  
            break # цикл находит первое попавшееся и выходит

now = s_len - 1 # запоминаю позиуию из которой я буду восстанавливать
ans = [] # список для слов
while now > 0: # пока позиция больше нуля
    ans.append(prev_word[now]) # я добавляю слово, которое хранится в prev_word, 
    now -= len(prev_word[now]) # из текущей позиции вычитаю длину слова
print(*ans[::-1]) # ответ вывожу задам напеёд





'''
def main():
    s = '#' + input()
    s_len = len(s)
    poss_end = [False] * s_len
    prev_word = [''] * s_len
    poss_end[0] = True
    words = set()
    n = int(input())
    max_len = 0

    for i in range(n):
        word = input()
        max_len = max(max_len, len(word))
        words.add(word)


    for i in range(1, s_len):
        for j in range(min(max_len, i)):
            if poss_end[i - j - 1] and s[i - j:i + 1] in words:
                poss_end[i] = True
                prev_word[i] = s[i - j:i + 1]
                break

    now = s_len - 1
    ans = []
    while now > 0:
        ans.append(prev_word[now])
        now -= len(prev_word[now])
    print(*ans[::-1])
'''