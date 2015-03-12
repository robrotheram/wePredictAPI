from flask import jsonify
from flask import request

from wePredictAPI.app import app
from wePredictAPI.app  import databaseConnection
from flask import Response
import simplejson

@app.route('/v1/getadress')
def getAdress():
    limit = request.args.get('limit')
    if limit is None:
        return jsonify(data=databaseConnection.getResult("SELECT * from ADRESS LIMIT "))
    else:
        return jsonify(data=databaseConnection.getResult("SELECT * from ADRESS LIMIT " + limit))

@app.route('/v1/getccg')
def getCCG():
    data = databaseConnection.getResult("SELECT CCG FROM CCG GROUP BY CCG")
    js_data = []
    for obj in data:
        objjst = {"CCG": obj[0]}
        js_data.append(objjst)
    return Response(simplejson.dumps(js_data), mimetype='application/json')
