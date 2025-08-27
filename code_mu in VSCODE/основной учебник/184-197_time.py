        # Работа с датами в Python

    # Для работы с датами в Python необходимо импортировать соответствующие модули. Делается это с помощью специальной инструкции import, после которой пишется имя модуля. Импорт записывается в самой верхней строке файла.

import datetime
import calendar
import time
import math

    # 184

    # Чтобы вывести дату, к импортированному модулю следует применить специальный метод .date В его параметрах задаются год, месяц, день. Для удобства полученную дату запишем в переменную res:
'''
res = datetime.date(2025, 12, 31)
print(res, type(res))


    # По сути теперь в переменной res хранится объект, содержащий дату. Он полезен тем, что из него можно вывести более подробные характеристики даты: день, месяц и год и т.д. Для этого только следует обратится к его свойствам - day, month, year:

print(res.day)
print(res.month)
print(res.year)
'''

# 1 Задайте переменной birthdate дату рождения пользователя. Затем выведите ее в формате год-месяц-день.
'''
birthday = datetime.date(2000, 4, 5)
print(birthday)
'''

# 2 Модифицируйте предыдущую задачу так, чтобы вывести только год рождения пользователя.
'''
birthday = datetime.date(2000, 4, 5)
print(birthday.year)
'''

# 3 Выведите из birthdate день, в который родился пользователь.
'''
birthday = datetime.date(2000, 4, 5)
print(birthday.day)
'''

# 4 Выведите из birthdate месяц рождения пользователя.
'''
birthday = datetime.date(2000, 4, 5)
print(birthday.month)
'''

    # 185 Вывод текущей даты. Чтобы вывести текущую дату, к модулю datetime нужно последовательно применить методы date и today.
'''
today = datetime.date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)
'''

    # 186 Получение дня недели Для получения номера текущего дня недели следует обратиться к свойству weekday. Оно возвращает числа от 0 до 6-ти, причем неделя начинается с понедельника и этот день имеет номер 0. Вторник - это день номер 1, среда - номер 2 и так далее.
'''
today = datetime.date.today()

print(today.weekday())

# Поскольку нумерация дней недели, начиная с 0 иногда может быть неудобной, можно применить специальное свойство isoweekday. Оно выведет номер дня при отсчете понедельника с 1:

print(today.isoweekday())

if today.weekday() == 5 or today.weekday() == 6:
    print(today.weekday())
    print('its weakend')
else:
    print('its wordays')
'''

# 3 Дата дата '2026-11-2'. Выведите ее день недели для двух случаев - при отсчете понедельника с 0 и при отсчете с 1.
'''
some_date = datetime.date(2026, 11, 2)

print(some_date.weekday())
print(some_date.isoweekday())
'''

    # 187 Разность двух дат При работе с датами может потребоваться определить разницу между ними. Для этой цели в Python применяется метод strptime модуля datetime.

    # Давайте узнаем сколько времени прошло между двумя датами: '25/05/2020 02:35:5' и '15/06/2020 10:17:23'. Для этого сначала применим метод datetime. Затем воспользуемся методом strptime, в первый параметр которого передадим нужную дату. А во втором параметре укажем ее формат. Далее выведем полученную разность на экран:
'''
start_time = datetime.datetime.strptime('25/05/2020 02:35:05', '%d/%m/%Y %H:%M:%S')
end_time = datetime.datetime.strptime('15/06/2020 10:17:23', '%d/%m/%Y %H:%M:%S')
time_dif = end_time - start_time

print(time_dif)
'''

# 1 Даны две даты: dt1 = '13/10/2018 22:15:45' dt2 = '15/11/2018 09:47:16' Определите сколько времени прошло между ними.
'''
date_1 = '13/10/2018 22:15:45'
date_2 = '15/11/2018 09:47:16'

start_time = datetime.datetime.strptime(date_1, '%d/%m/%Y %H:%M:%S')
end_time = datetime.datetime.strptime(date_2, '%d/%m/%Y %H:%M:%S')

time_dif = end_time - start_time
print(time_dif)
'''

# 2 Даны две даты: dt1 = '01-12-2025 16:07:5' dt2 = '31:12:2025 10:32:45' Определите сколько времени прошло между ними.
'''
date_1 = '01-12-2025 16:07:05'
date_2 = '31:12:2025 10:32:45'

start_time = datetime.datetime.strptime(date_1, '%d-%m-%Y %H:%M:%S')
end_time = datetime.datetime.strptime(date_2, '%d:%m:%Y %H:%M:%S')

time_dif = end_time - start_time
print(time_dif)
'''

    # 188 Определение високосного года. При определении високосности года с помощью математических методов нужно последовательно выполнить несколько операций, что не очень удобно. Однако в Python есть возможность значительно упростить данный процесс при помощи специального метода isleap модуля calendar. В параметр метода передается нужный год. Метод возвращает булевые значения. Если год високосный выведется True, в противном случае - False.

    # Для начала нужно импортировать модуль calendar: (импортировал его вначале файла рядом с datetime)
'''
res = calendar.isleap(2025)
print(res)
'''

# 1
'''
year = 2020
print(calendar.isleap(year))
'''

# 2
'''
year = 1910
print(calendar.isleap(year))
'''

# 3 Определите, является ли високосным текущий год.
'''
todays_date = datetime.date.today()
print(calendar.isleap(todays_date.year))
'''

    # 189 Вывод времени. Для того, чтобы работать с временем, нужно вывести его с помощью метода time модуля datetime. В параметры метода передаются час, минуты, секунды:
'''
res = datetime.time(12, 59, 59)
print(res)
print(res.hour)
print(res.minute)
print(res.second)

# Чтобы получить полную текущую дату и время в формате год-месяц-день час:минуты:секунды.миллисекунды, нужно последовательно применить методы datetime и now:

res_2 = datetime.datetime.now()
print(res_2)

# Также из данной полной даты можно вывести ее отдельные показатели, обратившись к соответствующим свойствам - day, month, year и т.д.:

print(res_2.year)
print(res_2.month)
print(res_2.day)
print(res_2.hour)
print(res_2.minute)
print(res_2.second)
print(res_2.microsecond)
'''

# 1 Выведите в консоль текущее время в формате часы:минуты:секунды.
'''
res = datetime.datetime.now()
res_2 = datetime.time(res.hour, res.minute, res.second)
print(res_2)
'''

# 2 Выведите в консоль текущее время в формате год-месяц-день часы:минуты:секунды.
'''
full_date_now = datetime.datetime.now()
full_date_now_edit = full_date_now.replace(microsecond=0)
print(full_date_now_edit)
'''

    # 190 Форматирование даты Давайте теперь выведем дату в определенном формате, например, год-месяц-день. Для этого объявим переменную dt, в которой нужная нам дата будет получена через метод datetime модуля datetime. Затем необходимо применить метод strftime к дате, записанной в dt. В параметры данного метода передается условное обозначение формата даты, записанное с помощью команды % и условного обозначения формата. Если нужно вывести год-месяц-день, то в параметр метода передается строка '%Y-%m-%d':
'''
dt = datetime.datetime(2025, 12, 31, 12, 59, 59)
res = dt.strftime('%Y:%m:%d')

print(res)
print(dt)
'''

# 1 Выведите в консоль текущую дату в формате день.месяц.год.
'''
date_now = datetime.datetime.now()
date_now_format = date_now.strftime('%d.%m.%Y')

print(date_now_format)
print(date_now)
'''

# 2 Выведите в консоль текущее время в следующем формате: часы:минуты:секунды год/месяц/день:день недели.
'''
date_now = datetime.datetime.now()
date_now_format = date_now.strftime('%H:%M:%S %Y/%m/%d')

print(date_now_format)
'''

    # 191 Получение времени в формате epoch. При работе с датой в Python существует специальный формат epoch, который отображает количество секунд, прошедшее с 1-го января 1970 года по текущий (или заданный) момент времени. Данный формат очень удобен для передачи и хранения данных о времени. Для получения epoch нужно сначала импортировать модуль time. А затем применить к нему специальный метод time. (импортировал вначале со всеми импортами)
'''
res = time.time()
res_2 = math.floor(res)

print(res, type(res))
print(res_2, type(res_2), len(str(res_2)))
'''

    # 192 Получение даты из формата epoch Чтобы из формата epoch вывести дату, нужно применить метод ctime. В его параметр передается epoch. Давайте получим дату текущего момент времени, преобразовав epoch:
'''
time_epoch = time.time()
date_epoch = time.ctime(time_epoch)

print(time_epoch, date_epoch)
'''

    # 193 Преобразование формата epoch в объект struct_time. Секунды, полученные из формата epoch можно преобразовать в особый объект struct_time. По структуре данных он похож на словарь. Объект struct_time нужен для более удобного работы с датами, хранящимися в epoch.
'''
time_epoch = time.time()
# получения объекта struct_time
res = time.localtime(time_epoch)

print(time_epoch)
print(res)
print(res.tm_mday)
print(res.tm_sec)
'''

# 3 Дана следующая epoch: dt = 1602314100.0 Получите из нее struct_time.
'''
dt = 1602314100.0
res = time.localtime(dt)

print(res)
'''

    # 194 Получить объект struct_time можно также с помощью метода gmtime модуля time. При этом время будет выводится по UTC - всемирному стандарту времени, не зависящему от локального часового пояса. Это значит, что полученный результат будет одинаковым независимо от того, где именно были произведены расчеты.
'''
time_epoch = time.time()
res = time.gmtime(time_epoch)

print(res)
'''

# 1 Получите часы и минуты из объекта struct_time по UTC. Сравните полученные результаты с работой метода localtime.
'''
time_epoch = time.time()
time_epoch_local = time.localtime(time_epoch)
time_epoch_utc = time.gmtime(time_epoch)

print(time_epoch_local)
print(time_epoch_utc)
'''

    # 195 Получение формата epoch из struct_time. Для того чтобы снова получить из объекта struct_time секунды epoch, можно применить метод mktime модуля time.
'''
time_now = time.time()
time_epoch_utc = time.gmtime(time_now)
res = time.mktime(time_epoch_utc)

print(time_epoch_utc)
print(res)
'''

    # 196 Разность эпох. Определить разность между заданным эпохами можно с помощью преобразования объекта struct_time в секунды методом mktime модуля time.

# Давайте найдем разницу между текущим моментом времени, заданным в формате epoch и датой '11/12/2023 19:25'. Вначале получаем epoch с помощью метода time:
'''
time_now = time.time()
dt = '11/12/2023 19:25'
dt_format = time.strptime(dt, '%d/%m/%Y %H:%M')
dt_epoch = time.mktime(dt_format)

res = time_now - dt_epoch

print(res, res / 60)
'''

# 1 Дана дата: dt = '24/07/2015 16:10' Найдите количество секунд, прошедшее с текущего момента времени до этой даты.
'''
time_now = time.time()
dt = '24/07/2015 16:10'
dt_format = time.strptime(dt, '%d/%m/%Y %H:%M')
dt_epoch = time.mktime(dt_format)

res = time_now - dt_epoch

print(res)
'''

# 2 Даны две даты: dt1 = '12/02/23 10:12:54' dt2 = '31/12/24 19:38:21' Найдите количество секунд, прошедшее между второй и первой датами.
'''
date_1 = '12/02/2023 10:12:54'
date_2 = '31/12/2024 19:38:21'
date_1_format = time.strptime(date_1, '%d/%m/%Y %H:%M:%S')
date_2_format = time.strptime(date_2, '%d/%m/%Y %H:%M:%S')

date_1_epoch = time.mktime(date_1_format)
date_2_epoch = time.mktime(date_2_format)

res = date_2_epoch - date_1_epoch

print(res)

# 3 Модифицируйте решение предыдущей задачи так, чтобы найти количество дней, прошедшее между двумя датами.
print(res / 60 / 60 / 24)
'''

    # 197 Задержка выполнения операции. Бывают ситуации, когда нужно, чтобы какая-либо операция выполнялась через определенный промежуток времени. Чтобы решить данную задачу, следует применить метод sleep модуля time. Давайте выведем в консоль сообщение через 5 секунд. Для этого вначале применим метод sleep, указав в его параметре нужную нам задержку в секундах. А затем укажем вывод сообщения в консоль:
'''
time.sleep(5)
print('!!!')
'''

# 1 Выведите на экран свое имя через 15 секунд.
'''
time.sleep(15)
print('Oleg')
'''

# 2 Выведите все его элементы через каждые 3 секунды. lst = ['a', 'b', 'c', 'd']
'''
lst = ['a', 'b', 'c', 'd']

for el in lst:
    time.sleep(3)
    print(el)
'''