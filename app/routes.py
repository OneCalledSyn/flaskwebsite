from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

# @ symbol indicates the use of 'decorators'
# Decorators dynamically alter the functionality of a function/method/class
# without directly using subclasses or changing the source code
# Think of a decorator as a wrapper
@app.route('/')
@app.route('/index')
# If the web browser requests either of the two routes in the decorators,
# Flask will invoke the 'index' function and pass the return value back to the browser
def index():
    user = {'username': 'Syniikal'}
    posts = [
        {
            'author': {'username': 'Hyponome'},
            'body': 'I am making sure the playoff map veto rules are not aids'
        },
        {
            'author': {'username': 'Ballkenende'},
            'body': 'I am eating Play-doh'
        },
        {
            'author': {'username': 'Sea.'},
            'body': 'I am rushing out of base'
        }
    ]
    return render_template('index.html', title = 'Home', user = user, posts = posts)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me = {}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title = 'Sign In', form = form)
