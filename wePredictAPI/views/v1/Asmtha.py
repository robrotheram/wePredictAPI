from flask import jsonify
from flask import request

from wePredictAPI import app
from wePredictAPI import databaseConnection




@app.route('/v1/getasmtha')
def getAsmtha():
    limit = request.args.get('limit')
    if limit is None:
        db = databaseConnection.getConnection()
        cursor = db.cursor()
        cursor.execute("SELECT * from ASTHMA_QOF")
        db.close()
        return jsonify(data=cursor.fetchall())
    else:
        db = databaseConnection.getConnection()
        cursor = db.cursor()
        cursor.execute("SELECT * from ASTHMA_QOF LIMIT " + limit)
        db.close()
        return jsonify(data=cursor.fetchall())
