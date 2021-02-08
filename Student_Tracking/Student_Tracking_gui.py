# Python Version:   3.9.1
#
# Author:   Elizabeth Bacon
#
# Purpose: Student Tracker Demo.  Use OOP, Tkinter GUI module,
#           show Parent/Child relationships, create & utilize dB with sqlite3



from tkinter import *
from tkinter import messagebox
import tkinter as tk
import Student_Tracking_main as Student_main
import Student_Tracking_functions as Student_func

def load_gui(self):
            # Create labels for entries
        self.lbl_Student = Label(self.master, text='Students:', fg='#3a5c29', font=('Georgia', 18, 'bold'))
        self.lbl_Student.grid(row=0, column=3, padx=(10,50), pady=(50,0), sticky=N+E+W)
        self.lbl_Fname = Label(self.master, text='First Name:', fg='#3a5c29', font=('Georgia', 18, 'bold'))
        self.lbl_Fname.grid(row=1, column=0, padx=(30,0), pady=(10,0), sticky=N+E+W)
        self.lbl_Lname = Label(self.master, text='Last Name:', fg='#3a5c29', font=('Georgia', 18, 'bold'))
        self.lbl_Lname.grid(row=2, column=0, padx=(30,0), pady=(10,0), sticky=N+E+W)
        self.lbl_Phone = Label(self.master, text='Phone Number:', fg='#3a5c29', font=('Georgia', 18, 'bold'))
        self.lbl_Phone.grid(row=3, column=0, padx=(30,0), pady=(10,0), sticky=N+E+W)
        self.lbl_Email =Label(self.master, text='Email Address:', fg='#3a5c29', font=('Georgia', 18, 'bold'))
        self.lbl_Email.grid(row=4, column=0, padx=(30,0), pady=(10,0), sticky=N+E+W)
        self.lbl_Course =Label(self.master, text='Current Course:', fg='#3a5c29', font=('Georgia', 18, 'bold'))
        self.lbl_Course.grid(row=5, column=0, padx=(30,0), pady=(10,0), sticky=N+E+W)


        # Create entry boxes
        self.txt_Fname = tk.Entry(self.master, text='', font=('Georgia', 18))
        self.txt_Fname.grid(row=1, column=1, columnspan=1, padx=(10,50), pady=(10,0), sticky=N+W)
        self.txt_Lname = tk.Entry(self.master, text='', font=('Georgia', 18))
        self.txt_Lname.grid(row=2, column=1, padx=(10,50), pady=(10,0), sticky=N+E+W)
        self.txt_Phone = tk.Entry(self.master, text='', font=('Georgia', 18))
        self.txt_Phone.grid(row=3, column=1, padx=(10,50), pady=(10,0), sticky=N+E+W)
        self.txt_Email = tk.Entry(self.master, text='', font=('Georgia', 18))
        self.txt_Email.grid(row=4, column=1, padx=(10,50), pady=(10,0), sticky=N+E+W)
        self.txt_Course = tk.Entry(self.master, text='', font=('Georgia', 18))
        self.txt_Course.grid(row=5, column=1, padx=(10,50), pady=(10,0), sticky=N+E+W)

        # Create listbox & scroolbar
        self.scrollbar = Scrollbar(self.master, orient=VERTICAL)
        self.lst_MainList = Listbox(self.master, exportselection=0, yscrollcommand=self.scrollbar.set)
        self.lst_MainList.bind('<<ListboxSelect>>', lambda event: Student_func.onSelect(self,event))
        self.scrollbar.config(command=self.lst_MainList.yview)
        self.lst_MainList.grid(row=1, column=3, rowspan=9, columnspan=4, padx=(0,0), pady=(10,0), sticky=N+E+S+W)
        self.scrollbar.grid(row=1, column = 8, rowspan=9, padx=(10,0), pady=(10,0), sticky=N+E+S+W)
        

        # Submit and Delete buttons:
        self.btn_add = tk.Button(self.master, width=8, height=2, text='Add', command=lambda: Student_func.addToList(self))
        self.btn_add.grid(row=10, column=3, sticky=W)
        self.btn_delete = tk.Button(self.master, width=8, height=2, text='Delete', bg='red', command=lambda: Student_func.deleteFromList(self))
        self.btn_delete.grid(row=10, column=4)

        Student_func.create_db(self)
        Student_func.onRefresh(self)
             


if __name__ == "__main__":
    pass
