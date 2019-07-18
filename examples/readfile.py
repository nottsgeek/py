#!/usr/bin/python

#you should have a file named template in your path
#Read file and store data as a string
'''
f=open('template', 'r')
data=f.read()
f.close()

print data
'''

#Read file line by line and store all lines as a list
'''
f=open("template", 'r')
datalist=f.readlines()
f.close()

print datalist
'''

#Read and process file line by line
'''
f=open('template', 'r')
line=f.readline()

while line:
  print line
  line=f.readline()
f.close()
'''
