git pull upstream master
manage.py makemigrations main
manage.py makemigrations accounts
manage.py makemigrations adminportal
manage.py makemigrations events
manage.py makemigrations registration
manage.py makemigrations sponsors
manage.py migrate
manage.py runserver
