from flask import Flask
from flask_cors import CORS, cross_origin

UPLOAD_FOLDER = './static/uploads/'


app = Flask(__name__)
CORS(app)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER