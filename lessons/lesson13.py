import requests
import random

def get_raw_quote(lang = "ru"):
    url = "http://api.forismatic.com/api/1.0/"
    params =  {"method": "getQuote",
           "format": "json",
           "lang": lang,
               "key": random.randint(1,9999)}
    response = requests.get(url, params=params)
    return response.json()

def get_quote(raw_quote):
    return raw_quote["quoteText"]


def get_author(raw_quote):
    return raw_quote["quoteAuthor"]

for requests_number in range(10):
    raw_quote = get_raw_quote()
    quote = get_quote(raw_quote)
    print(quote)


# print(response.status_code)
# print(response.json)
