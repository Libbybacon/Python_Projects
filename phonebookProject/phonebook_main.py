# Python version:   3.9.1
#
# Author:   Elizabeth Bacon
#
# Purpose:  Phonebook Demo.  Demonstrating OOP, Tkinter GUI module,
#           using Tkinter Parent and Child relationships
#
# Tested OS:  This code was written and tested to work with Mac OS High Sierra

from tkinter import *
import tkinter as tk

# Import other modules we will need
import phonebook_gui
import phonebook_functions as phonebook_func


# Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # Define our master frame configuration
        self.master = master
        self.master.minsize(500, 300)
        self.master.maxsize(500, 300)
        # CenterWindow centers app on user's screen
        phonebook_func.center_window(self, 500, 300)
        self.master.title('Tkinter Phonebook Demo')
        self.master.configure(bg='#FOFOFO')
        # This protocol method is a tkinter built-in method to catch if
        # the user clicks the upper corner, "X" on Windows OS
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        arg = self.master

        # Load in the GUI widgets from a separate module,
        # keeping code compartmentalized and clutter-free
        phonebook_gui.load_gui(self)


        

if __name__ ==" __main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()


        
