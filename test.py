import json

with open("config.json") as config_file:
 data = json.load(config_file)

one = data["Format"]
print(one)
#print(data)
