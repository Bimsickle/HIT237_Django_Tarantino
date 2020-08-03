from django.shortcuts import render
from .models import Movies, DictList

## Template page rendering functions ##
def home(request):
    '''url(r'^$', views.home), name ="home" '''
    context = {
        'intro' : create_home()
    }
    return render(request, 'quentin_app/home.html', context)


def movies(request):
    ''' url(r'^movies/?$', views.movies), name = "movies" '''
    context = {
        'thelist' : create_movies()
    }
    return render(request, 'quentin_app/movies.html', context)


def details(request, movie_id):
    '''
        url(r'^film/(\d{1,4})/?$', views.details), name = "film"
        View an individual movie that is clicked on from the table list.
    '''
    movie_list = create_movies()
    movie_id = int(movie_id)
    movie = None
    for film in movie_list:
        if film.movie_id == movie_id:
            movie = film
    context = {
        'movie' : movie
    }
    return render(request, 'quentin_app/details.html', context)


def model(request):
    '''
    url(r'^model/?$', views.model), name = "model"
    For creation of the data dictionary model page
    '''
    context = {
        'data_model' : create_dict()
    }
    return render(request, 'quentin_app/model.html', context)


def credits(request):
    '''
    url(r'^credits/?$', views.credits), name = "credits"
    For creation of the reference list page
    '''
    context = {
        'cred' : create_credits()
    }
    return render(request, 'quentin_app/credits.html', context)


def search(request):
    ''' url(r'^search/?$', views.search, name = "search"), '''
    if request.GET.get('search_term'):
        message = '%r' % request.GET['search_term']
    else:
        message = None
    context = {
        'message' : message
    }
    return render(request, 'quentin_app/search.html', context)



## Functions for creating class items ##

def create_movies():
    ''' Constructs a list dataset of Tarantino Movies class items '''
    movie_list = []
    try:
        movie_list.append(Movies(1, 'Resevoir Dogs', 1992, 1200000, 2832029, 99, 'Independant Crime', 8.3, \
                                ['Harvey Keitel', 'Tim Roth', 'Michael Madsen', 'Chris Penn', 'Steve Buscemi', 'Lawrence Tierney', 'Randy Brooks', 'Kirk Baltz', 'Edward Bunker', 'Quentin Tarantino'],\
                                True, 'https://www.imdb.com/title/tt0105236/', 'https://bit.ly/39L6wTm',\
                                'Eight men eat breakfast at a Los Angeles diner before carrying out a diamond heist. Led by Joe Cabot and his son and underboss "Nice Guy" Eddie Cabot, all other criminals \
                                use aliases: Mr. Brown, Mr. White, Mr. Blonde, Mr. Blue, Mr. Orange and Mr. Pink. After discussing the Madonna song "Like a Virgin" and arguing over Pink\'s habit of not tipping, \
                                the group leaves the diner to perform the heist.', \
                                '(Anon 2020b)'))
        movie_list.append(Movies(2, 'True Romance', 1993, 12500000, 12300000, 118, 'Romantic Crime', 7.9, \
                                ['Christian Slater', 'Patricia Arquette', 'Dennis Hopper', 'Val Kilmer', 'Gary Oldman', 'Brad Pitt', 'Christopher Walken', 'Bronson Pinchot', 'Samuel L. Jackson', 'Michael Rapaport'],\
                                False,'https://www.imdb.com/title/tt0108399/', 'https://bit.ly/3aQT7ul',\
                                'At a Detroit theater showing kung fu films, Alabama Whitman strikes up a conversation with Elvis Presley fanatic Clarence Worley. They later have sex at Clarence\'s apartment in \
                                downtown Detroit. Alabama tearfully confesses that she is a call girl hired by Clarence\'s boss as a birthday present but has fallen in love with Clarence. They marry.', \
                                '(Anon 2020d)'))
        movie_list.append(Movies(3, 'Pulp Fiction', 1994, 8500000, 213900000, 154, 'Crime', 8.9, \
                                ['Tim Roth', 'Amanda Plummer', 'Laura Lovelace', 'John Travolta', 'Samuel L. Jackson', 'Phil LaMarr', 'Frank Whaley', 'Burr Steers', 'Bruce Willis', 'Ving Rhames', \
                                'Paul Calderon', 'Bronagh Gallagher', 'Rosanna Arquette', 'Eric Stoltz', 'Uma Thurman'],\
                                True, 'https://www.imdb.com/title/tt0110912/', 'https://bit.ly/3aFPTth', \
                                'Hitmen Jules Winnfield and Vincent Vega arrive at an apartment to retrieve a briefcase for their boss, gangster Marsellus Wallace, from a business partner, Brett. After Vincent \
                                checks the contents of the briefcase, Jules shoots one of Brett\'s associates, then declaims a passage from the Bible before he and Vincent kill Brett for trying to double-cross \
                                Marsellus. They take the briefcase to Marsellus, but have to wait while he bribes champion boxer Butch Coolidge to take a dive in his upcoming match.', \
                                '(Wikipedia Contributors 2020c)'))
        movie_list.append(Movies(4, 'Kill Bill Volume 1', 2003, 30000000, 180900000, 111, 'Martial Arts', 8.1, \
                                ['Uma Thurman', 'Lucy Liu', 'Vivica A. Fox', 'Daryl Hannah', 'David Carradine', 'Michael Madsen', 'Julie Dreyfus', 'Chiaki Kuriyama', 'Shin\'ichi Chiba', 'Chia-Hui Liu', \
                                'Michael Parks', 'Michael Bowen'], \
                                True, 'https://www.imdb.com/title/tt0266697/', 'https://bit.ly/2JNgMQt',\
                                'A woman in a wedding dress, the Bride, lies wounded in a chapel in El Paso, Texas, having been attacked by the Deadly Viper Assassination Squad. She tells their leader, Bill, \
                                that she is pregnant with his baby. He shoots her in the head.',\
                                '(Wikipedia Contributors 2020a)'))
        movie_list.append(Movies(5, 'Kill Bill Volume 2', 2004, 30000000, 152200000, 136, 'Martial Arts', 8.0, \
                                ['Uma Thurman', 'Lucy Liu', 'Vivica A. Fox', 'Daryl Hannah', 'David Carradine', 'Michael Madsen', 'Julie Dreyfus', 'Chiaki Kuriyama', 'Shin\'ichi Chiba', 'Chia-Hui Liu', \
                                'Michael Parks', 'Michael Bowen'], \
                                False, 'https://www.imdb.com/title/tt0378194/','https://bit.ly/3bMo1DZ',\
                                'Four years before the events of Kill Bill: Volume 1, the pregnant Bride and her groom rehearse their wedding. Bill, the Bride\'s former lover, the father of her child, \
                                and the leader of the Deadly Viper Assassination Squad, arrives unexpectedly and orders the Deadly Vipers to kill everyone at the wedding. Bill shoots the Bride in the head, \
                                but she survives and swears revenge.', \
                                '(Anon 2020a)'))
        movie_list.append(Movies(6, 'Inglourious Basterds', 2009, 70000000, 321500000, 153, 'War', 8.3, \
                                ['Brad Pitt', 'Mélanie Laurent', 'Christoph Waltz', 'Eli Roth', 'Michael Fassbender', 'Diane Kruger', 'Daniel Brühl', 'Til Schweiger', 'Gedeon Burkhard', 'Jacky Ido', \
                                'B.J. Novak', 'Omar Doom', 'August Diehl', 'Denis Ménochet', 'Sylvester Groth', 'Martin Wuttke', 'Mike Myers','Julie Dreyfus'], \
                                True, 'https://www.imdb.com/title/tt0361748/','https://bit.ly/2woCpn1', \
                                'Part one, "Once Upon a Time in Nazi-Occupied France," is set in 1941. SS-Standartenführer Hans Landa interrogates French dairy farmer Perrier LaPadite as to the whereabouts \
                                of the last unaccounted-for Jewish family in the area, the Dreyfus family. Landa suspects that they are hiding under the floor and, in exchange for the Germans agreeing to leave his \
                                family alone for the rest of the war, LaPadite reluctantly confirms it. Landa orders his SS soldiers to shoot through the floorboards, killing all but one of the Dreyfus family; \
                                Shosanna, the daughter, escapes. As she runs, Col. Landa decides to spare her.', \
                                '(Wikipedia Contributors 2019b)'))
        movie_list.append(Movies(7, 'Django Unchained', 2012, 100000000, 425000000, 165, 'Revisionist Western', 8.4, \
                                ['Jamie Foxx', 'Christoph Waltz', 'Leonardo DiCaprio', 'Kerry Washington', 'Samuel L. Jackson', 'Walton Goggins', 'Dennis Christopher', 'James Remar', 'David Steen', \
                                'Dana Gourrier', 'Nichole Galicia'], \
                                True, 'https://www.imdb.com/title/tt1853728/','https://bit.ly/2JCQVu8',\
                                'In early 1858 Texas, brothers Ace and Dicky Speck drive a group of shackled black slaves on foot. Among them is Django, sold off and separated from his wife Broomhilda von Shaft, \
                                a house slave who speaks German and English. They are stopped by Dr. King Schultz, a German dentist-turned-bounty hunter seeking to buy Django for his knowledge of the three outlaw \
                                Brittle brothers, overseers at the plantation of Django\'s previous owner and for whom Schultz has a warrant. When Ace levels his gun at him, Schultz kills him and wounds Dicky. \
                                Schultz insists on paying a fair price for Django before leaving Dicky to the newly freed slaves, who kill him and follow the North Star to freedom. Schultz offers Django his \
                                freedom and $75 in exchange for help tracking down the Brittles.',\
                                '(Wikipedia Contributors 2019a)'))
        movie_list.append(Movies(8, 'The Hateful Eight', 2015, 44000000, 155800000, 187, 'Western Thriller', 7.8, \
                                ['Samuel L. Jackson', 'Kurt Russell', 'Jennifer Jason Leigh', 'Walton Goggins', 'Demián Bichir', 'Tim Roth', 'Michael Madsen', 'Bruce Dern', 'James Parks', 'Dana Gourrier', 'Zoë Bell'], \
                                True, 'https://www.imdb.com/title/tt3460252/','https://bit.ly/39J7orf',\
                                'In 1877, bounty hunter and Civil War veteran Major Marquis Warren is transporting three dead bounties to the town of Red Rock, Wyoming. He hitches a ride on a stagecoach \
                                driven by a man known only as O.B. Aboard is bounty hunter John Ruth, and handcuffed to him is fugitive Daisy Domergue, whom Ruth is escorting to Red Rock to collect her \
                                bounty and watch her hang. Ruth and Warren are previous acquaintances who bonded over Warren\'s personal letter from Abraham Lincoln. Former Lost-Causer militiaman Chris Mannix, \
                                who is traveling to Red Rock as the town\'s new sheriff, persuades Ruth and Warren to let him on the stagecoach. Warren and Ruth form an alliance to protect each other\'s bounties.',\
                                '(Anon 2020c)'))
        movie_list.append(Movies(9, 'Once Upon a Time in Hollywood', 2019, 96000000, 374300000, 161, 'Comedy-Drama', 7.7, \
                                ['Leonardo DiCaprio', 'Brad Pitt', 'Margot Robbie', 'Emile Hirsch', 'Margaret Qualley', 'Timothy Olyphant', 'Julia Butters', 'Austin Butler', 'Dakota Fanning', 'Bruce Dern', \
                                'Mike Moh', 'Luke Perry','Damian Lewis', 'Al Pacino'], \
                                True, 'https://www.imdb.com/title/tt7131622/','https://bit.ly/3e0KjnD',\
                                'In February 1969, veteran Hollywood actor Rick Dalton (DiCaprio), star of 1950s Western television series Bounty Law, fears his career is waning. Casting agent Marvin Schwarz \
                                (Pacino) recommends he make Spaghetti Westerns in Italy, which Dalton feels are beneath him. Dalton\'s best friend and stunt double, Cliff Booth (Pitt)—a war veteran skilled in \
                                hand-to-hand combat who lives in a tiny trailer with his pit bull, Brandy—drives Dalton around Los Angeles because Dalton\'s driver\'s license has been suspended due to DUI. \
                                Booth struggles to find stunt work in Hollywood because of rumors he murdered his wife. Actress Sharon Tate (Robbie) and her husband, director Roman Polanski (Zawierucha), \
                                have moved next door to Dalton. He dreams of befriending them to revive his declining acting career. That night, Tate and Polanski attend a celebrity-filled party at \
                                the Playboy Mansion.',\
                                '(Wikipedia Contributors 2020b)'))
    except Exception:
        #Runs if a value is missng from the list that is passed to the class object
        movie_list.append(Movies(0, 'There was an error in your movie list and some data was missing, please check the values and try again', 1111, 2, 1, 0, 'None', 0.0, 'None', 0, 'None', 'None', 'None', 'None'))
    return movie_list


def create_dict():
    ''' Constructs a list of data dictionary model values. '''
    dictlist = []
    try:
        dictlist.append(DictList('Movie ID', 'For identifying each movie by a unique number', 'Integer', 'Unique'))
        dictlist.append(DictList('Movie Title', 'The title of each Tarantino film', 'Text String', 'None'))
        dictlist.append(DictList('Release Year', 'The year the movie was released', 'Integer - YYYY', 'None'))
        dictlist.append(DictList('Budget', 'The budget spent on each movie in USD', 'Number as a string in comma form 0,000', 'None'))
        dictlist.append(DictList('US Box Office', 'The amount received in the US box office in USD', 'Number as a string in comma form 0,000', 'None'))
        dictlist.append(DictList('Profit', 'The profit made from the movie USD', 'Number as a string in comma form 0,000', 'None'))
        dictlist.append(DictList('Run Time', 'Number of minutes the movie runs for', 'Minutes - Integer', 'None'))
        dictlist.append(DictList('Genre', 'The genre of the film as specified on Wikipedia', 'Text String', 'None'))
        dictlist.append(DictList('IMDB Score', 'The rating given to the movie on the IMDb website', 'Float', 'None'))
        dictlist.append(DictList('Lead Actors', 'List of some of the first actors on the cast list', 'String List', 'None'))
        dictlist.append(DictList('QT Cameo', 'True or False if Quentin Tarantino has a cameo role in the film', 'Boolean', 'Boolean, defaults True'))
        dictlist.append(DictList('Movie Poster', 'Url path to the movie poster on IMDb review page', 'Url path', 'None'))
        dictlist.append(DictList('IMDB Review', 'Url path to IMDb review of the film', 'Url path', 'None'))
        dictlist.append(DictList('Plot', 'The first paragraph of the movie plot from Wikipedia', 'Text String', 'None'))
        dictlist.append(DictList('Plot Trimmed', 'The first 95 characters of the plot, followed by \'...\'', 'Text String', 'Limit 98 characters'))
        dictlist.append(DictList('Citation', 'Citation used for plot direct quote from Wikipedia', 'Text String', 'None'))
    except:
        #Runs if a value is missng from the list that is passed to the class object
        dictlist.append(DictList('Error', 'There was an error in one of your data model items, please check the list and refresh page', 'None', 'None'))

    return dictlist



#Functions for creating other non-class lists

def create_home():
    ''' Contruction of the home page content paragraphs '''
    maintext = []
    maintext.append('Have you ever read a movie title and you just "knew" exactly what the film would be about? Then, whilst you are watching the movie, about halfway through found yourself thinking, \
                    "Wow, I didn\'t think the plotline would go there"?')
    maintext.append('Great! Do you remember the following scene…')
    maintext.append('[Jules] "Well, there\'s this passage I\'ve got memorized that sort of fits this occasion. Ezekiel 25:17. The path of the righteous man is beset on all sides by the iniquities \
                    of the selfish and the tyranny of the evil men. Blessed is he who, in the name of charity and goodwill, shepherds the weak through the valley of darkness, for he is truly \
                    his brother\'s keeper, and the finder of lost children. And I will strike down upon thee with great vengeance and furious anger those who attempt to poison and destroy my brothers. \
                    And you will know my name is the Lord when I lay my vengeance upon thee!" (Jackson S.L.)')
    maintext.append('This particular rendition of the line is not from a sermon in a church or spoken by someone of a religious position. It is Samuel L. Jackson in one of his most memorable movie moments. \
                    If you haven’t seen it, or wish to remind yourself you can do so by clicking ‘About’. (Strong violence warning!)')
    maintext.append('Let\'s take a moment and step away from movie clips and quotes and back to movie backgrounds and facts. Whilst perusing this site, you will glean a small amount of information \
                    about several of my favourite Tarantino films, and you may find out if he actually does play a cameo role to some degree or another in "all" of his movies.')
    maintext.append('And besides, they must be good movies if one of them has "Django" in the title... right?')
    maintext.append('Enjoy!')
    return maintext


def create_credits():
    ''' Create the reference list for the credits page '''
    credlist = []
    credlist.append('Anon 2020a, Kill Bill Volume 2, https://en.wikipedia.org/wiki/Kill_Bill:_Volume_2')
    credlist.append('Anon 2020b, Reservoir Dogs, https://en.wikipedia.org/wiki/Reservoir_Dogs')
    credlist.append('Anon 2020c, The Hateful Eight, https://en.wikipedia.org/wiki/The_Hateful_Eight')
    credlist.append('Anon 2020d, True Romance, https://en.wikipedia.org/wiki/True_Romance')
    credlist.append('Jackson S.L. (1994), Ezekiel 25:17 - Pulp Fiction High Quality Full Scene [Online Video] Available at: https://www.youtube.com/watch?v=wtf5ZoFiKm0&feature=youtu.be&t=101, Accessed [8 April 2020]')
    credlist.append('Simpson, R 2019. ringer_tarantino_r1.0.jpg, https://www.theringer.com/movies/2019/7/24/20708337/quentin-tarantino-movies-life')
    credlist.append('Wikipedia Contributors 2019a, Django Unchained, https://en.wikipedia.org/wiki/Django_Unchained')
    credlist.append('Wikipedia Contributors 2019b, Inglorious Basterds, https://en.wikipedia.org/wiki/Inglourious_Basterds')
    credlist.append('Wikipedia Contributors 2019c, Pulp Fiction, https://en.wikipedia.org/wiki/Pulp_Fiction')
    credlist.append('Wikipedia Contributors 2020a, Kill Bill Volume 1, https://en.wikipedia.org/wiki/Kill_Bill:_Volume_1')
    credlist.append('Wikipedia Contributors 2020b, Once Upon a Time in Hollywood, https://en.wikipedia.org/wiki/Once_Upon_a_Time_in_Hollywood')
    return credlist
