# -*- coding: utf-8 -*-
from app import db
from app import admin
from flask_admin.contrib.mongoengine import ModelView
from Company import CompanyMd
class User(db.Document):   
    meta = {
        'collection': 'Users2',
        'ordering': ['createat'],
    }
    username = db.StringField(max_length=30, required=True)
    password = db.StringField(max_length=30, required=True)
    company  = db.StringField()
    createat = db.DateTimeField()
    deadtime = db.DateTimeField()
    lastlogin = db.StringField()
    macaddrs = db.StringField()
    def __unicode__(self):
        return self.username

    def tojson(self):
        return {
            'username': self.username,
            'password': self.password,
            'createat': self.createat,
            'deadtime': self.deadtime,
            'lastlogin': self.lastlogin,
            'macaddrs': self.macaddrs
        }

admin.add_view(ModelView(User))
