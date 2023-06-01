from flask_app import app
from flask import render_template, redirect, request,session
from flask_app.models.ninja import Ninja

from flask_app.models.dojo import Dojo

@app.route('/ninjas')
def new_book():
    dojos = Dojo.get_all()
    return render_template("new_ninja.html", dojos=dojos)

@app.route('/ninjas/create', methods=['POST'])
def create_ninja():
    print(request.form,"*"*25)
    Ninja.create_ninja(request.form)
    return redirect('/')

