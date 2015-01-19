__author__ = 'robert'
from flask import jsonify
from flask import request
from flask import Response
import simplejson

from wePredictAPI import app
import MySQLdb


@app.route('/v1/getcopd')
def getcopd():
    limit = request.args.get('limit')
    if limit is None:
        db = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="mallard", db="wePredict")
        cursor = db.cursor()
        cursor.execute("SELECT * from COPD");
        db.close()
        return jsonify(data=cursor.fetchall())
    else:
        db = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="mallard", db="wePredict")
        cursor = db.cursor()
        cursor.execute("SELECT * from COPD LIMIT " + limit);
        db.close()
        return jsonify(data=cursor.fetchall())


@app.route('/v1/getcopdaverage')
def getcopdaverage():
    db = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="mallard", db="wePredict")
    cursor = db.cursor()
    cursor.execute("SELECT Avg(Value_09), Avg(Value_10), Avg(Value_11), Avg(Value_12), Avg(Value_13) FROM COPD");
    db.close()
    data = cursor.fetchall()
    js_data = []
    for obj in data:
        objjst = {"y": "2009", "value_y": obj[0]}
        js_data.append(objjst)
        objjst = {"y": "2010", "value_y": obj[1]}
        js_data.append(objjst)
        objjst = {"y": "2011", "value_y": obj[2]}
        js_data.append(objjst)
        objjst = {"y": "2012", "value_y": obj[3]}
        js_data.append(objjst)
        objjst = {"y": "2013", "value_y": obj[4]}
        js_data.append(objjst)

    return Response(simplejson.dumps(js_data), mimetype='application/json')