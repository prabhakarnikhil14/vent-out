from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from elasticsearch import Elasticsearch
from celery import Celery
import os

app = Flask(__name__)

app.config['CELERY_BROKER_URL'] = 'amqp://'
app.config['CELERY_RESULT_BACKEND'] = 'amqp://'

celery_down = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery_down.conf.update(app.config)

app.config['SECRET_KEY'] = '04f75668f033b427c20fba935b2f831c'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
es = Elasticsearch('http://127.0.0.1:9200')

from ventout import routes
