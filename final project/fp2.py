from flask import Blueprint, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
from database.db import get_db_connection #no external module named as database

blueprint = Blueprint('blueprint', __name__)

@blueprint.route('/login', methods=['POST'])
def login():
    db = get_db_connection()
    cursor = db.cursor()
    data = request.json
    cursor.execute("SELECT id, password FROM users WHERE username = %s", (data['username'],))
    user = cursor.fetchone()
    if user and check_password_hash(user[1], data['password']):
        session['user_id'] = user[0]
        return jsonify({'message': 'Login succeeded!'}), 200
    return jsonify({'message': 'Login failed'}), 401

@blueprint.route('/protected', methods=['GET'])
# flask_login.login_required -5pts
def protected():
    if 'user_id' not in session:
        return jsonify({'message': 'Unauthorized'}), 401
    return jsonify({'message': 'You are viewing a protected route'}), 200
