# Implementation in Tcl/Tk
#
# package require Tk
# grid [ttk::button .b -text "Hello, World!"]

# In Python 3, the correct import is tkinter not Tkinter. Tkinter was the name of the module used for Python 2
from tkinter import *
from tkinter import ttk    # ttk is the Python binding to the newer "themed widgets" added in Tk version 8.5

root = Tk()
ttk.Label(root, text="Hello, World!", padding=(30, 10)).pack()

root.mainloop()
