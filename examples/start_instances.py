#!/usr/bin/python

#Script to start stopped instances in an aws account

import json
import os

#get list of instances and store it in instance_details.json file
os.system("aws ec2 list-instances --region=eu-west-2 >> instance_details.json")

#Read the instance_details.json in script and convert data to dict
with open('instance_details.json') as fh:
  data = json.load(fh)

#determince the total instance count
instance_count = len(data["Reservations"])

#Looping through all instances, store the id and state in vars
for i in range(0,instance_count):
  InstanceId=data["Reservations"][i]["Instances"][0]["InstanceId"]
  InstanceState=data["Reservations"][i]["Instances"][0]["State"]["Name"]
  #if state is stopped perform a start on id
  if InstanceState == "stopped":
    print("%s is stopped" %InstanceId)
    os.system("aws ec2 start-instances --region=eu-west-2 --instance-ids %s" %InstanceId)
