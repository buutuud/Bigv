# -*- coding=utf-8 -*-
from ServerMd import Server as Model
from flask import Blueprint
from flask import request
from flask import jsonify
bp = Blueprint('Server', __name__)

@bp.route('/api/server/get', methods=['POST'])
def server_get():
    dat = request.json
    servers = Model.objects().all()
    serverary = []
    for e in servers:
        serverary.append(e.tojson())
    return jsonify({'err': 0,
                    'msg': u'获取服务器列表成功',
                    'dat': serverary})
