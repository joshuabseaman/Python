from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.model_dojo import Dojo
from flask_app.models.model_ninja import Ninja

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    return render_template('index.html', dojos=Dojo.get_all())

@app.route('/dojo/create', methods=['post'])
def create_dojo():
    print(request.form)
    Dojo.save(request.form)
    return redirect('/dojos')

@app.route('/dojo/show/<int:id>')
def show_dojo(id):
    data = {
        "id": id
    }
    return render_template("show_dojo.html", dojos=Dojo.get_dojo_with_ninjas(data))