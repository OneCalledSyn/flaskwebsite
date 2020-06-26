from flask import render_template
from app import application

# @ symbol indicates the use of 'decorators'
# Decorators dynamically alter the functionality of a function/method/class
# without directly using subclasses or changing the source code
# Think of a decorator as a wrapper
@application.route('/')
@application.route('/index')
# If the web browser requests either of the two routes in the decorators,
# Flask will invoke the 'index' function and pass the return value back to the browser
def index():
    user = {'username': 'Syniikal'}
    posts = [
        {
            'author': {'username': 'Giga Brain Wongderful'},
            'body': 'The Marvel movies are actually just a worse version of anime'
        },
        {
            'author': {'username': 'Mega Mind Legman'},
            'body': 'Beautiful day to stay inside away from COVID-19'
        }
    ]
    return render_template('index.html', title = 'Home', user = user, posts = posts)
