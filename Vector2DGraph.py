import matplotlib.pyplot as plotter
from VectorList2D import *

class Vector2DGraph:

    def __init__(self):
        self.xComponents = []
        self.yComponents = []
        self.scaleSize = 0

    def graphSingleVector(self, vector):
        plotter.title("Plot Single Vector")

        # Holds vector components
        self.xComponents = vector.getX()
        self.yComponents = vector.getY()

        # Creating plot
        plotter.quiver([0], [0], self.xComponents, self.yComponents, angles='xy', scale_units='xy', scale=1)

        # x-lim and y-lim
        plotter.xlim(-1.25 * max(abs(vector.getX()), abs(vector.getY())), 1.25 * max(abs(vector.getX()) , abs(vector.getY())))
        plotter.ylim(-1.25 * max(abs(vector.getX()), abs(vector.getY())), 1.25 * max(abs(vector.getX()) , abs(vector.getY())))

        #Draw and display graph.
        plotter.grid()
        plotter.show()

    def graphMultipleVectors(self, vectorList):
        plotter.title("Graph of Multiple Vectors")
        self.lengthList = vectorList.getSize()

        # Holds origin for graph
        self.originPoints = [0] * self.lengthList

        # Creates empty list. Will later be filled with the x and y components of vector objects
        self.xComponents = [0] * self.lengthList
        self.yComponents = [0] * self.lengthList
        
        self.vectorCounter = 0

        for vector in vectorList.getListVectors():
            self.xComponents[self.vectorCounter] = vector.getX() 
            self.yComponents[self.vectorCounter] = vector.getY() 
            self.vectorCounter += 1

        #Scales vector graph to fit largest vector
        self.scaleSize = 0
        self.prevMax = 0
        for vector in vectorList.getListVectors():
            # Gets the max value of the current vector either x component or 
            # y component and checks if it is bigger than the largest vector
            # component. This is done to scale the window automatically.
            self.biggestComp= max(abs(vector.getX()), abs(vector.getY()))
            if self.biggestComp > self.prevMax:
               self.prevMax = self.biggestComp
               self.scaleSize = self.prevMax

        # Creating plot 
        plotter.quiver(self.originPoints, self.originPoints, self.xComponents, self.yComponents, angles = 'xy', scale_units= 'xy', scale=1)

        # x-limit and y-limit of graph that is drawn
        plotter.xlim(-1.25 * max(abs(self.scaleSize), abs(self.scaleSize)), 1.25 * max(abs(self.scaleSize) , abs(self.scaleSize)))
        plotter.ylim(-1.25 * max(abs(self.scaleSize), abs(self.scaleSize)), 1.25 * max(abs(self.scaleSize) , abs(self.scaleSize)))

        #Draw and display graph.
        plotter.grid()
        plotter.show()

    def graphResultantVector(self, vectorList):
        plotter.title("Plot Resultant Vector")

        # Holds vector components
        self.xComponents = vectorList.getSumX()
        self.yComponents = vectorList.getSumY()

        # Creating plot
        plotter.quiver([0], [0], self.xComponents, self.yComponents, angles='xy', scale_units='xy', scale=1)

        # x-lim and y-lim
        plotter.xlim(-1.25 * max(abs(vectorList.getSumX()), abs(vectorList.getSumY())), 1.25 * max(abs(vectorList.getSumX()) , abs(vectorList.getSumY())))
        plotter.ylim(-1.25 * max(abs(vectorList.getSumX()), abs(vectorList.getSumY())), 1.25 * max(abs(vectorList.getSumX()) , abs(vectorList.getSumY())))

        #Draw and display graph.
        plotter.grid()
        plotter.show()

    def graphEquilibriumVector(self, vectorList):
        plotter.title("Plot Resultant Vector")

        # Holds vector components
        self.xComponents = -vectorList.getSumX()
        self.yComponents = -vectorList.getSumY()

        # Creating plot
        plotter.quiver([0], [0], self.xComponents, self.yComponents, angles='xy', scale_units='xy', scale=1)

        # x-lim and y-lim
        plotter.xlim(-1.25 * max(abs(vectorList.getSumX()), abs(vectorList.getSumY())), 1.25 * max(abs(vectorList.getSumX()) , abs(vectorList.getSumY())))
        plotter.ylim(-1.25 * max(abs(vectorList.getSumX()), abs(vectorList.getSumY())), 1.25 * max(abs(vectorList.getSumX()) , abs(vectorList.getSumY())))

        #Draw and display graph.
        plotter.grid()
        plotter.show()

