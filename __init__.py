from flask import Flask, jsonify
import simplejson as json
from flask import request
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
        return jsonify(data = cursor.fetchall())
    else:
        db = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="mallard", db="wePredict")
        cursor = db.cursor()
        cursor.execute("SELECT * from ADRESS LIMIT "+limit);
        db.close()
        return jsonify(data = cursor.fetchall())

@app.route('/getsmoking')
def getsmoking():
    limit = request.args.get('limit')
    if limit is None:
        db = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="mallard", db="wePredict")
        cursor = db.cursor()
        cursor.execute("SELECT * from SMOKING");
        db.close()
        data = cursor.fetchall()
        json.dumps(data, use_decimal=True)
        return data
    else:
        db = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="mallard", db="wePredict")
        cursor = db.cursor()
        cursor.execute("SELECT * from SMOKING LIMIT "+limit);
        db.close()
        data = cursor.fetchall()
        json.dumps(data, use_decimal=True)
        return data



@app.route("/")
def hello():
    return "Hello, apache!!!!!"
