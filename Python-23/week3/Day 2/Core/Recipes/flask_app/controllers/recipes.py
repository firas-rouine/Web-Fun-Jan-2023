from flask_app import app
from flask_app.models.recipe import Recipe
from flask_app.models.user import User
from flask import request , redirect, session, render_template, flash


@app.route('/recipes/new' )
def new_recipe():
    if 'user_id' not in session:
        return redirect('/') 
    return render_template("new_recipe.html") 

@app.route('/recipes/create', methods=['POST'])
def add_party():
    if 'user_id' not in session:
        return redirect('/') 
    if not Recipe.validate_party(request.form):
        return redirect("/recipes/new")
    data = {
        **request.form,
        'user_id': session["user_id"] 
    }
    Recipe.create_recipe(data)
    
    return redirect("/dashboard")

@app.route('/recipes/<int:id>')
def show_party(id):
    if 'user_id' not in session:
        return redirect('/') 
    recipe = Recipe.get_by_id({'id':id})
    user = User.get_by_id({'id':id})
    return render_template("show_recipe.html",  recipe = recipe ,user=user)


@app.route('/recipes/<int:id>/edit')
def edit_recipe(id):
    if 'user_id' not in session:
        return redirect('/') 
    recipe = Recipe.get_by_id({'id':id})
    return render_template("edit_recipe.html",  recipe = recipe)


@app.route('/recipes/<int:id>/update',methods=['post'])
def update_recipe(id):
    if not Recipe.validate_recipe(request.form):
        return redirect(f"/recipes/{id}/edit")
    Recipe.update_recipe(request.form)
    return redirect('/dashboard')

@app.route('/recipes/<int:id>/delete')
def delete_recipes(id):
    Recipe.delete_recipes({'id':id})
    return redirect('/dashboard')


