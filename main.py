## Import site package -> why __init__.py was needed in the folder structure

import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__),"site"))



from .site.app import app


App = app.build()

if __name__ == "__main__":
    App.run(debug=True)
