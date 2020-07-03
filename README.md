1. dependencies used -> django / djangorestframework / mysqlclient. Application is run and dependencies collected in an virtural environment. Used dependencies are in requirements.txt (marked with pip freeze and can be satisfied with "pip install -r requirements.txt")

2. To create db run create_db.sh with root password. The script will change the configs in settings.py as well. (if error occurs saying permission denied run "chmod u+x create_db.sh" to give execution permission to the script).

3. Run following commands to generate tables.

	- virtualenv .env && source .env/bin/activate && pip install -r requirements.txt
	- python manage.py makemigrations league_stats_app
	- python manage.py migrate 

4. To run the server run
	- python manage.py runserver

5. Please note that only the crud operations are working for the given entities (league_user, team, game).
