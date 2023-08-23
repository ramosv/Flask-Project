## Import site package -> why __init__.py was needed in the folder structure

import os, sys
#sys.path.append(os.path.dirname(os.path.realpath(__file__)))

sys.path.append("c:/Users/ramosv/Desktop/Python_Flask_2.0/Flask-Project")

from .site import build


app = build()

if __name__ == "main":
    app.run(debug=True)
