from flask import jsonify
from flask import request
from flask import Response
import simplejson

from wePredictAPI import app
import MySQLdb


@app.route('/v1/getflu')
def getflu():
    limit = request.args.get('limit')
    if limit is None:
        db = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="mallard", db="wePredict")
        cursor = db.cursor()
        cursor.execute("SELECT * from FLU");
        db.close()
        return jsonify(data=cursor.fetchall())
    else:
        db = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="mallard", db="wePredict")
        cursor = db.cursor()
        cursor.execute("SELECT * from FLU LIMIT " + limit);
        db.close()
        return jsonify(data=cursor.fetchall())


@app.route('/v1/getflu_2012_address')
def getflu12adress():
    db = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="mallard", db="wePredict")
    cursor = db.cursor()
    cursor.execute(
        "SELECT SUM(Value_12), SUBSTRING(Postcode,1,2) As PC FROM FLU Join ADRESS on FLU.Practice_Code = ADRESS.PracticeCode GROUP BY PC;");
    db.close()
    data = cursor.fetchall()
    js_data = []
    for obj in data:
        objjst = {obj[0]: obj[1]}
        js_data.append(objjst)

    return Response(simplejson.dumps(js_data), mimetype='application/json')


