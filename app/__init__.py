# Create the application object as an instance of class 'Flask'
from flask import Flask
# 'app' variable is an instance of the class 'Flask' (changed name to application)
application = Flask(__name__)
# This is referencing the app package, not the variable app
from app import routes
# Importing routes at the bottom of the file instead of at the top avoids
# 'circular imports' issue
