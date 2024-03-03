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
    excluded_paths = [
        '/',
        '/signin/',
        '/signin',
        '/signup/',
        '/signup',
        '/generate_token',
        '/generate_token/',
        '/reset_passwd',
        '/reset_passwd/',
    ]

    if (request.cookies.get("session_id") is None):
        if (request.path in excluded_paths):
            pass
        else:
            abort(401)


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
