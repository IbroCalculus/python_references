
#A module is a file containing python code. It may contain functions, classes etc
#It is used with modular programming, which is used to separate a program into parts.

#Create and import your own custom module
#i.e Modules2

#On this machine, it always shows the red for custom module import, don't know why, but still works

import modules2
from modules2 import timesAll

x = modules2.sumAll(5,6,7)
y = timesAll(5,4,2)

print(f'sumAll = {x}, while timesAll = {y}')


#================= List all modules available on the computer ===============
print("LIST OF ALL AVAILABLE MODULES")
help('modules')