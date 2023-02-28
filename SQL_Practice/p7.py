# delete
import sqlite3
conn = sqlite3.connect("./SQL_Practice/test.db")
cursor = conn.cursor()

# printing table
print("Contents of table:  ")
cursor.execute("""SELECT * from EMPLOYEE""")
print(cursor.fetchall())

# deleting data
cursor.execute('''DELETE FROM EMPLOYEE WHERE LAST_NAME = 'Pawal' ''')

# after deleting content
print("Content of table:  ")
cursor.execute("""SELECT * from EMPLOYEE""")
print(cursor.fetchall())

conn.commit()
conn.close()