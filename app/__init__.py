# Create the application object as an instance of class 'Flask'
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# 'app' variable is an instance of the class 'Flask'
app = Flask(__name__)
app.config.from_object(Config)
# This is referencing the app package, not the variable app
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models
# Importing routes at the bottom of the file instead of at the top avoids
# 'circular imports' issue
