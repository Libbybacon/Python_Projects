# Create GUI with button widget and text widget
# Include button function that will invoke dialog modal when called
# Dialog modal will allow users the ability to select a folder directory from their system
# Script will show user's selected directory path in text field

# use askdirectory() method
# When user clicks button, selected file path is retained by askdirectory() method and print in text box

# Use command attribute to attach askdirectory() to button
# Will need to save file path from askdirectory() in a stringVar() object, then set text in entry box to that object

import tkinter as tk
from tkinter import *
from tkinter import filedialog


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.title('Directory Path')
        self.master.geometry('{}x{}'.format(500,200))

        self.btn_getPath = Button(self.master, text = 'Get Directory Path', command=lambda: getDirectoryPath(self))
        self.btn_getPath.grid(row=0, column=0, padx=(20, 0), pady=(30,0))

        self.txt_directoryPath = tk.Entry(self.master, text = '')# I want to set text = directoryPath
        self.txt_directoryPath.grid(row=0, column=1, padx=(20, 0), pady=(30,0))

def getDirectoryPath(self):
    directoryPath=tk.filedialog.askdirectory()
    print(directoryPath)

        


if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
        

