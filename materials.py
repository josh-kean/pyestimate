"""this file contains definitions for different bid materials"""
import math


class StandardFunctions:

    def __init__(self, quantity, cost, diameter=0, totalCost = 0):
        self.quantity = quantity
        self.cost = cost
        self.diameter = diameter
        self.totalCost = totalCost

    #this function takes the price per unit and multiplies the number of items
    def materialCost(self, augment=1):
        return self.quantity*self.cost*augment

    #this function takes the quantity of tasks to do by the price per tasks
    #and returns the cost to perform the task
    #it also allows an option to increase or decrease cost by a desired percent
    def laborCostQuantity(self, labor, augment=1):
        return self.quantity*labor*augment

    #this function multiplies the labor cost/hour by the time it takes to
    #install one unit by the number of units
    def laborCostTime(self, time, labor, augment=1):
        return time*labor*augment*self.quantity

    #need to change this function to work for pipes and complicated reducers
    def weldInches(self):
        return 3.14*self.quantity*self.diameter

class Pipe(StandardFunctions):

    def materialCost(self):
        return StandardFunctions.materialCost(self)

    def weldInches(self):
        return StandardFunctions.weldInches(self)

    def laborCostQuantity(self, labor, augment=1):
        # quantity = self.quantity
        self.labor = labor
        return StandardFunctions.laborCost(self, self.labor, augment )

class Fitting(StandardFunctions):
    def materialCost(self):
        return StandardFunctions.materialCost(self)

    def weldInches(self):
        return StandardFunctions.weldInches(self)

    def laborCostQuantity(self, labor, augment=1):
        self.labor = labor
        return StandardFunctions.laborCostQuantity(self.labor, augment)
