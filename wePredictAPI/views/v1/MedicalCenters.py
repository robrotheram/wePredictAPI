from flask import jsonify
from flask import request

from wePredictAPI import app
from wePredictAPI.settings import *
import MySQLdb


@app.route('/v1/getadress')
def getAdress():
    limit = request.args.get('limit')
    if limit is None:
        db = MySQLdb.connect(host=hostname, port=3306, user=username, passwd=password, db=database)
        cursor = db.cursor()
        cursor.execute("SELECT * from ADRESS");
        db.close()
        return jsonify(data=cursor.fetchall())
    else:
        db = MySQLdb.connect(host=hostname, port=3306, user=username, passwd=password, db=database)
        cursor = db.cursor()
        cursor.execute("SELECT * from ADRESS LIMIT " + limit);
        db.close()
        return jsonify(data=cursor.fetchall())