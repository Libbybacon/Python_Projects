import sqlite3

with sqlite3.connect(':memory:') as connection:
    cur = connection.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Roster(Name TEXT, Species TEXT, IQ INT")
    rosterValues = (('Jean-Paptiste Zorg', 'Human', 122), ('Korben Dallas', 'Meat Popsicle', 100), ('Ak\'not', 'Mangalore', -5))
    cur.execute("INSERT INTO Roster VALUES(?,?,?)", rosterValues)

    # Change Korben Dallas species to Human
    cur.execute("UPDATE Roster SET Species=? WHERE Name=? AND IQ=?", ('Human', 'Korben Dallas', 100))

    # Display names and IQs of all humans
    cur.execute("SELECT Name, IQ FROM Roster WHERE Species=Human")
    for row in cur.fetchall():
        print(row)
        
                
 
