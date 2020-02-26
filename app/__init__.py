from flask import Flask, jsonify
from flask_cors import CORS
import os


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__, static_url_path="", static_folder=os.path.abspath("app/static"))

# enable CORS
CORS(app)


# sanity check route
@app.route('/', methods=['GET'])
def home():
    return app.send_static_file('index.html')
