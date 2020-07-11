### IMPORT REQUIRED PYTHON MODULES ###
import json
# import sqlite3
# from sqlite3 import Error
# from flask import Flask, render_template, request, redirect, send_file
from project import app

### START THE APP ###    
if __name__ == '__main__':    
    app.run(host="0.0.0.0",port="8080")

# ### ALLOW RELOAD OF TEMPLATE FILES DURING DEVELOPMENT ###
# def before_request():
#     server.jinja_env.cache = {}
# server.before_request(before_request)

# ### DEFINE SQL QUERY FUNCTIONS FOR EACH QUERY TYPE ###

# # READ
# def select_all_query(query):
#     db_connection = connect_database()
#     cur = db_connection.cursor() 
#     cur.execute(query)
#     rows = cur.fetchall()
#     db_connection.close()
#     return rows

# # READ
# def select_query(query, var):
#     db_connection = connect_database()
#     cur = db_connection.cursor() 
#     cur.execute(query, var)
#     rows = cur.fetchall()
#     db_connection.close()
#     return rows

# # CREATE & UPDATE
# def create_update_query(query, var):
#     db_connection = connect_database()
#     cur = db_connection.cursor() 
#     cur.execute(query, var)
#     db_connection.commit()
#     db_connection.close()

# # DELETE
# def delete_query(query, var):
#     db_connection = connect_database()
#     cur = db_connection.cursor() 
#     cur.execute(query, var)
#     db_connection.commit()
#     db_connection.close()



# @server.route("/report")
# def report():
#     return render_template("report.html")

# @server.route("/report/report_all_employees")
# def report_all_employees():
#     results = select_all_query("SELECT * FROM EMPLOYEE")
#     return render_template("report_all_employees.html", results=results)


# ### START AND RUN THE SERVER ###
# if __name__ == "__main__": 
