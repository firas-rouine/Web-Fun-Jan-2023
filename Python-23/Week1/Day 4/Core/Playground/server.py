from flask import Flask,render_template
app= Flask(__name__)
@app.route('/play')
def index():
    return render_template("index.html",x=3)
@app.route("/play/<string:x>")
def repeat(x):
    x=int(x)
    return render_template("index.html",x=x)
@app.route("/play/<int:x>/<string:color>")
def color(x,color):
    return render_template("index.html",x=x,color=color)



if __name__=="__main__":
    app.run(debug=True , port=5000)