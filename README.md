# Backend task by Cezary Czemerda 

Api: http://www.omdbapi.com
CSV File: https://github.com/jimicc/
Database: https://github.com/jimicc/

Program is able to fill example database with data from OMBd API. 
Command line interface of program is capable of:

A) Sorting Movies by every column (argument = '--sort')

Syntax:

python movies.py --sort "COLUMN_NAME" "UP_OR_DOWN(optional)"
 
Example inputs:
 
python movies.py --sort year
python movies.py --sort year down
python movies.py --sort title up
 
B) Filtering by: (argument = '--filter')
1. Director (director)
2. Actor (actor)
3. Movies that was nominated  for Oscar but did not win any. (only_nominated)
4. Movies that won more than 80% of nominations (won_80)
5. Movies that earned more than 100,000,000 $ (box_100)
6. Only movies in certain Language (language)

Syntax for 1, 2:

python movies.py --filter "COLUMN_NAME" "FULL_NAME"

Syntax for 3, 4, 5, 6:

python movies.py --filter "OPTION" 
 
Example inputs:
 
python movies.py --filter director "Frank DaraBONt"
python movies.py --filter actor "morgan freeman"
python movies.py --filter only_nominated
python movies.py --filter won_80
python movies.py --filter box_100
python movies.py --filter language spanish
 
C) Comparing by: (argument = '--compare')
- IMDb Rating (imdb_rating)
- Box office earnings (box_office)
- Number of awards won (awards_won)
- Runtime (runtime)

Syntax:

python movies.py --compare "COLUMN" "FIRST_MOVIE" "SECOND_MOVIE" 
 
Example inputs:
 
python movies.py --compare imdb_rating "The Godfather" "Kac Wawa"
python movies.py --compare box_office "The Godfather" "Kac Wawa"
python movies.py --compare awards_won "The Dark Knight" "Memento"
python movies.py --compare runtime "Memento" "Memento"
 
D) Adding movies to data source (argument = '--add')

Syntax:

python movies.py --add "MOVIE_TITLE"

Example input:
 
python movies.py --add "Kac Wawa"
 
E) Showing current highscores in : (argument = '--highscores')
- Runtime
- Box office earnings
- Most awards won
- Most nominations
- Most Oscars
- Highest IMDB Rating
 
Example Input:
 
python movies.py --highscores

F) Download data from API: (argument: --download_api)

To test that function I recommend to swap content of movies.csv with content of empty_database.csv

Example Input:
 
python movies.py --download_api


G) Showing help in terminal : (argument = '--help')
 
Example Input:
 
python movies.py --help

"# Profil-Software"  git init git add README.md git commit -m "first commit" git remote add origin https://github.com/jimicc/Profil-Software.git git push -u origin master
"# Profil-Software" 
"# Profil-Software" 
