import requests


def get_raw_quote(key):
    url = "http://api.forismatic.com/api/1.0/"
    params = {"method": "getQuote",
              "key": key,
              "lang": "ru"}
    r = requests.get(url, params=params)
    try:
        quote = r.json()
    except Exception:
        quote = {}
    return quote


for key in range(10):
    quote = get_raw_quote(key)
    print(quote)
