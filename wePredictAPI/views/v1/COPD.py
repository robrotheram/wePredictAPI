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
        objjst = {"2009": obj[0], "2010": obj[1], "2011": obj[2], "2012": obj[3], "2013": obj[4]}
    js_data.append(objjst)
    return Response(simplejson.dumps(js_data), mimetype='application/json')