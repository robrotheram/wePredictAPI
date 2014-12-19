from decimal import *

from flask import Flask, jsonify
from flask import request
from flask import Response
from flask import render_template
import simplejson

import MySQLdb


app = Flask(__name__)

app.config['DEBUG'] = True
app.config['PROPAGATE_EXCEPTIONS'] = True


@app.route('/getadress')
def getAdress():
    limit = request.args.get('limit')
    if limit is None:
        db = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="mallard", db="wePredict")
        cursor = db.cursor()
        cursor.execute("SELECT * from ADRESS");
        db.close()
        return jsonify(data=cursor.fetchall())
    else:
        db = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="mallard", db="wePredict")
        cursor = db.cursor()
        cursor.execute("SELECT * from ADRESS LIMIT " + limit);
        db.close()
        return jsonify(data=cursor.fetchall())


@app.route('/getsmoking')
def getsmoking():
    limit = request.args.get('limit')
    if limit is None:
        db = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="mallard", db="wePredict")
        cursor = db.cursor()
        cursor.execute("SELECT * from SMOKING");
        db.close()
        data = cursor.fetchall()
        js_data = []
        for obj in data:
            objjst = {"Practice_Code": obj[0],
                      "Value_12": obj[1],
                      "Lower_CI_12": obj[2],
                      "Upper_CI_12": obj[3],
                      "Value_13": obj[4],
                      "Lower_CI_13": obj[5],
                      "Upper_CI_13": obj[6]
            }

            js_data.append(objjst)
        return Response(simplejson.dumps(js_data), mimetype='application/json')
    else:
        db = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="mallard", db="wePredict")
        cursor = db.cursor()
        cursor.execute("SELECT * from SMOKING LIMIT " + limit);
        db.close()
        data = cursor.fetchall()
        js_data = []
        for obj in data:
            objjst = {"Practice_Code": obj[0],
                      "Value_12": obj[1],
                      "Lower_CI_12": obj[2],
                      "Upper_CI_12": obj[3],
                      "Value_13": obj[4],
                      "Lower_CI_13": obj[5],
                      "Upper_CI_13": obj[6]
            }

            js_data.append(objjst)
        return Response(simplejson.dumps(js_data), mimetype='application/json')


@app.route('/getflu')
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


@app.route('/getcopd')
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


@app.route('/getpollution')
def getpollution():
    limit = request.args.get('limit')
    if limit is None:
        db = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="mallard", db="wePredict")
        cursor = db.cursor()
        cursor.execute("SELECT * from POLLUTION");
        db.close()
        return jsonify(data=cursor.fetchall())
    else:
        db = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="mallard", db="wePredict")
        cursor = db.cursor()
        cursor.execute("SELECT * from POLLUTION LIMIT " + limit);
        db.close()
        return jsonify(data=cursor.fetchall())


@app.route('/test')
def test():
    data = Decimal(19.123)
    return jsonify(data)


@app.route('/test_table')
def testtable():
    db = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="mallard", db="wePredict")
    cursor = db.cursor()
    cursor.execute("SELECT * from test_table");
    db.close()
    data = cursor.fetchall()
    js_data = []
    for obj in data:
        objjst = {"id": obj[0], "name": obj[1], "age": obj[2]}
        js_data.append(objjst)
    return Response(simplejson.dumps(js_data), mimetype='application/json')


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/chart")
def chartTest():
    return render_template('chart_test.html')