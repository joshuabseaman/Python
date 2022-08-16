from flask import render_template, request, redirect
from flask_app import app
from flask_app.models import model_dojo
from flask_app.models import model_ninja

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    return render_template('index.html', dojos=model_dojo.Dojo.get_all())

@app.route('/dojo/create', methods=['post'])
def create_dojo():
    print(request.form)
    model_dojo.Dojo.save(request.form)
    return redirect('/dojos')

@app.route('/dojo/show/<int:id>')
def show_dojo(id):
    data = {
        "id": id
    }
    return render_template("show_dojo.html", dojos=model_dojo.Dojo.get_dojo_with_ninjas(data))