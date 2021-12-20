from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/home')
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/contact')
def contact_page():
    return render_template("contact.html")

@app.route('/assignment8')
def hobbies():
    return render_template("assignment8.html", hobbies=["Basketball", "Guitar", "Ice Hockey", "Running", "Football" , "dogeball","Tennis","Baseball","soccerball"])
@app.route('/about')
def about():
    return render_template("include.html")

if __name__ == "__main__":
    app.run(dubug = True)