# fetchall db data
import sqlite3
conn = sqlite3.connect("./SQL_Practice/test.db")
cursor = conn.cursor()

cursor.execute("""SELECT * from EMPLOYEE""")

result = cursor.fetchone()
print(result)

result = cursor.fetchall()
print(result)

conn.commit()
conn.close()