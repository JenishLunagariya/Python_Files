import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
sql = '''
        CREATE TABLE EMPLOYEE(
            FIRST_NAME CHAR(20) NOT NULL,
            LAST_NAME CHAR(20),
            AGE INT,
            SEX CHAR(1),
            INCOME FLOAT
        )
        '''
cursor.execute()