# update ing records
import sqlite3
conn = sqlite3.connect("./SQL_Practice/test.db")
cursor = conn.cursor()

sql = '''UPDATE EMPLOYEE SET AGE=AGE+1 WHERE SEX = 'M' '''
cursor.execute(sql)
print('Table updated....')

cursor.execute('''SELECT * from EMPLOYEE''')
print(cursor.fetchall())

conn.commit()
conn.close()