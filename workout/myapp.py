from flask import Flask
from routes import *

app = Flask(__name__)

#launching our server
if __name__ == '__main__':
    app.run()
