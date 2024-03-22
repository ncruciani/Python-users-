from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import users #importing the class here
#There will be other imports need depending what you're trying to use in this file
#You will also need a bycrypt import (we will introduce this week 5)


@app.route('/') #Get request for 127.0.0.1:5000
def home():
    return render_template('index.html')

@app.route('/create/user', methods =['POST'])
def create_user():
    data = {
        'first_name' : request.form['first_name'] , 
        'last_name' : request.form['last_name'] , 
        'email' : request.form['email']
    }

    users.save(data)
    return redirect('/create')

@app.route('/create')
def created_users():
    user_data = users.userdata()
    data=[]
    for user in user_data:
        data.append(
            {'id': user.id , 'first_name': user.first_name , 'last_name' : user.last_name , 'email' : user.email , 'created_at': user.created_at}
        ) 
    print(data)
    return render_template('create.html' , people = data)
