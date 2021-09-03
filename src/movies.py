import json
from datetime import datetime

def add_to_watch(name, year, genre):
    with open('data_files/to_watch.json','r') as open_file:
        to_watch_data = json.load(open_file)
    to_watch = to_watch_data['to_watch']

    with open('data_files/id.json', 'r') as open_file:
        id_data = json.load(open_file)
    curr_id = id_data['id']
    curr_id = curr_id + 1

    # create a new movie
    new_movie = {
        'id': curr_id,
        'name': name,
    }
    # if the year and genre are not entered
    if year == None:
        new_movie['year'] = 'None'
    else:
        new_movie['year'] = year
    if genre == None:
        new_movie['genre'] = 'None'
    else:
        new_movie['genre'] = genre

    to_watch.append(new_movie)

    with open('data_files/to_watch.json','w') as open_file:
        json.dump(to_watch_data, open_file)
    with open('data_files/id.json', 'w') as open_file:
        json.dump({'id': curr_id}, open_file)

def add_new_watched(name, year, genre, date):
    with open('data_files/watched.json','r') as open_file:
        watched_data = json.load(open_file)
    watched = watched_data['watched']

    with open('data_files/id.json', 'r') as open_file:
        id_data = json.load(open_file)
    curr_id = id_data['id']
    curr_id = curr_id + 1


    # create a new movie
    new_movie = {
        'id': curr_id,
        'name': name,
    }
    # if the year and genre are not entered
    if year == None:
        new_movie['year'] = 'None'
    else:
        new_movie['year'] = year
    if genre == None:
        new_movie['genre'] = 'None'
    else:
        new_movie['genre'] = genre
    if date == None:
        new_movie['date_watched'] = 'None'
    else:
        # date format: dd/mm/yyyy
        new_movie['date_watched'] = date

    watched.append(new_movie)

    with open('data_files/watched.json','w') as open_file:
        json.dump(watched_data, open_file)
    with open('data_files/id.json', 'w') as open_file:
        json.dump({'id': curr_id}, open_file)

def remove_movie(id):
    pass