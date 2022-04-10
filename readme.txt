Version3

This version is stable and ready for deployment.


How to run)

$ python3 GuiRoot.py

Quick overview of classes

GuiRoot.py: This class is the driver program and also contains the root 
object for containing the frames and program. It is the main class and 
container for this program

Frames.py: This class handles all the aspects of the gui and its program.
GuiRoot will contain a frame object from this class. The frame objects of this class
defines what is drawn inside the gui and when buttons are pressed it calls helper functions
and classes to perform actions.

Vector2D.py: contains all the methods and properties we would expect a 2D vector to have

VectorList2D.py: Holds Vector2D objects and performs actions on these collections. So the 
user may enter vector components in the frame class which calls the Vector2D class to 
create a vector with these values and then these vectors can be added to this list. The main 
vector calculations are contained in this class

Vector2DGraph: This class handles the graphing of vectors. It takes either a Vector2D or
VectorList2D object and renders it in a graph.  

main features)

- Methods for working with 2D vectors 

- A gui that works and is stable and includes the ability to scale
dynamically.

- Calculations that work and are accurate

- The graph autoscales and helps with the visualization of vectors 

