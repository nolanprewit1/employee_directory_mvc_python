### IMPORT REQUIRED PYTHON MODULES ###
from flask import Flask, render_template, request, redirect, send_file
from project import app
from project.models import model_employees
from project import db_connection

### DEFINE THE ROUTES ###
# CREATE
@app.route("/employees/create", methods=["GET", "POST"])
def employee_create():
    if request.method == "GET":
        return render_template("employees/create.html")
    elif request.method == "POST":
        data = model_employees.Employees(
            firstName = request.form['firstName'],
            lastName = request.form['lastName'],
            position = request.form['position']
        )
        db_connection.add(data)
        db_connection.commit()
        return redirect("/employees", code=302)
    else:
        return redirect("/employees", code=302)

# READ
@app.route("/employees")
def employees_index():
    results = db_connection.query(model_employees.Employees).all()
    return render_template("employees/index.html", results=results)

@app.route("/employees/detail/<id>", methods=["GET"])
def employees_detail(id):
    if request.method == "GET":
        # results = select_query(
        #     'SELECT * FROM EMPLOYEE WHERE id = ?', 
        #     (id,)
        # )
        results = db_connection.query(data)\
            .filter(employees.id==id)
    #     session.query(User)\
    # .filter(Address.email_address=='ed@google.com')\
    # .first()
        return render_template("employees/detail.html", results=results)
    else:
        return redirect("/", code=302)

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