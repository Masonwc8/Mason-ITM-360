from flask import Blueprint, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector

blueprint = Blueprint('blueprint', __name__)

@blueprint.route('/signup', methods=['POST'])
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

@blueprint.route('/login', methods=['POST'])
def login():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Foxtrot8",
        database="STUDENT_LOGIN"
    )
    data = request.json
    mycursor = db.cursor()
    mycursor.execute("SELECT Password, StudentID FROM Students WHERE Email = %s", (data['Email'],))
    record = mycursor.fetchone()
    if record and check_password_hash(record[0], data['Password']):
        session['student_id'] = record[1]  # Save the student id in session #session is not yet declared; -5pts
        return jsonify({'message': 'Login succeeded!'}), 200
    return jsonify({'message': 'Login failed! Wrong email or password'}), 401

@blueprint.route('/gpa', methods=['GET'])
#@flask_login.login_required, so it is protected for authenticated user only; -5pts
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
