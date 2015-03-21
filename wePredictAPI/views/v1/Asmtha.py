from flask import jsonify,g,request
from wePredictAPI.app  import app

@app.route('/v1/getasmtha')
def getAsmtha():
    limit = request.args.get('limit')
    if limit is None:
        return jsonify(data=g.db.getResult("SELECT * from ASTHMA_QOF"))
    else:
        return jsonify(data=g.db.getResult(("SELECT * from ASTHMA_QOF LIMIT " + limit)))
