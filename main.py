## Import site package -> why __init__.py was needed in the folder structure
from site import build

app = build()  

if __name__ == '__main__':
    app.run(debug=True)