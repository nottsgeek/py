#!/usr/bin/python

import json
import os

os.system("aws ec2 list-instances --region=eu-west-2 >> instance_details")

with open('instance_details') as fh:
  data = json.load(fh)


instance_count = len(data["Reservations"])
for i in range(0,instance_count):
  InstanceId=data["Reservations"][i]["Instances"][0]["InstanceId"]
  InstanceState=data["Reservations"][i]["Instances"][0]["State"]["Name"]
  if InstanceState == "stopped":
    print("%s is stopped" %InstanceId)
    os.system("aws ec2 start-instances --region=eu-west-2 --instance-ids %s" %InstanceId)
