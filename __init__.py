from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = "Q\xcc\xb8%\x07\x04A\xdeF\xffr\xcb\xd9\xa6!V"
app.config["SQLALCHEMY_DATABASE_URI"] =