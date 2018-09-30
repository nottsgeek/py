#!/usr/bin/python
#This program illustrates variable types in Python


#Numbers
"""
x = 1       # integer
x = 1.1     # float
x = a + yi  # complex
"""

#Strings
"""
TextVar = "TextVar is a string"
print(TextVar)

print(type(TextVar))
"""

#Lists
"""
RegionList = ["us-west-1", "us-west-2", "eu-west-1", "us-east-1"]
print(RegionList)
print(RegionList[0])
#calculating the length of list
print(len(RegionList))
#modifying a list
#print(RegionList[1])
#RegionList[1]="no-region"
print(RegionList[1])
"""

#tuples
"""
RegionTup = ("us-west-1", "us-west-2", "eu-west-1", "us-east-1")
print(RegionTup[1])

#Try Changing tuple
try:
    RegionTup[1]="no-region"
except TypeError:
    print("sorry can't change tuple")
except:
    print("Looks like something else went wrong")
"""

#Sets
"""
RegionSet = {"us-west-1", "us-west-2", "us-east-2", "us-west-1"}
print RegionSet
"""

"""
#Dictionaries
#Dictionary = {key1: 'value1', key2: 'value2'}
AwsDict = {'InstanceType': 't2.micro', 'region': 'us-east1', 'SecurityGroup': 'SG-29axc87xxx67'}
print(AwsDict)
#print(AwsDict['InstanceType'])

#Complex Dictionaries
#AwsDict = {'ec2': {
                 'InstanceType': ['t2.micro','x2.large'],
                 'region': 'us-east1',
                 'SecurityGroup': 'SG-29axc87xxx67'
                 },
          'SecurityGroup': {
                           'VPCID': ['new1-578bcbds', 'bcu88-u3jccd'],
                           'subnet': 'jkdcnjkde',
                           'ingress': 'cdscd',
                           'egress': 'cdcde'
                           }
           }
#print(AwsDict)
#print(AwsDict['ec2']['InstanceType'][1])
"""
