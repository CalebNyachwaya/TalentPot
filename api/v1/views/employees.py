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

@app_views.route('/employees/<company>', methods=['POST'], strict_slashes=False)
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
