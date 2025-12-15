# пример бинароного посика, когда слева всё было плохо, а с определённого момента стало хорошо, обязтельное условие то, что должно быть минимум один хороший исход
# это поиск первого хорошего числа
'''
def l_bin_search(l, r, check, check_params): # 
    while l < r: # 
        m = (l + r) // 2 # 
        if check(m, check_params): # 
            r = m # 
        else: # 
            l = m + 1 # 

    return l # 


# это поиск последнего хорошего числа
def r_bin_search(l, r, check, check_params): # 
    while l < r: # 
        m = (l + r + 1) // 2 # 
        if check(m, check_params): # 
            l = m # 
        else: # 
            r = m - 1 # 
        
    return l #
'''

# ршение задачи с родителями в правляющем совете школы
'''
def l_bin_search(l, r, check, check_params):
    while l < r:
        m = (l + r) // 2
        if check(m, check_params):
            r = m
        else:
            l = m + 1

    return l

def check_end_ownment(m, params): # функция проверки чт овсё хорошо
    n, k = params

    return (k + m) * 3 >= n + m
'''


#  решение задачки с подготовкой к собеседованию
'''
def l_bin_search(l, r, check, check_params):
    while l < r:
        m = (l + r) // 2
        if check(m, check_params):
            r = m
        else:
            l = m + 1

    return l

def check_problem_count(days, params):
    n, k = params
    return (k + (k + days - 1)) * days // 2 >= n
'''

'''
def r_bin_search(l, r, check, check_params):
    while l != r
    m = (l + r + 1) // 2
    if check(m, check_params):
        l = m
    else:
        r = m - 1

def check_stickers(size, params):
    n, w, h = params
    return (w // size) * (h // size) >= n
'''


# тут не написан бинпоиск, только код после него
'''
def check_is_ge(index, params):
    seq, x = prarams
    return seq[index] >= x

def find_first_ge(seq, x):
    ans = l_bin_search(0, len(seq) - 1, check_is_ge, (seq, x))
    if seq[ans] < x:
        return len(seq)
    return ans
'''

# задача о ежемесячном проценте
'''
def check_monthly_perc(m_perc, y_perc):
    m_sum = 1 + m_perc / 100
    y_sum = 1 + y_perc / 100
    return m_sum ** 12 >= y_sum

def f_bin_search(l, r, eps, check, check_params):
    while l + eps < r:
        m = (l + r) / 2
        if check(m, check_params):
            r = m
        else:
            l = m
    return l

x = 12
eps = 0.0001
m_perc = f_bin_search(0, x, eps, check_monthly_perc, x)
print(m_perc)
'''

# задача об аннуитетном платеже

def check_credit(m_pay, params):
    periods, credit_sum, m_perc = params
    for i in range(periods):
        perc_pay = credit_sum * (m_perc / 100)
        credit_sum -= m_pay - perc_pay
    return credit_sum <= 0

def f_bin_search(l, r, eps, check, check_params):
    while l + eps < r:
        m = (l + r) / 2
        if check(m, check_params):
            r = m
        else:
            l = m
    return l

eps = 0.01
m = 10000000
n = 300
monthly_pay = f_bin_search(0, m, eps, check_credit, (n, m, m_perc))
print(monthly_pay)