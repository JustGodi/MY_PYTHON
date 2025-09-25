# import libs
import pandas as pd
import numpy as np
import requests
from requests import Response
from bs4 import BeautifulSoup
from tqdm import tqdm

import re
import json


# var init
base_url = 'https://monasterium.ru/monastyri/'
headers = {
    'User-Agent':
           'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ' \
           '(KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}
def get_request(url: str, headers: dict) -> Response:
    try:
        response = requests.get(url, headers=headers)
        return response
    except requests.exceptions.InvalidSchema:
        print("HTTP Error. No connection adapters were found or Misstake in url")
    except requests.exceptions.ConnectionError:
        print('HTTP Error. No Internet')


response = get_request(base_url, headers)

page = BeautifulSoup(response.content, 'html.parser')

find_data = str(page.find('script', string=re.compile('var coords =')))

list_of_monasteries = re.findall(r'\{"name".*?\}\}', find_data, re.DOTALL)
edited_list_of_monasteries = [json.loads(monastery) for monastery in list_of_monasteries]

data = pd.DataFrame(edited_list_of_monasteries)

data.drop(columns=['distance', 'props'], inplace=True)

data['url'] = data['url'].apply(lambda x: x[11:])

data.to_csv('./monasteries.csv')

data = pd.read_csv('./monasteries.csv')

data.info()

data[['founded', 'address', 'eparhia']] = np.nan

for idx in tqdm(range(data.shape[0])):
    row_url = data.loc[idx, 'url']
    complete_url = url + row_url
    response = get_request(complete_url, headers=headers)

    
    founded = str(page.find('founded', string=re.compile('var coords =')))
    addres = str(page.find('script', string=re.compile('var coords =')))

