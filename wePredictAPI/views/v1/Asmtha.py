from flask import jsonify
from flask import request

from wePredictAPI.app  import app
from wePredictAPI.app  import databaseConnection

@app.route('/v1/getasmtha')
def getAsmtha():
    limit = request.args.get('limit')
    if limit is None:
        return jsonify(data=databaseConnection.getResult("SELECT * from ASTHMA_QOF"))
    else:
        return jsonify(data=databaseConnection.getResult(("SELECT * from ASTHMA_QOF LIMIT " + limit)))
