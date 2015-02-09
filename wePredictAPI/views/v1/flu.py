from flask import jsonify
from flask import request
from flask import Response
import simplejson
from wePredictAPI import app
from wePredictAPI import databaseConnection

@app.route('/v1/getflu')
def getflu():
    limit = request.args.get('limit')
    if limit is None:
        return jsonify(data= databaseConnection.getResult("SELECT * from FLU"))
    else:
        return jsonify(data= databaseConnection.getResult("SELECT * from FLU LIMIT " + limit))


@app.route('/v1/getflu_2012_address')
def getflu12adress():
    data = databaseConnection.getResult("SELECT SUM(Value_12), SUBSTRING(Postcode,1,2) As PC FROM FLU Join ADRESS on FLU.Practice_Code = ADRESS.PracticeCode GROUP BY PC;")
    js_data = []
    for obj in data:
        objjst = {"pc": obj[1], "value": obj[0]}  # Postcode first Value second
        js_data.append(objjst)

    return Response(simplejson.dumps(js_data), mimetype='application/json')


