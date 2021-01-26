from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/")
def index(user=None):
    if user:
        message = f"<h1>Username:{user[0]}</h1>"
        message+= f"<p>Your password is {user[1]}</p>"
    else:
        message = "Hello"
    return message;

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/login1", methods=["POST"])
def login1():
    name = request.form.get("name")
    password = request.form.get("pass")
    return index([name,password])
app.run()