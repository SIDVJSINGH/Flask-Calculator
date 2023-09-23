from flask import Flask
from flask_pymongo import PyMongo

# Flask object declaration
app = Flask(__name__)

# Database connection
# local server connection with flask app
app.config["MONGO_URI"] = "mongodb+srv://sidvjsingh:qns6OsGz45N9rouO@flaskapp.0o6otdg.mongodb.net/calculator"

# Mongodb Object declaration
mongo = PyMongo(app)
# local database collection 
# db = mongo.db.history

from application import routes