# drop table
import sqlite3
conn = sqlite3.connect('./SQL_Practice/test.db')
cursor = conn.cursor()

cursor.execute("""DROP TABLE IF EXISTS EMPLOYEE""")
print(cursor.fetchall())
conn.commit()
conn.close()