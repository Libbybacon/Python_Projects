# This script creates a new database and adds certain files from a given list into it.

import sqlite3

conn = sqlite3.connect('filesDB.db')

fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

# Create a new table with two fields in filesDB database 
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS fileNames(\
                ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                fileName STRING \
                )")
    conn.commit()
conn.close()


# Iterates through fileList to find files that end in '.txt'
# Then it adds those files to the fileNames table in dB
# and prints names of .txt files to console

conn = sqlite3.connect('filesDB.db')

for file in fileList:
    if file.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO fileNames(fileName) VALUES (?)", (file,)) 
        conn.commit()
        print("The following file has the '.txt' extenstion: {}".format(file))
conn.close()












