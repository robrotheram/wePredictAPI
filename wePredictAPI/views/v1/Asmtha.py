from flask import jsonify
from flask import request

from wePredictAPI import app
from wePredictAPI.settings import *
import MySQLdb


@app.route('/v1/getasmtha')
def getAsmtha():
    limit = request.args.get('limit')
    if limit is None:
        db = MySQLdb.connect(host=hostname, port=3306, user=username, passwd=password, db=database)
        cursor = db.cursor()
        cursor.execute("SELECT * from ASTHMA_QOF");
        db.close()
        return jsonify(data=cursor.fetchall())
    else:
        db = MySQLdb.connect(host=hostname, port=3306, user=username, passwd=password, db=database)
        cursor = db.cursor()
        cursor.execute("SELECT * from ASTHMA_QOF LIMIT " + limit);
        db.close()
        return jsonify(data=cursor.fetchall())
