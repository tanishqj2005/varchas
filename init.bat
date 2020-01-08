git pull upstream master
python manage.py makemigrations main
python manage.py makemigrations accounts
python manage.py makemigrations adminportal
python manage.py makemigrations events
python manage.py makemigrations registration
python manage.py makemigrations sponsors
python manage.py migrate
python manage.py runserver
