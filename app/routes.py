from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, login_required, logout_user
from app.models import User
from flask import request
from werkzeug.urls import url_parse

# @ symbol indicates the use of 'decorators'
# Decorators dynamically alter the functionality of a function/method/class
# without directly using subclasses or changing the source code
# Think of a decorator as a wrapper
@app.route('/')
@app.route('/index')
@login_required
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
    return render_template('index.html', title = 'Home', posts = posts)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title = 'Sign In', form = form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title = 'Register', form = form)
