#!/usr/bin/python3

import xmltodict



# parse xml to python dictionary
with open("inventory.xml") as data:
    xml_example = data.read()

xml_dict = xmltodict.parse(xml_example)

print(xml_dict)

#unparse python dictionary back to xml

print(xmltodict.unparse(xml_dict, pretty=True))

# To write back to the file

with open("inventory.xml","w") as data:
    data.write(xmltodict.unparse(xml_dict, pretty=True))
