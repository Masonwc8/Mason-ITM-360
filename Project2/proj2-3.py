import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Foxtrot8",
    database="STUDENTS"
)

mycursor = mydb.cursor()

mycursor.execute("""CREATE TABLE STUDENTS(
                 STUDENTID INT NOT NULL,
                 PASSWORD VARCHAR(255) NOT NULL,
                 EMAIL LONGTEXT NOT NULL,
                 GPA FLOAT
)""")

mycursor.execute("ALTER TABLE STUDENTS MODIFY STUDENTID INT NOT NULL PRIMARY KEY")
