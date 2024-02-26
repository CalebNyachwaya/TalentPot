#!/usr/bin/python3
""" Flask Application """
from models import storage
from api.v2.views import app_views
from os import environ
from flask import Flask, render_template, make_response, jsonify
from flask_cors import CORS
from flasgger import Swagger
from flasgger.utils import swag_from
from api.v2.auth.auth import Auth
AUTH = Auth()

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/api/v2/*": {"origins": "*"}})


@app.teardown_appcontext
def close_db(error):
    """ Close Storage """
    storage.close()


@app.before_request
def filteringrequest():
    """function to filter out routes that dont need authentication"""
    if auth is None:
        return
    excluded_paths = [
        '/api/v1/stat*',
        '/api/v1/unauthorized/',
        '/api/v1/forbidden/',
        '/api/v2/reset_password/',
        '/api/v2/users/',
        'api/v2/sessions/'
    ]
    if not auth.require_auth(request.path, excluded_paths):
        return

    if auth.authorization_header(request) is None and auth.session_cookie(
            request) is None:
        abort(401)
    usr = auth.current_user(request)
    if usr is None:
        abort(403)
    request.current_user = usr


@app.errorhandler(401)
def unauthorized(error) -> str:
    """ 401 Error
    ---
    responses:
      401:
        description: unautorized access
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def unauthorized(error) -> str:
    """ 403 Error
    ---
    responses:
      403:
        description: forbidden access
    """
    return jsonify({"error": "Forbidden"}), 403


@app.errorhandler(404)
def not_found(error):
    """ 404 Error
    ---
    responses:
      404:
        description: a resource was not found
    """
    return make_response(jsonify({'error': "Not found"}), 404)

app.config['SWAGGER'] = {
    'title': 'AirBnB clone Restful API',
    'uiversion': 3
}

Swagger(app)


if __name__ == "__main__":
    """ Main Function """
    host = environ.get('TP_API_HOST')
    port = environ.get('TP_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)
