from flask import jsonify
from flask import request

from wePredictAPI.app import app
from wePredictAPI.settings import *
import MySQLdb


@app.route('/v1/getpollution')
def getpollution():
    limit = request.args.get('limit')
    if limit is None:
        db = MySQLdb.connect(host=hostname, port=3306, user=username, passwd=password, db=database)
        cursor = db.cursor()
        cursor.execute("SELECT * from POLLUTION");
        db.close()
        return jsonify(data=cursor.fetchall())
    else:
        db = MySQLdb.connect(host=hostname, port=3306, user=username, passwd=password, db=database)
        cursor = db.cursor()
        cursor.execute("SELECT * from POLLUTION LIMIT " + limit);
        db.close()
        return jsonify(data=cursor.fetchall())