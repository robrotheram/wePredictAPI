__author__ = 'robert'

from flask import request
from flask import Response
import simplejson

from wePredictAPI.app import app
from wePredictAPI.settings import *
import MySQLdb


@app.route('/v1/getsmoking')
def getsmoking():
    limit = request.args.get('limit')
    if limit is None:
        db = MySQLdb.connect(host=hostname, port=3306, user=username, passwd=password, db=database)
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
        db = MySQLdb.connect(host=hostname, port=3306, user=username, passwd=password, db=database)
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
