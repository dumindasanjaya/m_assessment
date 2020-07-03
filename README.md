1. To create db run create_db.sh with root password as given below. The script will change the configs in settings.py as well. (if error occurs with message permission denied run "chmod u+x create_db.sh" to give execution permission to the script).

	- ./create_db.sh <your_root_password_here>

2. Run following commands to generate tables.

	- python3 -m venv .env && source .env/bin/activate && pip install -r requirements.txt
	- python manage.py makemigrations league_stats_app
	- python manage.py migrate 

3. To run the server run
	- python manage.py runserver

4. Please note that only the get and post operations are working for the given entities (league_user, team, game).

NOTE: before running follwing curls, run populate_data to populate master data.(if error occurs with message permission denied run "chmod u+x populate_data.sh" to give execution permission to the script).

	- ./populate_data.sh <your_root_password_here>

examples :-

create team
--------------- 
curl  -X POST 'http://127.0.0.1:8000/team' --header 'Content-Type: application/json' --data-raw '{ "name": "team-4" }'

get teams
--------------
curl 'http://127.0.0.1:8000/team'

create player
--------------- 
curl -X POST 'http://127.0.0.1:8000/league_user' --header 'Content-Type: application/json' --data-raw '{ "name": "dd", "email": "dd@lakers.com", "height": 6.5, "isLoggedIn": 1, "team": 1, "userType": 1 }'

get players
--------------- 
curl 'http://127.0.0.1:8000/league_user' 

create game
-------------
curl -X POST 'http://127.0.0.1:8000/game' --header 'Content-Type: application/json' --data-raw '{ "name": "game1", "gameDateTime": null, "homeTeamScore": 70, "awayTeamScore": 54, "awayTeam": 1, "homeTeam": 2, "wonByTeam": 1 }'

get games
--------------
curl 'http://127.0.0.1:8000/game' 
