### IMPORT REQUIRED PYTHON MODULES ###
from flask import Flask, render_template, request, redirect, send_file
# from employee_directory_mvc_python import app
from project import app

### DEFINE THE ROUTES ###

# CREATE
@app.route("/employees/create", methods=["GET", "POST"])
def employee_create():
    if request.method == "GET":
        return render_template("employees/create.html")
    # elif request.method == "POST":
    #     employee_first_name = request.form['employee_first_name']
    #     employee_last_name = request.form['employee_last_name']
    #     employee_position = request.form['employee_position']
    #     create_update_query(
    #         'INSERT INTO EMPLOYEE (first_name,last_name,position) VALUES (?,?,?)', 
    #         (employee_first_name,employee_last_name,employee_position)
    #     )
    #     return redirect("/", code=302)
    else:
        return redirect("/", code=302)

# READ
# @app.route("/")
@app.route("/employees")
def employees_index():
    # results = select_all_query("SELECT * FROM EMPLOYEE")
    # return render_template("index.html", results=results)
    return render_template("employees/index.html")

# @app.route("/employee/detail/<id>", methods=["GET"])
# def employe_detail(id):
#     if request.method == "GET":
#         results = select_query(
#             'SELECT * FROM EMPLOYEE WHERE id = ?', 
#             (id,)
#         )
#         return render_template("employee_detail.html", results=results)
#     else:
#         return redirect("/", code=302)

#UPDATE
# @app.route("/employee/update/<id>", methods=["GET", "POST"])
# def employee_update(id):
#     if request.method == "GET":
#         results = select_query(
#             'SELECT * FROM EMPLOYEE WHERE id = ?', 
#             (id,)
#         )
#         return render_template("employee_update.html", results=results)
#     elif request.method == "POST":
#         employee_first_name = request.form['employee_first_name']
#         employee_last_name = request.form['employee_last_name']
#         employee_position = request.form['employee_position']
#         print(id)
#         create_update_query(
#             'UPDATE EMPLOYEE SET first_name = ?, last_name = ?, position = ? where id = ?',
#             (employee_first_name,employee_last_name,employee_position,id)
#         )
#         return redirect("/", code=302)
#     else:
#         return redirect("/", code=302)

#DELETE
# @app.route("/employee/delete/<id>", methods=["GET", "POST"])
# def employee_delete(id):
#     if request.method == "GET":
#         results = select_query('SELECT * FROM EMPLOYEE WHERE id = ?', (id,))
#         return render_template("employee_delete.html", results=results)
#     elif request.method == "POST":
#         delete_query(
#             'DELETE FROM EMPLOYEE WHERE ID = ?',
#             (id,)
#         )
#         return redirect("/", code=302)
#     else:
#         return redirect("/", code=302)