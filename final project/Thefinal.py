# The modules in this folder do not talk with other; the app will execute given their independencies; -30pts
# missing a README file explaining the structure and the functionalities this app can serve. -10pts


import mysql.connector
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    # Implement login functionality
    data = request.get_json() 
    username = data['username']
    password = data['password']
    # Verify username and password from database
    return jsonify({"message": "Login successful"})  # Placeholder

# Add more routes for task management 

if __name__ == '__main__':
    app.run(debug=True)


class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Foxtrot8",
            database="Task_Manager"
        )
        self.cursor = self.connection.cursor()
    
        self.cursor.execute("CREATE DATABASE Task_Manager")
    def create_tables(self):
        # Create tables if not exists
        user_table = """CREATE TABLE IF NOT EXISTS users (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            username VARCHAR(50) UNIQUE NOT NULL,
                            password VARCHAR(50) NOT NULL
                        )"""
        task_table = """CREATE TABLE IF NOT EXISTS tasks (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            title VARCHAR(100) NOT NULL,
                            description TEXT,
                            completed BOOLEAN DEFAULT FALSE,
                            user_id INT,
                            FOREIGN KEY (user_id) REFERENCES users(id)
                        )"""
        self.cursor.execute(user_table)
        self.cursor.execute(task_table)
        self.connection.commit()

    def insert_user(self, username, password):
        # Insert user into users table
        query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        self.cursor.execute(query, (username, password))
        self.connection.commit()

    def get_user_by_credentials(self, username, password):
        # Retrieve user by username and password
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        self.cursor.execute(query, (username, password))
        user = self.cursor.fetchone()
        return user

    def close(self):
        # Close database connection
        self.cursor.close()
        self.connection.close()

# Usage example
def main():
    db = Database()
    db.create_tables()
    db.insert_user("testuser", "testpassword")
    user = db.get_user_by_credentials("testuser", "testpassword")
    print(user)  # Should print user details if found
    db.close()

if __name__ == "__main__":
    main()

