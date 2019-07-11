import os
import sys
import random
import math
import datetime 
try
except


print(dir(os))
os.lsdir()
os.walk()
os.rmdir()
os.chdir()
print(os.stat('test.py'))

'''
x=os.stat('test.py').st_atime
print datetime.fromtimestamp(x)
'''

#print(os.getcwd())
os.mkdir('tempDir')
os.makedir('dir1/dir2')

if not os.path.exists(dirName):
    os.mkdir(dirName)

#print math.sqrt(25) 
#x = datetime.datetime.now()
#print(x)

print random.randint(0, 5)

myList = ["aws", "connector", 37, 5, "port", 473, "wwn"]
random.choice(myList)

