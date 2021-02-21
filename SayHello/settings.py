import os
from SayHello import app

dev_db = 'sqlite:///' + os.path.join(os.path.dirname(app.root_path), 'SayHello/static/data.db')

SECRET_KEY = os.getenv('SECRET_KEY', 'YouCantGuessIt')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)
