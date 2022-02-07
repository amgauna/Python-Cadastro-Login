import sqlite3
db=sqlite3.connect('test.db')
qry="DELETE from student where name=?;"
try:
    cur=db.cursor()
    cur.execute(qry, ('Bill',))
    db.commit()
    print("record deleted successfully")
except:
    print("error in operation")
    db.rollback()
db.close()
