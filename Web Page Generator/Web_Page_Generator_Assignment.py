#   Python version:   3.9.1
#
#   Author: Elizabeth Bacon   
#
#   Purpose:
#   Create GUI that let's user input text and initiate page generation process
#   Web page sets user's input as body text


# Import all necessary modules
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import font
import webbrowser 


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.title('Web Page Generator')
        self.master.geometry('{}x{}'.format(700,500))

        self.lbl_Update = tk.Label(self.master, text='Enter the text you would like the website to display:')
        self.lbl_Update.grid(row=0, column=0, columnspan=8, padx=(30,30), pady=(20,0), sticky=E+W)
        master.columnconfigure(0, weight=4)

        # Scrolled text box where user can enter as much text as they want
        self.txt_newText = scrolledtext.ScrolledText(self.master, wrap=tk.WORD)
        self.txt_newText.grid(row=1, column=0, columnspan=8, padx=(30,30), pady=(20,20), sticky=N+E+S+W)
        master.rowconfigure(1, weight=12)

        # Sumbit Changes button that calls generateWebPage function
        buttonFont = font.Font(size=16, weight='bold')
        self.btn_SubmitChanges = Button(self.master, text='Submit \nChanges', width= 9, height=3, bg='red', font=buttonFont, command= lambda: generateWebPage(self))
        self.btn_SubmitChanges.grid(row=14, column=1, rowspan=2, pady=(20,40), sticky=N+S+W)
        master.columnconfigure(1, weight=4)

# Function that saves user's text input as stringVar
# Then opens the html file for the web page
# And inserts text into the body of the page
# Then opens the page in a new tab in the default browser
def generateWebPage(self):
    newBodyText = self.txt_newText.get('1.0', tk.END)
    print(newBodyText)
    f = open("WebPageGenerator.html", "w")
    f.write('<html> \n\t<body> \n\t\t<h1> {} \n\t\t</h1> \n\t</body> \n</html>'.format(newBodyText))
    f.close()
    url = ('file:///Users/Libby/Python Practice/WebPageGenerator.html')
    webbrowser.open_new_tab(url)
        
    

            
if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
                        
            
