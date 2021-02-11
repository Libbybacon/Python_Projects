#
#Challenge: recreate an exact copy of a GUI from the image provided
#

import tkinter as tk
from tkinter import *




def ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.config(bg='lightgray')
        self.master.title('GUI replica')

        self.btn_browse1 = Button(self.master, text='Browse...')
        self.btn_browse1.grid(row=0, column=0)
        self.btn_browse2 = Button(self.master, text='Browse...')
        self.btn_browse2.grid(row=1, column=0)
        self.btn_chkFiles = Button(self.master, text='Check for files...')
        self.btn_chkFiles.grid(row=2, column=0, rowspan=2)
        self.btn_closePrgm = Button(self.master, text='Close Program')
        self.btn_closePrgm.grid(row=2, column=3, rowspan= 2)

        self.txt_blank1 =  tk.Entry(self.master, text='')
        self.txt_blank1.grid(row=0, column=1, columnspan=3)
        self.txt_blank2 = tk.Entry(self.master, text='')
        self.txt_blank2.grid(row=1, column=1, columnspan=3)







if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
