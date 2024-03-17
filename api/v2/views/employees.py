#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Employees """
from models.employee import Employee
from models import storage
from api.v2.views import app_views
from flask_mail import Message
from flask import abort, jsonify, make_response, request
"""from flasgger.utils import swag_from"""


<<<<<<< HEAD

=======
>>>>>>> f607b66765d80f63581aa085b24ac2daea58cb90
@app_views.route('/employees/<company>', methods=['GET'], strict_slashes=False)
def get_employees(company):
    """
    Retrieves the list of all employees in a given company
    """
    cooki = request.cookies.get("session_id")
    if cooki is None:
        abort(403)
    from api.v2.app import AUTH
    usr = AUTH.get_user_from_session_id(cooki)
    if usr is None:
        abort(403)
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
        if "hashed_password" in dict_employees:
            del dict_employees["hashed_password"]
        if "session_id" in dict_employees:
            del dict_employees["session_id"]
        if "session_created_at" in dict_employees:
            del dict_employees["session_created_at"]
        if "reset_token" in dict_employees:
            del dict_employees["reset_token"]
        if len(dict_employees) >= 1:
            list_employees.append(dict_employees)
        dict_employees = {}
    return jsonify(list_employees)

@app_views.route('/add/employees/<company>', methods=['POST'], strict_slashes=False)
def post_employees(company):
    """To add employee of a company to the db"""
    cooki = request.cookies.get("session_id")
    if cooki is None:
        abort(403)
    from api.v2.app import AUTH
    usr = AUTH.get_user_from_session_id(cooki)
    if usr is None:
        abort(403)
    data = request.get_json()
    if not data:
        abort(404, description="Not a JSON")
    if ("company" not in data or "DOB" not in data
        or "address" not in data or "city" not in data
        or "country" not in data or "dept" not in data
        or "position" not in data or "phone" not in data
        or "first_name" not in data or "last_name" not in data):
        abort(404, description="Missing item")

    if "id" in data:
        del data["id"]
    if "hashed_password" in data:
        del data["hashed_password"]
    if "session_id" in data:
        del data["session_id"]
    if "session_created_at" in data:
        del data["session_created_at"]
    if "reset_token" in data:
        del data["reset_token"]
    if "updated_at" in data:
        del data["updated_at"]
    if "created_at" in data:
        del data["created_at"]
    data["company"] = company
<<<<<<< HEAD
    AUTH.update_usr(cooki, data)
    return make_response(jsonify(usr.to_dict()), 201)
=======
    dct = {}
    if usr.email == data.get("email"):
        for arr, brr in  data.items():
            if len(brr) > 2:
                dct[arr] = brr
        for ab, ac in dct.items():
            setattr(usr, ab, ac)
            storage.save()
            return make_response(jsonify(usr.email), 200)
    abort(404, 'Not found..')
>>>>>>> f607b66765d80f63581aa085b24ac2daea58cb90

@app_views.route('/employees/<company>/<dept>', methods=['GET'], strict_slashes=False)
def get_dept_employees(company, dept):
    """
    Retrieves the list of all department employees in a given company
    """
    cooki = request.cookies.get("session_id")
    if cooki is None:
        abort(403)
    from api.v2.app import AUTH
    usr = AUTH.get_user_from_session_id(cooki)
    if usr is None:
        abort(403)
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
        if "hashed_password" in dict_employees:
            del dict_employees["hashed_password"]
        if "session_id" in dict_employees:
            del dict_employees["session_id"]
        if "session_created_at" in dict_employees:
            del dict_employees["session_created_at"]
        if "reset_token" in dict_employees:
            del dict_employees["reset_token"]
        if len(dict_employees) >= 1:
            list_employees.append(dict_employees)
        dict_employees = {}
    dept_list = []
    for c in list_employees:
        if dept in c.values():
            dept_list.append(c)
    return jsonify(dept_list)

@app_views.route('/modify/employees/<company>/', methods=['PUT'],
                 strict_slashes=False)
def employee_with_id(company):
    """
        employees route that handles http requests with ID given
    """
    cooki = request.cookies.get("session_id")
    if cooki is None:
        abort(403)
    from api.v2.app import AUTH
    usr = AUTH.get_user_from_session_id(cooki)
    if usr is None:
        abort(401)
    req_json = request.get_json()
    if req_json is None:
        abort(400, 'Not a JSON')
    dct = {}
    if usr.email == req_json.get("email"):
        for arr, brr in  req_json.items():
            if len(brr) > 2:
                dct[arr] = brr
        for ab, ac in dct.items():
            setattr(usr, ab, ac)
            storage.save()
            return make_response(jsonify(usr.email), 200)
    abort(404, 'Not found..')


@app_views.route('/delete/employees/<company>/', methods=['DELETE'], strict_slashes=False)
def employee_delete(company):
    """
    """
    cooki = request.cookies.get("session_id")
    if cooki is None:
        abort(403)
    from api.v2.app import AUTH
    usr = AUTH.get_user_from_session_id(cooki)
    if usr is None:
        abort(403)
    employee_obj = storage.all(Employee).values()
    if employee_obj is None:
        abort(404, 'Not found')
    req_json = request.get_json()
    if req_json is None:
        abort(400, 'Not a JSON')
    for a in employee_obj:
        emp_obj = a.to_dict()
        for x, y in emp_obj.items():
            if req_json["email"] == y:
                storage.delete(a)
                storage.save()
                return jsonify({}), 200
        emp_obj = {}
    abort(404, 'Not found..')


@app_views.route('/users', methods=[
    'POST'], strict_slashes=False)
def reg_user() -> str:
    """register a user to the server"""
    data = request.get_json()
    if not data:
        abort(404)
    email = data.get("email")
    password = data.get("password")
    if email and password:
        try:
            from api.v2.app import AUTH
            usr = AUTH.register_user(email, password)
            return jsonify({"email": usr.email,
                            "message": "user created"})
        except ValueError:
            return jsonify({"message": "email already registered"}), 400


@app_views.route('/sessions', methods=[
    'POST'], strict_slashes=False)
def login() -> str:
    """method to comfirm logged in"""
    data = request.get_json()
    if not data:
        abort(404)
    email = data.get("email")
    password = data.get("password")
    from api.v2.app import AUTH
    if AUTH.valid_login(email, password):
        uid = AUTH.create_session(email)
        response = jsonify({"email": email, "message": "logged in", "sess": uid})
        response.set_cookie("session_id", uid, max_age=900)
        return response
    else:
        abort(401)


@app_views.route('/sessions', methods=[
    'DELETE'], strict_slashes=False)
def logout():
    """method to delete session. same as logout"""
    cooki = request.cookies.get("session_id")
    if cooki is None:
        abort(404)
    from api.v2.app import AUTH
    usr = AUTH.get_user_from_session_id(cooki)
    if usr is None:
        return jsonify([])
    AUTH.destroy_session(usr.id)
    return jsonify([])
    


@app_views.route('/profile', methods=[
    'GET'], strict_slashes=False)
def profile() -> str:
    """method to get user profile page by session_id"""
    cooki = request.cookies.get("session_id")
    if cooki is None:
        abort(403)
    from api.v2.app import AUTH
    usr = AUTH.get_user_from_session_id(cooki)
    if usr is None:
        abort(403)
    return jsonify({"email": usr.email}), 200


@app_views.route('/check/<sess>', methods=[
    'GET'], strict_slashes=False)
def check(sess) -> str:
    """method to check user by session_id"""
    if sess is None:
        abort(403)
    from api.v2.app import AUTH
    usr = AUTH.get_user_from_session_id(sess)
    if usr is None:
        abort(403)
    return jsonify({"email": usr.email}), 200


@app_views.route('/reset_password', methods=[
    'POST'], strict_slashes=False)
def get_reset_password_token() -> str:
    """method to get a reset password token"""
    from api.v2.app import mail
    data = request.get_json()
    if not data:
        abort(404)
    email = data.get("email")
    try:
        from api.v2.app import AUTH
        r_tok = AUTH.get_reset_password_token(email)
        if r_tok is None:
            abort(403)
        msg = Message('Token', sender='chekwasybuildex@gmail.com', recipients=[email])
        msg.body = f"Your Token is: {r_tok}"
        mail.send(msg)
        return jsonify({"email": email, "reset_token": r_tok})
    except ValueError:
        abort(403)


@app_views.route('/reset_password', methods=[
    'PUT'], strict_slashes=False)
def update_password() -> str:
    """route to update password for user"""
    data = request.get_json()
    if not data:
        abort(404)
    email = data.get("email")
    reset_token = data.get("reset_token")
    new_password = data.get("new_password")
    try:
        from api.v2.app import AUTH
        AUTH.update_password(reset_token, new_password)
        return jsonify({"email": email, "message": "Password updated"})
    except ValueError:
        abort(403)
