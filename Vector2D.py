#IMPORT STATEMENTS
import math

class Vector2D:

#CONSTRUCTOR
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.magnitude = 0

#GETTERS

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getMagnitude(self):
        return self.magnitude

#SETTERS
    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def setMagnitude(self, magnitude):
        self.magnitude = magnitude

#METHODS
    def calcMagnitude(self):
        self.magnitude = math.sqrt((self.x**2) + (self.y**2))

#PRINT STATEMENTS

    def printMagnitude(self):
        print("The magnitude is " + str(self.magnitude))

    def printX(self):
        print("The x component is " + str(self.x))

    def printY(self) :
        print("The y component is " + str(self.y))

    def toString(self):
        self.string = "X = " + str(self.getX()) + "   Y = " + str(self.getY())
        return self.string
