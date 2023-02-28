# orderby statement
import sqlite3
conn = sqlite3.connect('./SQL_Practice/test.db')
cursor = conn.cursor()

cursor.execute('''
    INSERT INTO EMPLOYEE (FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) 
    VALUES ('Ramya','Priya',27,'F',90000)
''')
# BUG: Below code not working
# cursor.execute('''
#     INSERT INTO EMPLOYEE (FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)
#     VALUES  ('Vinay','Bhattacharya',20,'M',60000),
#             ('Sharukh','Sheik',25,'M',83000)
#             ('Sarmista','Sharma',26,'F',100000),
#             ('Sandeep','Mishra',24,'F',50000);
# ''')
conn.commit()

cursor.execute("SELECT * from EMPLOYEE ORDER BY FIRST_NAME")

print(cursor.fetchall())

conn.commit()
conn.close()