import pytest
import requests
import json

from src import server, config
from datetime import date

@pytest.fixture
def clear():
    requests.delete(config.url + 'clear/all')

@pytest.fixture
def sample_to_watch(clear):
    requests.post(config.url + 'towatch/new', json = {
        'name': 'new movie', 'year': 2021, 'genre': 'comedy'
    })
    requests.post(config.url + 'towatch/new', json = {
        'name': 'another movie', 'year': 2020, 'genre': 'thriller'
    })
    requests.post(config.url + 'towatch/new', json = {
        'name': 'third movie', 'year': 1999, 'genre': 'romance'
    })

@pytest.fixture
def sample_watched(clear):
    requests.post(config.url + 'watched/new', json = {
        'name': 'first movie', 'year': 2021, 'genre': 'comedy', 'date_watched': '01/01/2021', 'score': 5
    })
    requests.post(config.url + 'watched/new', json = {
        'name': 'second movie', 'year': 2020, 'genre': 'thriller', 'date_watched': '01/03/2021', 'score': 2
    })
    requests.post(config.url + 'watched/new', json = {
        'name': 'third movie', 'year': 2019, 'genre': 'romance', 'date_watched': '01/09/2021', 'score': 7
    })
    requests.post(config.url + 'watched/new', json = {
        'name': 'fourth movie', 'year': 2018, 'genre': 'sci-fi', 'date_watched': '01/04/2021', 'score': 10
    })

def test_list_to_watch(sample_to_watch):
    response = requests.get(config.url + 'towatch/list')
    assert(response.status_code == 200)
    assert(response.json() == {'to_watch_list': [
        {'name': 'another movie',
        'year': 2020,
        'genre': 'thriller',},
        {'name': 'new movie',
        'year': 2021,
        'genre': 'comedy',},
        {'name': 'third movie',
        'year': 1999,
        'genre': 'romance'},
    ]})

def test_list_watched(sample_watched):
    response = requests.get(config.url + 'watched/list')
    assert(response.status_code == 200)
    assert(response.json() == {'watched_list': [
        {'name': 'fourth movie',
        'year': 2018,
        'genre': 'sci-fi',
        'date_watched': '01/04/2021',
        'score': 10},
        {'name': 'third movie',
        'year': 2019,
        'genre': 'romance',
        'date_watched': '01/09/2021',
        'score': 7},
        {'name': 'first movie',
        'year': 2021,
        'genre': 'comedy',
        'date_watched': '01/01/2021',
        'score': 5},
        {'name': 'second movie',
        'year': 2020,
        'genre': 'thriller',
        'date_watched': '01/03/2021',
        'score': 2}
    ]})