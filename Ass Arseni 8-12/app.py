from flask import Flask, redirect, url_for, render_template, jsonify
from flask import request
from flask import session
import mysql.connector
import requests
import random
from interact_with_DB import *
#APP SET UP
app = Flask(__name__)
app.secret_key = '123'
app.config.from_pyfile('settings.py')

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



#Convert USERS TABLES from mysql to JASON using Jsonfy function
@app.route('/assignment11/users')
def read_jason():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM users''')
    rv = cur.fetchall()
    payload = []
    content = {}
    for result in rv:
        content = {'id': result[0], 'name': result[1], 'Age': result[2],'City': result[3] }
        payload.append(content)
        content = {}
    return jsonify(payload)

@app.route('/assignment11/outer_source', methods = ['GET'])
def req_front_back():
    # back side
    users = []
    if 'user_id' in request.args:
         user_id = int(request.args['user_id'])
         res = requests.get(f'https://reqres.in/api/users{user_id}')
         res = res.json()
         users.append(res)
         return render_template('outer_source.html', users = users)
    #front side
    if 'user_id_front' in request.args:
        user_id_front = int(request.args['user_id_front'])
        return render_template('outer_source.html', user_id_front = user_id_front)

    return render_template('outer_source.html')





                     #Blueprint Routs Connections
#assignment10 Blueprint
#from pages.assignment10.assignment10 import assignment10
#app.register_blueprint(assignment10)

# ------------------------------------------------- #
# ------------- DATABASE CONNECTION --------------- #
# ------------------------------------------------- #
def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         passwd='root',
                                         database='myappdb')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)
    #

    if query_type == 'commit':
        # Use for INSERT, UPDATE, DELETE statements.
        # Returns: The number of rows affected by the query (a non-negative int).
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        # Use for SELECT statement.
        # Returns: False if the query failed, or the result of the query if it succeeded.
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value


# ------------------------------------------------- #
# ------------------------------------------------- #


if __name__ == "__main__":
    app.run(dubug = True)