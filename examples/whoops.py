#!/usr/bin/python
'''
for i in range(1,10):
	print i

for i in range(0,10,2):
	print i
	
my_list=[112,43,12,"sdcdsc","9nu"]

for i in my_list:
	print i

my_list=["test1", "test2", "test3"]
for i in my_list:
	print("you are dealing with "+ i)

my_tuple=(112,43,12,"sdcdsc","9nu")
for i in my_tuple:
	print i

my_tuple=(112,43,12,"sdcdsc","9nu")
for i in range(0, len(my_tuple)):
	print(my_tuple[i])

#Read a list and create a tupple with if condition satisfies

my_list1=[]
my_tuple=[112,"test"]
my_list=[112,43,12,"sdcdsc","9nu"]
for i in my_list:
	if i in my_tuple:
		my_list1.append(i)

print my_list1
'''
###############################   Nested for loops ##############################
'''
my_tuple=(10,20,30,40)
my_list=[1,2,34]
#my_list=[[1,2,3,4], [5,6,7,8], [9,10,11,12]]
for i in my_tuple:
	for j in my_list:
#		for k in j:
#			print i + k
		print i + j
'''

###############################   While loops ##############################
'''
while(<condition>):
	code

i=0
while i<10:
	print i
	i += 1
	
i=0
while i!=10:
	x = int(raw_input('Enter a number : '))
	
'''
###############################   Input validation ##############################
'''
my_list = ["option1", "option2"]
option = ""
while option not in my_list:
	option = raw_input("here : ")
'''
