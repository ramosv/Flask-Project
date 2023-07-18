from flask import Flask
import sqlalchemy

# Define the application
app = Flask(__name__)

# Define the Database
db = sqlalchemy(app)

#Register Controller
from .controllers import auth_controller
app.register_blueprint(auth_controller)