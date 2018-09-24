from ventout.models import User, Post
from flask import render_template, url_for, flash, redirect
from ventout.forms import RegistrationForm, LoginForm
from flask import Request
from flask_login import login_user
from ventout import app, db, bcrypt

my_posts = [{'title': 'Post 1', 'author': 'Nikhil', 'content': 'It is the first blog', 'date': '21 September, 2018'},
            {'title': 'Post 2', 'author': 'Prabhakar',
                'content': 'It is the second blog', 'date': '22 September, 2018'},
            {'title': 'Post 3', 'author': 'Styler', 'content': 'It is the third blog', 'date': '23 September, 2018'}]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=my_posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        user = User(username=form.username.data,
                    email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):    
            login_user(user, remember=form.remember.data)
            flash(f'Welcome {user.username}!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Wrong Username or Password', 'danger')
    return render_template('login.html', title='Login', form=form)