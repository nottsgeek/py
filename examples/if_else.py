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
  
'''
###############################          NESTING      ##########################################
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
	if <sub conidition 5>:
		do this
	elif <sub consition 6>:
		do this
	else:
		do this
 '''