#!/usr/bin/python

import json

ec2 = '{ "region":"us-east1", "count":3, "type":"t2.micro"}'

data = json.loads(ec2)

print(data["region"])

data["region"] = "eu-west2"

ec2 = json.dumps(data)

print(ec2)


with open('cft.json') as fh:
  data = json.load(fh)
  
print(data)
