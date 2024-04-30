import mysql.connector
from flask_login import UserMixin

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Foxtrot8",
        database="library_management"
    )

def db_config(app):
    # Here you could initialize a more Flask-friendly ORM if needed
    pass

class User(UserMixin):
    def __init__(self, mno, password):
        self.id = mno
        self.password = password

    # User loader
    @staticmethod
    def load_user(user_id):
        db = connect_db()
        cursor = db.cursor()
        cursor.execute("SELECT Mno, Password FROM Member WHERE Mno = %s", (user_id,))
        result = cursor.fetchone()
        if result:
            return User(result[0], result[1])
        return None
