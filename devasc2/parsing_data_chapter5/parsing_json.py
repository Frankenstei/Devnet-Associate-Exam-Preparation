#!/usr/bin/python3

#

import json

with open("interface.json") as data:
    json_data = data.read()

json_dict = json.loads(json_data)
print(json_dict)

##converting this dictionary back to json
with open("interface.json", "w") as fh:
    json.dump(json_dict, fh, indent = 4)
