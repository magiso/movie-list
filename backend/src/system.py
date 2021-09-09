import json

from datetime import date, datetime

################################################################################
#                            Clearing Functions                                #
################################################################################

'''
clear all movies from the to watch list
'''
def clear_to_watch():
    with open("data_files/to_watch.json", "w") as open_file:
        json.dump({'to_watch': []}, open_file)
    return {}

'''
clear all movies from the watched list
'''
def clear_watched():
    with open("data_files/watched.json", "w") as open_file:
        json.dump({'watched': []}, open_file)
    return {}

'''
clear movie id tracker
'''
def clear_ids():
    with open("data_files/id.json", "w") as open_file:
        json.dump({'id': 0}, open_file)
    return {}

'''
clear all data including movies from to watch list, watched list, and movie id tracker
'''
def clear_all ():
    clear_to_watch()
    clear_watched()
    clear_ids()
    return {}

################################################################################
#                            Listing Functions                                 #
################################################################################

'''
list all movies in the to watch list sorted by name
return format:
    {'to_watch_list': [
        {'name': string,
        'year': int,
        'genre': string},
        ...
    ]}
'''
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

'''
list all movies in the watched list sorted by score (descending), 
the date watched (newest to oldest), then by name (ascending)
return format:
    {'to_watch_list': [
        {'name': string,
        'year': int,
        'genre': string,
        'date_watched': date(YYYY,MM,DD),
        'score': double},
        ...
    ]}
'''
def list_watched():
    with open("data_files/watched.json","r") as open_file:
        watched_data = json.load(open_file)
    watched = watched_data['watched']

    all_watched = []
    for movie in watched:

        datetime_object = date.min
        if movie['date_watched'] != 'None':
            datetime_object = datetime.strptime(movie['date_watched'], '%d/%m/%Y').date()
        
        next_movie = {
            'name': movie['name'],
            'year': movie['year'],
            'genre': movie['genre'],
            'date_watched': datetime_object,
            'score': movie['score'],
        }
        all_watched.append(next_movie)

    # sort alphabetically
    all_watched = sorted(all_watched, key = lambda id: id['name'])
    # sort first by score (highest to lowest) then by date watched (newest to oldest)
    all_watched = sorted(all_watched, key = lambda id: (id['score'], 
    id['date_watched']), reverse = True)

    # return all date objects to strings
    for movie in all_watched:
        movie['date_watched'] = movie['date_watched'].strftime('%d/%m/%Y')

    return {'watched_list': all_watched}
    