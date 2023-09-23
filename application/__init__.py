from flask import Flask
from flask_pymongo import PyMongo

# Flask object declaration
app = Flask(__name__)

# Database connection
# local server connection with flask app
app.config["MONGO_URI"] = "{{ secrets.MONGODB_URI }}/calculator"

# Mongodb Object declaration
mongo = PyMongo(app)
# local database collection 
# db = mongo.db.history

from application import routes
