from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo
@app.route('/')
def index():
    dojos = Dojo.get_all()
    return render_template("index.html", dojos=dojos)

@app.route('/dojos/create', methods=['POST'])
def create():
    Dojo.create_dojo(request.form)
    return redirect('/')

app.route('/dojos/<int:id>')
def show(id):
    dojos = Dojo.get_all(id)
    print(dojos,"++++++*******"*20)
    return render_template("show_ninjas.html", dojos=dojos)
    