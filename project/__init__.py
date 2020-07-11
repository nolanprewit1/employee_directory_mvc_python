### IMPORT REQUIRED PYTHON MODULES ###
import sqlite3
import json
from flask import Flask, redirect, url_for

### IMPORT CONFIG FILE ### 
with open("config.json") as config_file:
    config = json.load(config_file)

### CONNECT TO THE DATABASE ###
try:
    db_connection = (sqlite3.connect(config.get("database_file"))).cursor()
except:
    print("There was an error connecting to the database...")

### DEFINE THE FLASK APP ###
app = Flask('project')
app.debug = True

### SET DEFAULT ROUTE REDIRECT ###
@app.route('/')
def index_redirect():
    return redirect(url_for('employees_index'))

### IMPORT CONTROLLERS ###
from project.controllers import employees

