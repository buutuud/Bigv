# -*- coding=utf-8 -*-
import os
from flask import Flask
from flask_session import Session
from flask_admin import Admin
from flask_mongoengine import MongoEngine
app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db':   'SuperVip',
    'host': 'ts.alphaz.cn',
    'port': 27017
}

app.config['SECRET_KEY'] = os.urandom(24)
app.config['SESSION_TYPE'] = 'filesystem'
ss = Session(app)
db = MongoEngine(app)

admin = Admin(app, name='BigV', template_mode='bootstrap3')


from User import UserController
from Server import ServerController

app.register_blueprint(UserController.bp)
app.register_blueprint(ServerController.bp)