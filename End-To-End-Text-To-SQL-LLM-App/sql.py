# Import module 
import sqlite3 

##connect to sqllite
connection=sqlite3.connect("student.db")

##create a cursor object to inster record, create table, retrieve
cursor=connection.cursor()

##create the table
table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SELECTION VARCHAR(25),MARKS INT);

"""
cursor.execute(table_info)

##Insert Some more record

cursor.execute('''INSERT INTO STUDENT VALUES ('Krish', 'Data Science', 'A',80)''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Darius', 'Data Science', 'B',100)''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Sudhanshu', 'Devops', 'A',86)''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Vikash', 'Data Science', 'A',50)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Dipesh', 'Devops', 'A',35)''')

##Display all the records
print("The inserted records are")

data=cursor.execute('''Select *From STUDENT''')

for row in data:
    print(row)
    
##Close the connection

connection.commit()
connection.close() 