from flask import Flask
from SimpleSite.config import Config
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config.from_object(Config)

db = MongoEngine()
db.init_app(app)

from SimpleSite.application import routes
