# -*- coding=utf-8 -*-
# -*- coding: utf-8 -*-
from app import db
from app import admin
from flask_admin.contrib.mongoengine import ModelView

class Company(db.Document):   
    meta = {
        'collection': 'Company',        
    }

    company_name = db.StringField(max_length=30, required=True)
    deadtime = db.DateTimeField()            
    def tojson(self):
        return {
            'company_name': self.company_name,
            'deadtime': self.password
        }

admin.add_view(ModelView(Company))