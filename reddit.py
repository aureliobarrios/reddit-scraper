import json
import requests

#receive url
url = input("Insert URL w/ JSON format: ")

#make request
headers = {'User-Agent': 'Mozilla/5.0'}
page = requests.get(url, headers=headers)

#load in json data
data = json.loads(page.text)