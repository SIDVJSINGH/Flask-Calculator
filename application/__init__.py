from flask import Flask
from flask_pymongo import PyMongo

# Flask object declaration
app = Flask(__name__)

# Database connection
db = PyMongo(app, uri="mongodb://localhost:27017/<database>")

from application import routes