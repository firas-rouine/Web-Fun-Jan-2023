from flask_app import app
from flask import render_template, redirect, request,session
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja
@app.route('/')
def index():
    dojos = Dojo.get_all()
    return render_template("index.html", dojos=dojos)

@app.route('/dojos/create', methods=['POST'])
def create():
    dojo_id= Dojo.create_dojo(request.form)
    session["dojo_id"]=dojo_id
    return redirect('/')

@app.route('/dojos/<int:dojo_id>')
def my_ninjas(dojo_id):
    dojo_ninjas = Ninja.get_dojo_ninjas({'dojo_id':session['dojo_id']})
    dojo = Dojo.get_by_id({'id':session['dojo_id']})
    return render_template("show_ninjas.html", dojo_ninjas = dojo_ninjas,dojo=dojo)
    