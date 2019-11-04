# Backend task by Cezary Czemerda
http://cezaryczemerda.pl

Api: http://www.omdbapi.com

CSV File: https://github.com/jimicc/Profil-Software/blob/master/movies.csv

Script file: https://github.com/jimicc/Profil-Software/blob/master/movies.py

Program is able to fill example database with data from OMBd API.
Command line interface of program is capable of:

<b>A)</b> Sorting Movies by every column (argument = '--sort')

<b>Syntax:</b>

python movies.py --sort "COLUMN_NAME" "UP_OR_DOWN(optional)"

<b>Example inputs:</b>

python movies.py --sort year

python movies.py --sort year down

python movies.py --sort title up

<b>B)</b> Filtering by: (argument = '--filter')
1. Director (director)
2. Actor (actor)
3. Movies that was nominated  for Oscar but did not win any. (only_nominated)
4. Movies that won more than 80% of nominations (won_80)
5. Movies that earned more than 100,000,000 $ (box_100)
6. Only movies in certain Language (language)

<b>Syntax for 1, 2:</b>

python movies.py --filter "COLUMN_NAME" "FULL_NAME"

<b>Syntax for 3, 4, 5, 6:</b>

python movies.py --filter "OPTION"

<b>Example inputs:</b>

python movies.py --filter director "Frank DaraBONt"

python movies.py --filter actor "morgan freeman"

python movies.py --filter only_nominated

python movies.py --filter won_80

python movies.py --filter box_100

python movies.py --filter language spanish

<b>C)</b> Comparing by: (argument = '--compare')
- IMDb Rating (imdb_rating)
- Box office earnings (box_office)
- Number of awards won (awards)
- Runtime (runtime)

<b>Syntax:</b>

python movies.py --compare "COLUMN" "FIRST_MOVIE" "SECOND_MOVIE"

<b>Example inputs:</b>

python movies.py --compare imdb_rating "The Godfather" "Kac Wawa"

python movies.py --compare box_office "The Godfather" "Kac Wawa"

python movies.py --compare awards "The Dark Knight" "Memento"

python movies.py --compare runtime "Memento" "Memento"

<b>D)</b> Adding movies to data source (argument = '--add')

<b>Syntax:</b>

python movies.py --add "MOVIE_TITLE"

<b>Example input:</b>

python movies.py --add "Kac Wawa"

<b>E)</b> Showing current highscores in : (argument = '--highscores')
- Runtime
- Box office earnings
- Most awards won
- Most nominations
- Most Oscars
- Highest IMDB Rating

<b>Example Input:</b>

python movies.py --highscores

<b>F)</b> Download data from API: (argument: --download_api)

To test that function I recommend to swap content of movies.csv with content of empty_database.csv

<b>Example Input:</b>

python movies.py --download_api

<b>G)</b> Showing help in terminal : (argument = '--help')

<b>Example Input:</b>

python movies.py --help
