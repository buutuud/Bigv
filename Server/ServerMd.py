# -*- coding=utf-8 -*-
# -*- coding: utf-8 -*-
from app import db
from app import admin
from flask_admin.contrib.mongoengine import ModelView

class Server(db.Document):   
    meta = {
        'collection': 'Servers',        
    }
    
    ip  = db.StringField(max_length=30, required=True)
    port = db.StringField(max_length=30)
    tag = db.StringField(max_length=30)

    def tojson(self):
        return {
            'ip': self.ip,
            'port': self.port,
            'tag': self.tag
        }

admin.add_view(ModelView(Server))