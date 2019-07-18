#!/usr/local/python

#defining a function
def demo_func():
  print(demo)
  
#calling a function
demo_func()
#----------------------------------------
#passing argument to a function
def demo_func(x):
  print(x)
  
demo_func(5)

#----------------------------------------
#passing multiple arguments to a function
def demo_func(x,y):
  z=x+y
  print(z)
 
demo_func(4,5)

#----------------------------------------
#Getting return value
def demo_func(x,y):
  z=x+y
  return z
 
print(demo_func(4,5))

#----------------------------------------
#Default parameter
def demo_func(x,y=5):
  z=x+y
  return z
 
print(demo_func(4))

#----------------------------------------
#multiple parameters
#list as a parameter
#Recursion
