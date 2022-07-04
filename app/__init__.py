import os
from flask import Flask
from app import main
from app.main.api import api
from flask_cors import CORS

# Flask App Initialization
app = Flask(__name__)
CORS(app)

# Flask API Initialization
api.init_app(app)