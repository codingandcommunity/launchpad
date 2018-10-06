# Launchpad 
The website for students to access coding&&community curriculums online.

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
export FLASK_APP=launchpad
pip install -e .
flask run
```
Then go to your web browser, and navigate to http://localhost:5000

Instructions may be different on Windows.


