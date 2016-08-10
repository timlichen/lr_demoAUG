from flask import Flask, render_template, session, redirect, request, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = "catdogtim"
mysql = MySQLConnector(app, 'login_registration')

@app.route("/")
def doIEevenGetBro():
    return render_template("index.html")

@app.route("/register", methods=['POST'])
def doYouEVEnREgisterbro():

    error = False

    if len(request.form['fName']) < 2:
        error = True
    if len(request.form['lName']) < 2:
        error = True
    if len(request.form['email']) < 2:
        error = True

    if error:
        return redirect("/")
    else:
        query = "INSERT INTO users (email, first_name, last_name, password, created_at, updated_at) VALUES (:email, :first_name, :last_name, :password, NOW(), NOW())"

        email = request.form['email']

        data = {
            "email": email,
            "last_name": request.form['lName'],
            "first_name": request.form['fName'],
            "password": request.form['password'],
        }

        print mysql.query_db(query, data)
        print "reg yes"

        return redirect("/")

@app.route("/login", methods=["POST"])
def plzLoginIfuCan():
    query = "SELECT email, password FROM users WHERE email = :email AND password = :password"
    email = request.form['email']
    data = {
        "email": email,
        "password": request.form['password']
    }

    user = mysql.query_db(query, data)
    if user:
        query = "SELECT first_name, last_name, created_at, updated_at FROM users"
        all_users = mysql.query_db(query)
        print all_users
        print user
    else:
        print user
        print "empty lists are evaluted as false"

    print "we at login"
    return redirect("/")

app.run(debug=True)
