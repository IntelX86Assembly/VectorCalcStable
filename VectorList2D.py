from Vector2D import *

class VectorList2D():

#CONSTRUCTOR
    def __init__(self):
        self.listVectors = []
        self.sumX = 0
        self.sumY = 0
        self.sumMagnitude = 0
        self.equilibriumVector = 0
        self.size = 0

#GETTERS
    def getListVectors(self):
        return self.listVectors

    def getSumX(self):
        return self.sumX

    def getSumY(self):
        return self.sumY

    def getSumMagnitude(self):
        return self.sumMagnitude

    def getEquilibriumVector(self):
        return self.equilibriumVector

    def getSize(self):
        self.size = len(self.listVectors)
        return self.size

#SETTERS

    def setListVectors(self, listVectors):
        self.listVectors = listVectors
        
    def setSumX(self, sumX):
        self.sumX = sumX

    def setSumY(self, sumY):
        self.sumY = sumY

    def setMagnitude(self, sumMagnitude):
        self.sumMagnitude = sumMagnitude
    
    def setEquilibriumVector(self, equilibriumVector):
        self.equilbriumVector = equilibriumVector

    def setSize(self, size):
        self.size = size

#METHODS
    def appendVector2D(self, x, y):
        self.listVectors.append(Vector2D(float(x), float(y)))

    def removeVector2D(self):
        self.listVectors.pop()

    def sumVectors(self):
        self.sumX = 0
        self.sumY = 0
        for vector in self.listVectors:
            self.sumX += vector.getX()
            self.sumY += vector.getY()

    def clearListVectors(self):
        self.listVectors.clear()

    def calcResultant(self):
        self.sumMagnitude = math.sqrt((self.sumX**2) + (self.sumY**2))

    def calcEquilibriumVector(self):
        self.sumMagnitude = math.sqrt((self.sumX**2) + (self.sumY**2))
        self.equilibriumVector = -sumMagnitude

    #TODO print to screen vector components and result
    def toString(self):
        self.string = ""
        for vector in self.getListVectors():
            self.string += vector.toString() + "\n"
        self.string +="Number of Vectors = " + str(self.getSize())
        return self.string
