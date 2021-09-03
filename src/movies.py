import json
from datetime import datetime

################################################################################
#                             Adding Functions                                 #
################################################################################

'''
Add a movie to the to watch list
Has structure:
    {'id': int
    'name': string,
    'year': int,
    'genre': string}
Returns:
    {'movie_id': curr_id}
    The current id of the newly created movie
'''
def add_to_watch(name, year, genre):
    with open('data_files/to_watch.json','r') as open_file:
        to_watch_data = json.load(open_file)
    to_watch = to_watch_data['to_watch']

    with open('data_files/id.json', 'r') as open_file:
        id_data = json.load(open_file)
    curr_id = id_data['id']
    curr_id = curr_id + 1

    # create a new movie
    new_movie = create_new_movie(name, year, genre, None, curr_id, None)

    to_watch.append(new_movie)

    with open('data_files/to_watch.json','w') as open_file:
        json.dump(to_watch_data, open_file)
    with open('data_files/id.json', 'w') as open_file:
        json.dump({'id': curr_id}, open_file)

    return {'id': curr_id}

'''
Add a new movie to the watched list
Has structure:
    {'id': int
    'name': string,
    'year': int,
    'genre': string,
    'date_watched': date(YYYY,MM,DD),
    'score': double}
Returns:
    {'movie_id': curr_id}
    The current id of the newly created movie
'''
def add_new_watched(name, year, genre, date, score):
    with open('data_files/watched.json','r') as open_file:
        watched_data = json.load(open_file)
    watched = watched_data['watched']

    with open('data_files/id.json', 'r') as open_file:
        id_data = json.load(open_file)
    curr_id = id_data['id']
    curr_id = curr_id + 1

    # create a new movie
    new_movie = create_new_movie(name, year, genre, date, curr_id, score)

    watched.append(new_movie)

    with open('data_files/watched.json','w') as open_file:
        json.dump(watched_data, open_file)
    with open('data_files/id.json', 'w') as open_file:
        json.dump({'id': curr_id}, open_file)

    return {'id': curr_id}

'''
Add a movie to the watched list from the to watch list, and remove the movie from
the to watch list
Has structure:
    {'id': int
    'name': string,
    'year': int,
    'genre': string,
    'date_watched': date(YYYY,MM,DD),
    'score': double}
Returns:
    {'movie_id': int}
    The current id of the moved movie
'''
def add_list_watched(movie_id, date, score):
    with open('data_files/to_watch.json','r') as open_file:
        to_watch_data = json.load(open_file)
    to_watch = to_watch_data['to_watch']

    with open('data_files/watched.json','r') as open_file:
        watched_data = json.load(open_file)
    watched = watched_data['watched']

    for movie in to_watch:
        if movie_id == movie['id']:
            to_watch.remove(movie)
            new_movie = create_new_movie(movie['name'], movie['year'], movie['genre']
            , date, movie['id'], score)
            watched.append(new_movie)
            break

    with open('data_files/to_watch.json','w') as open_file:
        json.dump(to_watch_data, open_file)
    with open('data_files/watched.json','w') as open_file:
        json.dump(watched_data, open_file)

    return {'id': movie_id}

################################################################################
#                            Remove Functions                                  #
################################################################################

'''
Remove a movie from any list with the given movie id

Returns:
    boolean: status of whether it was removed or not
'''
def remove_movie(movie_id):
    with open('data_files/to_watch.json','r') as open_file:
        to_watch_data = json.load(open_file)
    to_watch = to_watch_data['to_watch']

    with open('data_files/watched.json','r') as open_file:
        watched_data = json.load(open_file)
    watched = watched_data['watched']

    # Remove the movie from to_watch
    for movie in to_watch:
        if movie_id == movie['id']:
            to_watch.remove(movie)
            with open('data_files/to_watch.json','w') as open_file:
                json.dump(to_watch_data, open_file)
            return True
    
    # Remove the movie from watched
    for movie in watched:
        if movie_id == movie['id']:
            watched.remove(movie)
            with open('data_files/watched.json','w') as open_file:
                json.dump(watched_data, open_file)
            return True

    return False

################################################################################
#                            Helper Functions                                  #
################################################################################

def create_new_movie(name, year, genre, date_watched, movie_id, score):
    # create a new movie
    new_movie = {
        'id': movie_id,
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

    if date_watched == None:
        new_movie['date_watched'] = 'None'
    else:
        # date format: dd/mm/yyyy
        new_movie['date_watched'] = date_watched

    if score == None:
        new_movie['score'] = 'None'
    else:
        new_movie['score'] = score

    return new_movie