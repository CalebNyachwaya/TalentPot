#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Employees """
from models.employee import Employee
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
"""from flasgger.utils import swag_from"""


@app_views.route('/employees/<company>', methods=['GET'], strict_slashes=False)
def get_employees(company):
    """
    Retrieves the list of all employees in a given company
    """
    all_employees = storage.all(Employee).values()
    list_employees = []
    dict_employees = {}
    found = False
    for emp in all_employees:
        all_emp = emp.to_dict()
        for a, b in all_emp.items():
            if a == "company" and b == company and found is False:
                dict_employees = all_emp.copy()
                found = True
        found = False
        if "password" in dict_employees:
            del dict_employees["password"]
        if len(dict_employees) >= 1:
            list_employees.append(dict_employees)
        dict_employees = {}
    return jsonify(list_employees)

@app_views.route('/add/employees/<company>', methods=['POST'], strict_slashes=False)
def post_employees(company):
    """To add employee of a company to the db"""
    data = request.get_json()
    if not data:
        abort(404, description="Not a JSON")
    if ("email" not in data or "password" not in data
        or "company" not in data or "DOB" not in data
        or "address" not in data or "city" not in data
        or "country" not in data or "dept" not in data
        or "position" not in data or "phone" not in data
        or "first_name" not in data or "last_name" not in data):
        abort(404, description="Missing item")

    if "id" in data:
        del data["id"]
    if "updated_at" in data:
        del data["updated_at"]
    if "created_at" in data:
        del data["created_at"]
    data["company"] = company
    emp_ins = Employee(**data)
    emp_ins.save()
    return make_response(jsonify(emp_ins.to_dict()), 201)

@app_views.route('/employees/<company>/<dept>', methods=['GET'], strict_slashes=False)
def get_dept_employees(company, dept):
    """
    Retrieves the list of all department employees in a given company
    """
    all_employees = storage.all(Employee).values()
    list_employees = []
    dict_employees = {}
    found = False
    for emp in all_employees:
        all_emp = emp.to_dict()
        for a, b in all_emp.items():
            if a == "company" and b == company and found is False:

                dict_employees = all_emp.copy()
                found = True
        found = False
        if "password" in dict_employees:
            del dict_employees["password"]
        if len(dict_employees) >= 1:
            list_employees.append(dict_employees)
        dict_employees = {}
    dept_list = []
    for c in list_employees:
        if dept in c.values():
            dept_list.append(c)
    return jsonify(dept_list)

@app_views.route('/modify/employees/<company>', methods=['DELETE', 'PUT'],
                 strict_slashes=False)
def employee_with_id(company):
    """
        employees route that handles http requests with ID given
    """
    employee_obj = storage.all(Employee).values()
    if employee_obj is None:
        abort(404, 'Not found')

    if request.method == 'DELETE':
        req_json = request.get_json()
        if req_json is None:
            abort(400, 'Not a JSON')
        for a in employee_obj:
            emp_obj = a.to_dict()
            if req_json["email"] == emp_obj["email"]:
                if emp_obj["company"] == req_json["company"]:
                    storage.delete(a)
                    storage.save()

                    return jsonify({}), 200
                else:
                    abort(404, 'Not a company member')
            emp_obj = {}
        abort(404, 'Not found..')

    if request.method == 'PUT':
        req_json = request.get_json()
        dct = {}
        if req_json is None:
            abort(400, 'Not a JSON')
        for arr, brr in  req_json.items():
            if len(brr) > 2:
                dct[arr] = brr
        for b in employee_obj:
            emp_obj = b.to_dict()
            if emp_obj["email"] == req_json["email"]:
                if emp_obj["company"] == req_json["company"]:
                    for x, y in dct.items():
                        setattr(b, x, y)
                        storage.save()
                    return make_response(jsonify(b.to_dict()), 200)
                else:
                    abort(404, 'Not a company member')
            emp_obj = {}
        abort(404, 'Not found..')
