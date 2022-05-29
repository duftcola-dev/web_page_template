install:

	python -m venv venv
	. venv/bin/activate ; pip install -r  ./app/requirements/base_requirements.txt
	. venv/bin/activate ; pip install -e .
	. venv/bin/activate ; pip list

develop:
	. venv/bin/activate ; export FLASK_APP=app 
	. venv/bin/activate ; gunicorn -w 4 -b 0.0.0.0:3000 -e FLASK_ENV=development main:app
