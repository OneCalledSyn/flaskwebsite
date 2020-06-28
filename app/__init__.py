# Create the application object as an instance of class 'Flask'
from flask import Flask
from config import Config
# 'app' variable is an instance of the class 'Flask'
app = Flask(__name__)
app.config.from_object(Config)
# This is referencing the app package, not the variable app
from app import routes
# Importing routes at the bottom of the file instead of at the top avoids
# 'circular imports' issue
