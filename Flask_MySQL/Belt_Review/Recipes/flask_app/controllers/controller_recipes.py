from flask import render_template, request, redirect, session, flash
from flask_app import app, bcrypt
from flask_app.models import model_recipe, model_user


@app.route('/recipes')
def recipes():
    if not session:
        return redirect('/')
    session_data = {
        "id": session['user_id']
    }
    user = model_user.User.get_one(session_data)
    recipes = model_recipe.Recipe.get_users_with_recipes()
    return render_template("recipes.html", recipes=recipes,
    user=user)
    

@app.route('/recipes/new')
def new_recipe():
    if not session:
        return redirect('/')
    return render_template("new_recipe.html")

@app.route('/recipes/create', methods=['post'])
def create_recipe():
    if not session:
        return redirect('/')
    print(request.form)
    if not model_recipe.Recipe.validate_recipe(request.form):
        return redirect('/recipes/new')
    model_recipe.Recipe.save(request.form)
    return redirect('/recipes')

@app.route('/recipes/<int:id>')
def view_recipe(id):
    if not session:
        return redirect('/')
    data = {
        "id": id
    }
    session_data = {
        "id": session['user_id']
    }
    recipes = model_recipe.Recipe.get_one_with_user(data)
    user = model_user.User.get_one(session_data)
    return render_template("view_recipe.html", recipes=recipes, user=user)

@app.route('/recipes/edit/<int:id>')
def edit_recipe(id):
    if not session:
        return redirect('/')
    # if not model_recipe.Recipe.validate_recipe(request.form):
    #     return redirect('/recipes/new')
    recipe = model_recipe.Recipe.get_one({"id":id})
    return render_template("edit_recipe.html", recipe=recipe)

@app.route('/recipes/edit/<int:id>', methods=['post'])
def return_recipe(id):
    if not session:
        return redirect('/')
    if not model_recipe.Recipe.validate_recipe(request.form):
        return redirect(f'/recipes/edit/{id}')
    recipe_data = {
        **request.form,
        "id": id,
        "user_id": session['user_id']
    }
    model_recipe.Recipe.update_one(recipe_data)
    return redirect("/recipes")

@app.route('/recipes/delete/<int:id>')
def delete_recipe(id):
    if not session:
        return redirect('/')
    model_recipe.Recipe.delete_one({"id":id})
    return redirect('/recipes')
