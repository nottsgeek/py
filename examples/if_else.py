#!/usr/bin/python


AwsDict = {'ec2': {
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

value=2
if len(AwsDict['SecurityGroup']['VPCID']) <= value:
	print("There are less than %s regions" % value)
elif len(AwsDict['SecurityGroup']['VPCID']) > 2:
	print("there are exactly two regions")
else:
	print("Total number of regions are more than %s" % value)
  
###############################          NESTING      ##########################################
'''
if <condition 1>:
	if <sub conidition 1>:
		do this
	elif <sub conidition 2>:
		do this
	else:
		do this
elif <conidition 2>:
	if <sub condition 3>:
		do this
	elif <sub condition 4>:
		do this
	else:
		do this
else:
	do this
 '''

###############################          AND(&) OR(|)      ##########################################
'''
#!/usr/bin/python

x=2
y=3
z=4

if (x==y) and (x==z):
	print("Condition matched")
else:
	print("No Matches")


#(x<=y) & (z>=y) | (x!=y)
'''

############################### Check if a variable exists ##########################################
'''
x=0
if x:
	print("Yeah it exists")
else:
	print("Nope nothing is there")
'''

###############################           Negation         ##########################################
'''
if x != y:
	print("x isn't equal to y")

if x in my_list:
	print("x is there in the list")

if x not in my_list:
	print("x is not there in the list")
'''
###############################       Ternary Operator     ##########################################
'''
if x > y:
  print x
else:
  print y

print(x if x>y else y)
'''
