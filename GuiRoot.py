#RUN THIS PROGRAM WITH "$python3 GuiRoot.py"
#THIS PROGRAM IS THE DRIVER PROGRAM. IT DRAWS THE
#ROOT WINDOW AND CALLS SUBCLASSES TO GET WORK DONE


#IMPORT STATEMENTS

#Import tkinter for drawing gui. Import ttk, messagebox
#to get access to modern UI widgets and messagebox pop ups.
from tkinter import *
from tkinter import ttk, messagebox

from Frames import *
class DrawRootWindow():

    
    def __init__(self):

        self.helpDialog=''' 
QUICK START:

1.)
Click on the Graph menu item and select an option to begin graphing vectors.
or 
Click on the Calculations menu item to perform calculations on vectors.

2.)
Click on a button in selected menu item to start that program.

3.)
Input fields will then appear asking for vector components.

4.)
Enter the vectors components i.e. their x, y, or z values as a number

5.)
The program will then perform an action based on what option you have selected.
'''


        #Create the main/root window of the program
        self.root = Tk()
        
        #Sets the size and title of the window
        self.root.geometry("1080x720")
        self.root.title("VectorCalc")
        self.root.minsize(720,480)
        
        #Creates a frame to put in the root window. When a menu option
        #is selected then the frame is clear and repopulated with widgets.
        self.frame = Frame(self.root)
        self.frame.pack(fill="both", expand=1)
      #  self.frame.grid(column=0, row=0)
        
      #  self.frame.columnconfigure(0, weight=1)
      #  self.frame.rowconfigure(0, weight=1)

        #Create a menu bar to act as container for menu buttons
        #and tell the root window to use this menuBar as our menu
        self.menuBar = Menu(self.root)
        self.root.config(menu=self.menuBar)

        #Instantiating Menu items to act as our buttons in the menu bar
        self.fileButton = Menu(self.menuBar, tearoff = 0)
        self.graphButton = Menu(self.menuBar, tearoff = 0)
        self.calcButton = Menu(self.menuBar, tearoff = 0)
        self.helpButton = Menu(self.menuBar, tearoff = 0)
        #Calls the add_cascade method to cause these buttons 
        #to show up in the menu.
        self.menuBar.add_cascade(label="File", menu=self.fileButton)
        self.menuBar.add_cascade(label="Graph", menu=self.graphButton)
        self.menuBar.add_cascade(label="Calculations", menu=self.calcButton)
        self.menuBar.add_cascade(label="Help", menu=self.helpButton)

        #Add commands to the "File" menu option
        self.fileButton.add_command(label="Exit",command=lambda:self.fileMenuAction("Exit"))
        self.fileButton.add_command(label="Clear",command=lambda:self.fileMenuAction("Clear"))

        #Adds commands to the "Graph" menu button
        self.graphButton.add_command(label="Plot Single 2D Vector",command=lambda:self.graphMenuAction("plotSingle2DVector"))
        self.graphButton.add_command(label="Plot Multiple 2D Vectors",command=lambda:self.graphMenuAction("plotMultiple2DVectors"))

        #Adds commands to the "Calculations" menu button
        self.calcButton.add_command(label="Resultant 2D Vector",command=lambda:self.calcMenuAction("findResultant2DVectors"))
        self.calcButton.add_command(label="Find Equlibrium 2D Vector",command=lambda:self.calcMenuAction("findEquilibrium2DVectors"))

        #Adds command to the Help menu for getting help
        self.helpButton.add_command(label="Get help",command=self.showHelp)

        self.labelStartMessage = ttk.Label(self.frame, text=self.helpDialog, font="bold")
        self.labelStartMessage.grid(column=0, row=0, pady=(75,50), padx=(75,0), sticky=(N))
        
        #Cause main window to run in loop to make gui interactive
        #like keeping track of mouse position and refreshing display
        self.root.mainloop()


    def graphMenuAction(self, menuSelection):
        #clears the frame first before we add widgets back when we redraw it.
        for widget in self.frame.winfo_children():
            widget.destroy()
        #Defines what frame will be drawn dependent on the menu item selected by the user.
        if(menuSelection == "plotSingle2DVector"):
            self.currentProgram = FrameSingle2DVector(self.frame)
        elif(menuSelection == "plotMultiple2DVectors"):
            self.currentProgram = FrameMultiple2DVectors(self.frame)
   
    def calcMenuAction(self, menuSelection):
        #clears the frame first before we add widgets back when we redraw it.
        for widget in self.frame.winfo_children():
            widget.destroy()
        if(menuSelection == "findResultant2DVectors"):
            self.currentProgram = FrameResultant2DVector(self.frame)
        elif(menuSelection == "findEquilibrium2DVectors"):
            self.currentProgram = FrameEquilibrium2DVector(self.frame)
 
    def fileMenuAction(self, menuSelection):
        if(menuSelection == "Exit"):
            self.exitProgram()
        elif(menuSelection == "Clear"):
            self.clearProgram()

    def exitProgram(self):
        self.response = messagebox.askokcancel("Quit Program?", "Warning: Are you sure you want to quit?")
        if self.response ==1:
            self.root.destroy()
       
    def clearProgram(self):
        self.response = messagebox.askokcancel("Warning", "Are you sure you want to clear the current program from the workspace?")
        if self.response == 1:
            for widget in self.frame.winfo_children():
                widget.destroy()

       #Displays a popup that gives help to the user
    def showHelp(self):
        messagebox.showinfo("Quick Help Guide", self.helpDialog)

window = DrawRootWindow()
