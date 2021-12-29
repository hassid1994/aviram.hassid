from flask import Flask, redirect, url_for, render_template
from flask import request
from flask import session


app = Flask(__name__)
app.secret_key = '123'

users = {
         'user1': {'name': 'avirom', 'email': 'avirom@gmail.com'},
         'user2': {'name': 'eitan', 'email': 'eitan@gmail.com'},
         'user3': {'name': 'itamr', 'email': 'noam@gmail.com'},
         'user4': {'name': 'ofir', 'email': 'ofir@gmail.com'},
         'user5': {'name': 'lior', 'email': 'lior@gmail.com'}}


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

@app.route('/assignment9', methods = ['GET', 'POST'])
def get_post():
    if 'email' in request.args:
        email = request.args['email']
        if email == '':
            return render_template("assignment9.html", user_list = users)
        for key,value in users.items():
            if value.get('email') == email:
                return render_template("assignment9.html",u_name=value.get('name'), u_email=value.get('email'))
    if request.method == 'POST':
        session['username'] = request.form['username']
    return render_template("assignment9.html")

@app.route('/signout' , methods = ['GET', 'POST'])
def sign_out():
    session['username'] = ""
    return render_template("assignment9.html")





if __name__ == "__main__":
    app.run(dubug = True)