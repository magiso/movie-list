import sys
from json import dumps
from flask import Flask, request
from flask_cors import CORS

from src.movies import *
from src.system import *

def defaultHandler(err):
    response = err.get_response()
    print('response', err, err.get_response())
    response.data = dumps({
        "code": err.code,
        "name": "System Error",
        "message": err.get_description(),
    })
    response.content_type = 'application/json'
    return response

#APP = Flask(__name__, static_url_path='/user_profile_photos/')
APP = Flask(__name__)
CORS(APP)

APP.config['TRAP_HTTP_EXCEPTIONS'] = True
APP.register_error_handler(Exception, defaultHandler)

################################################################################

@APP.route("/")
def nothing():
    # Default route
    return "Hello World!"

################################################################################