from flask_app import app
from flask import render_template,request,redirect
from flask_app.models.user import User

@app.route('/users')
def index():
    users = User.get_all()
    return render_template("read_all.html",users=users)

@app.route('/users/new')
def new_user():
    return render_template("create.html")

@app.route('/users', methods=['POST'])
def create():
    User.create(request.form)
    return redirect('/users')

@app.route('/users/<int:user_id>')
def one_user(user_id):
    data = {
        'id':user_id
    }
    user = User.get_one(data)
    return render_template('read_one.html',user=user)
@app.route('/users/<int:user_id>/edit')
def edit_user(user_id):
    user = User.get_one({'id':user_id})
    return render_template("edit_user.html",user=user)

@app.route('/users/<int:user_id>/edit', methods=['POST'])
def update_user(user_id):
    data = {
        "first_name":request.form["first_name"],
        "last_name":request.form["last_name"],
        "email":request.form["email"],
        "id":user_id
        }
    User.update(data)
    return redirect('./edit')

@app.route('/users/<int:user_id>/delete')
def delete(user_id):
    User.delete(user_id)
    return redirect('/users')