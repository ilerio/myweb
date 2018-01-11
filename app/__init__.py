import os

from flask import Flask
from config import Config
from flask_moment import Moment
from flask_mail import Mail

app = Flask(__name__)
app.config.from_object(Config)
moment = Moment(app)
mail = Mail(app)

from app import routes
