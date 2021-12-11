from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route("/contact")
def contact():
    return "<h1>please enter you details down below<h1>"

@app.route("/home")
def home():
    return redirect(url_for('hello_world'))


@app.route("/")
def hello_world():
    return "<p>Hello World!</p>"

@app.route("/admin")
def admin():
    return "Hi there I am your admin"




if __name__ == "__main__":
    app.run()