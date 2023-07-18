# Flask-Project
Python Flask project

## Setup

### Create virtul enviroment in windows using bash
$ cd project_folder
$python3 -m venv .venv 

### Activate Virtual Enviroment
$ . .venv/Scripts/activate
$ (.venv) shows activating virtual enviroment was successful

### Install flask
$ pip install flask

Add .venv to git.ignore that way we are pushing the enviroment to github
$ touch .gitignore


### Flash Building Blocks
app.py: Creates the app and starts the server.   
models.py: Define what the entity will look like (e.g, UserModel has username, email, password etc.) 
controllers.py: Fetches Data from database, generates HTML and sends the response to the user browser.

### Hirarchy
project/
    - app.py
    - models.py
    - controllers.py

## Install SQLAlchemy
-$ pip install SQLAlchemy
-cd into SQLAlchemy source distibution
    -cd path/to/sqlalchemy
    -pip install cython
    -Optional: build cything extensions ahead of install
    -python setup.py build_ext