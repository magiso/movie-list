import pytest

from src.system import *
from src.movies import *
from datetime import date

# test removing a movie from the to watch list
def test_remove_to_watch():
    clear_all()
    new_movie = add_to_watch("new movie", 2021, "comedy")
    assert list_to_watch() == {'to_watch_list': [
        {'name': 'new movie',
        'year': 2021,
        'genre': 'comedy'}
    ]}

    remove_to_watch(new_movie['id'])
    assert list_to_watch() == {'to_watch_list': []}

# test removing a movie from the watched list
def test_remove_watched():
    clear_all()
    new_movie = add_new_watched("new movie", 2021, "comedy", "01/01/2021", 10)
    assert list_watched() == {'watched_list': [
        {'name': 'new movie',
        'year': 2021,
        'genre': 'comedy',
        'date_watched': date(2021,1,1),
        'score': 10}
    ]}

    remove_watched(new_movie['id'])
    assert list_watched() == {'watched_list': []}