from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config.from_object('config')
app.config.from_pyfile('development.cfg')
#print(app.title)

db = SQLAlchemy(app)

from flask_blog.views.entries import entry

app.register_blueprint(entry, url_prefix = '/users')

from flask_blog.views import views