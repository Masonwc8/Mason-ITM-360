# Import necessary libraries
from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector

# Create the Flask application
app = Flask(__name__)
app.secret_key = 'your_secret_key'

def createdb():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Foxtrot8"
    )
    cursor = db.cursor()

    cursor.execute("CREATE DATABASE library_management")


# Configure the database connection
def createtable():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Foxtrot8",
        database="library_management"
    )


    cursor = db.cursor()

    library_record = """CREATE TABLE LIBRARY ( 
                    MNO  VARCHAR(50) NOT NULL, 
                    PASSWORD VARCHAR(20) NOT NULL
                    )
                    """

    cursor.execute(library_record)

def updatetable():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Foxtrot8",
        database="library_management"
    )


    cursor = db.cursor()


    cursor.execute("ALTER TABLE LIBRARY MODIFY MNO VARCHAR(50) NOT NULL PRIMARY KEY")

# Define the User class that inherits from UserMixin
class User(UserMixin):
    def __init__(self, mno, password):
        self.id = mno
        self.password = password

# Set up the LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Foxtrot8",
        database="library_management")
    cursor = db.cursor()
    cursor.execute("SELECT Mno, Password FROM Member WHERE Mno = %s", (user_id,))
    result = cursor.fetchone()
    if result:
        return User(result[0], result[0], result[1])
    return None

# Member sign-up route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        mno = request.form['mno']
        name = request.form['name']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])
        db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Foxtrot8",
        database="library_management")
        cursor = db.cursor()
        cursor.execute("INSERT INTO Member (Mno, Name, Email, Password) VALUES (%s, %s, %s, %s)", (mno, name, email, password))
        db.commit()

        return redirect(url_for('login'))

    return render_template('signup.html')

# Member authentication route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        mno = request.form['mno']
        password = request.form['password']
        db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Foxtrot8",
        database="library_management")
        cursor = db.cursor()
        cursor.execute("SELECT Mno, Password FROM Member WHERE Mno = %s", (mno,))
        result = cursor.fetchone()

        if result and check_password_hash(result[1], password):
            user = User(result[0], result[0], result[1])
            login_user(user)
            return redirect(url_for('protected'))
        else:
            return redirect(url_for('invalid'))

    return render_template('login.html')

@app.route('/invalid')
def invalid():
    return 'Invalid login credentials'

@app.route('/protected')
@login_required
def protected():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Foxtrot8",
        database="library_management")
    
    mno = current_user.id

    cursor = db.cursor()
    cursor.execute("SELECT Bname FROM Bookrecord WHERE Bno IN (SELECT Bno FROM Issue WHERE Mno = %s)", (mno,))
    books = [row[0] for row in cursor.fetchall()]
    return render_template('protected.html', books=books)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
