from flask import Flask , render_template, request, redirect,session

app = Flask(__name__)
app.secret_key = 'no secrets on GitHUB'

@app.route('/')
def index():
    return render_template("index.html")

# ? ACTION ROUTE - FROM SUBMIT (POST) 📤📤
@app.route('/process', methods=['post'])
def process():
    print("Request Object ", request.form, "*"*25)
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['langauage'] = request.form['langauage']
    session['comment'] = request.form['comment']
    return redirect('/result')

# ? ROUTE PAGE - DISPLAY 👀
@app.route('/result')
def display():
    # print("Username : ", session['name'],"-"*25)
    return render_template("result.html")

# ? ACTION ROUTE - CLEAR SESSION 🧹
@app.route('/clear')
def clear_session():
    session.clear()
    return redirect('/display')

if __name__ =='__main__':
    app.run(debug = True, port = 5000)