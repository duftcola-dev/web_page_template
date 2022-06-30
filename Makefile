install:

	python -m venv venv
	. venv/bin/activate ; pip install -r  ./requirements/requirements.txt
	. venv/bin/activate ; pip install -e .
	. venv/bin/activate ; pip list

database : 

	- sqlite3 ./app/database/test-db.db  ".read ./app/database/test-init.sql"

console:

	- sqlite3 ./app/database/test-db.db

develop:
	. venv/bin/activate ; export FLASK_APP=app 
	. venv/bin/activate ; gunicorn -w 4 -b 0.0.0.0:3000 --reload -e FLASK_ENV=development main:app

test:

	. venv/bin/activate ; coverage run -m pytest
	. venv/bin/activate ; coverage report 
	. venv/bin/activate ; coverage html 
	google-chrome ./htmlcov/index.html
	