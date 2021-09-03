import json

from datetime import date, datetime

def clear_to_watch():
    with open("data_files/to_watch.json", "w") as open_file:
        json.dump({'to_watch': []}, open_file)

def clear_watched():
    with open("data_files/watched.json", "w") as open_file:
        json.dump({'watched': []}, open_file)

def clear_ids():
    with open("data_files/id.json", "w") as open_file:
        json.dump({'id': 0}, open_file)

def clear_all ():
    clear_to_watch()
    clear_watched()
    clear_ids()

def list_to_watch():
    with open("data_files/to_watch.json","r") as open_file:
        to_watch_data = json.load(open_file)
    to_watch = to_watch_data['to_watch']

    all_to_watch = []
    for movie in to_watch:
        next_movie = {
            'name': movie['name'],
            'year': movie['year'],
            'genre': movie['genre']
        }
        all_to_watch.append(next_movie)
    all_to_watch = sorted(all_to_watch, key = lambda id: id['name'])
    return {'to_watch_list': all_to_watch}

def list_watched():
    with open("data_files/watched.json","r") as open_file:
        watched_data = json.load(open_file)
    watched = watched_data['watched']

    all_watched = []
    for movie in watched:
        if movie['date_watched'] != 'None':
            datetime_object = datetime.strptime(movie['date_watched'], '%d/%m/%Y').date()
        else:
            datetime_object = date.min
        next_movie = {
            'name': movie['name'],
            'year': movie['year'],
            'genre': movie['genre'],
            'date_watched': datetime_object
        }
        all_watched.append(next_movie)

    all_watched = sorted(all_watched, key = lambda id: (id['date_watched'], id['name']))
    return {'watched_list': all_watched}
    