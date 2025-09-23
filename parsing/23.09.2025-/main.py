import requests, json, re
from bs4 import BeautifulSoup
url = 'https://monasterium.ru/monastyri/?FILTER%5BNAME%5D=&FILTER%5BSTART_FROM_H%5D=&FILTER%5BSTART_FROM_M%5D=&FILTER%5BEND_FROM_H%5D=&FILTER%5BEND_FROM_M%5D=&FILTER%5BHOLYMANS%5D=&FILTER%5BHOLYPLACES%5D=&FILTER%5BTEMPLES%5D=&FILTER%5BHOLYDAYS%5D=&FILTER%5BBUILDED_FROM%5D=&FILTER%5BBUILDED_TO%5D=&FILTER%5BRESTORED_FROM%5D=&FILTER%5BRESTORED_TO%5D=&SORT%5BBY%5D=BY_ABC&PAGING%5BPAGE%5D=3&PAGING%5BPAGE_SIZE%5D=20'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
request = requests.get(url, headers=headers)
soup = BeautifulSoup(request.content, 'html.parser')
script = soup.find('script', string=re.compile('var coords ='))
beauti_to_string = str(script)
list_of_monasteries = re.findall(r'\{"name".*?\}\}', beauti_to_string, re.DOTALL)
print(list_of_monasteries[1:10])
print(type(list_of_monasteries))
print(len(list_of_monasteries))