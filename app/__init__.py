import os
from flask import Flask
from app import main
from app.main.api import api

# Flask App Initialization
app = Flask(__name__)

# Flask API Initialization
api.init_app(app)