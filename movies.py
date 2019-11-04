import csv, requests, argparse, threading
path = "movies.csv"
file = open(path, newline='')
fields = ['id','title','year','runtime','genre','director','cast','writer','language','country','awards','imdb_rating','imdb_votes','box_office']
reader = csv.reader(file)
header = next(reader)


class Movie:
    def __init__(self, title = '', year = '', runtime = '', genre = '', director = '', cast = '', writer = '', language = '', country = '', awards = '', imdb_rating = '', imdb_votes = '', box_office = '',  id  = ''):
        self.id = int(id)
        self.title = title
        self.year = year
        self.runtime = runtime
        self.genre = genre
        self.director = director
        self.cast = cast
        self.writer = writer
        self.language  = language
        self.country = country
        self.awards = awards
        self.imdb_rating = imdb_rating
        self.imdb_votes = imdb_votes
        self.box_office = box_office

class Movies:
    def __init__(self, database):
        self.database = database

    def get_numeric(self, numeric_string):
        result = ''
        for i in range(len(numeric_string)):
            if numeric_string[i].isnumeric():
                result += numeric_string[i]
        if result == '':
            result += '0'
        return int(result)

    def download(self):
        keys = ['Id','Title','Year','Runtime','Genre','Director','Actors','Writer','Language','Country','Awards','imdbRating','imdbVotes','BoxOffice']
        data = [row for row in reader]
        with open(path, mode='w', newline='',encoding='utf-8') as csv_file:
            counter = 0
            writer = csv.DictWriter(csv_file, fieldnames = fields)
            writer.writeheader()
            for row in data:
                print(row)
                response = requests.get(f"http://omdbapi.com/?t={row[1]}&type=movie&r=json&apikey=ef090e9b")
                response = response.json()
                d1 = {'id': str(counter)}
                d2 = {fields[i]: response.get(keys[i]) for i in range(1,14,1)}
                d1.update(d2)
                writer.writerow(d1)
                counter += 1

    def get_wins_and_nominations(self, index_number):
        list_of_numbers = ''
        all_wins = 0
        all_nominations = 0
        win_oscar = 0
        list_of_numbers = [s for s in movies.database[index_number]['awards'].split() if s]
        if list_of_numbers[0] == 'Nominated' and (list_of_numbers[3] == 'Oscar.' or list_of_numbers[3] == 'Oscars.' or list_of_numbers[3] == 'Golden' or list_of_numbers[3] == 'BAFTA'):
            all_nominations += int(list_of_numbers[2])

        if list_of_numbers[0] == 'Won':
            if (list_of_numbers[2] == 'Oscar.' or list_of_numbers[2] == 'Oscars.'):
                win_oscar += int(list_of_numbers[1])
            elif (list_of_numbers[2] == 'BAFTA.'):
                all_wins += int(list_of_numbers[1])
            elif (list_of_numbers[2] == 'Golden.'):
                all_wins += int(list_of_numbers[1])

        if (len(list_of_numbers) > 1):
            if (list_of_numbers[1] == 'wins.'):
                all_wins += int(list_of_numbers[0])
            if (list_of_numbers[1] == 'nominations.'):
                all_nominations += int(list_of_numbers[0])
            if 'wins' in list_of_numbers:
                wins = list_of_numbers.index('wins')
                wins = int(list_of_numbers[wins-1])
                all_wins += wins + win_oscar
            if 'nominations.' in list_of_numbers:
                nominations = list_of_numbers.index('nominations.')
                nominations = int(list_of_numbers[nominations-1])
                all_nominations += nominations
        results = {'oscars': win_oscar, 'wins': all_wins, 'nominations': all_nominations, 'index': index_number}
        return results

    def comparison(self, table_name, first_movie, second_movie):
        found_movies = []

        for i in range(len(movies.database)):
            if (movies.database[i]['title'].lower() == first_movie.lower()):
                found_movies += '1'
                movie_one = Movie(title = movies.database[i]['title'],
                                runtime = movies.database[i]['runtime'],
                                awards = movies.database[i]['awards'],
                                imdb_rating = movies.database[i]['imdb_rating'],
                                box_office = movies.database[i]['box_office'],
                                id = movies.database[i]['id'])

            if (movies.database[i]['title'].lower() == second_movie.lower()):
                found_movies += '2'
                movie_two = Movie(title = movies.database[i]['title'],
                                runtime = movies.database[i]['runtime'],
                                awards = movies.database[i]['awards'],
                                imdb_rating = movies.database[i]['imdb_rating'],
                                box_office = movies.database[i]['box_office'],
                                id = movies.database[i]['id'])

        if '1' not in found_movies:
            print(f"'{first_movie}' not found in database")
        if '2' not in found_movies:
            print(f"'{second_movie}' not found in database")
        if len(found_movies) > 1:
            if table_name == 'runtime':
                if movies.get_numeric(movie_one.runtime) > movies.get_numeric(movie_two.runtime):
                    print(f"Title: {movie_one.title}\t{table_name}: {movie_one.runtime}")
                elif movies.get_numeric(movie_one.runtime) < movies.get_numeric(movie_two.runtime):
                    print(f"Title: {movie_two.title}\t{table_name}: {movie_two.runtime}")
                else:
                    if movies.get_numeric(movie_two.runtime) == 0:
                            print(f'{table_name} of this movies is unknown')
                    else:
                        print(f"'{table_name}' of this movies is equal {movie_two.runtime} for '{movie_one.title}' and '{movie_two.title}'")

            elif table_name == 'box_office':
                if movies.get_numeric(movie_one.box_office) > movies.get_numeric(movie_two.box_office):
                    print(f"Title: {movie_one.title}\t{table_name}: {movie_one.box_office}")
                elif movies.get_numeric(movie_one.box_office) < movies.get_numeric(movie_two.box_office):
                    print(f"Title: {movie_two.title}\t{table_name}: {movie_two.box_office}")
                else:
                    if movies.get_numeric(movie_two.box_office) == 0:
                            print(f'{table_name} of this movies is unknown')
                    else:
                        print(f"'{table_name}' of this movies is equal {movie_two.box_office} for '{movie_one.title}' and '{movie_two.title}'")

            elif table_name == 'imdb_rating':
                if movies.get_numeric(movie_one.imdb_rating) > movies.get_numeric(movie_two.imdb_rating):
                    print(f"Title: {movie_one.title}\t{table_name}: {movie_one.imdb_rating}")
                elif movies.get_numeric(movie_one.imdb_rating) < movies.get_numeric(movie_two.imdb_rating):
                    print(f"Title: {movie_two.title}\t{table_name}: {movie_two.imdb_rating}")
                else:
                    if movies.get_numeric(movie_two.imdb_rating) == 0:
                            print(f'{table_name} of this movies is unknown')
                    else:
                        print(f"'{table_name}' of this movies is equal {movie_two.imdb_rating} for '{movie_one.title}' and '{movie_two.title}'")

            elif table_name == 'awards':
                movie_one_awards = movies.get_wins_and_nominations(movie_one.id)
                movie_two_awards = movies.get_wins_and_nominations(movie_two.id)
                if movie_one_awards['wins'] > movie_two_awards['wins']:
                    print(f"Title: {movie_one.title}\t{table_name}: {movie_one_awards['wins']}")
                elif movie_one_awards['wins'] < movie_two_awards['wins']:
                    print(f"Title: {movie_two.title}\t{table_name}: {movie_two_awards['wins']}")
                else:
                    if movie_two_awards['wins'] == 0:
                            print(f'{table_name} of this movies is unknown or equal to 0')
                    else:
                        print(f"'{table_name}' of this movies is equal {movie_two.imdb_rating} for '{movie_one.title}' and '{movie_two.title}'")

    def filter_by_actor_or_director(self, column_name, full_name):
        if column_name == 'actor':
            column_name = 'cast'
        counter = 0
        id_list = []
        for i in range(len(movies.database)):
            if full_name.lower() in movies.database[i][column_name].lower():
                counter += 1
                id_list.append(i)
        return id_list

    def won_80(self):
        id_list = []
        percentage = 0.0
        for i in range(len(movies.database)):
            win_results = movies.get_wins_and_nominations(i)
            # win results returns dictionary with items: oscars, wins, nominations and index of movie
            if (win_results['wins'] + win_results['nominations']) > 0:
                percentage = win_results['wins']/(win_results['wins']+win_results['nominations'])
            percentage = round(percentage, 2)
            if percentage > 0.8:
                id_list.append(i)
        return id_list

    def box_100(self):
        id_list = []
        for i in range(len(movies.database)):
            if len(movies.database[i]['box_office']) > 11:
                id_list.append(i)
        return id_list

    def language(self, language):
        for i in range(len(movies.database)):
            if language in movies.database[i]['language'].lower():
                print(f" title:{movies.database[i]['title']}  language:{movies.database[i]['language']} ")

    def highscores(self, column_name):
        column_value = 0
        column_index = []
        print(f"#################### {column_name} ########################")
        if (column_name == 'oscars') or (column_name == 'wins') or (column_name == 'nominations'):
            for i in range(len(movies.database)):
                result = movies.get_wins_and_nominations(i)
                if (result[column_name] == column_value):
                    column_index.append(i)
                elif (result[column_name] > column_value):
                    column_index = []
                    column_index.append(i)
                    column_value = result[column_name]
            for item in column_index:
                print(f"Title: {movies.database[item]['title']}\t {column_name.capitalize()}: {column_value}")

        elif (column_name == 'runtime') or (column_name == 'imdb_rating') or (column_name == 'box_office'):
            for i in range(len(movies.database)):
                if (movies.get_numeric(movies.database[i][column_name]) == column_value):
                    column_index.append(i)
                elif (movies.get_numeric(movies.database[i][column_name]) > column_value):
                    column_index = []
                    column_index.append(i)
                    column_value = movies.get_numeric(movies.database[i][column_name])
            for item in column_index:
                print(f"Title: {movies.database[item]['title']}\t {column_name.capitalize()}: {movies.database[item][column_name]}")
    def awards_won(self, movie_title):
        for i in range(len(movies.database)):
            if movies.database[i]["title"].lower() == movie_title.lower():
                win_results = movies.get_wins_and_nominations(i)
        return win_results

    def add_movie(self, movie_title):
        if_exists = True
        counter = 0
        for i in range(len(movies.database)):
            counter += 1
            if movies.database[i]['title'].lower() == movie_title.lower():
                print(f"'{movies.database[i]['title']}' is already in database")
                if_exists = False
        if if_exists == True:
            keys = ['Id','Title','Year','Runtime','Genre','Director','Actors','Writer','Language','Country','Awards','imdbRating','imdbVotes','BoxOffice']
            with open(path, mode='a', encoding='utf-8', errors='ignore', newline='') as append_movie:
                writer2 = csv.DictWriter(append_movie, fieldnames = fields)
                response = requests.get(f"http://omdbapi.com/?t={movie_title}&type=movie&r=json&apikey=ef090e9b")
                response = response.json()
                d1 = {'id': str(counter)}
                d2 = {fields[i]: response.get(keys[i]) for i in range(1,14,1)}
                d1.update(d2)
                if d1['title'] == None:
                    print(f"'{movie_title}' is not in omdb database")
                else:
                    writer2.writerow(d1)
                    print(f"'{d1['title']}' added to database")

    def only_nominated(self):
        id_list = []
        for i in range(len(movies.database)):
            list_of_numbers = [s for s in movies.database[i]['awards'].split() if s]
            if (list_of_numbers[0] == 'Nominated') and ((list_of_numbers[3] == 'Oscar.') or (list_of_numbers[3] == 'Oscars.')):
                id_list.append(i)
        return id_list

    def sort(self, column_name, direction):
        if (args.sort[0] in fields):
            col = fields.index(args.sort[0])
            if (args.sort[0] == 'id') or (args.sort[0] == 'year') or (args.sort[0] == 'runtime') or (args.sort[0] == 'awards') or (args.sort[0] == 'imdb_rating') or (args.sort[0] == 'imdb_votes') or (args.sort[0] == 'box_office'):
                sortedlist = sorted(reader, key=lambda row: movies.get_numeric(row[col]), reverse=direction)
            else:
                sortedlist = sorted(reader, key=lambda row: row[col], reverse=direction)
            index = fields.index(args.sort[0])
            for row in sortedlist:
                if row[col] == 'N/A':
                    pass
                else:
                    if args.sort[0] == 'title':
                        print(f"Id:{row[0]} Title: {row[1]}")
                    else:
                        print(f"Title: {row[1]}, {args.sort[0].capitalize()}: {row[index]}")
        else:
            print('No such column.')

with open(path) as fh:
    database = ''
    rd = csv.DictReader(fh, delimiter=',')
    dictdata = [row for row in rd]
    movies = Movies(dictdata)

parser = argparse.ArgumentParser(description='Backend task for "Profil Software" by Cezary Czemerda')
parser.add_argument("--filter", nargs='*', metavar="str", type=str, help='filter movies by: "director", "actor", "only_nominated", "box_100", "language".', required=False)
parser.add_argument("--sort", nargs='*', metavar="str", type=str, help='Sort movies by every column. ', required=False)
parser.add_argument("--compare", nargs='*', metavar="str", type=str, help='Compare movies by certain column', required=False)
parser.add_argument("--add", nargs='*', metavar="str", type=str, help='Adding movie to database', required=False)
parser.add_argument("--download_api", nargs='*', type=str, help='Download api from omdb', required=False)
parser.add_argument("--highscores", nargs='*', type=str, help='Show current highscores in: runtime, box_office, awards, nominations, oscars, imdb_rating', required=False)
args = parser.parse_args()
if  args.filter != None:
    if len(args.filter) > 0:
        if args.filter[0].lower() == 'director' or args.filter[0].lower() == 'actor':
            if len(args.filter) > 1:
                full_name = " ".join(args.filter[1:])
                result = movies.filter_by_actor_or_director(args.filter[0], full_name)
                if len(result) == 0:
                    print(f"There is no person '{full_name}' in this database")
                for i in result:
                    if args.filter[0] == 'director':
                        print(f"Title: {movies.database[i]['title']}, {args.filter[0].capitalize()}: {movies.database[i]['director']}")
                    elif args.filter[0] == 'actor':
                        print(f"Title: {movies.database[i]['title']}, {args.filter[0].capitalize()}: {movies.database[i]['cast']}")




            else:
                print('please type a name eg. "python movies.py --filter actor "morgan freeman"')
        elif args.filter[0].lower() == 'language':
            movies.language(args.filter[1].lower())
        elif args.filter[0].lower() == 'box_100':
            result = movies.box_100()
            for i in result:
                print(f" Title:{movies.database[i]['title']}, box_office:{movies.database[i]['box_office']} ")
        elif args.filter[0].lower() == 'won_80':
            result = movies.won_80()
            for i in result:
                print(f"Title: {movies.database[i]['title']}  Awards: {movies.database[i]['awards']} ")
        elif args.filter[0].lower() == 'only_nominated':
            result = movies.only_nominated()
            for i in result:
                print(f"Title: {movies.database[i]['title']}, Awards: {movies.database[i]['awards']} ")
    else:
        print("""
    Not enough arguments.
    Example: 'python movies.py --filter language french'
    Type "python movies.py --help" for more information or read "Readme" file".
                        """)
elif args.compare != None:
    if len(args.compare) > 0:
        if args.compare[0].lower() == 'runtime':
            movies.comparison('runtime',args.compare[1],args.compare[2])
        if args.compare[0].lower() == 'box_office':
            movies.comparison('box_office', args.compare[1], args.compare[2])
        if args.compare[0].lower() == 'imdb_rating':
            movies.comparison('imdb_rating', args.compare[1], args.compare[2])
        if args.compare[0].lower() == 'awards':
            first = movies.awards_won(args.compare[1])
            second = movies.awards_won(args.compare[2])
            s = second['index']
            f = first['index']
            if first['wins'] > second['wins']:
                print(f"title:{dictdata[f]['title']}\t awards:{first['wins']}")
            elif first['wins'] < second['wins']:
                print(f"title:{dictdata[s]['title']}\t awards:{second['wins']}")
            else:
                if first['wins'] > 1:
                    print(f"title: '{dictdata[f]['title']}'' and '{dictdata[s]['title']}'' both have: {first['wins']} awards.")
                else:
                    print('no data for this movies')
    else:
         print("""
    Not enough arguments.
    Example: 'python movies.py --compare imdb_rating "joker" "12 angry men"'
    Type "python movies.py --help" for more information or read "Readme" file".
                        """)
elif args.add != None:
    if len(args.add) > 0:
        movies.add_movie(args.add[0])
    else:
         print("""
    Not enough arguments.
    Example: 'python movies.py --add "Kac Wawa"'
    Type "python movies.py --help" for more information or read "Readme" file".
                        """)
elif args.sort != None:
    if len(args.sort) > 0:
        if len(args.sort) > 1:
            if args.sort[1].lower() == 'down':
                movies.sort(args.sort[0], True)
            else:
                movies.sort(args.sort[0], False)
        movies.sort(args.sort[0], False)
    else:
        print("""
    Not enough arguments.
    Example: 'python movies.py --sort year down'
    Type "python movies.py --help" for more information or read "Readme" file".
                        """)
elif args.download_api != None:
        movies.download()
elif args.highscores != None:

    t1 = threading.Thread(target=movies.highscores('runtime'))
    t2 = threading.Thread(target=movies.highscores('box_office'))
    t3 = threading.Thread(target=movies.highscores('imdb_rating'))
    t4 = threading.Thread(target=movies.highscores('oscars'))
    t5 = threading.Thread(target=movies.highscores('wins'))
    t6 = threading.Thread(target=movies.highscores('nominations'))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    print(f"#########################################################")
else:
    print("""
    You did not choose any option.
    Type "python movies.py --help" for more information or read "Readme" file".
                        """)
