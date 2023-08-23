# This file makes the site folder a python package
## Allows contects of site to run automatomatically
## works sort of as a constructor for the site folder

from flask import Flask

class app:
    def build():
        ##App object - initilizes app
        app = Flask(__name__)

        ##Key built with my password generator located @ https://github.com/ramosv/Python-MiniProjects/blob/main/password_generator.py
        ##Doesn't matter because project is still public 
        ##Secret key: secures cookies and setion data
        #app.config['SECRET_KEY'] = '9+Fu+8&u49D=3.?4&7~1]T&v93'

        ## return flask object
        return app