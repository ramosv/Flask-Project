from flask import Flask,request,url_for,render_template
from markupsafe import escape
import sqlalchemy

# Define the application
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        return 'login'
    else:
        return 'try again'

@app.route('/user/<username>')
def profile(username):
    return f"{username}'s profile"

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))

# Define the Database
#db = sqlalchemy(app)

#Register Controller
#from .controllers import auth_controller
#app.register_blueprint(auth_controller)