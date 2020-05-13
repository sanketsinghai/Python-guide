from flask import Flask,render_template

app= Flask(__name__)
@app.route("/")
def index():
    headline=True
    new_year=False
    names=["Mukesh Jain","Shashi Jain" ,"Shubham", "Sachin","Sanket","Sanyam"]
    return render_template("index.html", headline=headline, names=names)

@app.route("/about")
def sanket():
    return "Hello I am sanket I am woking in Terralogic Inc."
@app.route("/<string:name>")
def name(name):
    return f"<h1>Hello {name}</h1>"
