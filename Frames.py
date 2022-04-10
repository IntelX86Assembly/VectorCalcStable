from VectorList2D import *
from Vector2DGraph import * 
from tkinter import *
from tkinter import ttk

class FrameSingle2DVector():

    def __init__(self, refreshFrame):
        
        #put frame inside refreshframe and expand it
        self.centerFrame = Frame(refreshFrame)
        self.centerFrame.pack(fill="both", expand=1, padx=(50,50), pady=(50,50))
        
        self.divL = Frame(self.centerFrame)
        self.divL.grid(column=0, row=1)

        self.divR = Frame(self.centerFrame)
        self.divR.grid(column=0, row=2)

        self.divT = Frame(self.centerFrame)
        self.divT.grid(column=1, row=0)

        self.divB = Frame(self.centerFrame)
        self.divB.grid(column=1, row=7)
       
        self.centerFrame.columnconfigure(0, weight = 3)
        self.centerFrame.columnconfigure(1, weight = 1)
        self.centerFrame.columnconfigure(2, weight = 3)

        self.centerFrame.rowconfigure(0, weight = 10)
        self.centerFrame.rowconfigure(1, weight = 3)
        self.centerFrame.rowconfigure(2, weight = 2)
        self.centerFrame.rowconfigure(3, weight = 1)
        self.centerFrame.rowconfigure(4, weight = 2)
        self.centerFrame.rowconfigure(5, weight = 1)
        self.centerFrame.rowconfigure(6, weight = 2)
        self.centerFrame.rowconfigure(7, weight = 15)
        
        #Top Label widget
        self.entryLabel = ttk.Label(self.centerFrame, text="Enter Vector Components", font="bold", anchor="center")
        self.entryLabel.grid(column=1, row=1, padx=(20,20), pady=(20,20), sticky="nesw")


        #Label and input box for x component
        self.labelX = ttk.Label(self.centerFrame, text="X-Component", anchor="center")
        self.labelX.grid(column=1, row=2, sticky="nesw")

        #Entry box for the x component
        self.entryX = ttk.Entry(self.centerFrame)
        self.entryX.grid(pady=(10,10), column=1, row=3, sticky="nesw")

        #Label and input box for y component
        self.labelY = ttk.Label(self.centerFrame, text="Y-Component", anchor="center")
        self.labelY.grid(column=1, row=4, sticky="nesw")


        #Entry box for the y component
        self.entryY = ttk.Entry(self.centerFrame)
        self.entryY.grid(pady=(10,10), column=1, row=5, sticky="nesw")

        #Plots the vector on a graph
        self.button = ttk.Button(self.centerFrame, text="Plot Vector", command=lambda:self.plotVector(self.entryX.get(), self.entryY.get()))
        self.button.grid(pady=(20,0), column=1, row=6, stick="nesw")

    def plotVector(self, x, y):
        #Create a 2D vector and graph it.
        self.vector2D = Vector2D(float(x), float(y))
        self.graph = Vector2DGraph()
        self.graph.graphSingleVector(self.vector2D)

class FrameMultiple2DVectors():

    def __init__(self, refreshFrame):
        
        #put frame inside refreshframe and expand it
        self.centerFrame = Frame(refreshFrame)
        self.centerFrame.pack(fill="both", expand=1)

        #Positions children widgets to left.
        self.leftFrame = Frame(self.centerFrame)
        self.leftFrame.grid(column=1, row=1, padx=(50,0), pady=(50,50), sticky="nwes")

        #Positions children widgets to right.
        self.rightFrame = LabelFrame(self.centerFrame)
        self.rightFrame.grid(column=2, row=1, padx=(50,50), pady=(50,50), sticky = "nwes")


        #This list belongs to this instance and is reset everytime this window is drawn so it is declared here
        #This list basically holds a list of vector2D objects as well as  providing convient calculation methods
        #on the collection of vectors.
        self.vectorList = VectorList2D() 

        self.centerFrame.columnconfigure(1, weight = 1)
        self.centerFrame.columnconfigure(2, weight = 3)
        self.centerFrame.rowconfigure(1, weight = 1)

        self.leftFrame.columnconfigure(1, weight = 1)
        self.leftFrame.rowconfigure(1, weight = 4)
        self.leftFrame.rowconfigure(2, weight = 4)
        self.leftFrame.rowconfigure(3, weight = 1)
        self.leftFrame.rowconfigure(4, weight = 4)
        self.leftFrame.rowconfigure(5, weight = 1)
        self.leftFrame.rowconfigure(6, weight = 4)
        self.leftFrame.rowconfigure(7, weight = 4)
        self.leftFrame.rowconfigure(8, weight = 4)
        self.leftFrame.rowconfigure(9, weight = 8)

        self.rightFrame.columnconfigure(1, weight = 1)

        #Top Label widget
        self.entryLabel = ttk.Label(self.leftFrame, text="Enter Multiple Vector Components", font="bold", anchor="center")
        self.entryLabel.grid(column=1, row=1, padx=(20,20), pady=(0,20))

        #Label and input box for x component
        self.labelX = ttk.Label(self.leftFrame, text="X-Component", anchor="center")
        self.labelX.grid(column=1, row=2, sticky="nesw")

        
        #Entry box for the x component
        self.entryX = ttk.Entry(self.leftFrame, width=20)
        self.entryX.grid(pady=(10,10), column=1, row=3, sticky="nesw")
        
        #Label and input box for y component
        self.labelY = ttk.Label(self.leftFrame, text="Y-Component", anchor="center")
        self.labelY.grid(column=1, row=4, sticky="nesw")
     
        #Entry box for the y component
        self.entryY = ttk.Entry(self.leftFrame, width=20)
        self.entryY.grid(pady=(10,10), column=1, row=5, sticky="nesw")

        #Add vector to list of vectors to graph
        self.addButton = ttk.Button(self.leftFrame, text="Add Vector", width=20, command=lambda: self.addButtonAction(self.entryX.get(), self.entryY.get(), self.vectorList, self.rightFrame))
        self.addButton.grid(column=1, row=6, sticky="nesw")

        #Plots the vectors on a graph.
        self.plotButton = ttk.Button(self.leftFrame, text="Plot Vectors", width=20, command=lambda: self.multiGraphButtonAction(self.vectorList))
        self.plotButton.grid(pady=(10,0), column=1, row=7, sticky="nesw")
    
        #Plots the vectors on a graph.
        self.resetButton = ttk.Button(self.leftFrame, text="Reset Program", width=20, command=lambda: self.resetFrame(self.rightFrame))
        self.resetButton.grid(pady=(20,0), column=1, row=8, sticky="nesw")
        
        self.spacer = ttk.Frame(self.leftFrame)
        self.spacer.grid(column=1, row=9, sticky="nesw")

        #Label to show the current vectors.
        self.labelVector = ttk.Label(self.rightFrame, text="Current Vectors:", anchor="center")
        self.labelVector.grid(padx=(100, 100), pady=(10, 20), column=1, row=1)


    def addButtonAction(self, x, y, vectorList, frameToPrintTo):
        vectorList.appendVector2D(x, y)
        #Should take the current list of vectors and display it in the right frame.
        self.outputToShowUser = ttk.Label(frameToPrintTo, text=vectorList.toString())
        self.outputToShowUser.grid(padx=(40, 40), column=1, row=2)

    #Resets current frame
    def resetFrame(self, frameToReset):
        self.response = messagebox.askokcancel("Warning", "Are you sure you want to delete all vectors and start over?")
        if self.response ==1:
            for widget in frameToReset.winfo_children():
                widget.destroy()
            #Label to show the current vectors.
            frameToReset.currentVectorLabel = ttk.Label(self.rightFrame, text="Current Vectors:")
            frameToReset.currentVectorLabel.grid(padx=(100, 100), pady=(20,20), column=1, row=1)
            self.vectorList.clearListVectors()
            self.outputToShowUser = ttk.Label(frameToReset, text=self.vectorList.toString())
            self.outputToShowUser.grid(padx=(40, 40), column=1, row=2)
 
    def multiGraphButtonAction(self, vectorList):
        self.graph = Vector2DGraph()
        self.graph.graphMultipleVectors(vectorList)

class FrameResultant2DVector():

    def __init__(self, refreshFrame):
        #put frame inside refreshframe and expand it
        self.centerFrame = Frame(refreshFrame)
        self.centerFrame.pack(fill="both", expand=1)

        #Positions children widgets to left.
        self.leftFrame = Frame(self.centerFrame)
        self.leftFrame.grid(column=1, row=1, padx=(50,0), pady=(50,50), sticky="nwes")

        #Positions children widgets to right.
        self.rightFrame = LabelFrame(self.centerFrame)
        self.rightFrame.grid(column=2, row=1, padx=(50,50), pady=(50,50), sticky = "nwes")


        #This list belongs to this instance and is reset everytime this window is drawn so it is declared here
        #This list basically holds a list of vector2D objects as well as  providing convient calculation methods
        #on the collection of vectors.
        self.vectorList = VectorList2D() 

        self.centerFrame.columnconfigure(1, weight = 1)
        self.centerFrame.columnconfigure(2, weight = 3)
        self.centerFrame.rowconfigure(1, weight = 1)

        self.leftFrame.columnconfigure(1, weight = 1)
        self.leftFrame.rowconfigure(1, weight = 4)
        self.leftFrame.rowconfigure(2, weight = 4)
        self.leftFrame.rowconfigure(3, weight = 1)
        self.leftFrame.rowconfigure(4, weight = 4)
        self.leftFrame.rowconfigure(5, weight = 1)
        self.leftFrame.rowconfigure(6, weight = 4)
        self.leftFrame.rowconfigure(7, weight = 4)
        self.leftFrame.rowconfigure(8, weight = 4)
        self.leftFrame.rowconfigure(9, weight = 8)

        self.rightFrame.columnconfigure(1, weight = 1)

        #Top Label widget
        self.entryLabel = ttk.Label(self.leftFrame, text="Enter Multiple Vector Components", font="bold", anchor="center")
        self.entryLabel.grid(column=1, row=1, padx=(20,20), pady=(0,20))

        #Label and input box for x component
        self.labelX = ttk.Label(self.leftFrame, text="X-Component", anchor="center")
        self.labelX.grid(column=1, row=2, sticky="nesw")

        
        #Entry box for the x component
        self.entryX = ttk.Entry(self.leftFrame, width=20)
        self.entryX.grid(pady=(10,10), column=1, row=3, sticky="nesw")
        
        #Label and input box for y component
        self.labelY = ttk.Label(self.leftFrame, text="Y-Component", anchor="center")
        self.labelY.grid(column=1, row=4, sticky="nesw")
     
        #Entry box for the y component
        self.entryY = ttk.Entry(self.leftFrame, width=20)
        self.entryY.grid(pady=(10,10), column=1, row=5, sticky="nesw")

        #Add vector to list of vectors to graph
        self.addButton = ttk.Button(self.leftFrame, text="Add Vector", width=20, command=lambda: self.addButtonAction(self.entryX.get(), self.entryY.get(), self.vectorList, self.rightFrame))
        self.addButton.grid(column=1, row=6, sticky="nesw")

        #Plots the vectors on a graph.
        self.plotButton = ttk.Button(self.leftFrame, text="Plot Resultant", width=20, command=lambda: self.plotResultant(self.vectorList))
        self.plotButton.grid(pady=(10,0), column=1, row=7, sticky="nesw")
    
        #Plots the vectors on a graph.
        self.resetButton = ttk.Button(self.leftFrame, text="Reset Program", width=20, command=lambda: self.resetFrame(self.rightFrame))
        self.resetButton.grid(pady=(20,0), column=1, row=8, sticky="nesw")
        
        self.spacer = ttk.Frame(self.leftFrame)
        self.spacer.grid(column=1, row=9, sticky="nesw")

        #Label to show the current vectors.
        self.labelVector = ttk.Label(self.rightFrame, text="Current Vectors:", anchor="center")
        self.labelVector.grid(padx=(100, 100), pady=(10, 20), column=1, row=1)

    def addButtonAction(self, x, y, vectorList, frameToPrintTo):
        self.vectorList.appendVector2D(x, y)
        #Should take the current list of vectors and display it in the right frame.
        self.outputToShowUser = ttk.Label(frameToPrintTo, text=vectorList.toString())
        self.outputToShowUser.grid(padx=(40, 40), column=1, row=2)

    def plotResultant(self, vectorList):
        self.vectorList.sumVectors()
        self.graph = Vector2DGraph()
        self.graph.graphResultantVector(vectorList)

    #Resets current frame
    def resetFrame(self, frameToReset):
        self.response = messagebox.askokcancel("Warning", "Are you sure you want to delete all vectors and start over?")
        if self.response ==1:
            for widget in frameToReset.winfo_children():
                widget.destroy()
            #Label to show the current vectors.
            frameToReset.currentVectorLabel = ttk.Label(self.rightFrame, text="Current Vectors:")
            frameToReset.currentVectorLabel.grid(padx=(100, 100), pady=(20,20), column=1, row=1)
            self.vectorList.clearListVectors()
            self.outputToShowUser = ttk.Label(frameToReset, text=self.vectorList.toString())
            self.outputToShowUser.grid(padx=(40, 40), column=1, row=2)

class FrameEquilibrium2DVector():

    def __init__(self, refreshFrame):
        #put frame inside refreshframe and expand it
        self.centerFrame = Frame(refreshFrame)
        self.centerFrame.pack(fill="both", expand=1)

        #Positions children widgets to left.
        self.leftFrame = Frame(self.centerFrame)
        self.leftFrame.grid(column=1, row=1, padx=(50,0), pady=(50,50), sticky="nwes")

        #Positions children widgets to right.
        self.rightFrame = LabelFrame(self.centerFrame)
        self.rightFrame.grid(column=2, row=1, padx=(50,50), pady=(50,50), sticky = "nwes")


        #This list belongs to this instance and is reset everytime this window is drawn so it is declared here
        #This list basically holds a list of vector2D objects as well as  providing convient calculation methods
        #on the collection of vectors.
        self.vectorList = VectorList2D() 

        self.centerFrame.columnconfigure(1, weight = 1)
        self.centerFrame.columnconfigure(2, weight = 3)
        self.centerFrame.rowconfigure(1, weight = 1)

        self.leftFrame.columnconfigure(1, weight = 1)
        self.leftFrame.rowconfigure(1, weight = 4)
        self.leftFrame.rowconfigure(2, weight = 4)
        self.leftFrame.rowconfigure(3, weight = 1)
        self.leftFrame.rowconfigure(4, weight = 4)
        self.leftFrame.rowconfigure(5, weight = 1)
        self.leftFrame.rowconfigure(6, weight = 4)
        self.leftFrame.rowconfigure(7, weight = 4)
        self.leftFrame.rowconfigure(8, weight = 4)
        self.leftFrame.rowconfigure(9, weight = 8)

        self.rightFrame.columnconfigure(1, weight = 1)

        #Top Label widget
        self.entryLabel = ttk.Label(self.leftFrame, text="Enter Multiple Vector Components", font="bold", anchor="center")
        self.entryLabel.grid(column=1, row=1, padx=(20,20), pady=(0,20))

        #Label and input box for x component
        self.labelX = ttk.Label(self.leftFrame, text="X-Component", anchor="center")
        self.labelX.grid(column=1, row=2, sticky="nesw")

        
        #Entry box for the x component
        self.entryX = ttk.Entry(self.leftFrame, width=20)
        self.entryX.grid(pady=(10,10), column=1, row=3, sticky="nesw")
        
        #Label and input box for y component
        self.labelY = ttk.Label(self.leftFrame, text="Y-Component", anchor="center")
        self.labelY.grid(column=1, row=4, sticky="nesw")
     
        #Entry box for the y component
        self.entryY = ttk.Entry(self.leftFrame, width=20)
        self.entryY.grid(pady=(10,10), column=1, row=5, sticky="nesw")

        #Add vector to list of vectors to graph
        self.addButton = ttk.Button(self.leftFrame, text="Add Vector", width=20, command=lambda: self.addButtonAction(self.entryX.get(), self.entryY.get(), self.vectorList, self.rightFrame))
        self.addButton.grid(column=1, row=6, sticky="nesw")

        #Plots the vectors on a graph.
        self.plotButton = ttk.Button(self.leftFrame, text="Plot Equilibrium Vector", width=20, command=lambda: self.plotEquilibriumVector(self.vectorList))
        self.plotButton.grid(pady=(10,0), column=1, row=7, sticky="nesw")
    
        #Plots the vectors on a graph.
        self.resetButton = ttk.Button(self.leftFrame, text="Reset Program", width=20, command=lambda: self.resetFrame(self.rightFrame))
        self.resetButton.grid(pady=(20,0), column=1, row=8, sticky="nesw")
        
        self.spacer = ttk.Frame(self.leftFrame)
        self.spacer.grid(column=1, row=9, sticky="nesw")

        #Label to show the current vectors.
        self.labelVector = ttk.Label(self.rightFrame, text="Current Vectors:", anchor="center")
        self.labelVector.grid(padx=(100, 100), pady=(10, 20), column=1, row=1)
    def addButtonAction(self, x, y, vectorList, frameToPrintTo):
        self.vectorList.appendVector2D(x, y)
        #Should take the current list of vectors and display it in the right frame.
        self.outputToShowUser = ttk.Label(frameToPrintTo, text=vectorList.toString())
        self.outputToShowUser.grid(padx=(40, 40), column=1, row=2)

    def plotEquilibriumVector(self, vectorList):
        self.vectorList.sumVectors()
        self.graph = Vector2DGraph()
        self.graph.graphEquilibriumVector(self.vectorList)

    #Resets current frame
    def resetFrame(self, frameToReset):
        self.response = messagebox.askokcancel("Warning", "Are you sure you want to delete all vectors and start over?")
        if self.response ==1:
            for widget in frameToReset.winfo_children():
                widget.destroy()
            #Label to show the current vectors.
            frameToReset.currentVectorLabel = ttk.Label(self.rightFrame, text="Current Vectors:")
            frameToReset.currentVectorLabel.grid(padx=(100, 100), pady=(20,20), column=1, row=1)
            self.vectorList.clearListVectors()
            self.outputToShowUser = ttk.Label(frameToReset, text=self.vectorList.toString())
            self.outputToShowUser.grid(padx=(40, 40), column=1, row=2)

