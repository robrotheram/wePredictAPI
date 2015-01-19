from flask import jsonify
from flask import request

from wePredictAPI import app
import MySQLdb


@app.route('/getasmtha')
def getAsmtha():
    limit = request.args.get('limit')
    if limit is None:
        db = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="mallard", db="wePredict")
        cursor = db.cursor()
        cursor.execute("SELECT * from ASTHMA_QOF");
        db.close()
        return jsonify(data=cursor.fetchall())
    else:
        db = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="mallard", db="wePredict")
        cursor = db.cursor()
        cursor.execute("SELECT * from ASTHMA_QOF LIMIT " + limit);
        db.close()
        return jsonify(data=cursor.fetchall())
