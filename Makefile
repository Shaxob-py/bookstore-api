mig:
	python3 manage.py makemigrations
	python3 manage.py migrate
run:
	python manage.py runserver