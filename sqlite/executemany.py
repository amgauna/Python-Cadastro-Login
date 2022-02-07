# The executemany() method is used to add multiple records at once. 
# Data to be added should be given in a list of tuples, with each 
# tuple containing one record. The list object (containing tuples) 
# is the parameter of the executemany() method, along with the query string.

# Example: Copy

import sqlite3
db=sqlite3.connect('test.db')
qry="insert into student (name, age, marks) values(?,?,?);"
students=[('Amar', 18, 70), ('Deepak', 25, 87)]
try:
    cur=db.cursor()
    cur.executemany(qry, students)
    db.commit()
    print ("records added successfully")
except:
    print ("error in operation")
    db.rollback()
db.close()
