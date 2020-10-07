# CollectableAPI

## What is it?
This is an API built specifically for my web app [CollectAble](https://github.com/MissPeperr/CollectAble). I built CollectAble while I was a student at Nashville Software School, and at the time of building the app, I only had knowledge of building front-end web applications. This API was meant to replace my use of a node package called [json-server](https://www.npmjs.com/package/json-server) as well as practice building RESTful APIs using [Django](https://www.djangoproject.com/) and [Django-REST](https://www.django-rest-framework.org/).
 
 ### Installation:
 1. Clone down the repo
 1. Set up a virtual environment: `python -m venv CollectableEnv`
 1. Activate virtual environment: `source ./CollectableEnv/bin/activate`
 1. Install dependencies: `pip install -r requirements.txt`
 1. Run migrations: `python manage.py migrate`
 1. Run server: `python manage.py runserver`

### Add some dummy data to play with:
- `python manage.py loaddata users.json`
- `python manage.py loaddata collections.json`
- `python manage.py loaddata collectables.json`