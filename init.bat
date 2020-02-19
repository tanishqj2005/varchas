git pull upstream master
python3 manage.py makemigrations main
python3 manage.py makemigrations accounts
python3 manage.py makemigrations adminportal
python3 manage.py makemigrations events
python3 manage.py makemigrations registration
python3 manage.py makemigrations sponsors
python3 manage.py migrate
python3 manage.py runserver
