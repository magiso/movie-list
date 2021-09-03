import pytest
import json

from src.system import *
from src.movies import *
from datetime import datetime, date

# test adding to the to watch list
def test_add_to_watch():
    clear_to_watch()

    add_to_watch("new movie", 2021, "comedy")
    assert list_to_watch() == {'to_watch_list': [
        {'name': 'new movie',
        'year': 2021,
        'genre': 'comedy'}
    ]}

    add_to_watch("another movie", None, "thriller")
    assert list_to_watch() == {'to_watch_list': [
        {'name': 'another movie',
        'year': 'None',
        'genre': 'thriller'},
        {'name': 'new movie',
        'year': 2021,
        'genre': 'comedy'},
    ]}

    add_to_watch("third movie", 2020, None)
    assert list_to_watch() == {'to_watch_list': [
        {'name': 'another movie',
        'year': 'None',
        'genre': 'thriller'},
        {'name': 'new movie',
        'year': 2021,
        'genre': 'comedy'},
        {'name': 'third movie',
        'year': 2020,
        'genre': 'None'}
    ]}

# test adding to the watched list from a new entry
def test_add_new_watched():
    clear_watched()

    add_new_watched("new movie", 2021, "comedy", None, 5)
    assert list_watched() == {'watched_list': [
        {'name': 'new movie',
        'year': 2021,
        'genre': 'comedy',
        'date_watched': date(1,1,1),
        'score': 5,}
    ]}

    add_new_watched("another movie", None, "thriller", None, 10)
    assert list_watched() == {'watched_list': [
        {'name': 'another movie',
        'year': 'None',
        'genre': 'thriller',
        'date_watched': date(1,1,1),
        'score': 10,},
        {'name': 'new movie',
        'year': 2021,
        'genre': 'comedy',
        'date_watched': date(1,1,1),
        'score': 5,},
    ]}

    add_new_watched("third movie", 2020, None, '01/01/2021', 7)
    assert list_watched() == {'watched_list': [
        {'name': 'another movie',
        'year': 'None',
        'genre': 'thriller',
        'date_watched': date(1,1,1),
        'score': 10},
        {'name': 'third movie',
        'year': 2020,
        'genre': 'None',
        'date_watched': date(2021,1,1),
        'score': 7,},
        {'name': 'new movie',
        'year': 2021,
        'genre': 'comedy',
        'date_watched': date(1,1,1),
        'score': 5,},
    ]}

    add_new_watched("later movie", 2021, None, '20/4/2020', 7)
    assert list_watched() == {'watched_list': [
        {'name': 'another movie',
        'year': 'None',
        'genre': 'thriller',
        'date_watched': date(1,1,1),
        'score': 10,},
        {'name': 'third movie',
        'year': 2020,
        'genre': 'None',
        'date_watched': date(2021,1,1),
        'score': 7},
        {'name': 'later movie',
        'year': 2021,
        'genre': 'None',
        'date_watched': date(2020,4,20),
        'score': 7},
        {'name': 'new movie',
        'year': 2021,
        'genre': 'comedy',
        'date_watched': date(1,1,1),
        'score': 5},
    ]}

# test adding to the watched list from an existing movie in the to watched list
def test_add_list_watched():
    clear_all()

    movie = add_to_watch("new movie", 2021, "comedy")
    assert list_to_watch() == {"to_watch_list": [
        {'name': 'new movie',
        'year': 2021,
        'genre': 'comedy'}
    ]}
    assert list_watched() == {'watched_list': []}

    add_list_watched(movie['id'], '12/1/2021', 10)
    assert list_to_watch() == {'to_watch_list': []}
    assert list_watched() == {'watched_list': [
        {'name': 'new movie',
        'year': 2021,
        'genre': 'comedy',
        'date_watched': date(2021,1,12),
        'score': 10}
    ]}