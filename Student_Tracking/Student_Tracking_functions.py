# Python Version:   3.9.1
#
# Author:   Elizabeth Bacon
#
# Purpose: Student Tracker Demo.  Use OOP, Tkinter GUI module,
#           show Parent/Child relationships, create & utlize dB with sqlite3
import os
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import sqlite3
import Student_Tracking_main
import Student_Tracking_gui

# Create Student_Tracker dB
def create_db(self):
    conn = sqlite3.connect('db_StudentTracker.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_StudentTracker(\
                    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                    col_Fname TEXT, \
                    col_Lname TEXT, \
                    col_FullName TEXT, \
                    col_Phone TEXT, \
                    col_Email TEXT, \
                    col_Course TEXT \
                    );")
        conn.commit()
    conn.close()
    first_run(self)

# Make first entry on first run so there is something in the dB
def first_run(self):
    conn = sqlite3.connect('db_StudentTracker.db')
    with conn:
        cur = conn.cursor()
        cur, count = count_records(cur)
        if count < 1:
            cur.execute("""INSERT INTO tbl_StudentTracker(col_Fname, col_Lname, col_FullName, col_Phone, col_Email, col_Course)\
                        VALUES(?,?,?,?,?,?)""",('testFname', 'testLname', 'testFname testLname', '000-000-0000','test@email.com', 'testCourse'))
            conn.commit
    conn.close()

def count_records(cur):
    count = ''
    cur.execute("""SELECT COUNT(*) FROM tbl_StudentTracker""")
    count = cur.fetchone()[0]
    return cur, count

# Select a student in the listbox
def onSelect(self, event):
    varMainList = event.widget
    select = varMainList.curselection()[0]
    value = varMainList.get(select)
    conn = sqlite3.connect('db_StudentTracker.db')
    with conn:
        cur = conn.cursor()
        cur.execute("""SELECT col_Fname, col_Lname, col_Phone, col_Email, col_Course FROM tbl_StudentTracker WHERE col_FullName = (?)""", [value])
        varBody = cur.fetchall()
        for data in varBody:
            self.txt_Fname.delete(0, END)
            self.txt_Fname.insert(0, data[0])
            self.txt_Lname.delete(0, END)
            self.txt_Lname.insert(0, data[1])
            self.txt_Phone.delete(0, END)
            self.txt_Phone.insert(0, data[2])
            self.txt_Email.delete(0, END)
            self.txt_Email.insert(0, data[3])
            self.txt_Course.delete(0, END)
            self.txt_Course.insert(0, data[4])
           
                    
# Add new entry to main list
def addToList(self):
    var_Fname = self.txt_Fname.get().strip().title()
    var_Lname = self.txt_Lname.get().strip().title()
    var_FullName = ("{} {}".format(var_Fname, var_Lname))
    print('var_FullName: {}'.format(var_FullName))
    var_Phone = self.txt_Phone.get().strip()
    var_Email = self.txt_Email.get().strip()
    var_Course = self.txt_Course.get().strip()

    # Make sure user enters all fields
    if(len(var_Fname) > 0) and (len(var_Fname) > 0) and (len(var_Phone) > 0) and (len(var_Email) > 0) and (len(var_Course) > 0):
        conn = sqlite3.connect('db_StudentTracker.db')
        with conn:
            cur = conn.cursor()
            cur.execute("""SELECT COUNT(col_FullName) FROM tbl_StudentTracker WHERE col_FullName = '{}'""".format(var_FullName))
            count = cur.fetchone() [0]
            checkName = count
            if checkName == 0:
                cur.execute("""INSERT INTO tbl_StudentTracker (col_Fname, col_Lname, col_FullName, col_Phone, col_Email, col_Course)\
                            VALUES (?,?,?,?,?,?)""",(var_Fname, var_Lname, var_FullName, var_Phone, var_Email, var_Course))
                self.lst_MainList.insert(END, var_FullName)
                onClear(self)
                #########onRefresh(self)
                
            else:
                messagebox.showerror("Name Error", "'{}' already exists in the Student database.".format(var_FullName))
        conn.commit()
        conn.close()
    else:
        messagebox.showerror("Missing Value Error", "Please fill every field.")

    

# Delete student from the main list
def deleteFromList(self):
    var_select = self.lst_MainList.get(self.lst_MainList.curselection())
    conn = sqlite3.connect('db_StudentTracker.db')
    with conn:
        cur = conn.cursor()
        cur.execute("""SELECT COUNT(*) FROM tbl_StudentTracker""")
        count = cur.fetchone()[0]
        if count > 1:
            confirm = messagebox.askokcancel("Delete Student Confirmation", "The student '{}' and all corresponding information\
                                            will be permanently deleted from the student database.\
                                            \n\nProceed with Delete request?".format(var_select))
            if confirm:
                conn = sqlite3.connect('db_StudentTracker.db')
                with conn:
                    cur = conn.cursor()
                    cur.execute("""DELETE FROM tbl_StudentTracker WHERE col_FullName = '{}'""".format(var_select))
                onRefresh(self)
                onClear(self)
                conn.commit()
        else:
            messagebox.showerror("Last Record Error", "'{}' is the last student in the database and cannot be deleted at this time.\
                                \n\nAnother student must be added before deleting '{}'".format(var_select, var_select))
    conn.close()
                                
            
# Clear all text from input boxes            
def onClear(self):
    self.txt_Fname.delete(0, END)
    self.txt_Lname.delete(0, END)
    self.txt_Phone.delete(0, END)
    self.txt_Email.delete(0, END)
    self.txt_Course.delete(0, END)

# Refresh main list to reflect changes in dB
def onRefresh(self):
    self.lst_MainList.delete(0, END)
    conn = sqlite3.connect('db_StudentTracker.db')
    with conn:
        cur = conn.cursor()
        cur.execute("""SELECT COUNT (*) FROM tbl_StudentTracker""")
        count = cur.fetchone()[0]
        i = 0
        while i < count:
            cur.execute("""SELECT col_FullName FROM tbl_StudentTracker""")
            varList = cur.fetchall()[i]
            for item in varList:
                self.lst_MainList.insert(0, str(item))
                i = i + 1
                
    conn.close()


if __name__ == "__main__":
    pass
            
            
            
