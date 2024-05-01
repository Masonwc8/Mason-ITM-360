from flask import Blueprint, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector

password_manager_bp = Blueprint('password_manager', __name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Foxtrot8",
    database="STUDENTS"
)

cursor = db.cursor(buffered=True)

@password_manager_bp.route('/signup', methods=['POST'])
def signup():
    data = request.json
    try:
        hashed_password = generate_password_hash(data['Password'])
        cursor.execute("INSERT INTO Students (StudentID, Email, Password, GPA) VALUES (%s, %s, %s, %s)",
                       (data['StudentID'], data['Email'], hashed_password, data['GPA']))
        db.commit()
        return jsonify({'message': 'Signup successful'}), 200
    except mysql.connector.Error as err:
        return jsonify({'message': str(err)}), 400

@password_manager_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    cursor.execute("SELECT Password, StudentID FROM Students WHERE Email = %s", (data['Email'],))
    record = cursor.fetchone()
    if record and check_password_hash(record[0], data['Password']):
        session['student_id'] = record[1]  # Save the student id in session
        return jsonify({'message': 'Login succeeded!'}), 200
    return jsonify({'message': 'Login failed! Wrong email or password'}), 401

@password_manager_bp.route('/gpa', methods=['GET'])
def get_gpa():
    if 'student_id' in session:
        cursor.execute("SELECT GPA FROM Students WHERE StudentID = %s", (session['student_id'],))
        gpa = cursor.fetchone()
        if gpa:
            return jsonify({'GPA': gpa[0]}), 200
        else:
            return jsonify({'message': 'GPA not found'}), 404
    return jsonify({'message': 'Unauthorized access'}), 401
