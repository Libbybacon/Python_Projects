#   Python version: 3.9.1
#
#   Author: Elizabeth Bacon

#   Challenge -- Create UI that:
#   - Lets users transfer files that have been modified w/in last 24hours from one folder to another
#   - Lets user browse and choose specific folder that will contain files to be checked daily
#   - Lets user browse and choose specific folder that will receive copied files
#   - Lets user initiate 'file'check process performed by the script

# Import necessary modules
import shutil
import os
import tkinter as tk
from tkinter import *
from tkinter import filedialog

# Create GUI
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.title('Transfer Recently Modified Files')
        self.master.geometry('{}x{}'.format(500,300))

        self.lbl_sourceDir = Label(self.master, text='Source directory:')
        self.lbl_sourceDir.grid(row=0, column = 0, padx=(0,0), pady=(20,0), sticky=E+W)
        self.lbl_destDir = Label(self.master, text='Destination directory:')
        self.lbl_destDir.grid(row=2, column = 0, padx=(0,0), pady=(20,0), sticky=E+W)

        # Text boxes that will display chosen directory path
        self.txt_sourceDir = tk.Entry(self.master)
        self.txt_sourceDir.grid(row=1, column=0, columnspan=3,padx=(20,0), pady=(20,0), sticky=W+E)
        self.txt_destDir = tk.Entry(self.master)
        self.txt_destDir.grid(row=3, column=0, columnspan=3,padx=(20,0), pady=(20,0), sticky=W+E)
        master.columnconfigure(0, weight=3)

        # Buttons that allow user to select source and destination folders
        self.btn_sourceDir = Button(self.master, text='Select \nSource', command=lambda: getSourcePath(self))
        self.btn_sourceDir.grid(row=1, column=3, padx=(20,20), pady=(20,0), sticky=N+E+S+W)
        self.btn_sourceDir = Button(self.master, text='Select \nDestination', command=lambda: getDestPath(self))
        self.btn_sourceDir.grid(row=3, column=3, padx=(20,20), pady=(20,0), sticky=N+E+S+W)

        # Button to initiate file check/transfer
        self.btn_Transfer = Button(self.master, text='Transfer \nFiles', command=lambda: transferFiles(self))
        self.btn_Transfer.grid(row=4, column=1, pady=(20,20), sticky=W)
        master.columnconfigure(1, weight=1)

# Choose source folder and display path in text box   
def getSourcePath(self):
    directoryPath = tk.filedialog.askdirectory()
    self.txt_sourceDir.insert(0, directoryPath)

# Choose destination folder and display path in text box
def getDestPath(self):
    directoryPath = tk.filedialog.askdirectory()
    self.txt_destDir.insert(0, directoryPath)

# Get modification time of each file in source folder, transfer files 
# to destination that have been modified in the last 24 hours
def transferFiles(self):
    source = self.txt_sourceDir.get()
    destination = self.txt_destDir.get()
    files = os.listdir(source)

    for i in files:
        fullPath = os.path.join(source, i)
        modTime = os.path.getmtime(fullPath)
        print(modTime)
        if modTime <= 86400:
            shutil.move(fullPath, destination)


if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
        
        
