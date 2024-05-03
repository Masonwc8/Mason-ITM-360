import mysql.connector
from flask import Flask
from server.blueprint_script import blueprint

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Foxtrot8",
        database="STUDENT_LOGIN"
    )

def initialize_db():
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255),
            password VARCHAR(255)
        );
    """)
    db.commit()
    db.close()



app = Flask(__name__)
app.secret_key = 'your_super_secret_key'
app.register_blueprint(blueprint)

if __name__ == '__main__':
    from database.db import initialize_db
    initialize_db()  # Initialize the database tables
    app.run(debug=True)