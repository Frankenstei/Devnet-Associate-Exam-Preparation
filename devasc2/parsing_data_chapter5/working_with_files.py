#!/usr/bin/python3

## The line enables you run the script by just using ./<file_name>

## Working with files

""" 

readdata = open("text.txt","r")
print(readdata.read())
readdata.close()

"""
## A better way of working with files

"""
with open("text.txt","r") as data:
    print(data.read())
"""

## Writing to the file
with open("text.txt","a+") as data:
    data.write('\nFourth line added by python\n')

