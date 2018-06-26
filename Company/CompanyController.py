# -*- coding=utf-8 -*-
from CompanyMd import Company as Model
from flask import Blueprint
from flask import request
from flask import jsonify


def AddCompany(companyname):
    c = Model()
    c.company_name = companyname
    c.deadtime = DataTime.Now()