import requests, json, re, csv
from bs4 import BeautifulSoup


url = 'https://monasterium.ru/monastyri/?FILTER%5BNAME%5D=&FILTER%5BSTART_FROM_H%5D=&FILTER%5BSTART_FROM_M%5D=&FILTER%5BEND_FROM_H%5D=&FILTER%5BEND_FROM_M%5D=&FILTER%5BHOLYMANS%5D=&FILTER%5BHOLYPLACES%5D=&FILTER%5BTEMPLES%5D=&FILTER%5BHOLYDAYS%5D=&FILTER%5BBUILDED_FROM%5D=&FILTER%5BBUILDED_TO%5D=&FILTER%5BRESTORED_FROM%5D=&FILTER%5BRESTORED_TO%5D=&SORT%5BBY%5D=BY_ABC&PAGING%5BPAGE%5D=3&PAGING%5BPAGE_SIZE%5D=20'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}


def get_request(url: str, headers: dict):
    try:
        request = requests.get(url, headers=headers)
        return request
    except requests.exceptions.InvalidSchema:
        print("HTTP Error. No connection adapters were found or Misstake in url")
    except requests.exceptions.ConnectionError:
        print('HTTP Error. No Internet')
request = get_request(url, headers)


soup = BeautifulSoup(request.content, 'html.parser')
script = soup.find('script', string=re.compile('var coords ='))
beauti_to_string = str(script)
list_of_monasteries = re.findall(r'\{"name".*?\}\}', beauti_to_string, re.DOTALL)



edited_list_of_monasteries = [json.loads(monastery) for monastery in list_of_monasteries]


names_of_columns = re.findall(r'("\w+?":)', list_of_monasteries[1])
edited_names_of_columns = [name.replace('"', '') for name in names_of_columns]
edited_names_of_columns_2 = [name.replace(':', '') for name in edited_names_of_columns]


with open('dict_monasteries.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=edited_names_of_columns_2)
    writer.writeheader()
    writer.writerows(edited_list_of_monasteries)