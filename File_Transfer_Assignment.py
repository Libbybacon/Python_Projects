# Create two folders: one to hold files that get created or modified throughout the day,
# Another to receive the files that your script determines should be copied
# Over to daily
#
# To aid in your development efforts, you should create .txt files to add to the first folder,
# Using notepad or similar.
# Copy some older text files in there if you want
# Use files that you can edit so you can control whether or not they are meant
#   Use getdirectory() to choose folders to move files from and to
#   Save those directory paths to stringVar
#   Use shutil to find new files
#       get modification time in seconds since epoch,
#       convert seconds to %H
#       if %H <= 23, transfer file
import shutil
import os
import tkinter as tk
from tkinter import *
from tkinter import filedialog

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
    
        self.txt_sourceDir = tk.Entry(self.master)
        self.txt_sourceDir.grid(row=1, column=0, columnspan=3,padx=(20,0), pady=(20,0), sticky=W+E)
        self.txt_destDir = tk.Entry(self.master)
        self.txt_destDir.grid(row=3, column=0, columnspan=3,padx=(20,0), pady=(20,0), sticky=W+E)
        master.columnconfigure(0, weight=3)

        self.btn_sourceDir = Button(self.master, text='Select \nSource', command=lambda: getSourcePath(self))
        self.btn_sourceDir.grid(row=1, column=3, padx=(20,20), pady=(20,0), sticky=N+E+S+W)
        self.btn_sourceDir = Button(self.master, text='Select \nDestination', command=lambda: getDestPath(self))
        self.btn_sourceDir.grid(row=3, column=3, padx=(20,20), pady=(20,0), sticky=N+E+S+W)

        self.btn_Transfer = Button(self.master, text='Transfer \nFiles', command=lambda: transferFiles(self))
        self.btn_Transfer.grid(row=4, column=1, pady=(20,20), sticky=W)
        master.columnconfigure(1, weight=1)
    
def getSourcePath(self):
    directoryPath = tk.filedialog.askdirectory()
    self.txt_sourceDir.insert(0, directoryPath)

def getDestPath(self):
    directoryPath = tk.filedialog.askdirectory()
    self.txt_destDir.insert(0, directoryPath)

def transferFiles(self):
    source = self.txt_sourceDir.get()
    destination = self.txt_destDir.get()
    files = os.listdir(source)

    for i in files:
        modTime = os.path.getmtime(i)
        if modTime <= 86400:
            shutil.move(source+i, destination)


if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
        
        
