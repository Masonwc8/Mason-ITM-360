from flask import Flask, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_super_secret_key'

def db():
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Foxtrot8",
            database="STUDENT_LOGIN"
        )

        mycursor = db.cursor()


        mycursor.execute("""CREATE TABLE STUDENTS(
                        STUDENTID INT NOT NULL,
                        PASSWORD VARCHAR(255) NOT NULL,
                        EMAIL LONGTEXT NOT NULL,
                        GPA FLOAT
        )""")

        mycursor.execute("ALTER TABLE STUDENTS MODIFY STUDENTID INT NOT NULL PRIMARY KEY")

        mycursor = db.cursor(buffered=True)

@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    


    db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Foxtrot8",
            database="STUDENT_LOGIN"
        )

    mycursor = db.cursor()
    try:
        hashed_password = generate_password_hash(data['Password'])
        mycursor.execute("INSERT INTO Students (StudentID, Email, Password, GPA) VALUES (%s, %s, %s, %s)",
                       (data['StudentID'], data['Email'], hashed_password, data['GPA']))
        db.commit()
        return jsonify({'message': 'Signup successful'}), 200
    except mysql.connector.Error as err:
        return jsonify({'message': str(err)}), 400

@app.route('/login', methods=['POST'])
def login():
    db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Foxtrot8",
            database="STUDENT_LOGIN"
        )
    studentid = request.form.get("StudentID")
    password = request.form.get("Password")

    mycursor = db.cursor()
    data = request.json
    mycursor.execute("SELECT Password, StudentID FROM Students WHERE Email = %s", (data['Email'],))
    record = mycursor.fetchone()
    if record and check_password_hash(record[0], data['Password']):
        session['student_id'] = record[1]  # Save the student id in session
        return jsonify({'message': 'Login succeeded!'}), 200
    return jsonify({'message': 'Login failed! Wrong email or password'}), 401

@app.route('/gpa', methods=['GET'])
def get_gpa():
    db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Foxtrot8",
            database="STUDENT_LOGIN"
        )

    mycursor = db.cursor()
    if 'student_id' in session:
        mycursor.execute("SELECT GPA FROM Students WHERE StudentID = %s", (session['student_id'],))
        gpa = mycursor.fetchone()
        if gpa:
            return jsonify({'GPA': gpa[0]}), 200
        else:
            return jsonify({'message': 'GPA not found'}), 404
    return jsonify({'message': 'Unauthorized access'}), 401

if __name__ == '__main__':
    app.run(debug=True)


db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Foxtrot8",
            database="STUDENT_LOGIN"
        )

mycursor = db.cursor()





