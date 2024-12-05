import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev_secret_key')
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL', f"sqlite:///{os.path.join(os.path.dirname(__file__), 'database', 'db_matchpoint.db')}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'app', 'static')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # Limit uploads to 16 MB
    UPLOAD_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.pdf']
