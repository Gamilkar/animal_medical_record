server:
	pipenv run python3 manage.py runserver


migrations:
	pipenv run python3 manage.py makemigrations


migrate:
	pipenv run python3 manage.py migrate