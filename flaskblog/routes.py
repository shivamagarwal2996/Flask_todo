from flaskblog.models import User, Post, Task
from flask import Flask, render_template, url_for, flash, redirect
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog import app,db
from flask import request, jsonify



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
        'date_posted': 'Jan 20 2018'
    
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


@app.route("/entry",methods=['POST'])
def entry():
    req_data = request.get_json()

    title = req_data['title']
    task = Task(title=title,completed=0)
    db.session.add(task)
    print(task)
    db.session.commit()
    #print(task_name)
    data = {
            'title':task.title,
            'completed':bool(task.completed),
            'id':task.id,
            'userId':task.userId
        }
    

    return( jsonify(data)) 

@app.route("/get_entries",methods=['GET'])
def get_entries():
    
    list_of_tasks = get_all_tasks()

    return( jsonify(list_of_tasks)) 

@app.route("/delete_entry",methods=['POST'])
def delete_entry():

    req_data = request.get_json()

    id = req_data['id']

    entry = Task.query.filter_by(id =id).first()
    if entry is None:
        return("entry with this id doesnot exist")
    #print(entry.content)
    db.session.delete(entry)
    db.session.commit()

    list_of_tasks = get_all_tasks()

    return( jsonify(list_of_tasks))    


@app.route("/update_entry",methods=['PATCH'])
def update_entry():

    req_data = request.get_json()

    id = req_data['id']

    entry = Task.query.filter_by(id =id).first()
    if entry is None:
        return("entry with this id doesnot exist")
    #print(entry.content)
    if entry.completed == 0:
        entry.completed = 1
    else:
        entry.completed = 0

    db.session.commit()

    list_of_tasks = get_all_tasks()

    return( jsonify(list_of_tasks))    
    

def get_all_tasks():
    list1 = []
    entries = Task.query.all()
    for entry in entries:
        data = {
            'title':entry.title,
            'completed':bool(entry.completed),
            'id':entry.id,
            'userId':entry.userId
        }
        list1.append(data)
    return (list1)
