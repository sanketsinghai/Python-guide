from flask import Flask,render_template

app= Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def sanket():
    return "Hello I am sanket I am woking in Terralogic Inc."
@app.route("/<string:name>")
def name(name):
    return f"<h1>Hello {name}</h1>"
