1. To create db run create_db.sh with root password as given below. The script will change the configs in settings.py as well. (if error occurs saying permission denied run "chmod u+x create_db.sh" to give execution permission to the script).

	- ./create_db.sh <your_root_password_here>

2. Run following commands to generate tables.

	- python3 -m venv .env && source .env/bin/activate && pip install -r requirements.txt
	- python manage.py makemigrations league_stats_app
	- python manage.py migrate 

3. To run the server run
	- python manage.py runserver

4. Please note that only the crud operations are working for the given entities (league_user, team, game).
