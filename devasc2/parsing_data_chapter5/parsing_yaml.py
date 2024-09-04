#!/usr/bin/python3

import yaml

with open("inventory.yaml") as data:
    yaml_sample = data.read()
    yaml_dict = yaml.load(yaml_sample, Loader=yaml.FullLoader)

print(yaml_dict)
yaml_dict["interface"]["name"] = "GigabeitEthernet1"

print(yaml.dump(yaml_dict,default_flow_style=False))
