import os

from flask import Flask
from config import Config
from flask_moment import Moment
#from flask_wtf import package/module

app = Flask(__name__)
app.config.from_object(Config)
moment = Moment(app)

from app import routes
