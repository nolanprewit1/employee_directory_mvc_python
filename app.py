### IMPORT REQUIRED PYTHON MODULES ###
import json
import sqlite3
from sqlite3 import Error
from flask import Flask, render_template, request, redirect, send_file

### IMPORT CONFIG FILE ### 
with open("config.json") as config_file:
    config = json.load(config_file)

### DEFINE THE FLASK APP ###
server = Flask(__name__)

### ALLOW RELOAD OF TEMPLATE FILES DURING DEVELOPMENT ###
def before_request():
    server.jinja_env.cache = {}
server.before_request(before_request)

### CONNECT TO THE DATABASE ###
def connect_database():
    try:
        return sqlite3.connect(config.get("database_file"))
    except:
        print("There was an error connecting to the database...")

### DEFINE SQL QUERY FUNCTIONS FOR EACH QUERY TYPE ###

# READ
def select_all_query(query):
    db_connection = connect_database()
    cur = db_connection.cursor() 
    cur.execute(query)
    rows = cur.fetchall()
    db_connection.close()
    return rows

# READ
def select_query(query, var):
    db_connection = connect_database()
    cur = db_connection.cursor() 
    cur.execute(query, var)
    rows = cur.fetchall()
    db_connection.close()
    return rows

# CREATE & UPDATE
def create_update_query(query, var):
    db_connection = connect_database()
    cur = db_connection.cursor() 
    cur.execute(query, var)
    db_connection.commit()
    db_connection.close()

# DELETE
def delete_query(query, var):
    db_connection = connect_database()
    cur = db_connection.cursor() 
    cur.execute(query, var)
    db_connection.commit()
    db_connection.close()

### DEFINE THE ROUTES ###
@server.route("/")
@server.route("/index")
def index():
    results = select_all_query("SELECT * FROM EMPLOYEE")
    return render_template("index.html", results=results)

@server.route("/report")
def report():
    return render_template("report.html")

@server.route("/report/report_all_employees")
def report_all_employees():
    results = select_all_query("SELECT * FROM EMPLOYEE")
    return render_template("report_all_employees.html", results=results)

@server.route("/employee/create", methods=["GET", "POST"])
def employee_create():
    if request.method == "GET":
        return render_template("employee_create.html")
    elif request.method == "POST":
        employee_first_name = request.form['employee_first_name']
        employee_last_name = request.form['employee_last_name']
        employee_position = request.form['employee_position']
        create_update_query(
            'INSERT INTO EMPLOYEE (first_name,last_name,position) VALUES (?,?,?)', 
            (employee_first_name,employee_last_name,employee_position)
        )
        return redirect("/", code=302)
    else:
        return redirect("/", code=302)

@server.route("/employee/detail/<id>", methods=["GET"])
def employe_detail(id):
    if request.method == "GET":
        results = select_query(
            'SELECT * FROM EMPLOYEE WHERE id = ?', 
            (id,)
        )
        return render_template("employee_detail.html", results=results)
    else:
        return redirect("/", code=302)

@server.route("/employee/update/<id>", methods=["GET", "POST"])
def employee_update(id):
    if request.method == "GET":
        results = select_query(
            'SELECT * FROM EMPLOYEE WHERE id = ?', 
            (id,)
        )
        return render_template("employee_update.html", results=results)
    elif request.method == "POST":
        employee_first_name = request.form['employee_first_name']
        employee_last_name = request.form['employee_last_name']
        employee_position = request.form['employee_position']
        print(id)
        create_update_query(
            'UPDATE EMPLOYEE SET first_name = ?, last_name = ?, position = ? where id = ?',
            (employee_first_name,employee_last_name,employee_position,id)
        )
        return redirect("/", code=302)
    else:
        return redirect("/", code=302)

@server.route("/employee/delete/<id>", methods=["GET", "POST"])
def employee_delete(id):
    if request.method == "GET":
        results = select_query('SELECT * FROM EMPLOYEE WHERE id = ?', (id,))
        return render_template("employee_delete.html", results=results)
    elif request.method == "POST":
        delete_query(
            'DELETE FROM EMPLOYEE WHERE ID = ?',
            (id,)
        )
        return redirect("/", code=302)
    else:
        return redirect("/", code=302)

### START AND RUN THE SERVER ###
if __name__ == "__main__": 
    server.debug = False
    server.run(host="0.0.0.0",port=config.get("web_port"))
    
    