#!/bin/sh
export FLASK_ENV=development
export FLASK_APP=./randompet/app.py
source $(pipenv --venv)/bin/activate
flask run -h 127.0.0.1 -p 5000