from flask import render_template, request, redirect, session, flash
from flask_app import app, bcrypt
from flask_app.models import model_user

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register',methods=['POST'])
def register():
    if not model_user.User.validate_registration(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password" : pw_hash,
        "confirm_password": pw_hash
    }
    user_id = model_user.User.save(data)
    session['user_id'] = user_id
    return redirect('/results')

@app.route('/login',methods=['POST'])
def login():
    if not model_user.User.validate_login(request.form):
        return redirect('/')
    data = { "email" : request.form["email"] }
    user_in_db = model_user.User.get_by_email(data)
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Email/Password")
        return redirect('/')
    session['user_id'] = user_in_db.id
    return redirect("/results")

@app.route('/results')
def results():
    if not id in session:
        return redirect('/')
    data = {
        "id": session['user_id']
    }
    return render_template("results.html",users=model_user.User.get_one(data))

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

