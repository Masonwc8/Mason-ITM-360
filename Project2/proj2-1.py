from flask import Flask
from password_manager_blueprint import password_manager_bp

app = Flask(__name__)
app.register_blueprint(password_manager_bp)

if __name__ == "__main__":
    app.run(debug=True)
