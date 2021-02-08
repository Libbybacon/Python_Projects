# Python Version:   3.9.1
#
# Author:   Elizabeth Bacon
#
# Purpose: Student Tracker Demo.  Use OOP, Tkinter GUI module,
#           show Parent/Child relationships, create & utilize dB with sqlite3

# Import needed modules
import tkinter as tk
from tkinter import *
import Student_Tracking_gui as Student_gui
import Student_Tracking_functions as Student_func

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.resizable(width=False, height= False)
        self.master.geometry('{}x{}'.format(800, 400))
        self.master.config(bg='white')
        self.master.title('Student Tracking')

        Student_gui.load_gui(self)        
                                   
                              
                            


if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
