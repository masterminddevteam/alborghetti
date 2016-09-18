DEV_SETTINGS=alborghetti.settings
project=alborghetti


migrate:
	python manage.py migrate --settings=$(DEV_SETTINGS)

makemigrations:
	python manage.py makemigrations --settings=$(DEV_SETTINGS)

superuser:
	@django/manage.py createsuperuser --settings=$(DEV_SETTINGS)

test: clean
	@py.test -x django/babel

test-debug: clean
	@py.test --pdb -x django/babel

test-matching: clean
	@py.test --pdb django/babel -k $(k)

shell:
	python manage.py shell --settings=$(DEV_SETTINGS)

run:
	python manage.py runserver 0.0.0.0:8000

run-celery:
	celery -A alborghetti worker -l info

install:
	@pip install -r django/requirements/development.txt

flake8:
	@flake8 --show-source .
