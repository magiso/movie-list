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

@APP.route("/towatch/new", methods=['POST'])
def add_to_watch_movie():
    # add a movie to the to watch list
    data = request.get_json()
    movie = add_to_watch(data['name'], data['year'], data['genre'])
    return dumps(movie)

@APP.route("/watched/new", methods=["POST"])
def add_new_watched_movie():
    # add a movie to the watched list
    data = request.get_json()
    movie = add_new_watched(data['name'], data['year'], data['genre'], data['date_watched'], data['score'])
    return dumps(movie)

@APP.route("/watched/move", methods=['POST'])
def add_watched_movie():
    # move a movie from to watch to watched
    data = request.get_json()
    movie = add_list_watched(data['id'], data['date_watched'], data['score'])
    return dumps(movie)

################################################################################

@APP.route("/towatch/remove", methods=['DELETE'])
def remove_to_watch_movie():
    # remove a movie from the to watch list
    data = request.get_json()
    success = remove_to_watch(data['id'])
    return dumps(success)

@APP.route("/watched/remove", methods=['DELETE'])
def remove_watched_movie():
    # remove a movie from the watched list
    data = request.get_json()
    success = remove_watched(data['id'])
    return dumps(success)

################################################################################

@APP.route("/towatch/clear", methods=['DELETE'])
def clear_to_watch_list():
    # clear the to watch list
    return dumps(clear_to_watch())

@APP.route("/watched/clear", methods=['DELETE'])
def clear_watched_list():
    # clear the watched list
    return dumps(clear_watched())

@APP.route("/clear/all", methods=['DELETE'])
def clear_all_lists():
    # clear all lists
    return dumps(clear_all())

@APP.route("/clear/id", methods=['DELETE'])
def clear_all_id():
    # clear all movie id tracking
    return dumps(clear_ids())

################################################################################

@APP.route("towatch/list", methods=['GET'])
def to_watch_list():
    # List all movies on the to watch list
    return dumps(list_to_watch())

@APP.route("watched/list", methods=['GET'])
def watched_list():
    # list all movies on the watched list
    return dumps(list_watched())
