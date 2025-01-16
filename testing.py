import requests
from pprint import pprint
import json

res = requests.get(
    "http://api.openweathermap.org/geo/1.0/direct?q=London&limit=1&appid=5da5999914549a585e1b005b89ad2444").text


file = open("testing.json", "w")
pprint(res)
file.write(res)
