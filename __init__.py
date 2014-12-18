from flask import Flask, jsonify
from flask import request
import MySQLdb

app = Flask(__name__)
db = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="mallard", db="wePredict")

@app.route('/getadress')
def getAdress():
    limit = request.args.get('limit')
    if limit is None:
        cursor = db.cursor()
        cursor.execute("SELECT * from ADRESS");
        return jsonify(data = cursor.fetchall())
    else:
        cursor = db.cursor()
        cursor.execute("SELECT * from ADRESS LIMIT "+limit);
        return jsonify(data = cursor.fetchall())

@app.route('/getsmoking')
def getSmoking():
    limit = request.args.get('limit')
    db = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="mallard", db="wePredict")
    if limit is None:
        cursor = db.cursor()
        cursor.execute("SELECT * from SMOKING");
        return jsonify(data = cursor.fetchall())
    else:
        cursor = db.cursor()
        cursor.execute("SELECT * from SMOKING LIMIT "+limit);
        return jsonify(data = cursor.fetchall())

@app.route('/getpolution')
def getPolution():
    limit = request.args.get('limit')
    return "POPULSTION"


@app.route('/getflu')
def getFlu():
    limit = request.args.get('limit')
    return "FLU"

@app.route('/getcopd')
def getCopd():
    limit = request.args.get('limit')
    return "COPD"


@app.route('/getasthamqof(')
def getAsthamQof():
    limit = request.args.get('limit')
    return "ASMATHA"



@app.route("/")
def hello():
    return "Hello, apache!!!!!"

if __name__ == "__main__":
    app.debug = True
    app.run()

