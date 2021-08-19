import my_module as mm
#this is the best way to import specific module classes
#from my_module import find_index, test
#this imports everything but not sure which one,
# from my_module import *

import sys
#append more directories to the path, lets you import the module and run the code
#sys.path.append('/Users/coreyscahfer/Desktop/My-Modules')
#might need to change env variables

courses = ['History', 'Math', 'Physics', 'CompSci']

index = mm.find_index(courses, 'Math')
print(index)
#prints your current directory
print(sys.path)

import os

print(os.__file__)