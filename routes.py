from flaskblog.models import User, Post
from flask import Flask, render_template, url_for, flash, redirect
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog import app,db


posts = [
    {
        'author' : 'Shivam Agarwal',
        'title': 'Blog Post',
        'content': 'First Post content',
        'date_posted': 'April 20 2018'
    
    },
    {
        'author' : 'Saksham Dubey',
        'title': 'Blog Post 2',
        'content': 'Seond Post content',
        'date_posted': 'Jan 20 2018'exiy
    
    }

]

@app.route("/")
def home():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/register",methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        print(user)
        db.session.commit()
        flash('Account created','success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login",methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Please check username and password','danger')
    return render_template('login.html', title='login', form=form)