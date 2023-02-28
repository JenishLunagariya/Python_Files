import sqlite3
conn = sqlite3.connect("./SQL_Practice/test.db")
cursor = conn.cursor()

# insert into table
cursor.execute("""
        INSERT INTO EMPLOYEE(
            FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)
            VALUES ('Jenish','Lunagariya',21,'M',30000)
""")

cursor.execute("""
        INSERT INTO EMPLOYEE(
            FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)
            VALUES ('Nihar','Desai',24,'M',40000)
        
""")

cursor.execute("""
        INSERT INTO EMPLOYEE(
            FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)
            VALUES ('Tushar','Bafna',27,'M',80000)
        
""")

cursor.execute("""
        INSERT INTO EMPLOYEE(
            FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)
            VALUES ('Haresh','Savliya',30,'M',100000)
        
""")

cursor.execute("""
        INSERT INTO EMPLOYEE(
            FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)
            VALUES ('Yogi','Pawal',26,'M',70000)
        
""")
conn.commit()
print("Records inserted....")
conn.close()