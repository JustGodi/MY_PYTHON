'''
import requests
import json







st_accept = 'txt/html' # говорим веб-серверу, что хотим получить html

# имитируем подключение через браузер Mozilla на macOS
st_useragent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15'

# формируем хеш заголовков
heafers = {
    'Accept': st_accept,
    'User-Agent': st_useragent
}
'''

import requests, json, re
from bs4 import BeautifulSoup

url = 'https://monasterium.ru/monastyri/?FILTER%5BNAME%5D=&FILTER%5BSTART_FROM_H%5D=&FILTER%5BSTART_FROM_M%5D=&FILTER%5BEND_FROM_H%5D=&FILTER%5BEND_FROM_M%5D=&FILTER%5BHOLYMANS%5D=&FILTER%5BHOLYPLACES%5D=&FILTER%5BTEMPLES%5D=&FILTER%5BHOLYDAYS%5D=&FILTER%5BBUILDED_FROM%5D=&FILTER%5BBUILDED_TO%5D=&FILTER%5BRESTORED_FROM%5D=&FILTER%5BRESTORED_TO%5D=&SORT%5BBY%5D=BY_ABC&PAGING%5BPAGE%5D=3&PAGING%5BPAGE_SIZE%5D=20'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

request = requests.get(url, headers=headers)
# print(request.status_code) # проверка успешного запроса, потом переделать в try except

# soup_pretti = BeautifulSoup(request.prettify()[:1000], 'html.parser')
# print(soup_pretti)

soup = BeautifulSoup(request.content, 'html.parser')

script = soup.find('script', string=re.compile('var coords ='))
#print(script)
beauti_to_string = str(script)
# print(str_of_answer)
#print(type(beauti_to_string))
#print(len(beauti_to_string))
#print(beauti_to_string[0:500])
#print('________________________________________________________-')
#print(beauti_to_string[-1500:-1])

# only_monasteries = re.findall('//{"name"(.+)//}//}', beauti_to_string)
list_of_monasteries = re.findall(r'\{"name".*?\}\}', beauti_to_string, re.DOTALL)
#print(list_of_monasteries[1:10])
#print(type(list_of_monasteries))
#print(len(list_of_monasteries))


'''string_of_monasteries = ', '.join(list_of_monasteries)
print(type(string_of_monasteries))
print(string_of_monasteries[1:500])
print('___________________________________________________________________')
del_useless_info_1 = re.sub(r'"img"\\:".*?",', '', string_of_monasteries)
del_useless_info_2 = re.sub(r'"props"\\:\\{.*?\\},', '', del_useless_info_1)
print(del_useless_info_2[1:500])'''






