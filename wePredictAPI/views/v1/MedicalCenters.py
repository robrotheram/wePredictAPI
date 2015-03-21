from flask import jsonify
from flask import request

from wePredictAPI.app import app
from wePredictAPI.app  import databaseConnection
from flask import Response
import urllib
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
        objjst = {"CCG": obj['CCG']}
        js_data.append(objjst)

    return Response(simplejson.dumps(js_data), mimetype='application/json')


@app.route('/v1/getpractice')
def getPractice():
    prac = request.args.get('practice')
    if prac is None:
        data = databaseConnection.getResult("SELECT Practice_Name FROM ADRESS join CCG on PracticeCode = CCG.Practice_Code")
        return Response(simplejson.dumps(data), mimetype='application/json')
    else:
        prac = urllib.unquote(prac)
        qurry = ("SELECT Practice_Name FROM ADRESS join CCG on PracticeCode = CCG.Practice_Code where CCG = '"+prac+"';")
        data = databaseConnection.getResult(qurry)
        js_data = []
        for obj in data:
            objjst = {"Practice": obj['Practice_Name']}
            js_data.append(objjst)
        return Response(simplejson.dumps(js_data), mimetype='application/json')
