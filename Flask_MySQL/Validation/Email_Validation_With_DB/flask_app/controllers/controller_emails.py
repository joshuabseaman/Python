from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models import model_email

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process',methods=['POST'])
def process():
    if not model_email.Email.is_valid(request.form):
        return redirect('/')
    model_email.Email.save(request.form)
    session['email'] = request.form['email_address']
    return redirect('/results')

@app.route('/results')
def results():
    return render_template("results.html",emails=model_email.Email.get_all())

@app.route('/destroy/<int:id>')
def destroy_email(id):
    data = {
        "id": id
    }
    model_email.Email.destroy(data)
    return redirect('/results')