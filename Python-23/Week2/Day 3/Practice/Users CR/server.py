from flask import Flask,render_template, redirect,request
from user_model import User
app = Flask(__name__)

@app.route('/')
def index():
    users = User.get_all()
    return render_template("read_all.html",users=users)

@app.route('/user/new')
def new_user():
    return render_template("create.html")

@app.route('/user', methods=['POST'])
def create():
    User.create(request.form)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug =True)