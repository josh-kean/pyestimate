"""this is a python project to estimate project costs
the stages of production will be as follows:
1. terminal input and cost output
2. GUI input and cost output
3. functionality to import csv file and output csv file"""

from materials import *

#function to assign identity of bid
bidName = "spagett"
print(bidName)

pipes = Pipe(3, 6, 4, 10)
print(pipes.quantity)
print(pipes.cost)
print(pipes.materialCost())
print(pipes.weldInches())
print(labor.laborCost())
