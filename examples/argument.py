#!/usr/bin/python
import sys
#try running as `./argument.py hey` and `./argument.py "hey there"`

try:
    print(sys.argv[1])
except IndexError:
    print("No argument passed")
