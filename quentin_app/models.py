from django.db import models
#Angie Hollingworth S324155, HIT237 Assignment 1, 2020

class Movies(object):
    '''This class is used to create all the attributes for a movie item.'''
    def __init__(self, movie_id, title, release_year, budget, box_office, running_time, genre, imdb, actors,cameo, review_imdb, cover, plot, ref):
        '''
        Initialise a new instance of a movie class item
        '''
        self.movie_id = movie_id
        self.title = title
        self.release_year = release_year
        # Format Budget, box office and profit as comma separated strings 0,000 for currency display
        self.budget = format(budget,",.0f")
        self.box_office = format(box_office,",.0f")
        self.profit = format(box_office - budget,",.0f")
        self.running_time = running_time
        self.genre = genre
        self.imdb = imdb
        self.lead_actors = actors
        self.cameo = cameo
        self.cover = cover
        self.review_imdb = review_imdb
        self.plot = plot
        self.plot_trimmed = self.plot[:95]+'...'
        self.ref = ref

    def __str__(self):
        '''Return a string representation of the movie item'''
        return str(self.title + ': ' + self.genre)


class DictList(object):
    '''This class will create the list of items for the data dictionary model.'''
    def __init__(self, name, purpose, type, constraint):
        self.type = type
        self.purpose = purpose
        self.name = name
        self.constraint = constraint

    def __str__(self):
        '''Return a string object of the data model item'''
        return str(self.name + ': ' + self.purpose + ', ' + self.type + ' (' + self.constraint + ')')
