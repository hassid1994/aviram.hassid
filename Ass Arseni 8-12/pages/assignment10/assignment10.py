from flask import Blueprint, render_template
import mysql.connector
from flask_mysqldb import MySQL

assignment10.config["MYSQL_HOST"]="localhost"
assignment10.config["MYSQL_USER"]="root"
assignment10.config["MYSQL_PASSWORD"]="root"
assignment10.config["MYSQL_DB"]="myappdb"
assignment10.config["MYSQL_CURSORCLASS"]="DictCursor"
mysql=MySQL(assignment10)


assignment10 = Blueprint('assignment10', __name__,
                          static_folder='static',
                          static_url_path='/assignment10',
                          template_folder='templates')
#Routes

@assignment10.route("/assignment10")
def assignemnt10():
    con=mysql.connection.cursor()
    sql="SELECT * FROM users"
    con.execute(sql)
    res=con.fetchall()
    return render_template("/assignment10",datas=res)


#New User Route
@assignment10.route("/insert_user",methods=['GET','POST'])
def addUsers():
    if request.method=='POST':
        name=request.form['name']
        Age=request.form['Age']
        City=request.form['City']
        con=mysql.connection.cursor()
        sql="insert into users(name,Age,City) value (%s,%s,%s)"
        con.execute(sql,[name,Age,City])
        mysql.connection.commit()
        con.close()
        flash('User Details Added')
        return redirect(url_for("assignment10.html"))
    return render_template("assignment10.html")

#Update User Route:

@assignment10.route("/editUser/<string:id>", methods=['GET', 'POST'])
def editUser(id):
    con = mysql.connection.cursor()
    if request.method == 'POST':
        name == request.form['name']
        Age  == request.form['Age']
        City  == request.form['Age']

        sql = "update users set name=%s,Age=%s,City=%s where ID=%s"
        con.execute(sql[ID,FirstName,LastName,Age])
        mysql.connection.commit()
        con.close()
        flash('User Detail Updated')
        return redirect(url_for("/assignment10"))
        con = mysql.connection.cursor()

    sql = "select * from users where ID=%s"
    con.execute(sql, [id])
    res = con.fetchone()
    return render_template("editUser.html", datas=res)

#Delete User
@assignment10.route("/deleteUser/<string:id>",methods=['GET','POST'])
def deleteUser(id):
    con=mysql.connection.cursor()
    sql="delete from users where ID=%s"
    con.execute(sql,id)
    mysql.connection.commit()
    con.close()
    flash('User Details Deleted')
    return redirect(url_for("assignment10"))


# SQL
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

