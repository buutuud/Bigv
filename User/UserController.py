# -*- coding=utf-8 -*-
from datetime import datetime as DateTime, timedelta as TimeDelta
from UserMd import User as Model
from Company import CompanyMd
from flask import Blueprint
from flask import request
from flask import jsonify

bp = Blueprint('User', __name__)

@bp.route('/api/user/register', methods=['POST'])
def user_reg():
    dat = request.json
    Model.drop_collection()
    user = Model.objects(username=dat['username']).first()
    users = Model.objects(macaddrs__contains=dat['macaddrs']).all()
    if len(users) >= 1:
        return jsonify({'err': 2, 'msg': u'用户多次注册'})

    if user is None:
        user = Model(username=dat['username'],
                    password=dat['password'],                                        
                    macaddrs=dat['macaddrs'])
        t = DateTime.today() 
        user.createat = t
        user.deadtime = t + TimeDelta(days=1)

        c = CompanyMd.Company.objects(company_name='default').first()
        if not dat.has_key('companyname'):            
            if c is None:
                c = CompanyMd.Company()
                c.company_name = 'default'
                c.save()
            user.company = c.to_dbref()
        else:
            c2 = CompanyMd.Company.objects(company_name=dat['companyname']).first()
            if c2 is None:
                user.company = c.to_dbref()
            else:
                user.company = c2.company_name
                user.deadtime = c2.deadtime
        user.save()
        return jsonify({'err': 0, 'msg': u'用户注册成功'})
    else:
        return jsonify({'err': 1, 'msg': u'用户已注册'})

@bp.route('/api/user/update', methods=['POST'])
def user_update():
    dat = request.json
    user = Model.objects(username=dat['username']).first()
    if user is not None:
        user.deadtime = dat['deadtime']
        user.macaddrs = dat['macaddrs']
        user.save()
        return jsonify({'err': 0, 'msg': u'用户更新成功'})
    else:
        return jsonify({'err': 1, 'msg': u'用户更新失败'})

@bp.route('/api/user/login', methods=['POST'])
def user_login():
    dat = request.json
    user = Model.objects(username=dat['username']).first()
    if user is None:
        return jsonify({'err': 1, 'msg': u'用户未注册'})
    else:
        if user.password == dat['password']:
            if dat.get('lastlogin') is not None:
            	user.lastlogin = dat['lastlogin']
            	user.save()
            return jsonify({'err': 0, 'msg': u'用户登陆成功', 'dat': user.tojson()})
        else:
            return jsonify({'err': 1, 'msg': u'密码错误'})