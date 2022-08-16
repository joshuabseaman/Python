from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.model_ninja import Ninja
from flask_app.models.model_dojo import Dojo

@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html', dojos=Dojo.get_all())

@app.route('/ninja/create', methods=['post'])
def create_ninja():
    print(request.form)
    Ninja.save(request.form)
    return redirect(f'/dojo/show/{request.form["dojo_id"]}')