import pytest
import json

from src.system import clear_to_watch, clear_watched, clear_all, clear_ids

def test_clear_to_watch():
    clear_to_watch()
    with open("data_files/to_watch.json", "r") as open_file:
        to_watch_data = json.load(open_file)
    to_watch = to_watch_data["to_watch"]
    assert len(to_watch) == 0

def test_clear_watched():
    clear_watched()
    with open("data_files/watched.json", "r") as open_file:
        watched_data = json.load(open_file)
    watched = watched_data["watched"]
    assert len(watched) == 0

def test_clear_id():
    clear_ids()
    with open("data_files/id.json",'r') as open_file:
        id_data = json.load(open_file)
    ids = id_data['id']
    assert ids == 0

def test_clear_all():
    clear_all()

    with open("data_files/to_watch.json", "r") as open_file:
        to_watch_data = json.load(open_file)
    to_watch = to_watch_data["to_watch"]
    assert len(to_watch) == 0

    with open("data_files/watched.json", "r") as open_file:
        watched_data = json.load(open_file)
    watched = watched_data["watched"]
    assert len(watched) == 0

    with open("data_files/id.json",'r') as open_file:
        id_data = json.load(open_file)
    ids = id_data['id']
    assert ids == 0
