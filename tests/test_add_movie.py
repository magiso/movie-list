import pytest
import json

from src.system import *
from src.movies import add_to_watch, add_new_watched
from datetime import datetime, date

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

def test_add_watched():
    clear_watched()

    add_new_watched("new movie", 2021, "comedy", None)
    assert list_watched() == {'watched_list': [
        {'name': 'new movie',
        'year': 2021,
        'genre': 'comedy',
        'date_watched': date(1,1,1)}
    ]}

    add_new_watched("another movie", None, "thriller", None)
    assert list_watched() == {'watched_list': [
        {'name': 'another movie',
        'year': 'None',
        'genre': 'thriller',
        'date_watched': date(1,1,1)},
        {'name': 'new movie',
        'year': 2021,
        'genre': 'comedy',
        'date_watched': date(1,1,1)},
    ]}

    add_new_watched("third movie", 2020, None, '01/01/2021')
    assert list_watched() == {'watched_list': [
        {'name': 'another movie',
        'year': 'None',
        'genre': 'thriller',
        'date_watched': date(1,1,1)},
        {'name': 'new movie',
        'year': 2021,
        'genre': 'comedy',
        'date_watched': date(1,1,1)},
        {'name': 'third movie',
        'year': 2020,
        'genre': 'None',
        'date_watched': date(2021,1,1)},
    ]}

    add_new_watched("later movie", 2021, None, '20/4/2020')
    assert list_watched() == {'watched_list': [
        {'name': 'another movie',
        'year': 'None',
        'genre': 'thriller',
        'date_watched': date(1,1,1)},
        {'name': 'new movie',
        'year': 2021,
        'genre': 'comedy',
        'date_watched': date(1,1,1)},
        {'name': 'later movie',
        'year': 2021,
        'genre': 'None',
        'date_watched': date(2020,4,20)},
        {'name': 'third movie',
        'year': 2020,
        'genre': 'None',
        'date_watched': date(2021,1,1)},
    ]}