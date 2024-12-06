from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_socketio import SocketIO
from flask_login import LoginManager
from flask_mail import Mail
from config import Config, FlaskConfig

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
socketio = SocketIO()
login_manager = LoginManager()
mail = Mail()

def create_app():
    app = Flask(__name__)
    config = Config()
    app.config.from_object(FlaskConfig)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    socketio.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    # Optionally load additional app-specific config
    app_config = Config()  # Load .yaml and .env
    app.yaml_config = app_config.yaml_config  # Access custom settings as needed

    # Set up login manager
    login_manager.login_view = "main.login"
    login_manager.login_message = "Please log in to access this page."
    login_manager.login_message_category = "info"

    # User loader for Flask-Login
    from .models import User  # Import User model
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))  # Retrieve user by ID

    # Import and register blueprints
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
