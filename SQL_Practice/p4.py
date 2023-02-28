# where statement
import sqlite3
conn = sqlite3.connect('./SQL_Practice/test.db')
cursor = conn.cursor()

cursor.execute("""
    SELECT * 
    from EMPLOYEE 
    WHERE AGE > 25
""")

print(cursor.fetchall())

conn.commit()
conn.close()