
import tkinter
from tkinter import *

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=False, height= False)
        self.master.geometry('{}x{}'.format(800, 500))
        self.master.config(bg='#fffaf3')

        self.varFname = StringVar()
        self.varLname = StringVar()

        self.lblFname = Label(self.master, text='First Name:', fg='#3a5c29', font=('Georgia', 18, 'bold'))
        self.lblFname.grid(row=0, column=0, padx=(30,0), pady=(30,0), sticky=N+E+S+W)
        self.lblLname = Label(self.master, text='Last Name:', fg='#3a5c29', font=('Georgia', 18, 'bold'))
        self.lblFname.grid(row=1, column=0, padx=(30,0), pady=(30,0), sticky=N+E+S+W)
        self.lblPhone = Label(self.master, text='Phone Number:', fg='#3a5c29', font=('Georgia', 18, 'bold'))
        self.lblPhone.grid(row=2, column=0, padx=(30,0), pady=(30,0), sticky=N+E+S+W)
        self.lblEmail =Label(self.master, text='Email Address:', fg='#3a5c29', font=('Georgia', 18, 'bold'))
        self.lblEmail.grid(row=3, column=0, padx=(30,0), pady=(30,0), sticky=N+E+S+W)
        self.lblCourse =Label(self.master, text='Current Course:', fg='#3a5c29', font=('Georgia', 18, 'bold'))
        self.lblCourse.grid(row=4, column=0, padx=(30,0), pady=(30,0), sticky=N+E+S+W)
                            


if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
