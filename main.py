"""this is a python project to estimate project costs
the stages of production will be as follows:
1. terminal input and cost output
2. GUI input and cost output
3. functionality to import csv file and output csv file"""

from materials import *


materials = []
count = 0


while True:
    selection = input("do you want to enter a pipe or a fitting? ")

    try:
        if selection.lower() == "pipe":
            # input("what do you want to call this pipe?")
            a = int(input("how many pipes do you have? "))
            b = int(input("how much does a pipe cost? "))
            c = float(input("what's the diameter of the pipe? "))
            materials.append(Pipe(a, b, c))
            print(materials[count].quantity)
            print(materials[count].cost)
            print(materials[count].diameter)
            print(materials[count].materialCost())
            proceed = input('do you want to add more items? y/n')
            if proceed.lower() == 'y':
                count +=1
            if proceed.lower() == 'n':
                break
    except:
        print('not a valid choice, try again')
    if selection.lower() == "fitting":
        pass
