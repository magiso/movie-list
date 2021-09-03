import pytest
import requests
import json

from src import server, config

@pytest.fixture
def clear():
    requests.delete(config.url + 'clear/all')

@pytest.fixture
def sample_to_watch(clear):
    movie = requests.post(config.url + 'towatch/new', json = {
        'name': 'new movie', 'year': 2021, 'genre': 'comedy'
    })
    return movie.json()

def test_add_to_watch(clear):
    response = requests.post(config.url + 'towatch/new', json = {
        'name': 'new movie', 'year': 2021, 'genre': 'comedy'
    })
    assert(response.status_code == 200)
    assert(response.json()['id'] == 1)

    response = requests.post(config.url + 'towatch/new', json={
        'name': 'another movie', 'year': 2020, 'genre': None
    })
    assert(response.status_code == 200)
    assert(response.json()['id'] == 2)

def test_add_watched(clear):
    response = requests.post(config.url + 'watched/new', json = {
        'name': 'new movie', 'year': 2021, 'genre': 'comedy', 'date_watched': '01/01/2021', 'score': 10
    })
    assert(response.status_code == 200)
    assert(response.json()['id'] == 1)

    response = requests.post(config.url + 'watched/new', json={
        'name': 'another movie', 'year': 2020, 'genre': None, 'date_watched': '01/01/2021', 'score': 10
    })
    assert(response.status_code == 200)
    assert(response.json()['id'] == 2)

def test_move_watched(sample_to_watch):
    response = requests.post(config.url + 'watched/move', json={
        'id': sample_to_watch['id'], 'date_watched': '01/01/2021', 'score': 10
    })
    assert(response.status_code == 200)
    assert(response.json()['id'] == sample_to_watch['id'])