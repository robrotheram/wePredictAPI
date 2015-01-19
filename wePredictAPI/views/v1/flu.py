from flask import jsonify
from flask import request

from wePredictAPI import app
import MySQLdb


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