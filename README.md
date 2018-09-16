# curriculumAPI
This is the backend that will support both the curriculum website and the plugin.
It will interface these frontends with the database and curriculum repository.

## Setup
Setup the virtual environment.
```
python3 -m venv venv
```
Every time you work on the project, start up venv:
```
. venv/bin/activate
```
Install Flask:
```
pip install Flask
```
Windows instructions at http://flask.pocoo.org/docs/1.0/installation/#installation

## Running for the first time
```
export FLASK_APP=curriculumAPI
pip install -e .
flask run
```
Instructions may be different on Windows.


