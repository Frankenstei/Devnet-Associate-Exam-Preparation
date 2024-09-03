#!/usr/bin/python3

import csv
samplefile = open("inventory.csv")
samplereader = csv.reader(samplefile)
sampledata = list(samplereader)
print(sampledata)


### We can then manipulate the python list as required as in
print(sampledata[0])
print(sampledata[0][1])
