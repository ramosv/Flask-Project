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
$ pip install flask-login
$ pip install flask-sqlalchemy

Add .venv to git.ignore that way we are pushing the enviroment to github
$ touch .gitignore


### Flash Building Blocks
app.py or main.py: Creates the app and starts the server.


models.py: Define what the entity will look like (e.g, UserModel has username, email, password etc.) 
auth.py: handles authentiction login data
views.py: front end of the application
__init__.py: This file makes the site folder a python package
Allows contects of site to run automatomatically
works sort of as a constructor for the site folder
controllers.py: Fetches Data from database, generates HTML and sends the response to the user browser.

### Hirarchy
project/
    - app.py
    - models.py
    - controllers.py


## Running the app from local machine
$ flask -app app run

## Run in debug mode
$$ flask --app app run --debug


### Running the app from local network
$ flask run --host=0.0.0.0 
    -this tells OS to listen on all public IPs

