#to run SQLite commands
import sqlite3

#Where our data is going to be stored
db = sqlite3.connect('database.db')
#If we create another table 'Person' it will be ignored
db.execute('DROP TABLE IF EXISTS Student')
 #Create Table 'Person' with said attributes
db.execute("""CREATE TABLE Student(
    firstname text,
    secondname text,
    age int)""")

db.execute("INSERT INTO Student VALUES('Harry', 'Nguyen', 25)")
db.commit()
db.execute("SELECT * FROM Student WHERE secondname = 'Nguyen'")
print(fetchall())
