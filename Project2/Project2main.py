from flask import Flask
from blueprint_script import blueprint

app = Flask(__name__)
app.secret_key = 'your_super_secret_key'

app.register_blueprint(blueprint)

if __name__ == '__main__':
    app.run(debug=True)