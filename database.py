#to run SQLite commands
import sqlite3

#Where our data is going to be stored
db = sqlite3.connect('weatherStations.db')
#If we create another table 'Person' it will be ignored
db.execute('DROP TABLE IF EXISTS Student')
 #Create Table 'Person' with said attributes
db.execute("""CREATE TABLE Student(
    firstname text,
    secondname text,
    age int)""")

db.execute("INSERT INTO Student VALUES('Harry', 'Nguyen', 25)")
db.commit()

#Adds column Year to Student Table and the input would be a text ie:Freshman, Sophomore, etc.
db.execute("ALTER TABLE Student ADD Year text")
db.commit()

db.execute("UPDATE Student SET Year = 'Senior' WHERE firstname = 'Harry'")
db.commit()
#db.execute('DROP TABLE Student')
#db.commit()

#print(cur.execute("SELECT * FROM Student WHERE secondname = 'Nguyen'"))
#db.execute("DELETE * FROM Student")
#db.commit()
