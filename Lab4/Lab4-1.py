from flask import Flask
from flask_login import LoginManager
from .blueprints.auth import auth_blueprint
from .models import db_config

def create_app():
    app = Flask(__name__)
    app.secret_key = 'your_secret_key'
    
    # Initialize LoginManager
    login_manager = LoginManager()
    login_manager.init_app(app)

    # Database setup
    db_config(app)

    # Register blueprints
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
