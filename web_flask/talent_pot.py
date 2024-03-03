#!/usr/bin/python3
""" Starts a Flash Web Application """
from models import storage
from models.employee import Employee
from os import environ
from flask import Flask, render_template, request, abort
app = Flask(__name__)
# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@app.before_request
def filteringrequest():
    """function to filter out routes that dont need authentication"""
    lock_paths = [
        '/aft_signin/',
        '/aft_signin',
    ]

    cooki = request.cookies.get("session_id")
    if (cooki is None):
        if (request.path in lock_paths):
            abort(401)
    if cooki:
        from api.v2.app import AUTH
        usr = AUTH.get_user_from_session_id(cooki)
        if usr is None:
            abort(403)


@app.route('/', strict_slashes=False)
def talent_pot():
    """ TALENTPOT is alive! """

    return render_template('index.html')

@app.route('/test', strict_slashes=False)
def test():
    """ Test is alive! """

    return render_template('test.html')

@app.route('/add', strict_slashes=False)
def add():
    """ Add is alive! """

    return render_template('add_user.html')

@app.route('/modify', strict_slashes=False)
def modify():
    """ Modify is alive! """

    return render_template('modify.html')

@app.route('/delete', strict_slashes=False)
def delete():
    """ Delete is alive! """

    return render_template('delete.html')


@app.route('/signin', strict_slashes=False)
def signin():
    """ Signin is alive! """

    return render_template('sign_in.html')


@app.route('/signup', strict_slashes=False)
def signup():
    """ Signup is alive! """

    return render_template('sign_up.html')


@app.route('/generate_token', strict_slashes=False)
def generatetoken():
    """ Token  is alive! """

    return render_template('token.html')


@app.route('/reset_passwd', strict_slashes=False)
def resetp():
    """ Reset password is alive! """

    return render_template('resetpass.html')


@app.route('/aft_signin', strict_slashes=False)
def aft_signin():
    """ after signin is alive! """

    return render_template('after-signin.html')


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
