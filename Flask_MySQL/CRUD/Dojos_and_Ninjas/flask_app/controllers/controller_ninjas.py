from flask import render_template, request, redirect
from flask_app import app
from flask_app.models import model_ninja
from flask_app.models import model_dojo

@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html', dojos=model_dojo.Dojo.get_all())

@app.route('/ninja/create', methods=['post'])
def create_ninja():
    print(request.form)
    model_ninja.Ninja.save(request.form)
    return redirect(f'/dojo/show/{request.form["dojo_id"]}')