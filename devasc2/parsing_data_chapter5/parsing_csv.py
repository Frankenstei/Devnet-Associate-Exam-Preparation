#!/usr/bin/python3

# Parsing csv file to python object

# Basic Example
"""
import csv
samplefile = open("inventory.csv")
samplereader = csv.reader(samplefile)
sampledata = list(samplereader)
print(sampledata)


### We can then manipulate the python list as required as in
print(sampledata[0])
print(sampledata[0][1])
"""

#Example2
"""

import csv

with open("inventory.csv") as data:
    csv_list = csv.reader(data)
    for row in csv_list:
        device = row[0]
        location = row[2]
        ip = row[1]
        print(f"{device} is in {location.rstrip()} and has IP {ip}.")

"""
#Example 3
import csv
print("Please add a new router to the list")
hostname = input("What is the hostname")
ip = input("What is the ip address")
location = input("What is the location?")

router = [hostname, ip, location]

with open("inventory.csv", "a") as data:
    csv_writer = csv.writer(data)
    csv_writer.writerow(router)
