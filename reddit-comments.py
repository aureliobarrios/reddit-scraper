import json
import requests

#file that scrapes all the comments to a post

#receive url
url = input("Insert URL w/ JSON format: ")

#make request
headers = {'User-Agent': 'Mozilla/5.0'}
page = requests.get(url, headers=headers)

#load in json data
data = json.loads(page.text)

#define recursive helper function that will scrape comment data
def comment_search(comment):
    #track only comments that are replies
    if comment['kind'] != 'more':
        data = {'text': comment['data']['body']}
    else:
        return None

    #handle instance where comment does not have replies
    if isinstance(comment['data']['replies'], str):
        data['children'] = []
    #scrape the replies of the comments
    else:
        data['children'] = []
        for reply in comment['data']['replies']['data']['children']:
            data['children'].append(comment_search(reply))
    
    return data

#get the original mention
scraped_data = {
    'text': data[0]['data']['children'][0]['data']['selftext'],
    'children': []
}

#get the comments to the original mention
for comment in data[1]['data']['children']:
    scraped_data['children'].append(comment_search(comment))