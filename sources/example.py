import json
with open("data.json","r") as reader:
    data=json.load(reader)
    print(data['Ebay'])