#!/usr/bin/python3
""" Starts a Flash Web Application """
from models import storage
from models.employee import Employee
from os import environ
from flask import Flask, render_template
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
    if AUTH is None:
        return
    excluded_paths = [
        '/api/v2/',
        '/api/v2/unauthorized/',
        '/api/v2/forbidden/',
        '/api/v2/reset_password/',
        '/api/v2/users/',
        '/api/v2/sessions/',
    ]
    if not AUTH.require_auth(request.path, excluded_paths):
        return

    if AUTH.session_cookie(
            request) is None:
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


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
