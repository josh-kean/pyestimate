"""this file contains definitions for different bid materials"""
import math


class StandardFunctions:

    def __init__(self, quantity, cost, diameter=0, totalCost = 0):
        self.quantity = quantity
        self.cost = cost
        self.diameter = diameter
        self.totalCost = totalCost

    def materialCost(self):
        return self.quantity*self.cost

    def laborCost(self, labor):
        self.labor = labor
        return self.quantity*self.labor

    def weldInches(self):
        return 3.14*self.quantity*self.diameter

class Pipe(StandardFunctions):

    def materialCost(self):
        return StandardFunctions.materialCost(self)

    def weldInches(self):
        return StandardFunctions.weldInches(self)

class Labor:

    def laborCost(self, labor):
        return StandardFunctions.laborCost(self, labor)
