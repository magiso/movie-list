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

@pytest.fixture
def sample_watched(clear):
    movie = requests.post(config.url + 'watched/new', json = {
        'name': 'new movie', 'year': 2021, 'genre': 'comedy', 'date_watched': '01/01/2021', 'score': 10
    })
    return movie.json()

def test_remove_to_watch(sample_to_watch):
    response = requests.delete(config.url + 'towatch/remove', json={
        'id': sample_to_watch['id']
    })
    assert(response.status_code == 200)
    assert(response.json()['status'] == True)

def test_remove_watched(sample_watched):
    response = requests.delete(config.url + 'watched/remove', json={
        'id': sample_watched['id']
    })
    assert(response.status_code == 200)
    assert(response.json()['status'] == True)