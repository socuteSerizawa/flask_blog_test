from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config.from_object('config')
app.config.from_pyfile('development.cfg')

db = SQLAlchemy(app)

import flask_blog.views