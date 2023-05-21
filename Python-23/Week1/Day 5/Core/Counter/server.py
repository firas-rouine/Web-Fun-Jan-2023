from flask import Flask, render_template,request,redirect,session
import base64

app = Flask(__name__)
app.secret_key = 'your_secret_key'
@app.route('/')
def index():
    count_val = session.get('count_val')
    session['count_val'] = count_val + 1
    return render_template('index.html', count=session['count'],count_val=count_val)
@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')

@app.route('/increment', methods=['POST'])
def increment():
    inc_val=int(request.form.get('increment'))
    count = session.get('count', 1)
    session['count'] = count + inc_val 
    return redirect('/')
@app.route('/reset', methods=['POST'])
def reset():
    session['count'] = 1 
    return redirect('/')
if __name__ == '__main__':
    app.run(debug=True)