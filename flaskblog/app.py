from flask import Flask,render_template, request

app= Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def sanket():
    return render_template("about.html")
@app.route("/<string:name>")
def name(name):
    return f"<h1>Hello {name}</h1>"


@app.route("/contact")
def contact():
    return render_template("contact.html")



@app.route("/hello" , methods=["POST"])
def hello():
    name = request.form.get("name")
    return render_template("hello.html", name=name)
