from flask import Flask  
app = Flask(__name__)    
@app.route('/')          
def hello_world():
    return 'Hello World!'  
@app.route('/dojo')
def dojo():
    return 'dojo'
@app.route('/say/<string:name>')
def say(name):
    return f"Hi {name}"
@app.route('/repeat/<int:num>/<string:word>')
def repeat(num,word):
    str=''
    for i in range(0,num):
        str=str+f"<h1>{word}</h1>"
    return str
@app.errorhandler(404)
def page_not_found(error):
    return "Sorry! No response. Try again."
if __name__=="__main__":   
    app.run(debug=True , port=5000)    

