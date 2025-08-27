import requests
import json

BASE_URL = "https://www.episodate.com/api/search"

def get_amount_of_pages():
    params = {
        "q" : q,
        "page" : 1
    }
    resp = requests.get(BASE_URL, params=params)
    resp_dict = resp.json()
    amount_of_pages = resp_dict['pages'] + 1

    return amount_of_pages

list_of_serials = []

CYRILLIC_LOWERCASE_LETTERS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

for q in CYRILLIC_LOWERCASE_LETTERS:
    amount_of_pages = get_amount_of_pages()

    for page in range(1, amount_of_pages):
        params = {
        "q": q,
        "page": page
        }
        print(q)
#        i+=1
#        print(i)
        print(amount_of_pages)

    resp = requests.get(BASE_URL, params=params)
    resp_dict = resp.json()
    list_of_serials.append(resp_dict['tv_shows'])

print(list_of_serials)

resp = requests.get(BASE_URL, params=params)
print(f"Запрос: {resp.url} — статус {resp.status_code}")