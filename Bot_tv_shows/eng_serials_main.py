import requests
import json
import string

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

for q in string.ascii_lowercase:
    amount_of_pages = get_amount_of_pages()

    for page in range(1, amount_of_pages):
        params = {
        "q": q,
        "page": page
        }

    resp = requests.get(BASE_URL, params=params)
    resp_dict = resp.json()
    list_of_serials.append(resp_dict['tv_shows'])

#print(list_of_serials)