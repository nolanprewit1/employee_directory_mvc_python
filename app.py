### IMPORT REQUIRED PYTHON MODULES ###
import json
import sqlite3
from sqlite3 import Error
from flask import Flask, render_template, request, redirect

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

# CREATE
# def create_query(query):
#     cur = db_connection.cursor() 
#     cur.execute(query)
#     rows = cur.fetchall()
#     return rows

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

# UPDATE
def update_query(query, var):
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
    db_connection.close()

### DEFINE THE ROUTES ###
@server.route("/")
@server.route("/index")
def index():
    results = select_all_query("SELECT * FROM EMPLOYEES")
    return render_template("index.html", results=results)

@server.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "GET":
        return render_template("create.html")
    else:
        return redirect("/", code=302)
    

### START AND RUN THE SERVER ###
if __name__ == "__main__": 
    server.debug = False
    server.run(host="0.0.0.0",port=config.get("web_port"))
    
    