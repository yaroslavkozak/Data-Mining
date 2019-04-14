import json

with open('tweets.txt') as json_file:
    data = json.load(json_file)
    for p in data:
        print('id: ' + p['id'])
